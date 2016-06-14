import csv

newrows = []

def password_from_dob(dob):
	dob = dob.replace('/', '')
	return dob

with open('students.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:

		dob = row[6]
		row.append(password_from_dob(dob))
		newrows.append(',' . join(row))

newcsv = open('students-processed.csv', 'w')
newcsv.write("\n" . join(newrows))

