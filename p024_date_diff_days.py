# 计算两个日期相隔的天数
import datetime


def get_diff_days(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime("%Y-%m-%d")


print(get_diff_days("2021-5-20", 1))
print(get_diff_days("2021-5-20", 3))
print(get_diff_days("2021-5-20", 7))
print(get_diff_days("2021-5-1", 3))
