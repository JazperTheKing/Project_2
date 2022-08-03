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


Open file using 'with' and 'open' keyword in 'read' mode
with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line)
        if day 
        
            print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")


        else:

            print("[CASH DEFICIT] DAY: {day} , AMOUNT: {amount}")



    

