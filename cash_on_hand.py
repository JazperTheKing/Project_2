import csv, re
from pathlib import Path

def cash_on_hand():
    fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    coh_empty_list = []
    days_empty_list = []
    amt_empty_list = []
    diff_empty_list = []
    exchange_rate = []


    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        coh_reader = csv.reader(file)
        next(coh_reader)

        for line in coh_reader:
            coh_empty_list.append(line)
            day = line[0]
            amt = line[1]
            days_empty_list.append(int(day))
            amt_empty_list.append(amt)


    with fp_write.open(mode= "r", encoding= "UTF-8") as file:
        summary_get = file.read()
        exchange_rate.append(summary_get)

        for info, content in enumerate(exchange_rate):
            forex = re.search(pattern= "SGD.+\d", string=content)
            forex = forex.group()
            if forex is None:
                return None
            
            forex = float(forex[3:10])
            
            for items in range(len(amt_empty_list)):
                diff = float(amt_empty_list[items]) - float(amt_empty_list[items-1])
                diff_empty_list.append(diff)
                usd_to_sgd = diff_empty_list[-1] * forex
                    
        with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
            for category in zip(days_empty_list, diff_empty_list):
                if category[1] <= 0:
                    file.write("\n[CASH DEFICIT]" " "f"DAY: {category[0]}, AMOUNT: SGD{category[1]*forex}")
                else:
                    file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

print(cash_on_hand())


