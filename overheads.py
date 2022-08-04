# import modules

import csv, re
from pathlib import Path



# check file path of current working directory
print(Path.cwd())

#from api_test import function

# Start of a function
def overheads():
    fp_write = Path.cwd()/"summary_report.txt"
    fp_get = Path.cwd()/"api.py"
    fp_read = Path.cwd()/"csv_reports"/"overheads-day-42.csv"
    # Checking if a file/directory exists with Pathlib
    # Returns: True if a file/directory exists, False if a file/directory does not exit
    print(fp_read.exists())

    #Create a list
    overheads_empty_list = []
    oh_cat = []
    oh_usd = []
    api_list = []
    
        # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_write.open(mode= "r", encoding= "UTF-8") as file:
        api_get = file.read()
        api_list.append(api_get)

        for info, content in enumerate(api_list):
            forex = re.search(pattern= "SGD.+\d", string=content)
            forex = forex.group()
            forex = float(forex[3:10])

    # Open file using 'with' and 'open' keyword in 'read' mode
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        oh_reader = csv.reader(file)
        # Use of next to skip first header row in csv file
        next(oh_reader)
       
        for line in oh_reader:
            # append to empty list
            overheads_empty_list.append(line)
            # for loop
            for sublist in overheads_empty_list:
                # sublist[0] is catergory column
                oh_cat.append(sublist[0])
                # sublist[1] is overhead column
                oh_usd.append(float(sublist[1]))
        
        # creating variable for max value
        max_value = max(oh_usd)
        # creating variable for max value category
        max_value_cat = oh_usd.index(max_value)
        # converting max value from USD to SGD
        usd_to_sgd = max_value * forex
        
    #Open file using 'with' and 'open' keyword in 'append' mode
        with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
            file.write("\n[HIGHEST OVERHEADS] " " "f"CATEGORY: {oh_cat[max_value_cat]}, AMOUNT: SGD{usd_to_sgd}")
                
print(overheads())
