import xml.etree.ElementTree as ET
import csv as cs

OutputCsv = 'H:/Automation/Python/MO/Output file/Output_sample.csv'
OutputFile = open(OutputCsv,'w')
OutputFile.write(str('Tag_Name')+ ',' + str('Value'))
OutputFile.write('\n')

def mydef(value,fulltag):
    for elem in value:
        tag1 = elem.tag.split("'")[0] + '/'
        fulltag += tag1
        if len(elem):
            mydef(elem,fulltag)
        else:
            print(tag1)
            print(elem.text)
            OutputFile.write(str(fulltag) + ',' + str(elem.text))
            OutputFile.write('\n')

root = ET.parse('H:/Automation/Python/MO/Input file/file4.xml').getroot()
mydef(root,'')


