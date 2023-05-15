import os
import csv
from statistics import mean

#get to csv file
budget_file = os.path.join("..", "Resources", "budget_data.csv")

#open file using DictReader to read in the file
with open(budget_file, 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file, delimiter=",")

    #set variables
    net_total = []
    average_list = []
    month_list = []

#for the total months, use enumerate to count each month and index, starting at 1
    for total_months, row in enumerate(csv_reader, start=1):


        #get full list of profit/loss and put it into net_value
        #get sum of all the data
        value = int(row['Profit/Losses'])
        net_total.append(value)
        total = sum(net_total)


    #get average change in profit/loss over entire period
    #set i to loop through all rows
    #subtract row from previous row using i-1
    for i in range(1, len(net_total)):
        x = net_total[i] - net_total[i-1] 
        average_list.append(x) 

        total_average = mean(average_list) 

    #grab the months
   
     
          
#print(month_list)

print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", total_months)
print(f"Total: ${total}")
print(f"Average Change: ${round(total_average, 2)}")
print(f"Greatest Increase in Profits: ${max(average_list)}")
print(f"Greatest Decrease in Profits: ${min(average_list)}")






        










    





