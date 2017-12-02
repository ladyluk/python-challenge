import os
import csv
#define filepath and open csv file in read mode
budget_data_file = input "Enter name of csv file" + ".csv"
budget_data_path = os.path.join("raw_data", budget_data_csv)

with open (budget_data_path, 'r') as budget_data_csv
	#split the data on commas
	csvreader = csv.reader(budget_data_csv, delimiter=',')
#print the following to the terminal:
#The total number of months included in the dataset

#The total amount of revenue gained over the entire period

#The average change in revenue between months over the entire period

#The greatest increase in revenue (date and amount) over the entire period

#The greatest decrease in revenue (date and amount) over the entire period

#export a text file with the results