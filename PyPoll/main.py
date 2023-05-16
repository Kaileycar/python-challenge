import os
import csv

election_file = os.path.join("Resources", "election_data.csv")

with open(election_file, 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file, delimiter=",")

    #create arrays to store data into
    ballot_ID = []
    county_data = []
    candidate_data = []
    total_votes = []
    unique_candidate = []
    vote_data = []
    

    for total_votes, row in enumerate(csv_reader, start=1):

        #set each column into an array
        value = int(row['Ballot ID'])
        value1 = str(row['County'])
        value2 = str(row['Candidate'])
        ballot_ID.append(value)
        county_data.append(value1)
        candidate_data.append(value2)

    
   
    #find unique values
    #put each value in unique_candidate list
    set_data = set(candidate_data)
    unique_candidate = (list(set_data))


output_path = os.path.join("Analysis", "Election_data.txt")

with open(output_path, 'w') as txtfile:

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    txtfile.write(f"\nElection Results\n")
    txtfile.write(f"\n---------------------------\n")
    txtfile.write(f"\nTotal Votes: {total_votes}\n")
    txtfile.write(f"\n---------------------------\n")



    #find the candidate with the most amount of votes
    for person in unique_candidate:
        x = candidate_data.count(person)
        vote_data.append(x)

        #find max amount of votes
        max_votes = max(vote_data)
   

    #find votes associated with each person using the count function
    #count how many times that person shows up in full list of candidates
    for person in unique_candidate:
        count_data = candidate_data.count(person)
   
    
        #calculate percent of each candidates votes
        #Have to print inside for loop
        percent_data = float(count_data/total_votes)*100
        
        print(f"{person}: {round(percent_data, 3)}% ({count_data})")
        txtfile.write(f"\n {person}: {round(percent_data, 3)}% ({count_data}) \n")

        #set winning person to a variable
        if max_votes == count_data:
            win_person = person



    print("---------------------------")
    print(win_person)
    print("---------------------------")    
    txtfile.write(f"\n---------------------------\n")
    txtfile.write(f"\n{win_person}\n")
    txtfile.write(f"\n---------------------------\n")      
