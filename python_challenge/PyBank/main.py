import csv
import os


csvpath = os.path.join('raw_data', 'budget_data_1.csv')

columnsum = 0
date = []
revenue = []
diff = []
loop = 1

print('Financial Analysis')
print('_________________________')
with open(csvpath, newline='') as f:
    with open('output1.txt', 'w') as text_file:  
        text_file.write("Financial Analysis\n" +"_________________________\n" )
        
        next(f)
        counter=csv.reader(f,delimiter=",")
        totalmonths = str(len(list(counter)))
        print( "Total Months: " + totalmonths)
        text_file.write("Total Months : " + totalmonths + "\n")
        f.seek(0)

        next(f)
        total = 0
        for row in counter:
            total+=int(row[1])
        money=float(total)
        amountindollars = '${:,.2f}'.format(money)
        print("Total revenue: " +amountindollars)
        text_file.write("Total Revenue : " + amountindollars + "\n")
        f.seek(0)
        
        #get date
        next(f)
        for row in counter:
            date.append(row[0])
        f.seek(0)
        
        #get revenue
        next(f)
        L=csv.reader(f,delimiter=",")
        for row in L:
            revenue.append(row[1])
            zerorow = int(revenue[0])
        diff.append(int(zerorow))         
        while (int(totalmonths)-loop)>0:
            diff.append(int(revenue[loop])-int(revenue[loop-1]))
            loop=loop+1
        minvalue = min(diff)
        maxvalue = max(diff)
        maxdate = diff.index(maxvalue)
        mindate = diff.index(minvalue)
        averagechange=sum(diff)/int(totalmonths)
        formataverage = str('${:,.2f}'.format(averagechange))
        printmaxval = str('${:,.2f}'.format(maxvalue))
        printminval = str('${:,.2f}'.format(minvalue))
        
        print("Average Change : " + formataverage)
        print("Greatest Increase in Revenue : " + str(date[maxdate]) + " " + printmaxval)
        print("Greatest Decrease in Revenue : " + str(date[mindate]) + " " + printminval)

        text_file.write("Average Change : " + formataverage +"\n")
        text_file.write("Greatest Increase in Revenue : " + str(date[maxdate]) + " "+ printmaxval +"\n")
        text_file.write("Greatest Decrease in Revenue : " + str(date[mindate]) + " " + printminval + "\n")


columnsum = 0
date1 = []
revenue1 = []
diff1 = []
loop1 = 1        

csvpath2 = os.path.join('raw_data', 'budget_data_2.csv')
print('Financial Analysis')
print('_________________________')
with open(csvpath2, newline='') as f:
    with open('output2.txt', 'w') as text_file:  
        text_file.write("Financial Analysis\n" +"_________________________\n" )
        
        next(f)
        counter=csv.reader(f,delimiter=",")
        totalmonths = str(len(list(counter)))
        print( "Total Months: " + totalmonths)
        text_file.write("Total Months : " + totalmonths + "\n")
        f.seek(0)

        next(f)
        total = 0
        for row in counter:
            total+=int(row[1])
        money=float(total)
        amountindollars = '${:,.2f}'.format(money)
        print("Total revenue: " +amountindollars)
        text_file.write("Total Revenue : " + amountindollars + "\n")
        f.seek(0)
        
        #get date
        next(f)
        for row in counter:
            date1.append(row[0])
        f.seek(0)
        
        #get revenue
        next(f)
        L=csv.reader(f,delimiter=",")
        for row in L:
            revenue1.append(row[1])
            zerorow = int(revenue1[0])
        diff1.append(int(zerorow))         
        while (int(totalmonths)-loop1)>0:
            diff1.append(int(revenue1[loop1])-int(revenue1[loop1-1]))
            loop1=loop1+1
        minvalue = min(diff1)
        maxvalue = max(diff1)
        maxdate = diff1.index(maxvalue)
        mindate = diff1.index(minvalue)
        averagechange=sum(diff1)/int(totalmonths)
        formataverage = str('${:,.2f}'.format(averagechange))
        printmaxval = str('${:,.2f}'.format(maxvalue))
        printminval = str('${:,.2f}'.format(minvalue))
        
        print("Average Change : " + formataverage)
        print("Greatest Increase in Revenue : " + str(date1[maxdate]) + " " + printmaxval)
        print("Greatest Decrease in Revenue : " + str(date1[mindate]) + " " + printminval)

        text_file.write("Average Change : " + formataverage +"\n")
        text_file.write("Greatest Increase in Revenue : " + str(date1[maxdate]) + " "+ printmaxval +"\n")
        text_file.write("Greatest Decrease in Revenue : " + str(date1[mindate]) + " " + printminval + "\n")


            