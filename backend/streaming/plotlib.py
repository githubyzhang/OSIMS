from tools.fileio import fileread

def hcPlot(i,*fargs):#filename=None,path=None):
    labels,data,length=fileread(filename=fargs[0], path=fargs[1])
    xdata=[]
    ydata=[]
    for i in range(20):
        index=len(data)-(20-i)
        frame=data[index]
        frame=frame[1:]
        for a in range(4800):
            frame[a]=float(frame[a])
        ydata.append(max(frame))
        xdata.append(i)
    ax=fargs[2]
    ax.clear()
    ax.plot(xdata,ydata)
    

def pixelPlot(i,*fargs):
    labels,data,length=fileread(filename=fargs[0], path=fargs[1])
    xdata=[]
    ydata=[]
    for i in range(20):
        index=len(data)-(20-i)
        frame=data[index]
        frame=frame[1:]
        for a in range(4800):
            frame[a]=float(frame[a])
        ydata.append(frame[fargs[3]])
        xdata.append(i)
    ax1=fargs[2]
    ax1.clear()
    ax1.plot(xdata,ydata)

