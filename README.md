# Import from PowerSchool to Follett Destiny

Using Destiny's 'Patron Import Converter' tools, these scripts allow you to automatically import students and faculty.

## Setup
Place the `faculty.csv` and `students.csv` files exported from PowerSchool into the `facults` or `students` directory respectively.

### Faculty fields to export from PowerSchool
**faculty.csv**
```
TeacherNumber
First_Name
Last_Name
Email_Addr
Title
Status
SchoolID
```

### Student fields to export from PowerSchool
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
Gender
Sched_YearOfGraduation
```

## Running

### Import Faculty

Open a command prompt (Win + R then type 'cmd')
```
E:
cd DestinyImport\faculty
import.bat
```
If you just click on the import.bat script from the File Explorer it will not work. You must run it from a command prompt.

What it does:
1. Runs a python script (`process-faculty.py`) to create the file `faculty-processed.csv`.
    - Skips inactive staff and those with invalid Powerschool IDs.
    - Determines the 'access level' the staff member should have in Destiny, from the PS 'title' field.
2. Runs Destiny's "Patron Import Converter" to generate the `faculty.xml` file, using the settings from `convert_faculty.properties`
3. Runs Destiny's `updatepatrons` command using the data from `faculty.xml` and the settings in `update_faculty.properties`


### Import Students

Open a command prompt (Win + R then type 'cmd')
```
E:
cd DestinyImport\students
import.bat
```
If you just click on the import.bat script from the File Explorer it will not work. You must run it from a command prompt.

What it does:
1. Runs a python script (`process-students.py`) to create the file `students-processed.csv`.
    - Fixes date of birth format.
    - Previously this generated a password for the student but that now comes from LDAP.
2. Runs Destiny's "Patron Import Converter" to generate the `students.xml` file, using the settings from `convert_students.properties`
3. Runs Destiny's `updatepatrons` command using the data from `students.xml` and the settings in `update_students.properties`


## Notes

All matching is done using the `District ID` field in Destiny. This should always be set to a person's PowerSchool ID.
