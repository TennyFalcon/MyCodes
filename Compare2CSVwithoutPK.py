import csv as csv

file1 = open('H:/Automation/Python/FileValidation/Input files/source40.csv','r')
file2 = open('H:/Automation/Python/FileValidation/Input files/target40.csv','r')

f1 = file1.readlines()
f2 = file2.readlines()

file1.close()
file2.close()

for x in f1:
    y = x
    break

print(y)

outputfile = open('H:/Automation/Python/FileValidation/Output files/result.csv','w')
outputfile.write(y)

for line in f2:
    if line not in f1:
        outputfile.write(line)

