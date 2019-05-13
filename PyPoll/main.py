import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    votes_list=[row[2] for row in csvreader]
    votes_list.pop(0)

#A complete list of candidates who received votes
candidates = []
for x in votes_list:
    if x not in candidates:
        candidates.append(x)

#The total number of votes cast
vote_total = len(votes_list)

def vote_percent(str):
    pc = "{:.2%}".format(votes_list.count(str)/vote_total)
    return pc

def vote_count(str):
    count=votes_list.count(str)
    return count

#The percentage of votes each candidate won
khan_pc= vote_percent('Khan')
correy_pc= vote_percent('Correy')
li_pc = vote_percent('Li')
ot_pc= vote_percent("O'Tooley")

#Total votes each candidate won
khan_count = vote_count('Khan')
correy_count=vote_count('Correy')
li_count = vote_count('Li')
ot_count = vote_count("O'Tooley")

#Find the winner
votes_d=dict(zip([khan_count,correy_count,li_count,ot_count],candidates))
winning_count=max(votes_d.keys())

#Print summary to Terminal and write to .txt file
output_text=f'''
Election Results
-------------------------
Total votes: 
-------------------------
Khan: {khan_pc} ({khan_count})
Correy: {correy_pc} ({correy_count})
Li: {li_pc} ({li_count})
O'Tooley: {ot_pc} ({ot_count})
-------------------------
Winner: {votes_d[winning_count]}
'''

print(output_text)

file = open('../election_summary.txt',"w") 
file.write(output_text)
file.close() 

