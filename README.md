## Readme!

This assignment was an introduction to Python code.  I found this assignment relatively straightforward.  Python is such a powerful language, and importing very large csv files seemed to be done with such ease compared to our previous assignment using Excel and VBA.  It was also quite interesting how easy it was to have the analysis text also be placed into the appropriate folder as in the Challenge Instructions.  The challenge I was having with that was when the "analysis" folder did not exist, but I found some tips on stackoverflow.com on how to check if the folder existed, and if not, to create it. 



## PyBank Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

--------------------------------------

For the PyBank Challenge, calculating the average of the changes in Profit/Losses was interesting because I had take the sum of all the changes, and divide by the number of changes in Profit/Losses. Since the first month did not count towards that, I asked the code to convert the amount changed to zero.  This would be so that when I asked the code to add all of the monthly changes together, the first month would not affect the sum.  Then when dividing, I subtracted 1 from the total number of monthly changes, and achieved the correct result.

Looking back at the assignment it probably would have been more efficient to append all of the monthly change into a new list, pop off the first month, and run calculations on the information remaining in the list to get the average change.

## PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

---------------------------------------

For the PyPoll challenge, it was not clear whether or not the code was supposed to be for an election where there were only these three candidates, or if a code was to be written for an election that could handle any number and names of candidates.  I decided to try for the latter, the former was relatively simple. 

This assignment was interesting because I wanted a way for it to create a list of all the unique candidates in the election, while still providing me a list that I could use to calculate percentages of votes.  I did discover various ways to do it, including using modules, but we had not covered that in class so I tried a different method.  I decided to try to use the idea of converting a list into a set, as a set will only keep unique values, which made finding the unique names in the election very easy.  The challenge I found was that sets do not maintain order, so I would get inconsistent results as I ran the code over and over.  The names of the candidates in the results screen would be ordered randomly.  I did want my output to match the results in the instructions, so I found tips on stackoverflow.com as to how to keep the order of the set to match that of the list that it came from.  With that, I was able to achieve consistent results every time.

--------------------------------------

I feel that these two assignments really helped reinforce the basic coding skills in Python that I will be using in this class.  It became much easier after I completed the first half, and starting the second assignment was no problem.  

Thank you for looking at my work!

~Owen