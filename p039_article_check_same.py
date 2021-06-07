# 模拟论文查重
import jieba.analyse

filepath_1 = ""
filepath_2 = ""


def get_keyword_from_article(filepath):
    with open(filepath, "r", encoding="utf-8") as fin:
        content = fin.read()
    return jieba.analyse.extract_tags(content, 50)


def compute_same(words_list_1, words_list_2):
    jiaoji = set(words_list_1).intersection(set(words_list_2))
    bingji = set(words_list_1).union(set(words_list_2))
    return round(len(jiaoji) * 100 / len(bingji), 2)


words_list_1 = get_keyword_from_article(filepath_1)
words_list_2 = get_keyword_from_article(filepath_2)

print("words_list_1 vs words_list_2", compute_same(words_list_1, words_list_2))
