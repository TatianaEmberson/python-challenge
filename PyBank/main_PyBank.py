# -*- coding: UTF-8 -*-
import os
import csv
Resources_PyBank = os.path.join("Resources_PB", "budget_data2.csv")
file_to_output = os.path.join("Resources_PB", "budget_analysis.txt")

total_months = 0
month_of_change =[]
net_change_list=[]
greatest_increase =["",0]
greatest_decrease = ["", 9999999999999999]
total_profits = 0
with open (Resources_PyBank) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row =next(csvreader)
   # first_row =next(csvreader)
    total_months += 1

    total_profits+=float(first_row[1])
    prev_net= float(first_row[1])

# Append months and profits to lists
    for rows in csvreader:
        total_months += 1
        print("row1")
        print(rows[1])
        print("profits")
        print(total_profits)
        #total_profits=int(total_profits)
        total_profits+=float(rows[1])
        net_change=float(rows[1])-prev_net
        prev_net = float(rows[1])
        net_change_list+= [net_change]
        month_of_change += [rows[0]]

        if net_change >  greatest_increase[1]:
            greatest_increase[0]=rows[0]
            greatest_increase[1]=net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=rows[0]
            greatest_decrease[1]=net_change
        
revenue_average = sum(net_change_list) / len(net_change_list)

output=(
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit: {total_profits}\n"
    f"Average Change: {revenue_average:.2f}\n"
    f" Greatest Increase: {greatest_increase[0]} , {greatest_increase[1]}\n"
    f" Greatest Decrease: {greatest_decrease[0]} , {greatest_decrease[1]}\n"
)
print (output)
    
# Export the results to te
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)