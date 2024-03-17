

import csv
import os

candidate_list=[]
candidatename=[]
candidatevote=[]
candidatepercent=[]
totalvotes=0

# code to make path to csv file compatible across OS
csvpath = os.path.join('Resources', 'election_data.csv')
# also puts analysis in appropriate folder as per instructions
txtpath = os.path.join('analysis', 'election_results.txt')

# code to read csv file

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    for line in csv_reader:
        totalvotes=totalvotes+1 # to count total number of votes, adds 1 to counter as it loops
        candidate_list.append(line[2]) # adds name of candidate to list of candidates to find all candidates in election

# turn candidate list into set - 
# sorted required to keep set order the same as when in a list, since set usually doesn't keep order but we want set because we don't want duplicates.
candidate_set=sorted(set(candidate_list), key=candidate_list.index)   

for x in candidate_set: 
        candidatename.append(x)
        candidatevote.append(candidate_list.count(x))
        candidatepercent.append(candidate_list.count(x)/totalvotes*100)

truncatedpercent=[] # https://www.geeksforgeeks.org/python-ways-to-format-elements-of-given-list/ helped for truncating decimals
for item in candidatepercent:
    truncated_value = round(item,3)
    truncatedpercent.append(str(truncated_value))

# determines winner by comparing percentages
winner=candidatename[candidatepercent.index(max(candidatepercent))]

# code to print results
print('\n'+'Election Results'+ '\n')
print('---------------------------------'+'\n')
print('Total Votes: ' + str(totalvotes) + '\n')

print('---------------------------------'+'\n')
for i in range(len(candidatename)):
        print(candidatename[i] + ": " + str(truncatedpercent[i]) + "% (" + str(candidatevote[i])+ ")"+'\n')

print('---------------------------------'+'\n')
print('Winner: ' + winner + '\n')
print('---------------------------------'+'\n')

# code to write election results to text file:

with open(txtpath, 'w') as text:
        text.write('\n'+'Election Results'+ '\n\n')
        text.write('----------------------------'+'\n\n')
        text.write('Total Votes: ' + str(totalvotes) + '\n\n')

        text.write('----------------------------\n\n')
        for i in range(len(candidatename)):
                text.write(candidatename[i] + ': ' + str(truncatedpercent[i]) + '% (' + str(candidatevote[i])+ ')' + '\n\n')

        text.write('----------------------------'+'\n\n')
        text.write('Winner: ' + winner + '\n\n')
        text.write('----------------------------'+'\n')