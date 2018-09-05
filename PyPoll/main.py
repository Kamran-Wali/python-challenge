import os
import csv

electionDataFile = os.path.join('election_data.csv')
    
# Set empty list variables
eCounty= []
eCandidate = []
eUniqueCandidate = []
CandidateVoteCount = []
CandidateVotePercent =[]
CandidateTotalCount = 0
CandidateCount = 0

with open(electionDataFile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     #skip headers
    next(csvreader, None)
    for row in csvreader:
        CandidateTotalCount = CandidateTotalCount + 1
        eCandidate.append(row[2])
    
    #assign unique values in the list above to a set to hold just the unique candidates
    
    for uc in set(eCandidate):
        #print(uc)
        eUniqueCandidate.append(uc)
        CandidateCount = eCandidate.count(uc)

        #print(CandidateCount)
        #Put together a list of counts grouped by the candidates
        CandidateVoteCount.append(CandidateCount)
        
        #Put together the percentage per candidate
        CandidateVotePercent.append(CandidateCount/CandidateTotalCount)

    WinningCandidate = eUniqueCandidate[CandidateVoteCount.index(max(CandidateVoteCount))]

    with open('Election_Results.txt', 'w') as text:
        text.write("Election Results From Data Taken From The election_data.csv Is As Follows: \n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(CandidateTotalCount) + "\n")
        text.write("----------------------------------------------------------\n")
        for x in range(len(set(eCandidate))):
            text.write(eUniqueCandidate[x] + ": " + str(round(CandidateVotePercent[x]*100,1)) + "% With a vote count of: " + str(CandidateVoteCount[x]) + "\n")
        text.write("----------------------------------------------------------\n")
        text.write("The Winning Candidate Is: " + WinningCandidate +"\n")
        text.write("----------------------------------------------------------\n")


