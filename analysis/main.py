import os
import csv

csvpath = os.path.join('/Users/kenuzb/python-challenge/PyPoll', 'Resources', 'election_data.csv')
csv_output = os.path.join('/Users/kenuzb/python-challenge/PyPoll', 'analysis', 'ready_data.csv')

Totalvotes=0
Candidate=[]
header=[]

CandidateName=[]
CandidateVotes=[]
Highvote=0
Winner=""


#with open(budget_data.csv, encoding='utf-8') as csvfile:
csvfile= open(csvpath, "r")
reader = csv.reader(csvfile)
    
header = next(reader)
print(f"CSV Header: {header}")
rows=[0]
for row in reader:
    Candidate.append(row[2])
    rows.append(row)
    Totalvotes+=1

csvfile.close()
print(Totalvotes)

i=int(0)
Name=""
j=int(-1)
CandidateName=[]
CandidateVotes=[]

for Name in Candidate:
    if Name not in CandidateName:
        CandidateName.append(Name)
        CandidateVotes.append(1)
    else:
        CandidateIndex = CandidateName.index(Name)
        CandidateVotes[CandidateIndex] +1

print(CandidateName)
print(CandidateVotes)
print(CandidateName[0],CandidateVotes[0])
print(CandidateName[1],CandidateVotes[1])
print(CandidateName[2],CandidateVotes[2])

with open (csv_output, "w") as csvfile:
    csvfile.write("Election Results\n")
    csvfile.write("-----------------\n")
    csvfile.write(f"Total votes: {Totalvotes}\n")
    csvfile.write("-----------------\n")

    for i in range(len(CandidateVotes)):
        VotePercentage=CandidateVotes[i]/Totalvotes
        csvfile.write (f"{CandidateName[i]}: {VotePercentage}%({CandidateVotes[i]})\n")
        if CandidateVotes[i]>=Highvote:
            Winner<CandidateName[0]
        #csvfile.write("-----------------\n")
        csvfile.write(f"Winner: {Winner}\n")
        csvfile.write("-----------------\n")