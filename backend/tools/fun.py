def main():
    x=3
    
    while x<1000000000000:
        num=2 * x
        a=1
        stillgoing=True
        while (a <= x+1) and stillgoing:
            stillgoing=True
            b=num-a
            if checkprime(a) and checkprime(b):
                print(num, "proved 1+1 --> a =", a, "b =", b)
                stillgoing=False
            if a>x:
                print("failed at", num)
                return
            a+=1
        x+=1
        
        
        
        
        
        
        
        
        
        
        
        
def checkprime(num=0):
    i = 1
    while i <= num:
        if (num%i == 0) and ((i!=1) and (i!=num)):
            return False
        i+=1
    
    return False if i==2 else True

        
        
if __name__=="__main__":
    main()