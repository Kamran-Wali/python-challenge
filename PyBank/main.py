#import os and CSV to read file
import os
import csv

# Read in the budget CSV file
budgetcsv = os.path.join('budget_data.csv')

# Declare and Initialize Variables
budget_dt = []
revenueList =[]
monthStr = []
yearStr =[]
ChangeInRevenue =[]
TotalRev =0
TotalRevcount = 0
RevBeg=0
RevChg=0
RevEnd=0
iCount = 0

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip headers
    next(csvreader, None)

    for row in csvreader:
        #Append data from the row
        iCount = iCount + 1
        budget_dt.append(row[0])
        revenueList.append(int(row[1]))
        TotalRev = TotalRev + int(row[1])
        RevEnd = int(row[1])
        RevChg = RevEnd - RevBeg
        TotalRevcount = TotalRevcount + RevChg
        ChangeInRevenue.append(RevChg)
        splitdate = row[0].split('-')
        monthStr.append(str(splitdate[0]))
        yearStr.append(splitdate[1][-2:])
        RevBeg = RevEnd

AveRevChg = TotalRevcount / iCount
GIncrease = max(ChangeInRevenue)
GDecrease = min(ChangeInRevenue)
IncreaseDate = budget_dt[ChangeInRevenue.index(GIncrease)]
DecreaseDate = budget_dt[ChangeInRevenue.index(GDecrease)]
CountM = len(set(budget_dt))

with open('financial_analysis_report' + '.txt', 'w') as text:
    text.write("Financial Analysis Of The budget_data_csv Is As Follows: "+"\n")
    text.write("----------------------------------------------------------\n")
    text.write("    Total Revenue Months: " + str(CountM) + "\n")
    text.write("    Total revenue: " + "$" + str(TotalRev) + "\n")
    text.write("    Average Change In Revenue: " + '$' + str(int(AveRevChg)) +'\n')
    text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
    text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")
