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
cand_votes = []
vote_percentage = 0
candidate_votes = 0
winner = 0
candidate = 0
candidate_list =[]
#PyPoll_data= {}
with open(csvpath, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  row = next(csvreader) 
  total_votes += 1
  for row in csvreader: 
      total_votes += 1
      if row[2] not in candidate_list: 
          candidate_list.append(row[2])
      for candidate in candidate_list: 
          cand_votes.append(row[0])

      #vote_percentage = (cand_votes/total_votes)*100
  print("Election Results")
  print("--------------------------------")
  print(f"Total Votes: {str(total_votes)}")
  print("--------------------------------")
  print (f"{str(candidate_list)}")
  print(f"{str(cand_votes)}")
  print(f"{str(vote_percentage)}")

    


 #"""print(f"Election Results")
  #print("------------------")
  #print(f"Total Votes: {str(total_votes)}")

    #return report_data
#with open(csvpath, 'r') as csvfile:
  #csvreader = csv.reader(csvfile, delimiter=',')
  #header = next(csvreader)
  #row = next(csvreader)"""