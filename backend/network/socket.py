import socket               # Import socket module





'''
Function: Echo Test Script
Author: Yuchang Zhang
Date: Jan 6, 2019
Description: Used to establish ethernet socket connection and transmit data.

Functions: 
    Function 1: 
    Author: Yuchang Zhang
    Description: 
    
    Inputs:
        1. 
    
    Outputs:
        1. 
    
    Example use:
        
'''
class Brd:
    def __init__(self):
        self.ip=None
        self.type=None
        self.port=None
        self.connected=False
        self.s=socket.socket()
    
    def setup(self,ip=None,type=None,port=None):
        self.ip=ip
        self.type=type
        self.port=port
        
    def echoTest(self):
        self.s.connect((self.ip, self.port))
        self.s.sendall(b'MQPspring2019')
        key='MQPspring2019'
        data=None
        data = self.s.recv(1024)
        print(data,type(data))
        self.connected=True if (data is not None) else False
        
    def camOn(self):
        if self.connected==False:
            print('Error: Device not found.')
        else: 
            self.s.sendall(b'CmdCamOn')
            print('command sent')
            
    def camOff(self):
        if self.connected==False:
            print('Error: Device not found.')
        else: 
            self.s.sendall(b'CmdCamOff')

def main():
    new=Brd()
    new.setup(ip='192.168.1.106', port=12345)
    new.echoTest()
    new.camOn()
    
if __name__=="__main__":
    main()