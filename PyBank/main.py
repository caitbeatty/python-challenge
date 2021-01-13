# import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')


# Read using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is not a header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader: