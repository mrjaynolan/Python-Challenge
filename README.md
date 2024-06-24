### Python-Challenge
## Justin Nolan Module 3 Homework

# PyBank and PyPoll Analysis

This repository contains two Python scripts, `PyBank` and `PyPoll`, designed to analyze financial and election data respectively. Both scripts read data from CSV files, process the data to generate meaningful summaries, and output the results to text files.

## PyBank

### Objective

The `PyBank` script performs a financial analysis on a given dataset containing monthly profit/loss figures. The analysis includes the total number of months, the total profit/loss, the average change in profit/loss, and the greatest increase and decrease in profits over the entire period.

### Input Data

The input data file should be named `budget_data.csv` and placed inside a `Resources` directory. The CSV file should have the following columns:
- `Date`: The month and year of the data entry.
- `Profit/Losses`: The profit or loss for the corresponding month.

### Output

The results are printed to the terminal and saved to a text file named `budget_data_output.txt` in an `analysis` directory.

### Running the Script

1. Ensure the `Resources` directory contains `budget_data.csv`.
2. Ensure the `analysis` directory exists (the script will create it if it doesn't).
3. Run the script using:
   ```bash
   python pybank.py

### PyBank Script


