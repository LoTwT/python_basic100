# 校验密码是否规范
"""
写一个函数, 验证密码是否满足条件
1. 长度在 [6, 20] 之间
2. 必须包含至少 1 个小写字母
3. 必须包含至少 1 个大写字母
4. 必须包含至少 1 个数字
5. 必须包含至少 1 个特殊字符

返回 True, 通过校验,
     或者 False, 原因
"""

import re


def check_password(password):
    if not 6 <= len(password) <= 20:
        return False, "密码长度必须在 6 ~ 20 之间"
    if not re.findall(r"[a-z]", password):
        return False, "必须包含至少 1 个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "必须包含至少 1 个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "必须包含至少 1 个数字"
    if not re.findall(r"[^a-zA-Z0-9]", password):
        return False, "必须包含至少 1 个特殊字符"
    return True, "通过校验"


print("HelloWord_123", check_password("HelloWord_123"))
print("hi_12", check_password("hi_12"))
print("hellooooooooooooooooo", check_password("hellooooooooooooooooo"))
print("HELLOWORD_123", check_password("HELLOWORD_123"))
print("helloword_123", check_password("helloword_123"))
print("HelloWord123", check_password("HelloWord123"))
print("HelloWord___", check_password("HelloWord___"))
