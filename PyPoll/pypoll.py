'''
something thoughtful
'''

import os
import csv

polls_csv = os.path.join("Resources","election_data.csv")

votes = []
chuck = "Charles Casper Stockham"
diana = "Diana DeGette"
ray = "Raymon Anthony Doane"
cv = []
dv = []
rv = []

with open (polls_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    next(csv_read)

    for row in csv_read:
        votes.append(row[2])

        if row[2] == chuck:
            cv.append(row[2])
        elif row[2] == diana:
            dv.append(row[2])
        else:
            rv.append(row[2])

most = max(len(cv),len(dv),len(rv))

if most == len(cv):
        winner = chuck
elif most == len(dv):
        winner = diana
elif most == len(rv):
        winner = ray
else: winner = "Sorry sonny, you've got a bug"

print(f"something" + str( len(cv) / len(votes) ))

print(f"\nElection Results\n")
print(f"---------------------------- \n")
print(f"Total Votes: " + str(len(votes)) + "\n")
print(f"---------------------------- \n")
print(f"{chuck}: " + str(len(cv)) +"\n")
print(f"{diana}: " + str(len(dv)) +"\n")
print(f"{ray}: " + str(len(rv)) +"\n")
print(f"---------------------------- \n")
print(f"Winner: {winner}\n")
print(f"---------------------------- \n")

