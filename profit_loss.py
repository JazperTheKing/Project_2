import csv, re
from pathlib import Path

# write a function: profit_and_loss() with no parameter 
def profit_and_loss():
  fp_read = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
  fp_write = Path.cwd()/"summary_report.txt"
  
  # create 5 empty lists
  pnl_empty_list = []
  days_empty_list = []
  net_profit_empty_list = []
  diff_empty_list = []
  exchange_rate = []

  # open 'profit-and-loss-usd.csv' file using 'with' and 'open' keyword in 'read' mode
  with fp_read.open(mode= "r", encoding= "UTF-8") as file:
    pnl_reader = csv.reader(file)
    next(pnl_reader)

    # append the 'day' and 'net profit' columns of values into 'pnl_empty_list', before appending the two columns of data 
    # into 2 different empty lists, 'days_empty_list' and 'net_profit_empty_list'
    for line in pnl_reader:
      pnl_empty_list.append(line)
      day = line[0]
      net_profit = line[4]
      days_empty_list.append(int(day))
      net_profit_empty_list.append(net_profit)

  # open "summary_report.txt" file using 'with' and 'open' keyword in 'read' mode
  with fp_write.open(mode= "r", encoding= "UTF-8") as file:
    summary_get = file.read()
    exchange_rate.append(summary_get)
   
     # using for loop with enumerate to in the empty list
    for info, content in enumerate(exchange_rate):
      forex = re.search(pattern= "SGD.+\d", string=content)
      forex = forex.group()
      forex = float(forex[3:10])
      
      # compute the net profit difference between each day and append the differences into 'diff_empty_list'
      # before converting the usd values to sgd values
      for items in range(len(net_profit_empty_list)):
        diff = float(net_profit_empty_list[items]) - float(net_profit_empty_list[items-1])
        diff_empty_list.append(diff)
        usd_to_sgd = diff_empty_list[-1] * forex
    
    # open "summary_report.txt" file using 'with' and 'open' keyword in 'append' mode 
    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
      for category in zip(days_empty_list, diff_empty_list):
        if category[1] <= 0:
          file.write("\n[NET PROFIT DEFICIT]" " "f"DAY: {category[0]}, AMOUNT: SGD{category[1]*forex}")
          # else if the category is more than 0, it will print this
        else:
          file.write("\n[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

print(profit_and_loss())
