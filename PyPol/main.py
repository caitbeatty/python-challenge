# import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

#create list of candidate names
candidate = []
candidate_vote = []
candidate_index = 0

# open csv 

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # loop through to pull unique names and add to count
    for row  in csvreader: 
        if row [2] not in candidate: 
            candidate.append(row[2]) 
            candidate_vote.append(int(1))
        else:
            candidate_index = candidate.index(row[2])
            candidate_vote[candidate_index] = candidate_vote[candidate_index] + 1

   
    #get total votes
    total_votes = sum(candidate_vote)

    #percentage vote
    #percent = int(candidate_vote)/int(total_vote)

    # determine winner
    winner = candidate_vote.index(max(candidate_vote))

#print statements
print("election results")
print("-------------")
print (f"total votes {total_votes}")
print("-------------")
#print (candidate)
#print (candidate_vote)

for index in range(len(candidate)):
    name = candidate[index]
    percent = "{:.3f}".format (candidate_vote[index]/total_votes * 100)
    print(f"{name}: {percent} % ({candidate_vote[index]})")

print("-------------")
print(f"winner:{candidate[winner]}")
print("-------------")

#export to text file

#export to text file
txtpath = os.path.join('.', 'txtfile_results.txt')
with open(txtpath, "w") as f:   
    
    # Opens file and casts as f 
    f.write("election results\n")
    f.write("-------------\n")
    f.write(f"total votes {total_votes}\n")
    f.write("-------------\n")

    for index in range(len(candidate)):
        name = candidate[index]
        percent = "{:.3f}".format (candidate_vote[index]/total_votes * 100)
        f.write(f"{name}: {percent} % ({candidate_vote[index]})\n")

    
    f.write("-------------\n")
    f.write(f"winner:{candidate[winner]}\n")
    f.write("-------------\n")
    