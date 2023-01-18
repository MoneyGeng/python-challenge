# Importing dependencies
import os
import csv

# Set path to csv file
csv_path = "Challenge\\python-challenge\\PyPoll\\Resource\\election_data.csv"

# Set Output path
output_path = "Challenge\\python-challenge\\PyPoll\\Analysis\\Election_Results.txt"

# Creating empty candidate list
candidate_list = []

# Creating dictionary for candidates and their votes
candidate_votes_dict = {} 

# Declaring variables
total_votes = 0

# Reading csv file
with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skipping header row
    next(csv_reader)

    # Iterate through rows in csv file
    for row in csv_reader:
        
        # Tabulating total number of votes
        total_votes += 1

        # Appending unique values in candiate column to create candidate list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        # Iterating though elements of Candidate list
        for candidate in candidate_list:

            # Adding list elements to candidate dictionary as keys
            if candidate not in candidate_votes_dict:
                candidate_votes_dict[candidate] = 0
            
            # Tabulating votes to each candidate
            if row[2] == candidate:
                candidate_votes_dict[candidate] += 1

# Return the winner by using max function of dictionary
winner = max(candidate_votes_dict, key=candidate_votes_dict.get)

# Calculating percentage of results
stockham_percent = (candidate_votes_dict['Charles Casper Stockham']/total_votes)*100
degette_percent = (candidate_votes_dict['Diana DeGette']/total_votes)*100
doane_percent = (candidate_votes_dict['Raymon Anthony Doane']/total_votes)*100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({candidate_votes_dict['Charles Casper Stockham']})")
print(f"Diana DeGette: {round(degette_percent,3)}% ({candidate_votes_dict['Diana DeGette']})")
print(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({candidate_votes_dict['Raymon Anthony Doane']})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

# Outputting results
with open(output_path,"w") as file:

    # Writing statements in output file
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({candidate_votes_dict['Charles Casper Stockham']})\n")
    file.write(f"Diana DeGette: {round(degette_percent,3)}% ({candidate_votes_dict['Diana DeGette']})\n")
    file.write(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({candidate_votes_dict['Raymon Anthony Doane']})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"----------------------------\n")