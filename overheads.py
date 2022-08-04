# import modules
import requests
from pathlib import Path
import csv, re, api

# check file path of current working directory
print(Path.cwd())

fp_get = Path.cwd()/"api.py"
fp_write = Path.cwd()/"summary_report.txt"
fp_read = Path.cwd()/"csv_reports"/"overheads-day-42.csv"
# Checking if a file/directory exists with Pathlib
# Returns: True if a file/directory exists, False if a file/directory does not exit
print(fp_read.exists())

# Create a list
overheads_empty_list = []
cat_empty_list = []
amt_empty_list = []
max_empty_list = []
api_list = []

# Start of a function
def overheads():
    # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        coh_reader = csv.reader(file)
        next(coh_reader)

    for line in coh_reader:
        overheads_empty_list.append(line)
        cat = line[0]
        amt = line[1]
        cat_empty_list.append(int(cat))
        amt_empty_list.append(amt)

    with fp_get.open(mode= "r", encoding= "UTF-8") as file:
        api_get = file.read()
        api_list.append(api_get)

        for info in enumerate(api_list):
            forex = re.search(pattern= "function", float=info)
        
        for items in range(1, len(amt_empty_list)):
            max = float(max(amt_empty_list))
            max_empty_list.append(max)
            for sublist in max_empty_list:
                usd_to_sgd = sublist * forex

    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
        for category in zip(cat_empty_list, amt_empty_list):
            file.write("\n[HIGHEST OVERHEADS]" " "f"DAY: {category[0]+1}, AMOUNT: SGD{usd_to_sgd}")
            
print(overheads())


# # start of a function
# def overhead_function():
#     # Open file using 'with' and 'open' keyword in 'read' mode
#     with fp_read.open('r', encoding = 'UTF-8', newline = '') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         category = 0
#         #
#         next(csv_reader)
#     for row in csv_reader:
#             max_overheads = max(row[0] for row in csv.reader(csv_file))
#             print(f'[HIGHEST OVERHEADS] {", ".join(row)}')
# print(overhead_function())