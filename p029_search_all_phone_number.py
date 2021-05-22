# 从文本中提取手机号
import re

content = """
    lfaskjdfl98765432100dfhajdhf,asjfij13123456789,lskdjfiasjf14987654321,sajdhf123123,4343423
"""

# 手机号的模式: 1 开头、第二位任意取 3~9 中一个, 总共 11 位

pattern = r"1[3-9]\d{9}"
result = re.findall(pattern, content)
print(result)
