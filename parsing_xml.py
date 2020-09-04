import xml.etree.ElementTree as ET
import xlsxwriter 

workbook = xlsxwriter.Workbook('your_data_has_been_extracted_1.xlsx') 
worksheet = workbook.add_worksheet() 

tree = ET.parse('example_data_1.xml')
root = tree.getroot()
row = 0
column = 0
text='.//*'
name_list=[]
found=tree.findall(text)
value_row=0
value_column=0


for i in found:
    name_list.append(i.tag)


new_set=list(set(name_list))

cell_format = workbook.add_format({'bold': True, 'font_color': 'blue'})

row = 0
column = 0
for i in new_set:
    count=0
    for node in tree.findall(text):
        if str(i) == str(node.tag) and node.text:
            worksheet.write(row, column, i, cell_format)
            value_row+=1
            worksheet.write(value_row, value_column, node.text)
            count+=1
    value_row=0
    column+=1
    value_column+=1
workbook.close()

