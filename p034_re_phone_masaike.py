# 文本内手机号打马赛克
import re
content = """
手机号:13123456789, 不是手机号456789123456789, 又是手机号: 13198765432
"""

pattern = r"(1[3-9])\d{9}"
print(re.sub(pattern, r"\1*********", content))
pattern1 = r"(1\d{2})\d{4}(\d{4})"
print(re.sub(pattern1, r"\1****\2", content))
