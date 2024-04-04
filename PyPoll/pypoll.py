'''
first, something clever... 
I once found a rock which measured 1760 yards in len() 
now, something thoughtful...
must have been some kind of milestone
...
anyways, enjoy my abuse of len()
'''


import os
import csv

polls_csv = os.path.join("Resources","election_data.csv")

chuck = "Charles Casper Stockham"           # I'm not typing these out again
diana = "Diana DeGette"
ray = "Raymon Anthony Doane"
votes = []                                  # creates a total votes list to be counted
cv = []                                     # creates a list of only chuck's votes
dv = []                                     # you get the idea...
rv = []                                     # PS. ((I'm going to count using len()))

with open (polls_csv, encoding='utf-8') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    next(csv_read)

    for row in csv_read:
        votes.append(row[2])                # copies Candidates column and stores to votes[]

        if row[2] == chuck:                 # copies only chucks votes to cv[]
            cv.append(row[2])               
        elif row[2] == diana:               # yada, yada, dianna 
            dv.append(row[2])
        else:                               # this else clause probably isn't the cleanest
            rv.append(row[2])               # way to "[insert here] proof" this, but I happen 
                                            # to know there are only 3 candidates in the file

most = max(len(cv),len(dv),len(rv))         # I warned you above

if most == len(cv):                         # loop to vet max count does at least two things:
        winner = chuck                                
elif most == len(dv):                           # -it's clever enough to read a new dataset
        winner = diana                              # (provided you don't add candidates)            
elif most == len(rv):                                                 
        winner = ray                            # -it allows me to debug    
else: winner = "Sorry sonny, you've got a bug"  

output = (                                  # defining output variable that started life 
    f"\nElection Results\n\n"               # as a print function... again abusing len()
    f"---------------------------- \n\n"
    f"Total Votes: {len(votes)}\n\n"
    f"---------------------------- \n\n"
    f"{chuck}: {len(cv) / len(votes) * 100:.3f}% ({len(cv)})\n\n"
    f"{diana}: {len(dv) / len(votes) * 100:.3f}% ({len(dv)})\n\n"
    f"{ray}: {len(rv) / len(votes) * 100:.3f}% ({len(rv)})\n\n"
    f"---------------------------- \n\n"
    f"Winner: {winner}\n\n"
    f"---------------------------- \n\n"
)

print("/n" + output)                        # print output to terminal
os.mkdir("analysis")                        # create directory and print as text file
results = os.path.join("analysis","results.txt")
with open (results,'w') as txt_file:
        txt_file.write(output)
