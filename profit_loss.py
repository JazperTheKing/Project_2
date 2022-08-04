from pathlib import Path
import re, csv

print(Path.cwd())

file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
print(file_path.exists())
print(file_path)

def profit_loss(forex):
  with file_path.open(mode="r", encoding = "UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(file)

    
    for line in reader:
      net_profit = print(line[0], line[4])
    return net_profit
(not complete)
