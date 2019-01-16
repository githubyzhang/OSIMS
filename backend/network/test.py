from brd import Brd

def main():
    
    '''
        The following lines of codes can be copied and pasted for establishing connection.
    '''
    
    brd=Brd()
    ip='192.168.1.106'
    port=12345
    brd.setup(ip=ip,port=port)
    
    brd.echoTest()


       
if __name__=="__main__":
    main()