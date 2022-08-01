import requests
from pathlib import Path
import re, csv

file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
print(file_path.exists())
print(file_path)


# Open the profit-and-loss-usd csv file to read it
with file_path.open(mode="r", encoding = "UTF-8", newline="") as file:
  reader = csv.reader(file)
  next(file)

  for line in reader:
   print(line)
   
