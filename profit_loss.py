from pathlib import Path
import re, csv


file_path_read = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
file_path_write = Path.cwd()/"summary_report.txt"
file_path_get = Path.cwd()/"api.py"

def profit_loss(forex):
  with file_path_read.open(mode="r", encoding = "UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(file)

    net_profit= []
    day = []
    net_profit_diff = []
    for line in reader:
      day.append(int(line[0]))
      net_profit.append(int(line[4]))

      api_list = []
      with file_path_get.open(mode= "r", encoding= "UTF-8") as file:
        api_get = file.read()
        api_list.append(api_get)

        for info in enumerate(api_list):
            forex = re.search(pattern= "function", float=info)

        for i in range(1,len(net_profit)):
          net_profit_diff.append(float(net_profit[i]) - float(net_profit[i-1]))
          for sublist in net_profit_diff:
                usd_to_sgd = sublist * forex

      with file_path_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:
        for category in zip(day, net_profit_diff):
            if category[1] <= 0:
              file.write("\n[PROFIT DEFICIT]" " "f"DAY: {category[0]+1}, AMOUNT: SGD{usd_to_sgd}")
            else:
                file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

print(profit_loss(forex))
