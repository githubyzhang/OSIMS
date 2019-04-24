import sys
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from streaming.plotlib import hcPlot
from tools.time import Time


style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.suptitle('Hot Corner Plot', fontsize=16)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')

t=Time()

filename=t.filenamegen()
path='/Users/yuchangzhang/git/OSIMS/data'

ani = animation.FuncAnimation(fig,hcPlot,fargs=(filename,path,ax),interval=1000)
plt.show()