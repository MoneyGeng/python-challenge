# Importing dependencies
import os
import csv

# Set path to csv file
csv_path = 'C:\\Users\\John\\Desktop\\Data Analytics Bootcamp\\UTOR-VIRT-DATA-PT-12-2022-U-LOLC-main\\03-Python\\Challenge\\python-challenge\\PyBank\\Resource\\budget_data.csv'

# Creating empty lists
months_list = []
amounts_list = []
monthly_change_list = []

# Declaring variables
total_months = 0 
total_amounts = 0
average_change = 0
greatest__increase_value = 0
greatest__decrease_value = 0
greatest__increase_month = ''
greatest__decrease_month = ''

# Set output file path
output_path = "C:\\Users\\John\\Desktop\\Data Analytics Bootcamp\\UTOR-VIRT-DATA-PT-12-2022-U-LOLC-main\\03-Python\\Challenge\\python-challenge\\PyBank\Analysis\\Financial_Analysis_Summary.txt"

# Reading csv file
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skipping header row
    next(csv_reader)

    # iterate through rows in the csv file
    for row in csv_reader:

        # Appending values of each row into corresponding lists
        months_list.append(row[0])
        amounts_list.append(int(row[1]))

    # Set variables to hold number of months and total profit/losses
    total_months = len(months_list)
    total_amounts = sum(amounts_list)

    # Iterate through amount list to get mohtly change in amounts
    for i in range(len(amounts_list) - 1):

        # Taking the difference between two months and appending to monthly_change_list 
        monthly_change_list.append(amounts_list[i + 1] - amounts_list[i])

    # Calculating average changes in profit and losses over entire period and storing in variable
    average_change = sum(monthly_change_list)/len(monthly_change_list)

    # Storing min and max of monthly change list
    greatest__increase_value = max(monthly_change_list)
    greatest__decrease_value = min(monthly_change_list)

    # Obtaining correlating min and max months from months list by using index of min and max amounts
    # Adding 1 to index as associated month with change is the month after
    greatest__increase_month = months_list[monthly_change_list.index(max(monthly_change_list)) + 1]
    greatest__decrease_month = months_list[monthly_change_list.index(min(monthly_change_list)) + 1]

# Printing statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amounts}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest__increase_month} (${greatest__increase_value})")
print(f"Greatest Decrease in Profits: {greatest__decrease_month} (${greatest__decrease_value})")

# Outputting results
with open(output_path,"w") as file:

    # Writing statements to text file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_amounts}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest__increase_month} (${greatest__increase_value})\n")
    file.write(f"Greatest Decrease in Profits: {greatest__decrease_month} (${greatest__decrease_value})\n")

    