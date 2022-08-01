from pathlib import Path
import re, csv
from collections import defaultdict

print(Path.cwd())

file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd .csv"
print(file_path.exists())
print(file_path)

columns = defaultdict(list)

# Open the profit-and-loss-usd csv file to read it
with file_path.open(mode="r", encoding = "UTF-8", newline="") as file:
  reader = csv.reader(file)
  next(file)

  for row in reader:
     for (i,v) in enumerate(row):
            columns[i].append(v)
print(columns[4])
(not complete)
