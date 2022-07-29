import requests
from pathlib import Path
import re, csv


print(Path.cwd())

filepath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
print(filepath.exists())
print(filepath)


with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line)
        #if 

    

print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
print("[CASH DEFICIT] DAY: {} , AMOUNT: {}")