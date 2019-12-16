#import csv
import os
import csv

#create path 
csvpath = os.path.join('..', 'PyBank', 'PyBank.csv')


#define report data
def report_data(PyBank_data):
    month= (PyBank_data[0])
    def average(PyBank_data):
        return sum(PyBank_data[1]/len(PyBank_data[1]))
    average_count= average
    month_count = sum(1 for row in csv.reader( open('PyBank.csv') ) )
    Total = int(PyBank_data[1])
    greatest_increase= max(PyBank_data[1])
    greatest_decrease= min(PyBank_data[1])
#print data
    print(f"Financial Analysis")
    print(f"Total Months: {month_count-1}")
    print(f"Total: {str(Total)}")
    print(f"Average Change: {average}")
    print(f"Greatest Increase: {str(month)} {str(greatest_increase)}")
    print(f"Greatest Decrease {str(month)} {str(greatest_decrease)}")
#read csv file
with open(csvpath, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  report_data



output_file = os.path.join("PyBank_final.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(cleaned_csv)
