#explanation of the pipeline and its purpose:
This project is a program that takes a data file and checks and cleans it, it has 4 main steps:
1) load: reas data from 3 different types of files like CS, JSON, and YAML
2) validate: Check that the data has the required columns and valid number (format is right)
3) Clean: Remove the duplicate rows, misiing values, and outliers
4) Save: Save the new clean data as CSV file

The project is organised into different files: 
-pipeline.py cordinates and runs the entire process
-data_loaders.py reads the input file
-data_validator.py checks if teh data is valid
-data_processor.py cleans the data and gives a report
-utils.py handles logging and basic file checks
-config/config.yaml controls what daa is requried and how it should be cleaned 
-fixtures/ contains sample data for testing 

The config/congif.yaml files controls which columns are required and how the data should be cleaned while the fixtures/ folder contains sample data how testing. The configuration file makes it posiible to process different datasets by changing the input file and setting without changing the code. To run teh program use a command that specifies teh input file, output location, config file and whether to show additional details, for example the report might show that the original dataset had 100 rows and 9 columns but after cleaning it had only 90 rows and 7 columns meaning 10 rows were removed and 2 columns were removed. 

