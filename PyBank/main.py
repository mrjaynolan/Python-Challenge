import os
import csv

# Set path for CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
months = 0
total_sum = 0
changes = []
dates = []
prev_value = None

# Print header for Financial Analysis
print("Financial Analysis")
print("--------------------------------------------------------------")

# Open and read the CSV file
with open(csv_path, 'r') as budget_file:
    csv_reader = csv.reader(budget_file)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        date, value = row[0], int(row[1])
        months += 1
        total_sum += value
        dates.append(date)

        if prev_value is not None:
            changes.append(value - prev_value)
        prev_value = value

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Determine greatest increase and decrease in profits
if changes:
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    date_of_greatest_increase = dates[changes.index(greatest_increase) + 1]
    date_of_greatest_decrease = dates[changes.index(greatest_decrease) + 1]
else:
    greatest_increase = greatest_decrease = 0
    date_of_greatest_increase = date_of_greatest_decrease = None

# Print results
print(f"Total Months: {months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: ${greatest_increase} on {date_of_greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_of_greatest_decrease}")

# Export results to a text file
output_file = os.path.join("analysis", "budget_data_output.txt")
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("--------------------------------------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total_sum}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: ${greatest_increase} on {date_of_greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: ${greatest_decrease} on {date_of_greatest_decrease}\n")