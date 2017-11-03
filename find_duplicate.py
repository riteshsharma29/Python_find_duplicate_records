#!/usr/bin/python
# coding: utf-8 -*-

import codecs,sys
import pandas as pd



def find_duplicate(filename):

#empty lists
    unq = []
    dup = []

#read records.txt file 
    filename = codecs.open(filename,encoding='utf-8')

    log_file = codecs.open("log.txt",'w',encoding='utf-8')
    log_file.write("Below values are duplicate" + '\n' + '\n')

#Iterate through the file
    for rec in filename:
        rec = rec.replace('\n',"")
        if rec != "" and rec not in unq:
            unq.append(rec)
        elif rec != "" and rec in unq:
            dup.append(rec)

#log duplicate values
    for vals in dup:        
        log_file.write(vals + '\n')
        print vals

'''Change sample.txt with your file
call find_duplicate function'''

find_duplicate("sample.txt")

#################################################################################################################

def find_duplicate_excel(excelfile,sheet,colheadr):

    df = pd.read_excel(excelfile,sheetname=sheet)

#empty lists
    unq = []
    dup = []

#read records from the excel column
    colvalues = df['Movies'].values

    log_file = codecs.open("excel_log.txt",'w',encoding='utf-8')
    log_file.write("Below values are duplicate in excel file's " + str(colheadr) + " column" + '\n' + '\n')


#Iterate through the column values
    for rec in colvalues:
        rec = rec.replace('\n',"")
        if rec != "" and rec not in unq:
            unq.append(rec)
        elif rec != "" and rec in unq:
            dup.append(rec)

#log duplicate values
    for vals in dup:        
        log_file.write(vals + '\n')
        print vals

'''Change sample.xlsx with your file
call find_duplicate_excel function
first parameter - excel filename
second parameter - excel sheet name
third parameter -column header consisting values 
'''

find_duplicate_excel('sample.xlsx','test','Movies')



