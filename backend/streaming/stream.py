import sys
from cv2 import COLORMAP_SPRING
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
from network.brd import Brd
from tools.time import Time
from tools.fileio import fileout, fileread1
from streaming.palette import palette
import cv2
import numpy as np
import matplotlib.pyplot as plt



# initialize
palette, palbar=palette()
logo=cv2.imread('/Users/yuchangzhang/git/OSIMS/frontend/images/OSIMS_icon.png')
a=Brd()
a.setup(ip='192.168.1.66', port=333)
a.connect()
frame=a.recvImage(9600)
timer=Time()
presec=timer.time()
video=cv2.VideoWriter('video.avi',-1,9,(800,600))
datapath = '/Users/yuchangzhang/git/OSIMS/data'
filename=timer.filenamegen()
hc_buffer=[]


# select palette range:
args = sys.argv
mode = args[1]   #'Default'    (20,60)
minval = int(args[2])
maxval = int(args[3])

if mode=='Default':
    floor=20
    ceiling=60
    floor=27315+floor*100
    ceiling=27315+ceiling*100
elif mode=='Auto':
    frame=a.recvImage(9600)
    x=0 
    y=x+2
    temp_ls=[]
    while x<9600:
        raw = frame[x:y]
        temp=int.from_bytes(raw, byteorder='little')
        temp_ls.append(temp)
        x+=2
        y=x+2
    floor=min(temp_ls)-100
    ceiling=max(temp_ls)+100
elif mode=='Manual':
    floor=27315+minval*100
    ceiling=27315+maxval*100
    
step=(ceiling-floor)/160


while 1:
    frame=a.recvImage(9600)
    rb=bytes()
    gb=bytes()
    bb=bytes()
    temp_ls=[]
    x=0 
    y=x+2
    while x<9600:
        raw = frame[x:y]
        temp=int.from_bytes(raw, byteorder='little')
        temp_ls.append(round(((temp-27315)/100),2))
        temp=temp-floor
        temp=int(temp/step)
        if temp>159:
            temp=159
        if temp<0:
            temp=0
        x+=2
        y=x+2

        rb+=bytes([palette[temp][0]])
        gb+=bytes([palette[temp][1]])
        bb+=bytes([palette[temp][2]])
        
    # create bgr image
    b = np.frombuffer(bb, np.uint8).reshape(60, 80)
    g = np.frombuffer(gb, np.uint8).reshape(60, 80)
    r = np.frombuffer(rb, np.uint8).reshape(60, 80)
    bgr_img = cv2.merge([b,g,r])       
    img = cv2.resize(bgr_img,(800,600))
    
    # add palette
    cv2.rectangle(img,(728,48),(752,532),(255,255,255),2)
    img[50:530, 730:750] = palbar
    cv2.putText(img,str(round((floor-27315)/100)),(720,570), 0, 1,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(img,str(round((ceiling-27315)/100)),(720,30), 0, 1,(255,255,255),1,cv2.LINE_AA)
    
    # add logo
#     img[0:121, 0:122] = logo
    
    # hot spot detection
    maxtemp=max(temp_ls)
    pos=temp_ls.index(maxtemp)
    pos_x=(pos%80)*10
    pos_y=int(pos/80)*10
    cv2.circle(img,(pos_x,pos_y), 7, (255,255,255), 2)
    cv2.putText(img,'Hot Corner:'+str(round(maxtemp,2)),(10,500), 0, 1,(255,255,255),1,cv2.LINE_AA)
    
    # put time and date
    time=timer.stringout()
    cv2.putText(img,time,(10,570), 0, 1,(255,255,255),1,cv2.LINE_AA)
    
    # pixel plot updater
    pxl_ls,length=fileread1(filename='pixel_list', path='/Users/yuchangzhang/git/OSIMS/system')
    print(pxl_ls)
    if length>0:
        for pixel in pxl_ls:
            px=int(pixel[0])
            py=int(pixel[1])
            index=int(px+(py-1)*80)
            px=int(px*10)
            py=int(py*10)
            cv2.circle(img,(px,py), 5, (0,255,0), 2)
            cv2.putText(img,str(temp_ls[index]),(px,py+60), 0, 1,(0,0,255),1,cv2.LINE_AA)
    
    # streaming
    cv2.imshow('image',img)

        
    '''
        !!!! 1 fps loop !!!!
    '''
    thissec=timer.time()
    if presec!=thissec:
        # save temperature file 1 fps
        fileout(filename=filename, path=datapath, data=[[thissec]+temp_ls])
        presec=thissec
    
    # output video
    video.write(img)
    k=cv2.waitKey(10)
    if k == ord('q'):
        #erase pixel list:
        fileout(filename='pixel_list', path='/Users/yuchangzhang/git/OSIMS/system', mode='w')
        break
        video.release()