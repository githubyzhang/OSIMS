import sys
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from streaming.plotlib import pixelPlot
from tools.time import Time
from tools.fileio import fileout

args = sys.argv
x_pos=int(args[1])
y_pos=int(args[2])

style.use('fivethirtyeight')

fig = plt.figure()

ax = fig.add_subplot(1,1,1,label='label')
fig.suptitle('Pixel Plot: ('+str(x_pos)+','+str(y_pos)+')', fontsize=16)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')


t=Time()

filename=t.filenamegen()
path='/Users/yuchangzhang/git/OSIMS/data'

pixel=int((y_pos-1)*80+x_pos)
fileout(filename='pixel_list', path='/Users/yuchangzhang/git/OSIMS/system',data=[[x_pos,y_pos]])

ani = animation.FuncAnimation(fig,pixelPlot,fargs=(filename,path,ax,pixel),interval=1000)
plt.show()