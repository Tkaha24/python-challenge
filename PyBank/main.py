import os
import csv

csvpath = os.path.join('budget_data.csv')
file_output = os.path.join('ready_data.csv')

profit = []
monthly_changes = []
date = []

# Initialize the variables as required.
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0


#with open(budget_data.csv, encoding='utf-8') as csvfile:
with open(csvpath, "r") as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print(f"CSV Header: {header}")
   
 

    for row in reader:
        # Use count to count the number months in this dataset
      count = count + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits from month to month.
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits - monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profits
      #average_change_profits = (monthly_change_profits / count)
      average_change_profits = (total_change_profits  / count )
      
      #Find the max and min change in profits 
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open(file_output, 'w') as text:
            text.write("----------------------------------------------------------\n")
            text.write("  Financial Analysis"+ "\n")
            text.write("----------------------------------------------------------\n\n")
            text.write("    Total Months: " + str(count) + "\n")
            text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
            text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
            text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
            text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
            text.write("----------------------------------------------------------\n")
