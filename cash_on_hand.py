import csv
from pathlib import Path
#from api_test import function

fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
fp_write = Path.cwd()/"summary_report.txt"

coh_empty_list = []
days_empty_list = []
amt_empty_list = []
diff_empty_list = []

def cash_on_hand(forex):
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        coh_reader = csv.reader(file)
        next(coh_reader)

        for line in coh_reader:
            coh_empty_list.append(line)
            day = line[0]
            amt = line[1]
            days_empty_list.append(int(day))
            amt_empty_list.append(amt)

        for items in range(1, len(amt_empty_list)):
            diff = float(amt_empty_list[items]) - float(amt_empty_list[items-1])
            diff_empty_list.append(diff)
            for sublist in diff_empty_list:
                usd_to_sgd = sublist * forex

    with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
        for category in zip(days_empty_list, diff_empty_list):
            if category[1] <= 0:
                file.write("\n[CASH DEFICIT]" " "f"DAY: {category[0]+1}, AMOUNT: SGD{usd_to_sgd}")
            else:
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
print(cash_on_hand(forex=1.38025))

