import requests
from pathlib import Path
import csv

# check file path of current working directory
print(Path.cwd())

filepath = Path.cwd()/"csv_reports"/"overheads-day-42.csv"
# check if the new file path exists will return True since "cash-on-hand-usd.csv" exists in the filepath
print(filepath.exists())
print(filepath)  

#define overhead function
def overhead_function():

    # Open file using 'with' and 'open' keyword in 'read' mode
    with filepath.open('r', encoding = 'UTF-8', newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        category = 0
        next(csv_reader)
        for row in csv_reader:
                max_overheads = max(row[0] for row in csv.reader(csv_file))
                print(f'[HIGHEST OVERHEADS] {", ".join(row)}')
print(overhead_function())