import csv
import os
import pandas as pd
import numpy as np


csvpath = os.path.join('raw_data', 'budget_data_1.csv')
columnsum = 0

print('Financial Analysis')
print('_________________________')
with open(csvpath, newline='') as f:
    next(f)
    counter=csv.reader(f,delimiter=",")
    
    totalmonths = str(len(list(counter)))
    print( "Total Months: " + totalmonths)
    f.seek(0)
    
    next(f)
    total = 0
    for row in counter:
        total+=int(row[1])
    money=float(total)
    amountindollars = '${:,.2f}'.format(money)
    print("Total revenue: " +amountindollars)
    f.seek(0)
    
    next(f)
    pd.read_csv(csvpath)
    columnsum = np.sum(row[1])
    print(columnsum)
    print("Average Revenue : ")
#    max = 0
#    maxdate = "date"
#    for row in counter:
#        if int(row[1])>int(max):
#                max = row[1]
#                maxdate=row[0]
#    money2=float(max) 
#    amountindollars2 = '${:,.2f}'.format(money2)
#    print("Average Revenue: " + float(int(amountindollars2/totalmonths)))
#    f.seek(0)
#    
#    next(f)
#
#title = input("Which title are you looking for?")
#is_found = tFalse
#
#with open(csvpath, 'rt') as f:
#    for row in reader:
#        if title == row[0]:
#            print("You are in luck! We have that title!" + row[0] + " is rated " + row[1] + " with a rating of " + row[6])
#            is_found = True
#            break
#    if is_found == False:
#        print("I am sorry we do not have that title.")