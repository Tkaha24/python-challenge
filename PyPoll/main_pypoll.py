import os
import csv

csvpath = os.path.join('election_data.csv')

csv_output = os.path.join('ready_data_Pypoll.csv')


with open(csvpath, newline = "") as csvfile:
    data_set = csv.reader(csvfile)
      
    ## Used the following line to check the header contents, if any:
    #print(next(data_set))
    ##yields: ['Voter ID', 'County', 'Candidate'] 
    #initialize counter at -1 in order to negate the header when counting rows/votes
    total_votes_count = -1

    # initialize counters for each candidate
    Diana_DeGette = Raymon_Anthony_Doane = Charles_Casper_Stockham = 0
    
    # initialize percentages for each candidate's vote count
    Diana_Percent = Raymon_Percent = Charles_Percent = 0

    # loop through each row of the data set
    for row in data_set:
            
                  

        # have a running counter that will yield the total number of rows
        # to use for calculating percentage of votes
        total_votes_count +=1
     

        # set up conditionals to identify contents of each 3rd column
        # and add to a counter that adds up all the votes for each candidate
        if row[2] == "Diana DeGette":
            Diana_DeGette +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane +=1
        elif row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham +=1
        
    
    #loop through dictionary to get candidate name as key and votes as value -->
    # create a dictionary with that assigns each key (candidate)
    # with the amount of votes they collect
    Results = {"Diana DeGette":Diana_DeGette, "Raymon Anthony Doane":Raymon_Anthony_Doane, "Charles Casper Stockham":Charles_Casper_Stockham}
    
    # Calculate percentages and round to 3 decimal places
    Diana_Percent = round((Diana_DeGette / total_votes_count) * 100, 3)
    Raymon_Percent = round((Raymon_Anthony_Doane / total_votes_count) * 100, 3)
    Charles_Percent = round((Charles_Casper_Stockham / total_votes_count) * 100, 3)
  
    # Find the max value from the values in the dictionary and return its key, then store as 'Winner'
    Winner = max(Results, key=Results.get)

    # create formatted text to print
    # (triple quotes allow multiple lines to be stored in string value)
    toprint = f"""Election Results

Total Votes: {total_votes_count} 
-----------------------
Diana_DeGette:  {Diana_Percent}% ({Diana_DeGette})
Raymon_Anthony_Doane:  {Raymon_Percent}% ({Raymon_Anthony_Doane})
Charles_Casper_Stockham:  {Charles_Percent}% ({Charles_Casper_Stockham})

-----------------------
Winner: {Winner} 
-----------------------"""

# print to Terminal
print(toprint)

with open(csv_output, "w") as text:
            text.write(f"Election Result\n")
            text.write("------------------\n")
            text.write(f"Total Votes: {total_votes_count}\n")
            text.write("------------------\n")
            text.write(f"Charles Casper Stockham: {Charles_Percent}% ({Charles_Casper_Stockham})\n")
            text.write(f"Diana DeGette: {Diana_Percent}% ({Diana_DeGette})\n")
            text.write(f"Raymon Anthony Doane: {Raymon_Percent}% ({Raymon_Anthony_Doane})\n")
            text.write("------------------\n")
            text.write(f"Winner: {Winner}")