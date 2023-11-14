import os
import csv

file_csv = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("analysis","output_data.txt")

Candidates = []

#much of the open csvfile syntax is borrowed from our teacher's lesson in-class, including the csvreader and header and the for row in csvreader syntax.
with open(file_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        Candidates.append(row[2])
        #We only care about the candidates here.  The other information is not useful.
        #So I'm building a list of all the candidates.
        
Total_Votes = len(Candidates)
Candidate_set = set(Candidates) 
#using set method idea came from https://www.geeksforgeeks.org/python-get-unique-values-list/
#set will give us just the unique items from the list, meaning we then know what candidates were
#in the election.
Candidate_list = sorted(list(Candidate_set))
#sorted syntax from https://stackoverflow.com/questions/7301110/why-does-return-list-sort-return-none-not-the-list
#The results of set were not in alphabetical order.  This function returns an alphabetical sort.

Candict = {}
for cand in Candidate_list:
    Candict[cand] = 0
#Building a dictionary with the candidate names as key values and defaulting them to 0.

for cand in Candidates:
    Candict[cand] += 1
#Then incrementing each candidate as they come up in the full vote list.

#creating an output list that contains all of the strings, since I need to write them to both the screen and a file.
output_string = []

output_string.append("Election Results")
output_string.append("")
output_string.append("-------------------------")
output_string.append("")
output_string.append(f"Total Votes: {Total_Votes}")
output_string.append("")
output_string.append("-------------------------")
output_string.append("")
for k, v in Candict.items():
    percent = v*100 / Total_Votes
    floatvalue = float("{:.3f}".format(percent))
    output_string.append(f"{k}: {floatvalue}% ({v})")
    output_string.append("")
output_string.append("-------------------------")
output_string.append("")
output_string.append(f"Winner: {max(Candict, key=Candict.get)}")
output_string.append("")
output_string.append("-------------------------")
#borrowed the float syntax from https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#using float to show only 3 decimals, as specified in the assignment


#borrowed file open and f.write from https://www.w3schools.com/python/python_file_write.asp
#borrowed "\n" from https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
f = open(outputfile, "w")
for o in output_string:
    print(o)
    f.write(o + "\n")
    
f.close()