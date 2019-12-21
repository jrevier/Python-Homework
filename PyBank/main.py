#import csv
import os
import csv

#create path 
csvpath = os.path.join('..', 'PyBank', 'PyBank.csv')

#create variables
total_months = 0
average = 0
total = 0
greatest_increase = 0
g_increase_month = 0
greatest_decrease= 0
g_decrease_month = 0
month_change = []


#read data file

with open(csvpath, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  row = next(csvreader)
#calculate total months and changes
  total_months += 1
  total= total + int(row[1])
  prev_rev = int(row[1])
  greatest_increase = int(row[1])
  g_increase_month= row[0]
  running_total = 0
#loop through csv
  for row in csvreader: 

    total_months +=1
    total= total + int(row[1])
    month_change = int(row[1])- prev_rev
    running_total = running_total + month_change
    prev_rev= int(row[1])
#calculate greatest increase and decrease
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        g_increase_month = row[0]
    if int(row[1]) < greatest_decrease: 
        greatest_decrease = int(row[1])
        g_decrease_month = row[0]   
    average = running_total/(total_months-1)
#print results

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total Revenue: {str(total)}")
print(f"Average Change: ${str(average)}")
print(f"Greatest Increase: {str(g_increase_month)} (${str(greatest_increase)})")
print(f"Greatest Decrease: {str(g_decrease_month)} (${str(greatest_decrease)})")


#write new csv
output_file = os.path.join("PyBank_final.csv")
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
