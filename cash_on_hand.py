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


with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    category = []
    cash_on_hand = []
    coh_change = []

    for i in range (1, len(cash_on_hand)):
        coh_change.append(cash_on_hand[i] - cash_on_hand[i-1])
        print(coh_change)






# Open file using 'with' and 'open' keyword in 'read' mode
# with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     def solve(csv_reader):
#         if csv_reader[1,1] <= csv_reader[0,1]:
#             return "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

#         for i in range(len(csv_reader)):
#             if i - 1 >= 0:
#                 if csv_reader[i] == csv_reader[i-1]:
#                     return "[CASH DEFICIT] DAY: , AMOUNT:"


# print(solve(csv_reader))


