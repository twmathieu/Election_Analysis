# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
      

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the text file.
    txt_file.write("Counties in the election\n-------\nArapahoe\nDenver\nJefferson")



# Close the file
outfile.close()     



# 1. the total number of votes cast
# 2. The total number of votes cast
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election

