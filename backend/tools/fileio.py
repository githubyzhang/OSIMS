import csv

'''
Function: fileout()
Author: Yuchang Zhang
Description: fileout() is to output matrix data in the file type of .cvs.
          if the file already exist, it will... i don't know yet i need to figure this out.
          if the file does not exist, the function will create a new file under the desired path with the given name.
          
Inputs:
    1. filename: the desired name of the file.
    2. path: the desired path of the file.
    3. labels: the labels of the data.
    4. data: the actual data array.
    
Example use:
    labels=['Name','Age','Major']
    data=[['Yuchang','22','ECE'],
          ['Michael','22','ECE']]
    fileout(name='MQP Team Member', path="C://Desktop",labels=labels,data=data)
 
'''

def fileout(filename='', path='', labels=None, data=None, mode='a'):
    with open(path+'/'+filename+'.csv', mode=mode) as temp_file:
        file_writer=csv.writer(temp_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        if labels is not None:
            file_writer.writerow(labels)
        for i in range(len(data)):
            file_writer.writerow(data[i])
            
            


'''
Function: fileread()
Author: Yuchang Zhang
Description: fileread() is a function that finds a csv file from a directory and returns data and labels contained in the file
            in the forms of arrays.
          
Inputs:
    1. filename: the name of the file that wants to read.
    2. path: the path of the file that wants to read.
    
Outputs:
    1. labels [list]: a list of labels for the data.
    2. data [array]: an array of data contained in the file.
    
Example use:
    data=[]
    labels=[]
    labels, data = fileread(filename='file_for_read', path='hypothetical_path')
    
'''
            
def fileread(filename='',path=''):
    data=[]
    labels=[]
    with open(path+'/'+filename+'.csv', mode='r') as temp_file:
        csv_reader=csv.reader(temp_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count==0:
                line_count+=1
                labels.append(row)
            else:
                data.append(row)
    return labels, data, len(data)

def fileread1(filename='',path=''):
    data=[]
    with open(path+'/'+filename+'.csv', mode='r') as temp_file:
        csv_reader=csv.reader(temp_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            data.append(row)
    return data, len(data)


            
            
            