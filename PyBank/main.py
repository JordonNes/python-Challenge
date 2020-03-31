import os
import csv
BANK_DATA = 'budget_data.csv'
with open(BANK_DATA, 'r') as bank_data:
    csvreader = csv.reader(bank_data, delimiter=',')

# Varibles
    header = next(bank_data)
    ROW1 = next(bank_data)
    Profit_Loss = ROW1.split(",")
    PL = int(Profit_Loss[1])
    Total_pl = int(PL)
    Grt_Increase = int(PL)
    Grt_Decrease = int(PL)
    Total_Months = 1

# Itterate the rows
    for row in csvreader:
        Last_pl = int(row[1])
        Total_pl = Total_pl + Last_pl
        Total_Months = Total_Months + 1
               
        if Last_pl > Grt_Increase:
            Grt_Increase = Last_pl
            Grt_Inc_Date = row[0] #max
        if Last_pl < Grt_Decrease:
            Grt_Decrease = Last_pl
            Grt_Dec_Date = row[0] #min
            
# Calculate final changes
Net_Change = Last_pl - PL
Avg_Change = int(Total_pl / Total_Months)


# Print results
lin1 = "Financial Analysis \n"
lin2 = "------------------------ \n"
lin3 = "Total Months: " + str(Total_Months) + "\n"
lin4 = "Net Change: $" + str(Net_Change) + "\n"
lin5 = "Average Change: $" + str(Avg_Change) + "\n"
lin6 = "Greatest Increase in profits: " + Grt_Inc_Date + " ($" + str(Grt_Increase) + ") \n"
lin7 = "Greatest Decrease in profits: " + Grt_Dec_Date + " ($" + str(Grt_Decrease) + ") \n"
PyBank_results = [lin1,lin2,lin3,lin4,lin5,lin6,lin7]
# Export file containing results
fileWrite = open("PyBankResults.txt","w")
fileWrite.writelines(PyBank_results)
print(lin1)
print(lin2)
print(lin3)
print(lin4)
print(lin5)
print(lin6)
print(lin7)