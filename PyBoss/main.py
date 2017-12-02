
# coding: utf-8

# In[33]:


import os
import csv
from datetime import datetime


# In[34]:


rawfile = input("Enter name of file")
rawfilepath = os.path.join("raw_data",rawfile + ".csv")
#print (rawfilepath)


# In[39]:


outputfile = input("Enter output file name")
with open(rawfilepath, 'r',newline="") as master, open(outputfile+".csv", 'w',newline="") as matched:
    cr = csv.reader(master)
    cw = csv.writer(matched)
    # write header to new file
    cw.writerow(next(cr))  


# In[40]:


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[41]:


with open(rawfilepath, "r", newline = "") as bossdata:
    bossdatacsv = csv.reader(bossdata, delimiter=',')

    #skip headers
    next(bossdatacsv, None)
    
    for row in bossdatacsv:
#The Name column should be split into separate First Name and Last Name columns. 
        first, last = row[1].split(" ") 
        #print (first, last)

#The DOB data should be re-written into DD/MM/YYYY format.
        oldformat = row[2]
        datetimeobject = datetime.strptime(oldformat,'%Y-%m-%d')
        newformat = datetimeobject.strftime('%m/%d/%Y')
        #print (newformat)

#The SSN data should be re-written such that the first five numbers are hidden from view.
        set1, set2, set3 = row[3].split("-")
        encryptedssn = "***-***-"+set3
        #print (encryptedssn)

#The State data should be re-written as simple two-letter abbreviations.
        for k, v in us_state_abbrev.items():
            s = us_state_abbrev[row[4]]
        employee = [row[0], first, last, newformat, s]
        #print (employee)
        with open(outputfile+".csv", 'a',newline="") as matched:
            cw = csv.writer(matched)
            cw.writerow(employee)

