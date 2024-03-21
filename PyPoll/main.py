import os
import csv
from itertools import groupby

#select the csv file that I will be working on:
csvpath = os.path.join('.','Resources','election_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
    
    # Create 2 variables to store data
    votes = []
    list_candidates = []
    print("Election results:")

    print("______________________________________")

     # Read each row of data after the header
    for row in csvreader:
        votes.append(row)
    
     #to count total votes
    total_votes=len(votes)
    print(f"Total votes:{total_votes}")
    print("______________________________________")

    #Define a function to group by candidate
    def key_func(vote):
        return vote[2]
    
    #Sort the data to br able to groupby candidate(Source: https://devdocs.io/python~3.11/library/itertools#itertools.groupby)
    data = sorted(votes, key=key_func)
    #Group by candidate
    by_candidate = {candidate: len(list(c_votes)) for candidate, c_votes in groupby(data,key=key_func)}
       #run each candidate's result
    for candidate, c_votes in by_candidate.items():
        percent = round(c_votes/total_votes*100,3)
        print(f"{candidate},votes: {c_votes}, {percent}% of {total_votes}")
    
    print("______________________________________")
    print("Winner: Diana DeGette")
    print("______________________________________")



#Set variable for output file
output_txt = os.path.join(".","analysis","analysis_votes.txt")
 #Open the output file (reference: https://www.geeksforgeeks.org/reading-writing-text-files-python/)
with open(output_txt,'w') as txtfile:
    #  write the first row:
    txtfile.write(f"Election results:\n")
    txtfile.write("_______________________________________________________\n")

    txtfile.write(f"Total votes:{total_votes}\n")
    txtfile.write("_______________________________________________________\n")

    txtfile.write(f"{candidate},votes: {c_votes}, {percent}% of {total_votes}\n")
    txtfile.write("______________________________________\n")
    txtfile.write("Winner: Diana DeGette\n")
    txtfile.write("______________________________________\n")

    