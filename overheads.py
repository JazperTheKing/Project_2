# import modules
import requests
from pathlib import Path
import csv, re

# check file path of current working directory
print(Path.cwd())

#from api_test import function
fp_write = Path.cwd()/"summary_report.txt"
fp_get = Path.cwd()/"api.py"
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
def overheads(forex):
    # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        oh_reader = csv.reader(file)
        # Use of next to skip first header row in csv file
        next(oh_reader)

    for line in oh_reader:
        overheads_empty_list.append(line)
        cat = line[0]
        amt = line[1]
        cat_empty_list.append(int(cat))
        amt_empty_list.append(amt)

    # Open file using 'with' and 'open' keyword in 'read' mode
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

    # Open file using 'with' and 'open' keyword in 'append' mode
    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
        for category in zip(cat_empty_list, amt_empty_list):
            file.write("\n[HIGHEST OVERHEADS] " " "f"DAY: {category[0]+1}, AMOUNT: SGD{usd_to_sgd}")
            
    print(overheads(forex))

