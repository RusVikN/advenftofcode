#!/usr/bin/python3

import csv

with open('day1elfs.txt') as file:
    fList = list(csv.reader(file))
print(fList)

elfs = []     
elfOne = []
for f in fList:
    if len(f)==0 or f[0]==' ':
        elfs.append(sum(elfOne))
        elfOne = []
    else:
        elfOne.append(int(f[0]))
         
print(max(elfs), elfs)
print()

