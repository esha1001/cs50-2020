from sys import argv, exit
import csv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

place = 0
counter = 0
tracker = set([0])
strlist = []
strcount = []
database = {}

with open(argv[1], "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # create a list containing names of the STRs that we want to look for
    strlist = next(csv_reader)
    strlist.remove("name")
    
    # create a dictionary: keys --> names // values --> lists of str counts
    for row in csv_reader:
        database[row[0]] = []
        for i in range(len(strlist)):
            database[row[0]].append(int(row[i+1]))

    # to check if everything is working correctly
    # print(database)
    # print(strlist)

with open(argv[2], 'r') as file:
    # copying contents of file into string dnasequence
    dnasequence = file.read()
    
# reading dnasequence to look for specific STR and storing max STR repeat in strcount list
for i in range(len(strlist)):
    for place in range(len(dnasequence)):
        while True:
            if dnasequence[place:place + len(strlist[i])] == strlist[i]:
                counter += 1
                place += len(strlist[i])
            else:
                tracker.add(counter)
                counter = 0
                break
    strcount.append(max(tracker))
    tracker = set([0])

# to check if everything is working correctly
# print(strcount)

if strcount in database.values(): 
    for dataname, datastrcount in database.items():
        if datastrcount == strcount:
            print(dataname)
else:
    print("No match")
        
