import csv
import pandas as pd

from collections import Counter

with open('raw_data/budget_data_1.csv', 'r') as f:
    row_count = sum(1 for row in f)
    row_count_total = row_count - 1 #remove count for header
    print('Total Number of Months: ' + str(row_count_total))
    
def average_column(budget_data_1):
    column_totals = Counter()
    with open('raw_data/budget_data_1.csv', 'r') as j:
        reader = budget_data_1.reader(j)
        row_count = 0
        for row in reader:
            for column_idx, column_value in enumerate(row):
                try:
                    n = float(column_value)
                    column_totals[column_idx] += n
                except ValueError:
                    print("Error -- ({}) Column({}) could not be converted to float!".format(column_value, column_idx))
                row_count += 1
                print(average_column)