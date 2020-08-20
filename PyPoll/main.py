import os
import csv

profit_losses = os.path.join("Resources", "Homework 3_PyPoll_Resources_election_data.csv")


with open(profit_losses,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvfile)

    total_votes = 0
    candidates_list = []
    votes_list = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    votes_list = []

    for row in csvreader:
        total_votes += 1
        candidates_list.append(row[2])
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1    

        

        
        khan_percentage = round(khan_votes / total_votes * 100)
        correy_percentage = round(correy_votes / total_votes * 100) 
        li_percentage = round( li_votes / total_votes * 100)
        otooley_percentage = round( otooley_votes / total_votes * 100)

    votes_list = [khan_votes,correy_votes,li_votes,otooley_votes]
    percentagesList = [khan_percentage, correy_percentage, li_percentage, otooley_percentage]

    res = {votes_list[i]: candidates_list[i] for i in range(len(votes_list))} 


    new_cand_list = list(dict.fromkeys(candidates_list))

    winner = res[max(votes_list)]
    #print(new_cand_list)    
    print(f"Total Votes: {total_votes}")
    print(f"{new_cand_list[0]}: {khan_percentage}% ({khan_votes})")
    print(f"{new_cand_list[1]}: {correy_percentage}% ({correy_votes})")
    print(f"{new_cand_list[2]}: {li_percentage}% ({li_votes})")
    print(f"{new_cand_list[3]}: {otooley_percentage}% ({otooley_votes})")
    print("---------------------")
    print(f"Winner: {winner}")
    
        

    
