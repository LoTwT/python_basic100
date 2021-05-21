# 用正则表达式判断字符串是否是日期
import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None


date1 = "2021-05-21"
date2 = "2021/05/21"
date3 = "20210521"
date4 = "2021a05b21"

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
