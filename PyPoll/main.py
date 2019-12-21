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
#create variables
total_votes = 0
cand_votes = []
vote_percentage = 0
candidate_votes = 0
winner = 0
candidate_list =[]
cand_dict = {}
cand_dict2 = {}
#read csv file
with open(csvpath, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  row = next(csvreader) 
  #calculate total votes
  total_votes += 1
  for row in csvreader: 
      total_votes += 1
 #make list of candidates and find their total votes
      if row[2] not in candidate_list: 
          candidate_list.append(row[2])
          cand_dict[row[2]] = 1
      cand_dict[row[2]] += 1
    #candidate percentage of votes
  for candidate in cand_dict.keys():  
      cand_dict2[candidate]= cand_dict[candidate]/total_votes*100
      Keymax = max(cand_dict, key=cand_dict.get)
#print results
  print("Election Results")
  print("--------------------------------")
  print(f"Total Votes: {str(total_votes)}")
  print("--------------------------------")
  
  for c in cand_dict.keys():
      print(c,": %",cand_dict2[c]," (",cand_dict[c],")",sep="")   
  print("--------------------------------")
  print (f"Winner: {str(Keymax)}")
#write csv file


