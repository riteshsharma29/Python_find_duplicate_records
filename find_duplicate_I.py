#!/usr/bin/python
# coding: utf-8 -*-

import codecs
from collections import Counter

def find_duplicate_1(filename):

#empty set
    myset = set()
#empty list
    mylist = []

#read records.txt file 
    filename = codecs.open(filename,encoding='utf-8')

    log_file = codecs.open("log.txt",'w',encoding='utf-8')
    log_file.write("Below values are duplicate" + '\n' + '\n')

#Iterate through the file
    for rec in filename:
        rec = rec.replace('\n',"")
        if rec != "":
           myset.add(rec)
           mylist.append(rec)

    #convert set into list
    #all duplicates removed
    newlist = list(myset)

    c1 = Counter(mylist)
    c2 = Counter(newlist)

    diff = c1 - c2
    #Print duplicate values
    print list(diff.elements())

'''Change sample.txt with your file
call find_duplicate function'''

find_duplicate_1("sample.txt")