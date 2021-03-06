
#Create imports
import os
import csv

#Initialize variable for votes
total_votes = 0

#Candidate options
candidate_options = []

#Dictionary for candidate votes
candidate_votes = {}

#Initialize string for winning candidate
winning_candidate = ''

#Initialize winning count to 0
winning_count = 0

#Winning % initialize to 0
winning_percentage = 0

#Assigning a variable for the file to load and the path
file_to_load = os.path.join('election_results.csv')

#Assigning a variable to save file
file_to_save = os.path.join('election_analysis.txt')

#Open the election results file and read
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read the header row
    headers = next(file_reader)
    
#Print each row in the CSV
    for row in file_reader:
        total_votes += 1

        #Skip header row
        candidate_name = row[2]

    #Iterate through candidates adding up to total votes
        if candidate_name not in candidate_options:
            #Identify the distinct candidates
            candidate_options.append(candidate_name)
            #Begin tracking votes for each candidate
            candidate_votes[candidate_name] = 0
        #Increment the votes for each candidate
        candidate_votes[candidate_name] += 1

#Begin writing to output file
with open(file_to_save, 'w') as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results, end='')
    txt_file.write(election_results)

    #Find the percentage of votes
    for candidate_name in candidate_votes:
        #Count each vote for the candidates
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes 
        vote_percentage = float(votes)/float(total_votes) * 100
        
        #Adding candidate results to terminal and output file
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        txt_file.write(candidate_results)

        #Determining the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    #Winner Summary
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}\n'
        f'-------------------------\n')
    print(winning_candidate_summary, end='')
    #Write winning summary to txt output file
    txt_file.write(winning_candidate_summary)
