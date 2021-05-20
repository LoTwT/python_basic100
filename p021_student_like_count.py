# 统计每个兴趣的学生人数

like_count = {}

with open("./p021/p021_student_like.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        name, like = line.split(" ")
        like_list = like.split(",")
        for like in like_list:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1

print(like_count)
