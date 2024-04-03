'''
something
'''

import os
import csv
import locale       
locale.setlocale(locale.LC_ALL,'')
'''
Source: StackAbuse.com https://stackabuse.com/format-number-as-currency-string-in-python/
After reading about a few modules, I decided to use what both ranked highly on google 
(meaning I'll likely find help more easily) and didn't require additional pip installs
'''

bank_csv = os.path.join("Resources","budget_data.csv")

month = []
pnl = []
change = []
last = 0

with open (bank_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")

    next(csv_read)   

    for row in csv_read:      
        month.append(row[0])
        pnl.append(float(row[1]))

        if last == 0:                   # nullifying first index in change to keep averaging RELATIVE INDEXING intact (1m - 0 = 1m)
            change.append(0)
        else:
            change.append(float(row[1])-last)
        last = float(row[1])

#total_months = len(month)
#big_inc = max(change)
#big_dec = min(change)
#total = sum(change) 
#average = sum(change) / (total_months - 1)
#average = ( pnl[(total_months-1)] - pnl[0] ) / total_months
#indy = change.index(big_inc)
print(f"\nFinancial Analysis \n")
print(f"---------------------------- \n")
print(f"Total Months: " + str(len(month)) + "\n")
print(f"Total: " + str(locale.currency(sum(pnl))) + "\n")
print(f"Average Change: " + str(locale.currency(sum(change) / (len(change) - 1))) + "\n") # len-1 ignores first index (null)
print(f"Greatest Increase in Profits: " + str(month[change.index(max(change))]) + " " + str(locale.currency(max(change))) + "\n")
print(f"Greatest Decrease in Profits: " + str(month[change.index(min(change))]) + " " + str(locale.currency(min(change))) + "\n")


