# import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')



# make empty lists 
total_months = []
total_amount= []
profit_change = []



# open using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # To add in the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Read each row of data after the header 
    #for row in csvreader:
        #print(row)
    
    #run through the rows in the file
    for row in csvreader:

        #loop through  months
        total_months.append(row[0])
        
        #loop through profit
        total_amount.append(int(row[1]))

    
#calculate total months   
months= len(total_months)


# loop through all amounts 
num_loops= len(total_amount)-1
for x in range(num_loops):

 #append    
    profit_change.append(total_amount[x+1]-total_amount[x])
	        
# Get  max profit change
max_profit_change = max(profit_change)
#Get min profit change 
min_profit_change = min(profit_change)
	

# Figure out which month the max increase is connected to
max_profit_month = profit_change.index(max(profit_change)) + 1
# Figure out which month the max decrease is connected to
min_profit_month = profit_change.index(min(profit_change)) + 1 
	

# print outputs
	

print("Financial Analysis")
print("-------------")
print(f"Total Months: {months}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_profit_month]} (${(max_profit_change)})")
print(f"Greatest Decrease in Profits: {total_months[min_profit_month]} (${(min_profit_change)})")
	 

#export to text file
txtpath = os.path.join('.', 'txtfile_results.txt')
with open(txtpath, "w") as f:   
    
    # Opens file and casts as f 
    f.write("Financial Analysis\n")
    f.write("-------------\n")
    f.write(f"Total Months: {months}\n")
    f.write(f"Total: ${sum(total_amount)}\n")
    f.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n")
    f.write(f"Greatest Increase in Profits: {total_months[max_profit_month]} (${(max_profit_change)})\n")
    f.write(f"Greatest Decrease in Profits: {total_months[min_profit_month]} (${(min_profit_change)})\n") 
    

