# 获取当前的日期和时间
import datetime

cur_datetime = datetime.datetime.now()
print(cur_datetime, type(cur_datetime))

# date time to string
str_time = cur_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("str_time", str_time)

print("year", cur_datetime.year)
print("month", cur_datetime.month)
print("day", cur_datetime.day)
print("hour", cur_datetime.hour)
print("minute", cur_datetime.minute)
print("second", cur_datetime.second)
print("date", cur_datetime.date())
