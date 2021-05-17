# 读取 txt 成绩文件实现排序

def read_file():
    result = []
    with open("./p012_student_grade_input.txt", "r", encoding="utf-8") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))  # 注意换行符
    return result


def sort_grades(datas):
    return sorted(datas, key=lambda x: int(x[2]), reverse=True)


def save_datas(datas):
    with open("./p012_student_grade_file_output.txt", "w", encoding="utf-8") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


# 读取文件
datas = read_file()
# 排序数据
datas = sort_grades(datas)
print(datas)
# 写出文件
save_datas(datas)
