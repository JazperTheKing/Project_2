import csv, re
from pathlib import Path

def profit_and_loss():
  fp_read = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
  fp_write = Path.cwd()/"summary_report.txt"
  pnl_empty_list = []
  days_empty_list = []
  net_profit_empty_list = []
  diff_empty_list = []
  exchange_rate = []


  with fp_read.open(mode= "r", encoding= "UTF-8") as file:
    pnl_reader = csv.reader(file)
    next(pnl_reader)

    for line in pnl_reader:
      pnl_empty_list.append(line)
      day = line[0]
      net_profit = line[4]
      days_empty_list.append(int(day))
      net_profit_empty_list.append(net_profit)


  with fp_write.open(mode= "r", encoding= "UTF-8") as file:
    summary_get = file.read()
    exchange_rate.append(summary_get)

    for info, content in enumerate(exchange_rate):
      forex = re.search(pattern= "SGD.+\d", string=content)
      forex = forex.group()
      forex = float(forex[3:10])
            
      for items in range(len(net_profit_empty_list)):
        diff = float(net_profit_empty_list[items]) - float(net_profit_empty_list[items-1])
        diff_empty_list.append(diff)
        usd_to_sgd = diff_empty_list[-1] * forex
                    
    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
      for category in zip(days_empty_list, diff_empty_list):
        if category[1] <= 0:
          file.write("\n[NET PROFIT DEFICIT]" " "f"DAY: {category[0]}, AMOUNT: SGD{category[1]*forex}")
        else:
          file.write("\n[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

print(profit_and_loss())
