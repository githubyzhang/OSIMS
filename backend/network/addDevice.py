import sys
from network.libs import addDevice
sys.path.insert(0,'/Users/yuchangzhang/git/OSIMS/backend')
args = sys.argv
msg=addDevice(device_type=args[1], name=args[2], ip=args[3])