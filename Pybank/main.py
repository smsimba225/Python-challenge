


import csv



deltaprofitloss = []
date = []
profit = []


totalmonths=0
totalprofitloss=0
starting_profit=0
ending_profit=0

with open('./resources/budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    next(csv_reader)

    for line in csv_reader:
        totalmonths = totalmonths+1 # adds 1 to counter
        date.append(line[0])
        profit.append(line[1])
        totalprofitloss = totalprofitloss + int(line[1])
        ending_profit=int(line[1])
        changeprofit = int(ending_profit)-int(starting_profit) #calculate change in profit
        
        deltaprofitloss.append(changeprofit) #add change to change profit list
        starting_profit=ending_profit #sets the starting profit to equal the last ending profit
        
   
    deltaprofitloss[0] = 0 #changes first change in profit 
    sumdelta = sum(deltaprofitloss)
    #print(deltaprofitloss)
    avgchangeprofit=round(sumdelta/(int(totalmonths)-1),2) # -1 is because first line doesn't count towards average
    greatest_increase = max(deltaprofitloss)
    greatest_decrease = min(deltaprofitloss)
    date_greatest_increase=date[deltaprofitloss.index(greatest_increase)]
    date_greatest_decrease=date[deltaprofitloss.index(greatest_decrease)]
    #print (totalmonths)
    #print (round(avgchangeprofit, 2))
 
    print ('Financial Analysis')
    print ('----------------------------')
    print ('Total Months:' + ' ' + str(totalmonths))
    print ('Total:' + ' ' + '$' + str(totalprofitloss))
    print ('Average Change:' + ' ' + '$' + str(avgchangeprofit))
    print ('Greatest Increase in Profits:' + ' ' + str(date_greatest_increase) + ' ' + '($' + str(greatest_increase)+')')
    print ('Greatest Decrease in Profits:' + ' ' + str(date_greatest_decrease) + ' ' + '($' + str(greatest_decrease)+')')
 