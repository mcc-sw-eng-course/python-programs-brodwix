import csv
import operator
sortChoice = input("Sort by name (N) or by position (P) or by bib (B)? ")
cyclingData = csv.reader(open('inputlist.csv'), delimiter = ',', lineterminator= '\n')

def convert_to_int(row):
    return [row[0], int(row[1]), int(row[2])]

repairedVersion = []
for row in cyclingData:
    repairedVersion.append(convert_to_int(row))

if sortChoice == 'N':
    byName = sorted(cyclingData, key=operator.itemgetter(0), reverse= True)
    for n in byName:
        n = n.rstrip('\n')
        print (n)
elif sortChoice == 'P':
    byPosition = sorted(cyclingData, key = operator.itemgetter(1))
    for n in byPosition:
        n = n.rstrip('\n')
        print (n)
elif sortChoice == 'B':
    byBib = sorted(repairedVersion, key = operator.itemgetter(2))
    for n in byBib:
        print (n)
else:
    print ('unkwown')
memoryLump.close()