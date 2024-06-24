import os
import csv

# Define the path for the CSV file
csv_path = os.path.join("Resources", "election_data.csv")

# Print header for Election Results
print("Election Results")
print("--------------------------------------------")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Print total votes
print(f"Total Votes: {total_votes}")
print("--------------------------------------------")

# Calculate and print each candidate's vote percentage and count
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}%, ({votes} votes)")

print("--------------------------------------------")

# Determine and print the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("--------------------------------------------")

# Export results to a text file
output_file = os.path.join("analysis", "election_data_output.txt")
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("--------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.2f}%, ({votes} votes)\n")
    file.write("--------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------------------------------\n")