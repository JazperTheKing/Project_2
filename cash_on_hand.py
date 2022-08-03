# import requests, re, csv module, pathlib
import requests
from pathlib import Path
import re, csv



# check file path of current working directory
print(Path.cwd())

filepath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# check if the new file path exists will return True since "cash-on-hand-usd.csv" exists in the filepath
print(filepath.exists())
print(filepath)  


# Open file using 'with' and 'open' keyword in 'read' mode
with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    amount = []

    #     if list[i] < list[i +1]:
    #         csv_file = True
        
    #     else:
    #         csv_file = False
    
    # if csv_file == True:
    #     print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # else: 
    #     print("[CASH DEFICIT] DAY: , AMOUNT:")




    # max_value = max(row[0] for row in csv.reader(csv_file))
    # #print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    # print(max_value)
    
    # min_value = min(row[0] for row in csv.reader(csv_file))
    # #print(f"[CASH DEFICIT] DAY: , AMOUNT:")
    # print(min_value)
