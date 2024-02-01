##THIS IMPORTS THE PATH CLASS IN PATHLIB AND IMPORTS CSV MODULE TO HANDLE OUR FILES##
from pathlib import Path
import csv

def function_overheads():

    """
    -FUNCTION AUTOMATICALLY DETECTS CATEGORY WITH THE HIGHEST OVERHEAD 
    -NO INPUT PARAMETERS REQUIRED 
    -FUNCTION RETRIEVES DATA FROM "OVERHEADS.CSV" FILE TO DETERMINE CATEGORY 
    WITH THE HIGHEST OVERHEAD
    -RETURNS AS A FORMATTED STRING, PROVIDING INFORMATION OF HIGHEST OVERHEAD,
    OUTPUT WRITTEN INTO "SUMMARY_REPORT.TXT'
    
    """
    
    ##CREATION OF FILE OBJECTS##
    #FILE PATH CREATED TO OVERHEADS.CSV TO RETRIEVE DATA
    fp = Path.cwd() / "csv_reports" / "Overheads.csv" 

    #.cwd() UTILIZED TO OBTAIN A WORKING DIRECTORY
    file_path = Path.cwd() / "summary_report.txt" 

    #EMPTY SUMMARY_REPORT.TXT FILE CREATED 
    file_path.touch()  


    #INITIALIZES VARIABLES 
    overheads = []  #TO STORE CATEGORIES AND RESPECTIVE OVERHEADS FEES FROM OVERHEADS.CSV
    output = ""     #ENSURES THAT EMPTY STRING VAR. STORES THE SUMMARY REPORT CREATED

    #THIS WOULD READ DATA IN THE OVERHEADS.CSV FILE WITH UTF-8 ENCODING 
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  #SKIPS FIRST ROW OF CSV FILE WHICH IS THE HEADER

        for row in reader:
            #DIRECTLY CONVERTS VALUE IN DATA TO FLOAT 
            overheads.append([row[0], float(row[1])]) 

    
    if overheads:
        maximum_overhead_category, maximum_value = overheads[0]  #RETRIEVES CATEGORY NAME AND VALUE FROM OVERHEADS LIST

        #LOOP ITERATES WITH EACH ENTRY IN OVERHEADS LIST
        for category, value in overheads:
            if value > maximum_value: #ANALYZES IF CURRENT OVERHEAD COST IS GREATER THAN MAXIMUM OVERHEAD COST
                maximum_value = value #MAXIMUM_OVERHEAD_VALUE VAR. STORES NEW MAXIMUM OVERHEAD COST IF CURRENT OVERHEAD COST IS GREATER THAN CURRENT MAXIMUM COST
                maximum_overhead_category = category #MAXIMUM_CATEGORY VAR. STORES CATEGORY NAME OF NEW MAXIMUM OVERHEAD COST


        #APPENDS STRING TO OUTPUT VAR.
        #STRING DEPICTS CATEGORY NAME (MAXIMUM_OVERHEAD_CATEGORY) AND RESPECTIVE OVERHEAD COST AMOUNT IN %
        output += f"\n[HIGHEST OVERHEAD] {maximum_overhead_category}: {maximum_value}%\n"

        #OPENS WRITE MODE IN 'SUMMARY_REPORT.TXT' FILE 
        with file_path.open(mode="w", encoding="UTF-8") as summary_file:
            summary_file.write(output) #WRITES OUTPUT VARIABLE TO SUMMARY_REPORT.TXT" FILE 

        return output
    else:
        return "No overhead data found.\n" #IN THE EVENT THAT OVERHEAD DATAS ARE NOT ABLE TO BE ACCESSED

#NAMING FUNCTION TO DOUBLE-CHECK ACTUAL OUTPUT
summary_output = function_overheads()
print(summary_output)
