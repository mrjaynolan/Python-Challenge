## Python-Challenge
Justin Nolan Module 3 Homework

# PyBank and PyPoll Analysis

This repository contains two Python scripts, `PyBank` and `PyPoll`, designed to analyze financial and election data respectively. Both scripts read data from CSV files, process the data to generate meaningful summaries, and output the results to text files.

## PyBank

### Objective

The `PyBank` script performs a financial analysis on a given dataset containing monthly profit/loss figures. The analysis includes:
- The total number of months.
- The total profit/loss.
- The average change in profit/loss.
- The greatest increase in profits.
- The greatest decrease in profits.

### Input Data

The input data file should be named `budget_data.csv` and placed inside a `Resources` directory. The CSV file should have the following columns:
- `Date`: The month and year of the data entry.
- `Profit/Losses`: The profit or loss for the corresponding month.

### Output

The results are printed to the terminal and saved to a text file named `budget_data_output.txt` in an `analysis` directory.

### Steps to Run the Script

1. Ensure the `Resources` directory contains `budget_data.csv`.
2. Run the script using:
   ```bash
   python pybank.py


## PyPoll

### Objective

The `PyPoll` script analyzes data to determine:
- The total number of votes cast.
- The percentage of votes each candidates won.
- The total number of votes of each candidate won.
- The winner of the election based on popular vote.

### Input Data

The input data file should be named `election_data.csv` and placed inside a `Resources` directory. The CSV file should have the following columns:
- `Voters ID`: The unique ID of each voter.
- `County`: The county of the voter.
- `Candidate`: The candidate voted for.

### Output

The results are printed to the terminal and saved to a text file named `election_data_output.txt` in an `analysis` directory.

### Steps to Run the Script

1. Ensure the `Resources` directory contains `election_data.csv`.
2. Run the script using:
   ```bash
   python pybank.py   

