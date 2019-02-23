from streaming.palette import palette
from PIL import Image

im_buffer=bytes()
palette = palette()
path='/Users/yuchangzhang/git/OSIMS/frontend/images'
filename='ir_image'
with open(path+'/'+filename+'.bin', mode='rb') as f:
    x=0
    y=0
    while y<60:
        while x<80:
            byte_1 = f.read(1)
            byte_2 = f.read(1)
            raw=byte_1+byte_2
            temp=int.from_bytes(raw, byteorder='little')
            temp=temp-29315
            temp=int(temp/25)
            red = palette[temp][0]
            green = palette[temp][1]
            blue = palette[temp][2]
            im_buffer=im_buffer+bytes([red])+bytes([green])+bytes([blue])
            x+=1     
        x=0
        y+=1

im=Image.frombytes(mode='RGB', size=(80,60), data=im_buffer)
im.show()
