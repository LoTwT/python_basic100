# 按文件后缀名整理文件夹
import os
import shutil

dir_path = "./arrange_dir"

for file in os.listdir(dir_path):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir_path}/{ext}"):
        os.mkdir(f"{dir_path}/{ext}")

    source_path = f"{dir_path}/{file}"
    target_path = f"{dir_path}/{ext}/{file}"
    shutil.move(source_path, target_path)
