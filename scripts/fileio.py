import csv

'''
Function: fileout() is to output matrix data in the file type of .cvs.
          if the file already exist, it will... i don't know yet i need to figure this out.
          if the file does not exist, the function will create a new file under the desired path with the given name.
Inputs:
    1. name: the desired name of the file.
    2. path: the desired path of the file.
    3. labels: the labels of the data.
    4. data: the actual data array.
    

'''

def fileout(name='', path='', labels=[], data=[]):
    with open(path+'/'+name, mode='w') as temp_file:
        file_writer=csv.writer(temp_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(labels)
        for i in range(len(data)):
            file_writer.writerow(data[i])