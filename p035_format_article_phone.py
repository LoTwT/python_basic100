# 将多种日期格式标准化
import re
content = """
    白日依2021/5/29山尽, 黄河入2021.5.29海流。
    欲穷千05-29-2021里目, 更上一5/29/2021层楼。
"""

content = re.sub(r"(\d{4})/(\d{1})/(\d{2})", r"\1-0\2-\3", content)
content = re.sub(r"(\d{4}).(\d{1}).(\d{2})", r"\1-0\2-\3", content)
content = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", content)
content = re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"\3-0\1-\2", content)
print(content)
