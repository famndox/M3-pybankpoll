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
        month.append(row[0])                        # copies Month column and stores to month[]
        pnl.append(float(row[1]))                   # copies Profit/Loss column and stores to pnl[]

        if last == 0:                               # nullifying first index in change[] to keep averaging clean in change[]
            change.append(0)                        # ..! also keeps relative indexing in tact from list to list
        else:
            change.append(float(row[1])-last)       # takes the difference between this and last period and stores to change[] 
        last = float(row[1])                        # final action of loop: stores this period as last to perform the above

print(f"\nFinancial Analysis \n")
print(f"---------------------------- \n")
print(f"Total Months: " + str(len(month)) + "\n")
print(f"Total: " + str(locale.currency(sum(pnl))) + "\n")
print(f"Average Change: " + str(locale.currency(sum(change) / (len(change) - 1))) + "\n") # len-1 ignores first index (null)
print(f"Greatest Increase in Profits: " + str(month[change.index(max(change))]) + " " + str(locale.currency(max(change))) + "\n")
print(f"Greatest Decrease in Profits: " + str(month[change.index(min(change))]) + " " + str(locale.currency(min(change))) + "\n")


