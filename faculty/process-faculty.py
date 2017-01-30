import csv

newrows = []

def get_access_level(title, school):
	if title == "Library Assistant":
		return "Library Assistant"
	elif title == "Library Administrator":
		return "Library Administrator"
	else:
		return "Teacher"

with open('faculty.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:

		powerschoolID = row[0]
		title = row[4]
		active = row[5]
		school = row[6]

		access_level = get_access_level(title, school)
		row.append(access_level)

		if active == '1' and powerschoolID and powerschoolID[:2] != '22' and powerschoolID[:2] != 'xx' and powerschoolID[:6] != 'xbatch' and len(powerschoolID) == 5:
			print(row)
			newrows.append(',' . join(row))

newcsv = open('faculty-processed.csv', 'w')
newcsv.write("\n" . join(newrows))

