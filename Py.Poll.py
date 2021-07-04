# Add dependencies
import csv
import os

#Add a variable to load a file from a path
file_to_load = os.path.join("Module 3","election-analysis","Resources","election_results.csv")

#Add a variable to write to file
file_to_write = os.path.join("Module 3","election-analysis","analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Create a list for Candidate names
candidate_options = []

#Create dictionary for Candidate votes
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # Check if candidate name is already in the list
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Iterate on candidate votes
        candidate_votes[candidate_name] +=1

with open(file_to_write,"w") as txt_file:
    election_results= (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")

    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)

    # Print the candidate vote dictionary totals
    #print(candidate_votes)

    # Divid the candidates votes count over the total vote
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage =float(votes) / float(total_votes) * 100

        #4 As a variable the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print to text file
        txt_file.write(candidate_results)

        #Check the first vote count is greater than zero
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    txt_file.write(winning_candidate_summary)
    