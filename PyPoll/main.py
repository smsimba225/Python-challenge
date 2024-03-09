

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
           
for x in set(candidate_list):
        candidatename.append(x)
        candidatevote.append(candidate_list.count(x))
        candidatepercent.append(candidate_list.count(x)/totalvotes*100)

print(candidatename)
truncatedpercent=[]
for item in candidatepercent:
    truncated_value = round(item,3)
    truncatedpercent.append(str(truncated_value))

for i in range(len(candidatename)):
        print(candidatename[i] + ": " + str(truncatedpercent[i]) + "% (" + str(candidatevote[i])+ ")")

winner=candidatename[candidatepercent.index(max(candidatepercent))]
print(winner)
