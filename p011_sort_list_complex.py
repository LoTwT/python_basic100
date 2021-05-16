# 复杂列表排序
students = [
    {"sno": 101, "sname": "小赵", "sgrade": 88},
    {"sno": 104, "sname": "小钱", "sgrade": 77},
    {"sno": 102, "sname": "小孙", "sgrade": 99},
    {"sno": 103, "sname": "小李", "sgrade": 66},
]

result = sorted(students, key=lambda x: x["sgrade"], reverse=False)

print(f"students: {students}")
print(f"students: {result}")
