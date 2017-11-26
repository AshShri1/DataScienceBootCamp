import os
import csv

electionDataFiles = ['1','2']

voterId  = []
county = []
candidate = []


# Loop through the election data files

for filesToCheck in electionDataFiles:

    # Grab election  CSV
    electionCSV = os.path.join('raw_data', 'election_data_' + filesToCheck + '.csv')

    # Open current election data CSV
    with open(electionCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)

        for row in csvReader:
            # Append data from the row
            voterId.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

    # Zip lists together
    cleanCSV = zip(voterId,county,candidate)

combinedElectionDataCSV = os.path.join('raw_data', 'combined_election_data.csv')

totalVotes = 0
candidate = {}
candidateName = ''

with open(combinedElectionDataCSV, 'w', newline="") as csvFile:

    csvWriter = csv.writer(csvFile, delimiter=',')

    # Write Headers into file
    csvWriter.writerow(["Voter Id", "County", "Candidate"])

    # Write the zipped lists to a csv
    csvWriter.writerows(cleanCSV)


with open(combinedElectionDataCSV, 'r') as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader, None)

    for row in csvReader:
        totalVotes = totalVotes+1
        candidateName = row[2]
        if (candidateName in candidate):
            candidate[candidateName] += 1
        else:
            candidate[candidateName] = 1



    print("---------------------------------")
    print("Election Results")
    print("---------------------------------")
    print("Total Votes : " + str(totalVotes))
    print("---------------------------------")

    percentVote = 0

    for key,value in candidate.items():

        percentVote = '{0:.2f}'.format(((value/totalVotes)*100))

        print(key + '             :  ' + str(percentVote) + '%' + '  Votes: (' + str(value) + ')' )

    print("---------------------------------")
    print("Winner : "  + str(max(candidate,key=candidate.get)))
    print("---------------------------------")


