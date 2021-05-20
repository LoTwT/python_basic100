# 批量 txt 文件合并
import os

data_dir = "./p020"

contents = []

for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as fin:
            contents.append(fin.read())

merge_contents = "\n".join(contents)

with open(f"./{data_dir}/merged_file.txt", "w", encoding="utf-8") as fout:
    fout.write(merge_contents)
