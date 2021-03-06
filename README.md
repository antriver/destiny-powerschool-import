# Import from PowerSchool to Follett Destiny

Using Destiny's 'Patron Import Converter' tools, these scripts allow you to automatically import students and faculty. This is tailored for Suzhou Singapore International School, but can be modified for use elsewhere.

## Setup
Place the students.csv or faculty.csv file exported from PowerSchool into the students or faculty directory respectively.

[`import.bat`](import.bat) runs the patron import into Destiny and should be set as a Scheduled Task on the server. (Using the automate scripts provided by Destiny didn't work, but this does and is simpler).

### Faculty fields to export (PowerSchool)
**faculty.csv**
```
TeacherNumber
First_Name
Last_Name
Email_Addr
Status
SchoolID
```

### Student fields to export (PowerSchool)
**students.csv**
```
Student_Number
ID
Grade_Level
Home_Room
Last_Name
First_Name
DOB
LTIS_DragonNet_Username
```

## Files

`convert_students.properties`: The settings used by Patron Import Converter (when parsing the .csv)

`import.bat`: Runs the CSV conversion and imports the generated XML to Destiny

`students-log.txt`: The log file from the Patron Import Converter. This will have many lines saying it can't match students. Those students are ones whose Grade Level in PowerSchool is not between 1 and 12.

`students.csv`: The exported data from PowerSchool. Overwrite this file with the latest data. (Keep the format the same though! If you change the format of this file, also edit convert_students.properties)

`students.xml`: The output generated by the Patron Import Converter from students.csv. Don't edit this file as it is automatically generated

`update_students.properties`: The settings used when importing the students.xml file

## Important! The first time it runs

District ID is not set on all current student entries in Destiny, only Barcode is.
To populate the District ID field, edit convert_students.properties and change
MatchUsingDistrictID=true
to
MatchUsingDistrictID=false

Then run import.bat once

After that, change back to MatchUsingDistrictID=true and future matches will be made using the now filled District ID instead of Site Name + Barcode. This allows students to be moved from Elementary School to Secondary School automatically, as the DistrictID is a unique ID across the entire installation, not just per site.
