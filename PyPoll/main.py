

import csv

candidate_list=[]
candidatename=[]
candidatevote=[]
candidatepercent=[]
totalvotes=0
with open('./resources/election_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    for line in csv_reader:
        totalvotes=totalvotes+1
        candidate_list.append(line[2]) 

candidate_set=sorted(set(candidate_list), key=candidate_list.index)   #sorted required to keep set order the same as when in a list, set because we don't want duplicates.

for x in candidate_set: 
        candidatename.append(x)
        candidatevote.append(candidate_list.count(x))
        candidatepercent.append(candidate_list.count(x)/totalvotes*100)

truncatedpercent=[] #https://www.geeksforgeeks.org/python-ways-to-format-elements-of-given-list/ helped for truncating decimals
for item in candidatepercent:
    truncated_value = round(item,3)
    truncatedpercent.append(str(truncated_value))

winner=candidatename[candidatepercent.index(max(candidatepercent))]

print('\n'+'Election Results'+ '\n')
print('---------------------------------'+'\n')
print('Total Votes: ' + str(totalvotes) + '\n')

print('---------------------------------'+'\n')
for i in range(len(candidatename)):
        print(candidatename[i] + ": " + str(truncatedpercent[i]) + "% (" + str(candidatevote[i])+ ")"+'\n')

print('---------------------------------'+'\n')
print('Winner: ' + winner + '\n')
print('---------------------------------'+'\n')

with open('election_results.txt', 'w') as text:
        text.write('\n'+'Election Results'+ '\n\n')
        text.write('----------------------------'+'\n\n')
        text.write('Total Votes: ' + str(totalvotes) + '\n\n')

        text.write('----------------------------\n\n')
        for i in range(len(candidatename)):
                text.write(candidatename[i] + ': ' + str(truncatedpercent[i]) + '% (' + str(candidatevote[i])+ ')' + '\n\n')

        text.write('----------------------------'+'\n\n')
        text.write('Winner: ' + winner + '\n\n')
        text.write('----------------------------'+'\n')