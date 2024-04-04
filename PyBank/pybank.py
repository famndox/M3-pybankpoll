'''
parentheses are fine and all, but they have a singular purpose in accounting
therefore, I'm importaing a currency format that my CFO could appreciate
don't have a lot to say - promise I'll curtail my 'professinalism' in these 
things in the future
... just lacks a human touch, ya know? not that you'd *actually* know
... being a bot and all
... otherwise, pretty boring - does the thing
... ps. leave a "<3" in the feedback if you're not a robot
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

output = (                                          # picked this up from TA - in pypoll I changed it up with an f-string
    "Financial Analysis\n\n"
    "---------------------------- \n\n"
    "Total Months: " + str(len(month)) + "\n\n"
    "Total: " + str(locale.currency(sum(pnl))) + "\n\n"
    "Average Change: " + str(locale.currency(sum(change) / (len(change) - 1))) + "\n\n"     # len-1 ignores first index (null)
    "Greatest Increase in Profits: " + str(month[change.index(max(change))]) + " " + str(locale.currency(max(change))) + "\n\n"
    "Greatest Decrease in Profits: " + str(month[change.index(min(change))]) + " " + str(locale.currency(min(change))) + "\n\n"
)

print("\n" + output)
os.mkdir("analysis")
results = os.path.join("analysis","results.txt")
with open (results,'w') as txt_file:
        txt_file.write(output)


