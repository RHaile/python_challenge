import os
import csv

csv_path = os.path.join('..', 'Resources', 'budget_data.csv')
analysis_file = os.path.join('..', 'Resources', 'budget_analysis.txt')

Total_Month = 0
Total_Revenue = 0
Previous_Revenue = 0
Change_Revenue = 0
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 99999999999]
Change_Month = []
Change_Revenue_List = []

with open (csv_path) as Data_Revenue:
	reader = csv.DictReader(Data_Revenue)

	for row in reader:
		Total_Month = Total_Month + 1
		Total_Revenue = Total_Revenue + int(row["Profit/Losses"])

		Change_Revenue = int(row["Profit/Losses"]) - Previous_Revenue
		Previous_Revenue = int(row["Profit/Losses"])
		Change_Month = Change_Month + [row["Date"]]

		if (Change_Revenue > Greatest_Increase[1]):
			Greatest_Increase[1] = Change_Revenue
			Greatest_Increase[0] = row["Date"]

		if (Change_Revenue < Greatest_Decrease[1]):
			Greatest_Decrease[0] = row["Date"]
			Greatest_Decrease[1] = Change_Revenue

try:
	Average_Revenue = sum(Change_Revenue_List) / len(Change_Revenue_List)
except ZeroDivisionError:
	Average_Revenue = 0

output = (
	f"\nFinancial Analysis\n"
	f"---------------------------\n"\
	f"Total Months: {Total_Month}\n"
	f"Total: ${Total_Revenue}\n"
	f"Average Change: ${Average_Revenue}\n"
	f"Greatest Increase in Profits: {Greatest_Increase[0]} ${Greatest_Increase[1]}\n"
	f"Greatest Decrease in Profits: {Greatest_Decrease[0]} ${Greatest_Decrease[1]}\n")

print(output)


with open (analysis_file, "w") as txt_file:
	txt_file.write(output)


