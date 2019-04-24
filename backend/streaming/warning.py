import os
import sys
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
from tools.time import Time
from tools.fileio import fileread

args=sys.argv

os.system('say O Sinmhs, Activated!')

t=Time()
filename=t.filenamegen()
path='/Users/yuchangzhang/git/OSIMS/data'
presec=t=Time()
limit=int(args[1])
buffer=None
counter=0

while 1:
    thissec=t.time()
    if presec!=thissec:
        # save temperature file 1 fps
        labels,data,length=fileread(filename=filename, path=path)
        presec=thissec
        data=data[len(data)-1]
        data=data[1:]
        for i in range(4800):
            data[i]=float(data[i])
        maxval=max(data)
        
        # check for timeout 5s:
        if maxval==buffer:
            counter+=1
        elif maxval!=buffer:
            buffer=maxval
            counter=0
        if counter>5:
            os.system('say "Error! timeout! O Sinmhs D Activated!"')
            break
        
        # give warning
        if maxval>limit:
            os.system('say "Warning! Warning! Temperature exceeds fucking limit."')
            os.system('say "Warning! Warning! Temperature exceeds fucking limit."')
            