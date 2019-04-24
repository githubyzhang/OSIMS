from time import localtime as get

'''
Class: Time
Author: Yuchang Zhang
Description: Can be instantiated as an object to be used to keep track of date and time.

Functions: 
    Function 1: update()
    Author: Yuchang Zhang
    Description: it returns an integer list consists year, month, date, hour, minute, second.
    
    Inputs:
        1. self
    
    Outputs:
        1. list of integers [year,month,date,hour,minute,second]
    
    Example use:
        t=Time()
        time_data=t.update()
'''

class Time:
    def __init__(self):
        self.year=get()[0]
        self.month=get()[1]
        self.date=get()[2]
        self.hour=get()[3]
        self.minute=get()[4]
        self.second=get()[5]
        self.string=''
        
    def update(self):
        self.year=get()[0]
        self.month=get()[1]
        self.date=get()[2]
        self.hour=get()[3]
        self.minute=get()[4]
        self.second=get()[5]
        return [self.year,self.month,
                self.date,self.hour,
                self.minute,self.second]
    
    def stringout(self):
        self.year=get()[0]
        self.month=get()[1]
        self.date=get()[2]
        self.hour=get()[3]
        self.minute=get()[4]
        self.second=get()[5]
        self.string = str(self.month)+'/'+str(self.date)+'/'+str(self.year)+'  '+str(self.hour)+':'+str(self.minute)+':'+str(self.second)
        return self.string

    def filenamegen(self):
        self.year=get()[0]
        self.month=get()[1]
        self.date=get()[2]
        self.hour=get()[3]
        self.minute=get()[4]
        self.second=get()[5]
        filename = str(self.month)+'_'+str(self.date)+'_'+str(self.year)
        return filename
    
    def time(self):
        self.year=get()[0]
        self.month=get()[1]
        self.date=get()[2]
        self.hour=get()[3]
        self.minute=get()[4]
        self.second=get()[5]
        time = str(self.hour)+':'+str(self.minute)+':'+str(self.second)
        return time
    
def main():
    t=Time()
    print(t.update())
    
if __name__=="__main__":
    main() 