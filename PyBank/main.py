import os
import csv

profit_losses = os.path.join("Resources", "Homework 3_PyBank_Resources_budget_data.csv")


with open(profit_losses,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvfile)

    months_count = 0
    profit_losses_count = 0 
    profitLossesList = []
    prev_row = 0
    differenceList = []

    for row in csvreader:
        months_count += 1
        profit_losses_count += int(row[1])
        profitLossesList.append(int(row[1]))

    for row in profitLossesList:
        difference = row - prev_row
        prev_row = row
        differenceList.append(difference)

    
    totalMonths = months_count
    total_profit_losses = profit_losses_count
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${total_profit_losses}")
    #print(profitLossesList)
    #print(differenceList)
    print(max(differenceList))
    print(min(differenceList))



    

