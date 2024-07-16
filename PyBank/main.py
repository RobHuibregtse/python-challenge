#Import modules needed to read csv from filepath
import os
import csv

#Find flat file and open it
budget_data_path = os.path.join("Resources","budget_data.csv")
budget_data_file = open(budget_data_path)

#Load flat file into Dictionary
budget_data = list(csv.DictReader(budget_data_file, delimiter=","))

#Calculate total number of months
total_months = len(budget_data)

#Calculate total
profits = [float(row["Profit/Losses"]) for row in budget_data]
total = sum(profits)

#Set 'Change' key to 0 for the first month in the list
budget_data[0]['Change'] = 0 

#Iterate through budget_data
for i in range(1, len(budget_data)):

    #Define change variable 
    change = int(budget_data[i]['Profit/Losses']) - int(budget_data[i-1]['Profit/Losses'])
    #Add change value to new key in dictionary
    budget_data[i]['Change'] = change

#Create list of change values
changes = [d['Change'] for d in budget_data]
#Calculate average change (and disregard the extra 0 value added to the first month by subracting 1 from the length of the list)
average_change = sum(changes)/(len(changes)-1)

#Find the month with the greatest increase in profits (variable stored as a unique disctionary)
max_increase_month = max(budget_data, key=lambda x: x['Change'])

#Find the month with the greatest decrease in profits (variable stored as a unique disctionary)
max_decrease_month = min(budget_data, key=lambda x: x['Change'])

#Define keys for use in f-strings, because for some reason it wouldn't accept the key otherwise
datekey = 'Date'
changekey = 'Change'
#Print statement
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {total_months}')
print(f'Total : {round(total)}')
print(f'Average Change: {round(average_change)}')
print(f'Greatest Increase in Profits: {max_increase_month[datekey]} ({max_increase_month[changekey]})')
print(f'Greatest Decrease in Profits: {max_decrease_month[datekey]} ({max_decrease_month[changekey]})')

#Open new file in write mode and write output to file
with open("Analysis/financial_analysis.txt","w") as file:
    file.write(f'Financial Analysis \n')
    file.write(f'-------------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total : {round(total)}')
    file.write(f'Average Change: {round(average_change)}\n')
    file.write(f'Greatest Increase in Profits: {max_increase_month[datekey]} ({max_increase_month[changekey]})\n')
    file.write(f'Greatest Decrease in Profits: {max_decrease_month[datekey]} ({max_decrease_month[changekey]})')