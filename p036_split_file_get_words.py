# 英文分词计算词频
import re
import pandas as pd

with open("./p036/p036.txt", "r", encoding="utf-8") as fin:
    content = fin.read()

words = re.split(r"[\s.()-?]+", content)

print(pd.Series(words).value_counts()[:20])
