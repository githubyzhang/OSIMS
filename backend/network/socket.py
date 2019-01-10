import socket               # Import socket module

'''
Class: Brd
Author: Yuchang Zhang
Date: Jan 10, 2019
Description: Used to establish ethernet socket connection to the board and transmit/receive data.

Function 1: setup()
    Author: Yuchang Zhang
    Description: 
        this function is used to configure the board.
        
    Inputs:
        1. ip (string): ip address.
        2. type (string): whether it is "IFU", Infrared Unit, or "O", other.
        3. port (int): number of port.
    
    Outputs: N/A
        
    Example use:
        new=brd()
        new.setup(ip='192.168.1.106', type='IFU', port=12345)
        
        
Function 2: echoTest()
    Author: Yuchang Zhang
    Description: 
        echoTest() is used to establish the Ethernet connection to the board and initiate an echo-test 
        by sending a string, expecting the board to be programmed to return the same string received.
        This function is called after the brd instance being setup.
        
    Inputs: N/A

    Outputs: 
        1. print(): print whether the connection is true or false.
    
    Example use:Example use:
        new=brd()
        new.setup(ip='192.168.1.106', type='IFU', port=12345
        new.echoTest()
        
        
Function 3: camOn()
    Author: Yuchang Zhang
    Description:
        This function is used after connection established by calling echoTest(). It send command to
        the board to turn on the camera.
        
    Inputs: N/A
    
    Outputs: N/A
        
    Example use:
        new=brd()
        new.setup(ip='192.168.1.106', type='IFU', port=12345
        new.echoTest()
        new.camOn()
        
        
Function 4: camOff()
    Author: Yuchang Zhang
    Description:
        This function is used after connection established by calling echoTest(). It send command to
        the board to turn off the camera.
        
    Inputs: N/A
    
    Outputs: N/A
        
    Example use:
        new=brd()
        new.setup(ip='192.168.1.106', type='IFU', port=12345
        new.echoTest()
        new.camOff()
    
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
        print('Connection', self.connected)
        
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