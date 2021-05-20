# 计算开始和结束范围的所有日期
import datetime


def get_date_range(begin_date, end_date, days=1):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        date_delta = datetime.timedelta(days=days)
        begin_date = (begin_date_obj + date_delta).strftime("%Y-%m-%d")
    return date_list


# 不要省略月份前的 0
begin_date = "2021-05-20"
end_date = "2021-05-30"
date_list = get_date_range(begin_date, end_date, days=2)
print(date_list)
