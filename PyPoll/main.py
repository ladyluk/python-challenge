
# coding: utf-8

# In[15]:


import os
import csv


# In[16]:


votefilename = input ("Enter name of csv file")


# In[18]:


#define filepath and open csv file in read mode
votefilepath = os.path.join("raw_data", votefilename + ".csv")


# In[19]:


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
            #candidatesname = row[2]
            #candidatesindext = candidates.index(candidatesname)
            #print (candidates[row[2]])
            votecount [candidates.index(row[2])] = votecount [candidates.index(row[2])] + 1
votedict ={}
numcandidates = len(candidates)
print (numcandidates)
for x in range (len(candidates)):
    votedict [candidates[x]]=votecount[x]
    
print (candidates)
print (votedict)


# In[20]:


print ("Election Results \n ---------------------------------")
print ("Total Votes: " + str(totvotecount))
print ("--------------------------------")
#4) The total number of votes each candidate won
#3) The percentage of votes each candidate won
for k, v in votedict.items():
    print (k + ": "+ str(v/totvotecount)+ " (" +str(v)+")")
print ("--------------------------------")
        
#5) The winner of the election based on popular vote.
winner = max(votedict, key = votedict.get)
print ("Winner: "+ winner)    
print ("--------------------------------")


# In[22]:


#export to text file
newfilename = input ("what is the new file name?")
#newfilepath = os.path.join("raw_data", votefilename + ".csv")

with open (newfilename + '.txt', 'w') as f:

    print ("Election Results", file = f) 
    print ("--------------------------------", file = f)
    print ("Total Votes: " + str(totvotecount), file = f)
    print ("--------------------------------", file = f)
   
    #4) The total number of votes each candidate won
    #3) The percentage of votes each candidate won
    for k, v in votedict.items():
        print(k + ": "+ str(v/totvotecount)+ " (" +str(v)+")", file =f)
    print ("--------------------------------", file = f)

    #5) The winner of the election based on popular vote.
    winner = max(votedict, key = votedict.get)
    print ("Winner: "+ winner, file = f)   
    print ("--------------------------------",file = f)
f.close()

