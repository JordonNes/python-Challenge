import os
import csv
ELECTION_DATA = 'Election_data.csv'
with open(ELECTION_DATA, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

# Varibles
    header = next(election_data)
    ROW1 = next(election_data)
    data_row = ROW1.split(",")
    
    VOTER_ID = int(data_row[0])
    County = str(data_row[1])
    Canidate = str(data_row[2])
 #Vote Counter   
    Khan_total = 0
    Correy_total = 0
    Li_total = 0
    Otooley_total = 0
    total_votes = 0
    total_candidate = []

#total Voters
    for row in csvreader:
        total_candidate.append(str(row[2]))
    total_candidate_count = {}

# Itterate the rows
    for row in csvreader:

    #Count the Total Vote
        total_votes = total_votes + 1
               
    # Sort the Vote
        if data_row[2] == "Khan":
            Khan_total = Khan_total + 1
        if Canidate == "Correy":
            Correy_total = Correy_total + 1
        if Canidate == "Li":
            Li_total = Li_total + 1
        if Canidate == "O'Tooley":
            Otooley_total = Otooley_total + 1            
    
#Percentage of each Vote
KP = (Khan_total / total_votes)*100
# CP = round((Correy_total / total_votes)*100,2)
# LP = round((Li_total / total_votes)*100,2)
# OP = round((Otooley_total / total_votes)*100,2)
print(total_votes)
print(Khan_total)
print(KP)
# Print results
    # lin1 = "Elections Results\n"
    # lin2 = "------------------------ \n"
    # lin3 = "Khan : " + KP + "(" + Khan_total + ")" "\n"
    # lin4 = "Net Change: $" + str(Net_Change) + "\n"
    # lin5 = "Average Change: $" + str(Avg_Change) + "\n"
    # lin6 = "Greatest Increase in profits: " + Grt_Inc_Date + " ($" + str(Grt_Increase) + ") \n"
    # lin7 = "Greatest Decrease in profits: " + Grt_Dec_Date + " ($" + str(Grt_Decrease) + ") \n"
    # PyBank_results = [lin1,lin2,lin3,lin4,lin5,lin6,lin7]
# Export file containing results
    # fileWrite = open("PyBankResults.txt","w")
    # fileWrite.writelines(PyBank_results)
    # print(lin1)
    # print(lin2)
    # print(lin3)
    # print(lin4)
    # print(lin5)
    # print(lin6)
    # print(lin7)