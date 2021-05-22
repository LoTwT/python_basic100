# 批量提取文本手机号
import re


pattern = r"1[3-9]\d{9}"

with open("./p030/p030_webpage_phone_number.txt", "r", encoding="utf-8") as fin:
    file_content = fin.read()

results = re.findall(pattern, file_content)

print(len(results))
for result in results:
    print(result)
