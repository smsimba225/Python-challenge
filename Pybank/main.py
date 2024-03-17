

import os
import csv



deltaprofitloss = []
date = []
profit = []


totalmonths=0
totalprofitloss=0
starting_profit=0
ending_profit=0
# makes path to csv file compatible across OS
csvpath = os.path.join('Resources', 'budget_data.csv') 

# also puts txt file in appropriate folder according to instructions
txtpath = os.path.join('analysis', 'financial_analysis.txt') 

# reads csv file
with open(csvpath) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    header = next(csv_reader)

    for line in csv_reader:
        totalmonths = totalmonths+1 # adds 1 to counter to find total number of months
        date.append(line[0])
        profit.append(line[1])
        totalprofitloss = totalprofitloss + int(line[1])
        ending_profit=int(line[1])
        changeprofit = int(ending_profit)-int(starting_profit) # calculate change in profit
        
        deltaprofitloss.append(changeprofit) # add change to change profit list
        starting_profit=ending_profit # sets the starting profit to equal the last ending profit
        
   
    deltaprofitloss[0] = 0 # changes first change in profit because first line doesn't count towards change in profits
    sumdelta = sum(deltaprofitloss)
    avgchangeprofit=round(sumdelta/(int(totalmonths)-1),2) # -1 is because first line doesn't count towards average of change in profits
    greatest_increase = max(deltaprofitloss)
    greatest_decrease = min(deltaprofitloss)
    date_greatest_increase=date[deltaprofitloss.index(greatest_increase)]
    date_greatest_decrease=date[deltaprofitloss.index(greatest_decrease)]
 
# code to display financial analysis
    print ('\n'+ 'Financial Analysis'+ '\n')
    print ('----------------------------'+"\n")
    print ('Total Months: ' + str(totalmonths)+ '\n')
    print ('Total: ' + '$' + str(totalprofitloss)+ '\n')
    print ('Average Change: ' + '$' + str(avgchangeprofit)+ '\n')
    print ('Greatest Increase in Profits: ' + str(date_greatest_increase) + ' ($' + str(greatest_increase)+')'+ '\n')
    print ('Greatest Decrease in Profits: ' + str(date_greatest_decrease) + ' ($' + str(greatest_decrease)+')'+ '\n')
 
# checks to see if analysis folder is available to put analysis text into.
if not os.path.exists('analysis'):
    os.mkdir('analysis')

 # code to write financial analysis to text
with open(txtpath, 'w') as text:
    text.write('Financial Analysis'+ '\n')
    text.write('--------------------------\n\n')
    text.write('Total Months: ' + str(totalmonths) + '\n')
    text.write('Total Profits: ' + '$' + str(totalprofitloss) + '\n')
    text.write('Average Change: ' + '$' + str(avgchangeprofit) + '\n')
    text.write('Greatest Increase in Profits: ' + str(date_greatest_increase) + ' ($' + str(greatest_increase) + ')\n')
    text.write('Greatest Decrease in Profits: ' + str(date_greatest_decrease) + ' ($' + str(greatest_decrease) + ')\n')