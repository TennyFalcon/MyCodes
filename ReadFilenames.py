import os

path = 'H:/Automation/Python/MO/XML files/'
OutputCsv = 'H:/Automation/Python/MO/Output file/Filenames.csv'
OutputFile = open(OutputCsv,'w')
OutputFile.write('Filenames')
OutputFile.write('\n')

files = []

for r,d,f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(file)

for f in files:
    OutputFile.write(f)
    OutputFile.write('\n')

OutputFile.close()



