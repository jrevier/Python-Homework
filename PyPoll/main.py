#The total number of votes cast #
# A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#import csv
import os
import csv

#create path 
csvpath = os.path.join('..', 'PyPoll', 'PyPoll.csv')
#create variabes
total_votes = 0
vote_percentage = 0
candidate_votes = 0
winner = 0
candidate_list =[]
#PyPoll_data= {}
with open(csvpath, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  row = next(csvreader) 
  candidate = (str(row[2]))
  for row in csvreader:
    total_votes =+ 1
    def candidate_list ():
        candidate_list =[]
        candidate = (str(row[2]))
        for candidate in candidate_list:
            candidate_list.append(candidate)
        for candidate in candidate_list:
            return(candidate)    
print(candidate_list())
   

    


 #"""print(f"Election Results")
  #print("------------------")
  #print(f"Total Votes: {str(total_votes)}")

    #return report_data
#with open(csvpath, 'r') as csvfile:
  #csvreader = csv.reader(csvfile, delimiter=',')
  #header = next(csvreader)
  #row = next(csvreader)"""