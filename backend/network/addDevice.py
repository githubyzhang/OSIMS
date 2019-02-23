import sys
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
from network.libs import addDevice
# libs = '/Users/yuchangzhang/git/OSIMS/backend/network/libs.py'
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.expanduser(libs)))
# from libs import addDevice

#from command line take arguments
args = sys.argv
# type_name, name ,ip = sys.argv
# msg=addDevice(device_type=type_name, name=name, ip=ip)
msg=addDevice(device_type=args[1], name=args[2], ip=args[3])
# sys.stdout(msg)