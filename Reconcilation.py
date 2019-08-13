
import csv as csv
import xlsxwriter
import pandas as pd


def GetDataFrameFromFile(file,encode):
   data = pd.read_csv(file,encoding=encode,error_bad_lines=False)
   return data

Dm_filename = input("Enter the filename of DM extract: ")
Wd_filename = input("Enter the filename of WD report: ")

DmPlinkExt  = "H:/Automation/Python/Reconhire/Input files/" + Dm_filename
WdReprtExt  = "H:/Automation/Python/Reconhire/Input files/" + Wd_filename

dm = []
wd = []

dm =  GetDataFrameFromFile(DmPlinkExt,"ISO-8859-1")
wd    =  GetDataFrameFromFile(WdReprtExt,"ISO-8859-1")

dm_primary_key = input("Enter the primary key of Dm Extract: ")
wd_primary_key = input("Enter the primary key of Wd report: ")

dm.rename(columns={dm_primary_key:'Primary_Key'},inplace=True)
wd.rename(columns={wd_primary_key:'Primary_Key'},inplace=True)

dm_add_column = dm_primary_key + '_dm'
wd_add_column = wd_primary_key + '_wd'

#adding primary key column to the dataframe
dm[dm_add_column] = dm['Primary_Key']
wd[wd_add_column] = wd['Primary_Key']

df_merged = pd.merge(dm,wd,how='left',on='Primary_Key',suffixes= ('_dm','_wd'))

# Getting values for pie chart for DmVsWd

Merged_Primary_Key_count = df_merged["Primary_Key"].count()
Dm_Primary_Key_count = df_merged[dm_add_column].count()
WD_Primary_Key_count = df_merged[wd_add_column].count()

print(Merged_Primary_Key_count)
print(Dm_Primary_Key_count)
print(WD_Primary_Key_count)


Dm_Primary_Key_blank_count = Merged_Primary_Key_count - Dm_Primary_Key_count
WD_Primary_Key_blank_count = Merged_Primary_Key_count - WD_Primary_Key_count
mismatch_count = Dm_Primary_Key_blank_count + WD_Primary_Key_blank_count
Matching_records_count = Merged_Primary_Key_count - mismatch_count

print("Mismatch count DmVsWD: " + str(mismatch_count))

piechart_values_Dmvswd = {'Total records': Merged_Primary_Key_count, 'Matching records': Matching_records_count,'Mismatching records': mismatch_count}

df = pd.DataFrame(piechart_values_Dmvswd,index=['SrcVsWd'])

sheet_name = "Pie_chart"

writer = pd.ExcelWriter('H:\Automation\Python\Reconhire\Output files\Recon.xlsx', engine='xlsxwriter')

df.to_excel(writer,sheet_name=sheet_name)
workbook = writer.book
worksheet = writer.sheets[sheet_name]

#setting column width
worksheet.set_column('B:B',18, None)
worksheet.set_column('C:C',18, None)
worksheet.set_column('D:D',18, None)


# Creating chart for DmVsWD
chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'categories': '=Pie_Chart!C1:D1',
    'values':     '=Pie_Chart!C2:D2',
    'name': 'Source Ext vs WD Ext',
    'line': {'color':'black'},
'data_labels': {'percentage':True}
})
worksheet.insert_chart('C8', chart)

# Writing the merged dataframe in new sheets

df_merged[dm_add_column] = df_merged[dm_add_column].fillna("Additional")
df_merged[wd_add_column] = df_merged[wd_add_column].fillna("Missing")


df_merged[['Primary_Key',dm_add_column,wd_add_column]].to_excel(writer,sheet_name='DmVsWd_Primary_Key')
workbook = writer.book
worksheet = writer.sheets['DmVsWd_Primary_Key']

#setting column width
worksheet.set_column('B:B',18, None)
worksheet.set_column('C:C',18, None)
worksheet.set_column('D:D',18, None)

df_merged.to_excel(writer,sheet_name='DmVsWd')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print('Program completed')
