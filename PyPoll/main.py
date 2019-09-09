import os
from collections import Counter
import csv

csv_path = os.path.join('..', 'Resources', 'election_data.csv')
analysis_file = os.path.join('..', 'Resources', 'election_analysis.txt')

Canidate_List = [] 
Percentage = [] 
Result = [] 
V_Count = Counter() 

with open(csv_path, 'r', newline='', encoding='latin-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 

    for row in csvreader: 
        Canidate_List.append(row[2])

    totalVotes = len(Canidate_List)

    for name in Canidate_List: 
        V_Count[name] += 1

    winner = max(zip(V_Count.values(), V_Count.keys())) 
    names = tuple(V_Count.keys())
    votes = tuple(V_Count.values())

    for x in votes:
        Percentage.append((int(x)/totalVotes)*100) 
    
output = (
    f"\nElection Results\n"
    f"---------------------------\n"\
    f"Total Votes: {totalVotes}\n"
    f"---------------------------\n"\
    for x in range(len(names))
        f"{names[x]} : {round(Percentage[x],1)}% , {votes[x]}\n"
    f"---------------------------\n"\
    f"Winner: {winner[1]}\n"
    f"---------------------------\n")

print(output)

with open(analysis_file, 'w') as txtfile:
    txtfile.write(output)
