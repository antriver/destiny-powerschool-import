E:

cd E:\DestinyImport\faculty

C:\Python34\python fix-faculty.py

cd E:\Follett\FSC-Destiny\fsc\bin\

PatronImportConverter "E:\DestinyImport\faculty\faculty-fixed.csv" "E:\DestinyImport\faculty\faculty.xml" "E:\DestinyImport\faculty\convert_faculty.properties"

updatepatrons "E:\DestinyImport\faculty\update_faculty.properties" "E:\DestinyImport\faculty\faculty.xml"
          