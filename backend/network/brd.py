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
        self.name=None
        self.port=None
        self.connected=False
        self.s=socket.socket()
    
    def setup(self,ip=None,name=None,port=None):
        self.ip=ip
        self.name=name
        self.port=port
    
    def connect(self):
        if self.connected==False:
            self.s.connect((self.ip, self.port))
            self.connected = True
            print('Connection', self.connected)
        else:
            print('Warning: Already Connected')
    
    def echoTest(self):
        if self.connected == False:
            print('Error: Not Connected!')
            return
        self.s.sendall(b'OSIMS')
        data = self.s.recv(1024)
        print(data,type(data))
        
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
            
    def recvImage(self,size):
        data = b''
        while len(data) < size:
            packet = self.s.recv(size - len(data))
            if not packet:
                return None
            data += packet
        return data
    
    def test1(self):
        if self.connected==False:
            print('Error: Device not found.')
        else: 
            self.s.sendall(b'redledon')
            print('command sent')
            
    def test2(self):
        if self.connected==False:
            print('Error: Device not found.')
        else: 
            self.s.sendall(b'blueledon')
            print('command sent')
    
    
def main():

    ip='192.168.1.66'
    port=12345
    brd=Brd()
    brd.setup(ip=ip, type='cam', port=port)
    brd.s.sendall(b'12345')
    data=None
    data=brd.s.recv(1024)
    print(data,type(data))

if __name__ == "__main__":
    main()
    