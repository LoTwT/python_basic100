# 递归搜索目录找出最大的文件
import os

search_dir = "."
result_files = []


for root, dirs, files in os.walk(search_dir):
    for file in files:
        file_path = f"{root}/{file}"
        result_files.append((file_path, os.path.getsize(file_path)))

print(sorted(result_files, key=lambda x: x[1], reverse=True)[:5])
