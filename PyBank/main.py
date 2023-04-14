import os
import csv

csvpath = os.path.join('/Users/kenuzb/python-challenge/PyBank', 'Resources', 'budget_data.csv')
file_output = os.path.join('/Users/kenuzb/python-challenge/PyBank', 'analysis', 'ready_data.csv')

total=0
profitloss=1
value=0
monthchange=0
profits=[]
dates=[]
total1=0


#with open(budget_data.csv, encoding='utf-8') as csvfile:
with open(csvpath, "r") as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print(f"CSV Header: {header}")
   
 

    for row in reader:
        #dates column
        dates.append(row[0])
        firstrow = next(reader)
        profitloss += int(firstrow[1])
        total +=2
        value =int(firstrow[1])

        #month calculation
        monthchange=int(row[1])-value
        profits.append(monthchange)
        value =int(row[1])
        total1 +1

        #profit change
        profitloss= profitloss +int(row[1])

        #prof increase
        profitincrease= max(profits)
        greatestindex = profits.index(profitincrease)
        greatesdate =dates[greatestindex]

        #captures prof decrease
        greatestdecrease= min(profits)
        lowestindex = profits.index(greatestdecrease)
        lowestdate =dates[lowestindex]

       # Average=0
       # Average =Totalnet/Totalmonth
        
        averagechange = sum(profits)/len(profits)
        #prints in terminal

        print("....................")
        print(f"TotalMonths:{str(total)}")
        print(f"Total:{str(profitloss)}")
        print(f"Average Change:${averagechange}\n")
        print(f"Greatest Increase in Profits:{greatesdate}(${profitincrease})")
        print(f"Greatest Decrease in Profits:{lowestdate}(${greatestdecrease})") 

       #file will be created and output will be printed
    with open(file_output, "w") as text:
        text.write(f"Finnancial Analysis\n")
        text.write("------------------\n")
        text.write(f"TotalMonths:{total}\n")
        text.write(f"Total:${profitloss}\n")
        text.write(f"Average Change:${averagechange}\n")
        text.write(f"Greatest Increase in Profits:{greatesdate}(${profitincrease})\n")
        text.write(f"Greatest Decrease in Profits:{lowestdate}(${greatestdecrease})") 








       