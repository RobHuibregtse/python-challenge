#Import modules needed to read csv from filepath
import os
import csv

#Find flat file and open it
election_data_path = os.path.join("Resources","election_data.csv")
election_data_file = open(election_data_path)

#Load flat file to new list of dictionaries
ballots = list(csv.DictReader(election_data_file, delimiter=","))

#Calculate total votes cast
total_votes = len(ballots)

#Create an empty list of unique candidates as dictionaries (to be used to store total votes as well)
candidates = []

#Set a list of unique candidates
unique_candidates = set()

#Iterate over the ballots to find each unique candidate
for ballot in ballots:
    #Set the candidate name to the name of the candidate on the current ballot
    candidate_name = ballot["Candidate"]
    #If the candidate name isn't in the list of unique candidates, then add the candidate name to the list and candidate as a dictionary with vote totals set to 0
    if candidate_name not in unique_candidates:
        unique_candidates.add(candidate_name)
        candidates.append({"Candidate": candidate_name, "Total Votes": 0, "Total Vote Percent": 0})
        
#Iterate over the ballots to total votes
for ballot in ballots:
    #Define voted candidate as the candidate on the current ballot
    voted_candidate = ballot["Candidate"]
    #Iterate through candidates and check if the current ballot should be counted as a vote for them
    for candidate in candidates:
        #If the ballot candidate matches the candidate, add 1 to their vote total and calculate their vote percentage
        if candidate["Candidate"] == voted_candidate:
            candidate["Total Votes"] += 1
            candidate["Total Vote Percent"] = candidate["Total Votes"] / total_votes * 100

#Determine winning candidate by finding the max number of votes among candidates
winning_candidate = max(candidates, key=lambda x: x['Total Votes'])

#Print summary to console
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
for candidate in candidates:
    print(f'{candidate["Candidate"]}: {round(candidate["Total Vote Percent"], ndigits=3)}%')
print(f'-------------------------')
print(f'Winner: {winning_candidate["Candidate"]}')

#Open new file in write mode and write output to file
with open("Analysis/election_results.txt","w") as file:
    file.write(f'Election Results\n')
    file.write(f'-------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write(f'-------------------------\n')
    for candidate in candidates:
        file.write(f'{candidate["Candidate"]}: {round(candidate["Total Vote Percent"], ndigits=3)}%\n')
    file.write(f'-------------------------\n')
    file.write(f'Winner: {winning_candidate["Candidate"]}')