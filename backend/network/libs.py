from tools.fileio import fileout
from tools.fileio import fileread


'''
Function: addDevice()
Author: Yuchang Zhang
Date: 02/07/2019
Description: addDevice() is a function that's called by frontend page "setting" via linker addDevice() 
            to add new device to the devicelist.csv
          
Inputs:
    1. device_type: the device_type of device, whether it is a camera or other,
    2. name: arbitrary name defied by user.
    3. ip: the ip address of the device.
    
Example use:
    addDevice(device_type=type, name=name, ip=ip)
 
'''
def addDevice(device_type=None, name=None, ip=''):
    readlabels, readdata, readsize = fileread(filename='devicelist', path='/Users/yuchangzhang/git/OSIMS/system')
    num=str(readsize+1)
    writedata=[]
    #check if the device with the ip address given already exist in the list
    for i in readdata:
        if ip == i[3]:
            msg="Error: device with the ip address:"+ip+" already exist!"
            print(msg)
            return msg
    writedata.append([num,device_type,name,ip])
    fileout(filename='devicelist', path='/Users/yuchangzhang/git/OSIMS/system', data=writedata)
    msg="Success: added new device with ip:"+ip
    print(msg)
    return msg



def refreshList():
    readlabels, readdata, readsize = fileread(filename='devicelist', path='/Users/yuchangzhang/git/OSIMS/system')
    print(readlabels)
    print(readdata)
    print(readsize)


def main():
    labels, data, size = fileread(filename='devicelist', path='/Users/yuchangzhang/git/OSIMS/system')
    print(labels,data, size)
    addDevice(device_type='Cam', Name='Zone1', ip='192.168.1.106')
    addDevice(device_type='Cam', Name='Zone1', ip='192.168.1.106')
    addDevice(device_type='Cam', Name='Zone1', ip='192.168.1.104')
    addDevice(device_type='Cam', Name='Zone1', ip='192.168.1.102')

       
if __name__=="__main__":
    main()