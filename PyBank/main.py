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
    data = []
   
  

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
    #subtract row from previous row using i-1
    #start at 0, but instead of appending first if statement to average_list, append to new list
    #This way we can keep the average the same without having the header as 1 count
    for i in range(0, len(net_total)):
        if i == 0:
            data.append(0)
        else:
            x = net_total[i] - net_total[i-1]
            average_list.append(x) 

            total_average = mean(average_list) 
    
    #add that 0 index value into average list to get index of max/min months
    data2 = (data + average_list)
   
   
    #grab the months
    #find the index of the max profit 
    #using that index, find the same index for the months since they have the same values in the list

    max_month = month_list[data2.index(max(data2))] 
    min_month = month_list[data2.index(min(data2))]  


#set text file to output
output_path = os.path.join("Analysis", "Budget_data.txt")

with open(output_path, 'w') as txtfile:
    
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", total_months)
    print(f"Total: ${total}")
    print(f"Average Change: ${round(total_average, 2)}")
    print(f"Greatest Increase in Profits: {max_month} ${max(average_list)}")
    print(f"Greatest Decrease in Profits: {min_month} ${min(average_list)}")

    txtfile.write(f"\nFinancial Analysis\n")
    txtfile.write(f"\n-------------------------------\n")
    txtfile.write(f"\nTotal Months: {total_months}\n")
    txtfile.write(f"\nTotal: ${total}\n")
    txtfile.write(f"\nAverage Change: ${round(total_average, 2)}\n")
    txtfile.write(f"\nGreatest Increase in Profits: {max_month} ${max(average_list)}\n")
    txtfile.write(f"\nGreatest Decrease in Profits: {min_month} ${min(average_list)}\n")

    






        










    





