# 计算日期数据周同比
import datetime

date_sale = {}
is_first_line = True

with open("./p027/p027_date_sale_data.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale_number = line.split("\t")
        date_sale[date] = float(sale_number)


def get_diff_days(date, days):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    date_delta = datetime.timedelta(days=days)
    return (date_obj + date_delta).strftime("%Y-%m-%d")


for date, sale_number in date_sale.items():
    date_minus_7 = get_diff_days(date, -7)
    sale_number_minus_7 = date_sale.get(date_minus_7, 0)
    if sale_number_minus_7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = (sale_number - sale_number_minus_7) / sale_number_minus_7
        print(date, sale_number, date_minus_7, sale_number_minus_7, week_diff)
