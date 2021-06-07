# 统计中文文章中的人名
import jieba.posseg as posseg

content = "张三喜欢王五"

for word, flag in posseg.cut(content):
    if flag == "nr":
        print(word, flag)
