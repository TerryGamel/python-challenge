import os
import csv

budgetcsv = os.path.join("Resources","budget_data.csv")
outputfile = os.path.join("analysis","output_data.txt")

total_months = 0
total_profit = 0
change_in_profits = [] #since I need max and min values for change in profits, keeping them in a list
last_month = 0
this_month = 0

#much of the open csvfile syntax is borrowed from our teacher's lesson in-class, including the csvreader and header and the for row in csvreader syntax.
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        last_month = this_month
        #I opted for this way of calculating total months rather than doing another for declaration because I figure
        #I'm already looping through the file once, I don't need to do it multiple times.
        total_months += 1
        this_month = int(row[1])
        total_profit += this_month
        if total_months > 1:
            change_in_profits.append((this_month - last_month)) #get the difference in profits and store it in my list

#borrowed the float syntax from https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#using float to show only 2 decimals, rounding to cents
average_change = float("{:.2f}".format(sum(change_in_profits) / len(change_in_profits)))

max_change = max(change_in_profits)
min_change = min(change_in_profits)

#creating an output list that contains all of the strings, since I need to write them to both the screen and a file.
output_string = []

output_string.append(f"Financial Analysis")
output_string.append("")
output_string.append("----------------------------")
output_string.append("")
output_string.append(f"Total Months: {total_months}")
output_string.append("")
output_string.append(f"Total: ${total_profit}")
output_string.append("")
output_string.append(f"Average Change: ${average_change}")
output_string.append("")
output_string.append(f"Greatest Increase in Profits: (${max_change})")
output_string.append("")
output_string.append(f"Greatest Decrease in Profits: (${min_change})")

#borrowed file open and f.write from https://www.w3schools.com/python/python_file_write.asp
#borrowed "\n" from https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
f = open(outputfile, "w")
for o in output_string:
    print(o)
    f.write(o + "\n")
    
f.close()