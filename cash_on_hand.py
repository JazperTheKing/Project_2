# import modules
import csv, re
from pathlib import Path

# check file path of current working directory
print(Path.cwd())

#from api_test import function
fp_write = Path.cwd()/"summary_report.txt"
fp_get = Path.cwd()/"api.py"
fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# Checking if a file/directory exists with Pathlib
# Returns: True if a file/directory exists, False if a file/directory does not exit
print(fp_read.exists())

# Create a list
coh_empty_list = []
days_empty_list = []
amt_empty_list = []
diff_empty_list = []
api_list = []

# Start of a function
def cash_on_hand(forex):
    # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        coh_reader = csv.reader(file)
        # Use of next to skip first header row in csv file
        next(coh_reader)

        for line in coh_reader:
            coh_empty_list.append(line)
            day = line[0]
            amt = line[1]
            days_empty_list.append(int(day))
            amt_empty_list.append(amt)

    # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_get.open(mode= "r", encoding= "UTF-8") as file:
        api_get = file.read()
        api_list.append(api_get)

        for info in enumerate(api_list):
            forex = re.search(pattern= "function", float=info)
        
        for items in range(1, len(amt_empty_list)):
            diff = float(amt_empty_list[items]) - float(amt_empty_list[items-1])
            diff_empty_list.append(diff)
            for sublist in diff_empty_list:
                usd_to_sgd = sublist * forex

    # Open file using 'with' and 'open' keyword in 'append' mode
    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
        for category in zip(days_empty_list, diff_empty_list):
            if category[1] <= 0:
                file.write("\n[CASH DEFICIT]" " "f"DAY: {category[0]+1}, AMOUNT: SGD{usd_to_sgd}")
            else:
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    print(cash_on_hand(forex))
