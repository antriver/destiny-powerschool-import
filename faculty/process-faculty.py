import csv

newrows = []

with open('faculty.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:

		powerschoolID = row[0]
		active = row[4]

		if active == '1' and powerschoolID and powerschoolID[:2] != '22' and powerschoolID[:2] != 'xx' and powerschoolID[:6] != 'xbatch' and len(powerschoolID) == 5:

			newrows.append(',' . join(row))

newcsv = open('faculty-processed.csv', 'w')
newcsv.write("\n" . join(newrows))

