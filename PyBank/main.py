import os
import csv
from statistics import mean

#get to csv file
budget_file = os.path.join("Resources", "budget_data.csv")

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
        value1 = str(row['Date'])
        net_total.append(value)
        month_list.append(value1)
        total = sum(net_total)


    #get average change in profit/loss over entire period
    #set i to loop through all rows
    #subtract row from previous row using i-1
    for i in range(1, len(net_total)):
        x = net_total[i] - net_total[i-1] 
        average_list.append(x) 

        total_average = mean(average_list) 

   

    #find the index below the max in order to pull the month it came from
    
    #grab the months
    #find the index of the max profit 
    #using that index, find the same index for the months since they have the same values in the list

    max_month = month_list[average_list.index(max(average_list))] 
    min_month = month_list[average_list.index(min(average_list))]  

    
    

print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", total_months)
print(f"Total: ${total}")
print(f"Average Change: ${round(total_average, 2)}")
print(f"Greatest Increase in Profits: {max_month} ${max(average_list)}")
print(f"Greatest Decrease in Profits: {min_month} ${min(average_list)}")






        










    





