def main():
    host='192.168.1.106'
    port=12345
    message='Test Echo Message'
    return_msg=echoTest(host=host, port=port, message=message)
    if message == return_msg:
        print('success', message)
    else:
        print('test failed')


       
if __name__=="__main__":
    main()