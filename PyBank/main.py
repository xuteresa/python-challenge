import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Add rows in CSVreader object to a dictionary with date as key and profit/loss as value
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    bank_dict= {row[0]:row[1] for row in csvreader}
    bank_dict.pop('Date')
    bank_dict = {k:int(v) for k, v in bank_dict.items()}

#The total number of months included in the dataset
total_months = len(bank_dict)
total_months

#The net total amount of profit/losses over the entire period
total_pnl = sum(bank_dict.values())

#The average of the changes in "Profit/Losses" over the entire period
keys_list=[]
values_list=[]
for k,v in bank_dict.items():
    keys_list.append(k)
    values_list.append(v)
deltas=[values_list[i+1]-values_list[i]for i in range(len(values_list)-1)]
deltas_avg=sum(deltas)/len(deltas)

# The greatest increase in profits (date and amount) over the entire period
deltas_dict=dict(zip(deltas, keys_list[1:]))  #removing first row of keys because the first month doesn't have a delta
max_v=max(deltas_dict.keys())
max_k=deltas_dict[max_v]
max_d={max_k:max_v}

# The greatest decrease in losses (date and amount) over the entire period
min_v=min(deltas_dict.keys())
min_k=deltas_dict[min_v]
min_d={min_k:min_v}

#Print summary to terminal and write to .txt file
output_text = f'''
Financial Analysis
----------------------------
    Total Months: {total_months}
    Total: ${total_pnl}
    Total Months: {total_months}
    Total: ${total_pnl}
    Average Change: ${deltas_avg}
    Greatest Increase in Profits: {max_k} (${max_v})
    Greatest Decrease in Profits: {min_k} (${min_v})
    '''
print(output_text)

file = open('../financial_summary.txt',"w") 
file.write(output_text)
file.close() 