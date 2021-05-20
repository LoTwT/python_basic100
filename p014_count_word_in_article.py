# 统计文章出现的英文单词数目

def count_word_in_article():
    word_count = {}
    with open("./p014/p014.txt", "r", encoding="utf-8") as fin:
        for line in fin:
            line = line[:-1]
            words = line.split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
    return word_count


word_count = count_word_in_article()
word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(word_count)
