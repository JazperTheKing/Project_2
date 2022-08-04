# import requests, re, csv module, pathlib
import requests
from pathlib import Path
import re
import csv

# check file path of current working directory
print(Path.cwd())

filepath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# check if the new file path exists will return True since "cash-on-hand-usd.csv" exists in the filepath
print(filepath.exists())
print(filepath)  

with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    day = []
    cash_on_hand = []
    coh_change = []

    for row in csv_reader:
        day.append(row[0])

    for i in range (1, len(cash_on_hand)):
        coh_change.append(cash_on_hand[i] - cash_on_hand[i-1])
        #coh_change = ("Cash On Hand")-("Cash On Hand").shift(1)
        max_coh_change = max(coh_change)
        max_coh_day = str(day[coh_change.index(max(coh_change))])
    
    print(f"[CASH DEFICIT] DAY: {max_coh_day} AMOUNT {max_coh_change}")

    

# "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
# return "[CASH DEFICIT] DAY: , AMOUNT:"


# def coh_function():
#     with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         category = []
#         cash_on_hand = []
#         coh_change = []

#     for i in range (1, len(cash_on_hand)):
#         #coh_change.append(cash_on_hand[i] - cash_on_hand[i-1])
#         coh_change = ["Cash On Hand"]-["Cash On Hand"].shift(1)


#     file_path = Path.cwd()/"summary_report.txt"
#     with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
#          file.write(coh_change)

# print(coh_function())
