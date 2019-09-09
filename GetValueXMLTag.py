import xml.etree.ElementTree as ET
import pandas as pd

filename_list = []
input_file_data = pd.read_csv('H:/Automation/Python/MO/Output file/Filenames.csv')
filename_list = input_file_data['Filenames']

tag_name = input('Enter the tag name: ')

OutputCsv = 'H:/Automation/Python/MO/Output file/Element_tag_value_function.csv'
OutputFile = open(OutputCsv,'w')
OutputFile.write(tag_name)
OutputFile.write('\n')

def Data(value1):
    for value in value1:
        tag1 = value.tag.split("'")[0]
        if tag1 == tag_name:
            print(str(value.text))
            OutputFile.write(str(value.text))
            OutputFile.write('\n')
        else:
            if len(value):
                Data(value)

for x in filename_list:
    print(x)
    root = ET.parse('H:/Automation/Python/MO/XML files/'+x).getroot()
    Data(root)

OutputFile.close()






