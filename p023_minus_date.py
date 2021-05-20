# 计算两个日期相隔的天数
import datetime

birthday = "1997-3-19"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

cur_datetime = datetime.datetime.now()
print(cur_datetime, type(cur_datetime))

minus_datetime = cur_datetime - birthday_date
print(minus_datetime, type(minus_datetime))

print(minus_datetime.days)
