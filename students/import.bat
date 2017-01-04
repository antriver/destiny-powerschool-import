E:

cd E:\DestinyImport\students

python process-students.py

cd E:\Follett\FSC-Destiny\fsc\bin\

PatronImportConverter "E:\DestinyImport\students\students-processed.csv" "E:\DestinyImport\students\students.xml" "E:\DestinyImport\students\convert_students.properties"

updatepatrons "E:\DestinyImport\students\update_students.properties" "E:\DestinyImport\students\students.xml"

cd E:\DestinyImport\students
