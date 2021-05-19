# 统计目录下的文件大小

import os


def size_of_dir(dirPath):
    sum_size = 0
    for file in os.listdir(dirPath):
        if os.path.isfile(file):
            sum_size += os.path.getsize(file)

    return sum_size


print(f"size_of_dir: {size_of_dir('.')} bytes")
