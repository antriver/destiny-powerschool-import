import csv

newrows = []

def get_access_level(powerschoolID, school):
	if powerschoolID == "55970" or powerschoolID == "53550":
		return "Library Assistant"
	elif powerschoolID == "52950":
		return "Library Administrator"
	elif school == 111 or school == 112:
		return "Teacher"
	else:
		return "Staff"

with open('faculty.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:

		powerschoolID = row[0]
		active = row[5]
		access_level = get_access_level(powerschoolID, row[5])
		row.append(access_level)

		if active == '1' and powerschoolID and powerschoolID[:2] != '22' and powerschoolID[:2] != 'xx' and powerschoolID[:6] != 'xbatch' and len(powerschoolID) == 5:
			print(row)
			newrows.append(',' . join(row))

newcsv = open('faculty-processed.csv', 'w')
newcsv.write("\n" . join(newrows))

