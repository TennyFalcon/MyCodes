import os

path = 'H:/Automation/Python/Reconhire/Input files/'
OutputCsv = 'H:/Automation/Python/Reconhire/Output files/Output.csv'
OutputFile = open(OutputCsv,'w')
OutputFile.write('Filenames')
OutputFile.write('\n')

files = []

for r,d,f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(file)

for f in files:
    OutputFile.write(f)
    OutputFile.write('\n')

OutputFile.close()



