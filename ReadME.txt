James Behnke - Module 3 Challenge

File Paths:

M3-pybankpoll
	ReadME.txt <-- [[you are here!]]
	PyBank
		pybank.py <- does the first part
		Resources
			budget_data.csv
		analysis <-- to be generated after pybank.py run (within it a txt)
	PyPoll
		pypoll.py <- does the second part
		Resources
			election_data.csv
		analysis <-- to be generated after pypoll.py run (within it a txt)
		

I see why we did this before learning jupyter, but can also sense I could have been 
far more concise with my scripts. Mostly referenced the homework, googled stuff, 
changed code and ran often in git bash. 

The two external and noteworthy realms I dove into were:

- how to use an accounting function to acoomodate for the negative currency values
- - commented in py.bank
- - Source: StackAbuse.com https://stackabuse.com/format-number-as-currency-string-in-python/

- how to get three decimal places for my float(average)
- - no comments in py.poll 
- - source: stackoverflow, multiple sub-comments steering folks away from "rounding"
- - just kind of went for it via trial and error
- - and accidentally discovered f-strings still work outside a print statement

Oh yea, I originally used various print() statements as I was writing to actively debug. 

Peace, love, etc	