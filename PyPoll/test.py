import os
import csv

votefilename = input ("Enter name of csv file")

#define filepath and open csv file in read mode
votefilepath = os.path.join("raw_data", votefilename + ".csv")

with open (votefilepath, 'r', newline ="") as votecsv:
    #split the data on commas
    csvreader = csv.reader(votecsv, delimiter=',')

    #skip headers
        #Voter ID
        #County
        #Candidate
    next(csvreader, None)
    
candidates=[]
votecount=[]

#1)The total number of votes casted
totvotecount = 0
    #loop through the rows in the file
for row in csvreader:
    if row[0] != "":
        totvotecount = totvotecount + 1

#2) A complete list of candidates who received votes
#4) The total number of votes each candidate won
    if row[2] not in candidates:
            candidates.append(row[2])
            votecount.append(1)
    else:
        votecount [index(candidates(row[2]))] = votecount [index(candidates(row[2]))] + 1
votedict ={}
numcandidates = len(candidates)
print (numcandidates)
#for x in range (len(candidates))
#votedict [candidates[x]]=votecount[x]

print ("Election Results \n ---------------------------------")
print ("Total Votes: " + totvotecount)
print ("--------------------------------")
#4) The total number of votes each candidate won
#3) The percentage of votes each candidate won
for x in range(len(candidates)):
    for k, v in votedict.items()
    print (k + ": "+ v/totvotecount+ "%" +" (" +v+")")
print ("--------------------------------")
        
#5) The winner of the election based on popular vote.
winner = max(votedict, key = votedict.get)
print ("Winner: "+ winner)    

```
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
```