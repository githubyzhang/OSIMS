from network.brd import Brd
from tools.time import Time
from streaming.palette import palette
import cv2
import numpy as np

# initialize
palette=palette()
a=Brd()
a.setup(ip='192.168.1.66', port=333)
a.connect()
new=a.recvImage(9600)
old=new
timer=Time()
time=''
video=cv2.VideoWriter('video.avi',-1,9,(800,600))

while 1:
    new=a.recvImage(9600)
    if new != old:
        rb=bytes()
        gb=bytes()
        bb=bytes()
        temp_ls=[]
        old = new
        x=0 
        y=x+2
        while x<9600:
            raw = new[x:y]
            temp=int.from_bytes(raw, byteorder='little')
            temp=temp-29315
            temp_ls.append(temp/100)
            temp=int(temp/25)
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
        
        # image processing
        maxtemp=max(temp_ls)
        pos=temp_ls.index(maxtemp)
        pos_x=(pos%80)*10
        pos_y=int(pos/80)*10
#         cv2.rectangle(img,(pos_x-10,pos_y-10),(pos_x+10,pos_y+10),(255,255,255),3)
        cv2.circle(img,(pos_x,pos_y), 10, (255,255,255), 3)
        
        # put time and date
        time=timer.stringout()
        cv2.putText(img,time,(10,570), 0, 1,(255,255,255),1,cv2.LINE_AA)
        # put max temperature reading
        cv2.putText(img,'max temperature:'+str(maxtemp+20),(10,500), 0, 1,(255,255,255),1,cv2.LINE_AA)
        
        # streaming
        cv2.imshow('image',img)
        
        # output video
        video.write(img)
        k=cv2.waitKey(10)
        if k == ord('q'):
            break
            video.release()