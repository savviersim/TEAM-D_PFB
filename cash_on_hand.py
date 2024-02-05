##THIS IMPORTS THE PATH CLASS IN PATHLIB AND IMPORTS CSV MODULE TO HANDLE OUR FILES##
from pathlib import Path
import csv

def cashOnHand_function():

    """

    -FUNCTION PERFORMS CALCULATION OF NET PROFIT DEFICITS FOR EACH DAY WITH A DEFICIT BASED
    ON DATA READ FROM "CASH_ON_HAND.CSV" FILE
    -IDENTIFIES THE TOP THREE HIGHEST CASH DEFICIT DAYS, IF THEY EXIST.
    -IF DEFICIT DAYS ARE ABSENT, IT DETERMINES THE HIGHEST NET PROFIT SURPLUS DAY 
    -RESULTS ARE WRITTEN TO "SUMMARY_REPORT.TXT" -> RETURNED AS A FORMATTED STRING,
    INCLUDING DEFICIT INFORMATION
    -NO PARAMETERES REQUIRED.
    
    """

    #CREATION OF FILE PATH#
    #FILE PATH CREATED TO CASH_ON_HAND.CSV TO RETRIEVE DATA#
    fp_read = Path.cwd() / "csv_reports" / "Cash_on_hand.csv"
    
    #CREATION OF FILE PATH TO SUMMARY_REPORT.TXT FILE IN WORKING DIRECTORY CURRENTLY
    #.cwd() UTILIZED TO OBTAIN A WORKING DIRECTORY
    fp_write = Path.cwd() / "summary_report.txt"

    
    #THIS WOULD READ DATA IN THE OVERHEADS.CSV FILE WITH UTF-8 ENCODING 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        #CREATES A CSV.READER CALLED READER TO READ DATA IN FILE WHICH IS OPENED
        reader = csv.reader(file)
        next(reader)  #SKIPS FIRST ROW OF CSV FILE WHICH IS THE HEADER
        #READS DATA INTO LIST, CONVERTING DAY INTO INTEGER & CASH ON HAND TO FLOAT
        cash_on_hand = [(int(row[0]), float(row[1])) for row in reader]


    #INITIALIZE EMPTY LISTS TO STORE AND KEEP TRACK OF DAYS WITH CASH DEFICITS AND ALL DEFICITS 
    deficits_days = []
    all_deficits = []  
    
    #INITIALIZES EMPTY STRING VARIABLE IN ORDER TO STORE THE GENERATED SUMMARY REPORT
    output = ""
    #INITIALIZES VARIABLE TO TRACK HIGHEST CASH SURPLUS AND SURPLUS DAY
    highest_surplus = 0
    surplus_day = 0


    #LOOP ITERATES ON THE RANGE OF DAYS (DAY11-DAY90) IN CASH_ON_HAND LIST
    for day_number in range(1, len(cash_on_hand)):
        current_day = cash_on_hand[day_number][0] 
        current_cash = cash_on_hand[day_number][1]  

        #RETRIEVES CASH AMOUNT FROM THE PREVIOUS DAY IN CASH_ON_HAND LIST, AND ASSIGNS IT TO THE PREVIOUS_CASH VARIABLE 
        previous_cash = cash_on_hand[day_number-1][1]  

        #ANALYZES IF PRESENT CASH AMOUNT IS LESS THAN THE CASH AMOUNT ON THE PREVIOUS DAY
        if current_cash < previous_cash:
            #CALCULATES DEFICIT WITH THE SUBTRACTION OF CURRENT DAY CASH AMT. FROM PREVIOUS DAY CASH AMT.
            deficit = previous_cash - current_cash

            #IF THERE IS A CASH DEFICIT, CURRENT DAY INDEX WILL BE ADDED TO DEFICIT DAY LIST TO KEEP TRACK OF DAYS WITH DEFICITS
            #STORES DAY NUMBER AND DEFICIT AMT.
            deficits_days.append((current_day, deficit)) 
            #STORES IN LIST OF ALL DEFICITS 
            all_deficits.append((current_day, deficit))  


    #THIS SORTS THE LIST OF DEFICITS BY DAY IN ASCENDING ORDER
    all_deficits.sort()

    #INITIALIZSES A LIST WITH THREE SUBLISTS, EACH CONTAINING TWO ZEROS,
    #TO STORE INFORMATION ABOUT THE TOP THREE DEFICITS(BY AMOUNT) LATER ON IN THE CODE
    top_deficits = [[0, 0], [0, 0], [0, 0]]
#THIS "FOR" LOOP FINDS THE TOP THREE DEFICITS BY ITS AMOUNT 
    #CHECKS IF AMT. OF CURRENT DEFICIT IS LARGER THAN ANY DEFICITS IN 'TOP_DEFICITS'
    #IF IT IS LARGER, CURRENT DEFICIT IS INSERTED INTO CORRECT POSITION IN 'TOP_DEFICITS' 
    #WHILE THE OTHER SMALLER DEFICITS WILL BE SHIFTED DOWN 
    for deficit in all_deficits:
        if deficit[1] > top_deficits[0][1]:
            top_deficits[2] = top_deficits[1]
            top_deficits[1] = top_deficits[0]
            top_deficits[0] = deficit
        elif deficit[1] > top_deficits[1][1]:
            top_deficits[2] = top_deficits[1]

#THIS "FOR" LOOP GOES THROUGH "ALL_DEFICITS" LIST WHICH IS SORTED BY DAY 
    #AND APPENDS A FORMATTED STRING FOR EACH DEFICIT TO THE OUTPUT VAR.
    #EACH LINE IN OUTPUT IS FORMATTED TO STATE THE DAY AND AMT. OF THE CASH DEFICIT 
    for day, amount in all_deficits:
        output += f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{int(amount)}\n"

    #THIS WILL OUTPUT THE TOP THREE DEFICITS IF THEY EXIST,
    #THIS LINE CHECKS THE IF THE AMT. OF THE HIGHEST CASH DEFICIT (FIRST ELEMENT OF 'TOP_DEFICITS' LIST, ACCESSED USING [0]),
    #IS GREATER THAN 0 -> CONDITION USED TO ENSURE THAT THERE IS AT LEAST ONE CASH DEFICIT WITH A POSITIVE,
    #AMOUNT BEFORE ATTEMPTING TO GENERATE THE OUTPUT MESSAGES.
    if top_deficits[0][1] > 0:

        #ORDINAL LIST CREATED CONTAINING '1ST HIGHEST', '2ND HIGHEST', AND '3RD HIGHEST',
        #THESE LABELS USED TO DESCRIBE THE ORDINAL RANKING OF THESE CASH DEFICITS.
        ordinal = ['HIGHEST', '2ND HIGHEST', '3RD HIGHEST']

        #INDEX REPRESENTS RANKING OF THE CURRENT CASH DEFICIT 
        for index, (day, amount) in enumerate(top_deficits): #ENUMERATE() USED AS IT CREATES AND RETURN A NEW OBJECT,
                                                         #INSTEAD OF VALUES, AND IS A METHOD TO REQUIRED TO RETRIEVE A VALUE,
                                                         #OF AN ENUMERATE OBJECT- USED TO GET BOTH INDEX,
                                                         #(which corresponds to the ordinal ranking) & (day, amount) FROM top_deficits,
                                                         #ALLOWS US TO ACCESS BOTH DAY AND AMOUNT ACCORDING TO THEIR RANKING
            
            #OUTPUT OF A FORMATTED STRING WILL BE GIVEN 
            #[{ORDINAL[INDEX]}CASH DEFICIT] CONSTRUCTED BY TAKING THE LABEL CORRESPONDING TO THE ORDINAL,
            #RANKING 9EG.'HIGHEST', '2ND HIGHEST' EG.) BASED ON THE INDEX VARIABLE 
            output += f"\n[{ordinal[index]} CASH DEFICIT] DAY: {day}, AMOUNT: SGD{int(amount)}"
            


    #IF DEFICIT_DAYS LIST IS EMPTY, THE FOLLOWING WILL BE EXECUTED
    if not deficits_days and cash_on_hand:
        surplus_day = cash_on_hand[-1][0]
        highest_surplus = int(cash_on_hand[-1][1] - cash_on_hand[0][1])

        #FORMATTED STRING APPENDED TO SHOW THAT ALL CASH AMT. ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY TO OUTPUT VAR.
        output += "\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

        #FORMATTED STRING APPENDED TO SHOW THE DAY OF THE HIGHEST SURPLUS & AMT OF HIGHEST SURPLUS TO OUTPUT VAR.
        output += f"\n[HIGHEST CASH SURPLUS] DAY: {surplus_day}, AMOUNT: SGD{highest_surplus}"

    #OPENS WRITE MODE IN 'SUMMARY_REPORT.TXT' FILE 
    with fp_write.open(mode="w", encoding="UTF-8") as summary_file:

        #WRITES OUTPUT VARIABLE TO SUMMARY_REPORT.TXT" FILE 
        summary_file.write(output)

    return output


#NAMING FUNCTION TO DOUBLE-CHECK ACTUAL OUTPUT
print(cashOnHand_function())
