import csv

allRows = []

with open('file_1.csv', 'r') as crimefile: #file header names will be the same in the write csv  file 
    for line in crimefile:
        allRows += line.strip().split(',')
        #write to new csv file 
        with open('file_2.csv', 'w') as newfile:
            for row in allRows:
                newfile.write(row + ',')
            newfile.close()
    crimefile.close()
    