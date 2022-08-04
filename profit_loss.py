
# check file path of current working directory
# import modules
from pathlib import Path
import re, csv

# check file path of current working directory
print(Path.cwd())

#from api_test import function
fp_get = Path.cwd()/"api.py"
fp_write = Path.cwd()/"summary_report.txt"
fp_read = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
# Checking if a file/directory exists with Pathlib
# Returns: True if a file/directory exists, False if a file/directory does not exit
print(fp_read.exists())

# Start of a function
def profit_loss():
  # Open file using 'with' and 'open' keyword in 'read' mode
  with fp_read.open(mode="r", encoding = "UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Use of next to skip first header row in csv file
    next(file)

    # Create lists
    net_profit= []
    day = []
    net_profit_diff = []
    for line in reader:
      day.append(int(line[0]))
      net_profit.append(int(line[4]))
      print(net_profit)

      api_list = []
       # Open file using 'with' and 'open' keyword in 'read' mode
      with fp_write.open(mode= "r", encoding= "UTF-8") as file:
        api_get = file.read()
        api_list.append(api_get)

        for info, content in enumerate(api_list):
            forex = re.search(pattern= "SGD.+\d", string=content)
            forex = forex.group()
            forex = float(forex[3:10])

        for i in range(len(net_profit)):
          
          net_profit_diff.append(float(net_profit[i]) - float(net_profit[i-1]))
          print(net_profit_diff[-1])
          for sublist in net_profit_diff:
                usd_to_sgd = sublist * forex

      # Open file using 'with' and 'open' keyword in 'append' mode
      with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:
        for category in zip(day, net_profit_diff):
            if category[1] <= 0:
              file.write("\n[PROFIT DEFICIT]" " "f"DAY: {category[0]}, AMOUNT: SGD{usd_to_sgd}")
            else:
                file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

print(profit_loss())
