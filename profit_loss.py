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

<<<<<<< HEAD
# Open the profit-and-loss-usd csv file to read it
with file_path.open(mode="r", encoding = "UTF-8", newline="") as file:
  reader = csv.reader(file)
  next(file)

  for row in reader:
     for (i,v) in enumerate(row):
            columns[i].append(v)
print(columns[4])

=======
    
    for line in reader:
      net_profit = print(line[0], line[4])
    return net_profit
(not complete)
>>>>>>> a5ab80a48fd5561160d077a1dccf5e5e4bd51a24
