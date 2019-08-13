import xml.etree.ElementTree as ET
import csv as csv

root = ET.parse('H:/Automation/Python/MO/Input file/file4.xml').getroot()

OutputCsv = 'H:/Automation/Python/MO/Output file/Output.csv'
OutputFile = open(OutputCsv,'w')

for elem in root:
    tag1 = elem.tag.split("'")[0] + '/'
    if len(elem):
        for subelem1 in elem:
            a = tag1
            a += subelem1.tag.split("'")[0] + '/'
            if len(subelem1):
                for subelem2 in subelem1:
                    a1 = a
                    a1 += subelem2.tag.split("'")[0] + '/'
                    if len(subelem2):
                        for subelem3 in subelem2:
                            b1 = a1
                            b1 += subelem3.tag.split("'")[0] + '/'
                            if len(subelem3):
                                for subelem4 in subelem3:  # subelem4 = itemDesc,itemName next loop #subelem4 = environmentType
                                    b2 = b1
                                    b2 += subelem4.tag.split("'")[0] + '/'
                                    if len(subelem4):
                                        for subelem5 in subelem4:  # environmentTypeCd
                                            b3 = b2
                                            b3 += subelem5.tag.split("'")[0] + '/'
                                            if len(subelem5):
                                                for subelem6 in subelem5:
                                                    b4 = b3
                                                    b4 += subelem6.tag.split("'")[0] + '/'
                                                    if len(subelem6):
                                                        for subelem7 in subelem6:
                                                            b5 = b4
                                                            b5 += subelem7.tag.split("'")[0] + '/'
                                                            if len(subelem7):
                                                                for subelem8 in subelem7:
                                                                    b6 = b5
                                                                    b6 += subelem8.tag.split("'")[0] + '/'
                                                                    if len(subelem8):
                                                                        for subelem9 in subelem8:
                                                                            b7 = b6
                                                                            b7 += subelem9.tag.split("'")[0] + '/'
                                                                            if len(subelem9):
                                                                                for subelem10 in subelem9:
                                                                                    b8 = b7
                                                                                    b8 += subelem10.tag.split("'")[
                                                                                              0] + '/'
                                                                                    if len(subelem10):
                                                                                        for subelem11 in subelem10:
                                                                                            b9 = b8
                                                                                            b9 += \
                                                                                            subelem11.tag.split("'")[
                                                                                                0] + '/'
                                                                                            if len(subelem11):
                                                                                                for subelem12 in subelem11:
                                                                                                    b10 = b9
                                                                                                    b10 += \
                                                                                                        subelem12.tag.split(
                                                                                                            "'")[
                                                                                                            0] + '/'
                                                                                                    if len(subelem12):
                                                                                                        for subelem13 in subelem12:
                                                                                                            b11 = b10
                                                                                                            b11 += \
                                                                                                                subelem13.tag.split(
                                                                                                                    "'")[
                                                                                                                    0] + '/'
                                                                                                            if len(
                                                                                                                    subelem13):
                                                                                                                for subelem14 in subelem13:
                                                                                                                    b12 = b11
                                                                                                                    b12 += \
                                                                                                                        subelem14.tag.split(
                                                                                                                            "'")[
                                                                                                                            0] + '/'
                                                                                                                    if len(
                                                                                                                            subelem14):
                                                                                                                        for subelem15 in subelem14:
                                                                                                                            b13 = b12
                                                                                                                            b13 += \
                                                                                                                                subelem15.tag.split(
                                                                                                                                    "'")[
                                                                                                                                    0] + '/'
                                                                                                                            if len(
                                                                                                                                    subelem15):
                                                                                                                                for subelem16 in subelem15:
                                                                                                                                    b14 = b13
                                                                                                                                    b14 += \
                                                                                                                                        subelem16.tag.split(
                                                                                                                                            "'")[
                                                                                                                                            0] + '/'
                                                                                                                                    if len(
                                                                                                                                            subelem16):
                                                                                                                                        for subelem17 in subelem16:
                                                                                                                                            b15 = b14
                                                                                                                                            b15 += \
                                                                                                                                                subelem17.tag.split(
                                                                                                                                                    "'")[
                                                                                                                                                    0] + '/'
                                                                                                                                            if len(
                                                                                                                                                    subelem17):
                                                                                                                                                for subelem18 in subelem17:
                                                                                                                                                    b16 = b15
                                                                                                                                                    b16 += b15
                                                                                                                                                    print(
                                                                                                                                                        b16)
                                                                                                                                                    print(
                                                                                                                                                        subelem18.text)
                                                                                                                                                    OutputFile.write(str(b16)+','+str(subelem18.text))
                                                                                                                                                    OutputFile.write(
                                                                                                                                                        '\n')
                                                                                                                                            else:
                                                                                                                                                print(
                                                                                                                                                    b15)
                                                                                                                                                print(
                                                                                                                                                    subelem17.text)
                                                                                                                                                OutputFile.write(
                                                                                                                                                    str(
                                                                                                                                                        b15) + ',' + str(
                                                                                                                                                        subelem17.text))
                                                                                                                                                OutputFile.write(
                                                                                                                                                    '\n')
                                                                                                                                    else:
                                                                                                                                        print(
                                                                                                                                            b14)
                                                                                                                                        print(
                                                                                                                                            subelem16.text)
                                                                                                                                        OutputFile.write(
                                                                                                                                            str(
                                                                                                                                                b14) + ',' + str(
                                                                                                                                                subelem16.text))
                                                                                                                                        OutputFile.write(
                                                                                                                                            '\n')
                                                                                                                            else:
                                                                                                                                print(
                                                                                                                                    b13)
                                                                                                                                print(
                                                                                                                                    subelem15.text)
                                                                                                                                OutputFile.write(
                                                                                                                                    str(
                                                                                                                                        b13) + ',' + str(
                                                                                                                                        subelem15.text))
                                                                                                                                OutputFile.write(
                                                                                                                                    '\n')
                                                                                                                    else:
                                                                                                                        print(
                                                                                                                            b12)
                                                                                                                        print(
                                                                                                                            subelem14.text)
                                                                                                                        OutputFile.write(
                                                                                                                            str(
                                                                                                                                b12) + ',' + str(
                                                                                                                                subelem14.text))
                                                                                                                        OutputFile.write(
                                                                                                                            '\n')
                                                                                                            else:
                                                                                                                print(
                                                                                                                    b11)
                                                                                                                print(
                                                                                                                    subelem13.text)
                                                                                                                OutputFile.write(
                                                                                                                    str(
                                                                                                                        b11) + ',' + str(
                                                                                                                        subelem13.text))
                                                                                                                OutputFile.write(
                                                                                                                    '\n')
                                                                                                    else:
                                                                                                        print(b10)
                                                                                                        print(subelem12.text)
                                                                                                        OutputFile.write(
                                                                                                            str(
                                                                                                                b10) + ',' + str(
                                                                                                                subelem12.text))
                                                                                                        OutputFile.write(
                                                                                                            '\n')
                                                                                            else:
                                                                                                print(b9)
                                                                                                print(subelem11.text)
                                                                                                OutputFile.write(
                                                                                                    str(b9) + ',' + str(
                                                                                                        subelem11.text))
                                                                                                OutputFile.write('\n')
                                                                                    else:
                                                                                        print(b8)
                                                                                        print(subelem10.text)
                                                                                        OutputFile.write(
                                                                                            str(b8) + ',' + str(
                                                                                                subelem10.text))
                                                                                        OutputFile.write('\n')
                                                                            else:
                                                                                print(b7)
                                                                                print(subelem9.text)
                                                                                OutputFile.write(
                                                                                    str(b7) + ',' + str(subelem9.text))
                                                                                OutputFile.write('\n')
                                                                    else:
                                                                        print(b6)
                                                                        print(subelem8.text)
                                                                        OutputFile.write(
                                                                            str(b6) + ',' + str(subelem8.text))
                                                                        OutputFile.write('\n')
                                                            else:
                                                                print(b5)
                                                                print(subelem7.text)
                                                                OutputFile.write(str(b5) + ',' + str(subelem7.text))
                                                                OutputFile.write('\n')
                                                    else:
                                                        print(b4)
                                                        print(subelem6.text)
                                                        OutputFile.write(str(b4) + ',' + str(subelem6.text))
                                                        OutputFile.write('\n')
                                            else:
                                                print(b3)
                                                print(subelem5.text)
                                                OutputFile.write(str(b3) + ',' + str(subelem5.text))
                                                OutputFile.write('\n')
                                    else:
                                        print(b2)
                                        print(subelem4.text)
                                        OutputFile.write(str(b2) + ',' + str(subelem4.text))
                                        OutputFile.write('\n')
                            else:
                                print(b1)
                                print(subelem3.text)
                                OutputFile.write(str(b1) + ',' + str(subelem3.text))
                                OutputFile.write('\n')
                    else:
                        print(a1)
                        print(subelem2.text)
                        OutputFile.write(str(a1) + ',' + str(subelem2.text))
                        OutputFile.write('\n')
            else:
                print(a)
                print(subelem1.text)
                OutputFile.write(str(a) + ',' + str(subelem1.text))
                OutputFile.write('\n')
    else:
        print(tag1)
        print(elem.text)
        OutputFile.write(str(tag1) + ',' + str(elem.text))
        OutputFile.write('\n')
OutputFile.close()
