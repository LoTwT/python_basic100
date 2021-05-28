# 提取文本内商品价格
import re
content = """
小明上街买菜
买了1斤黄瓜花了8元
买了2斤葡萄花了13.5元
买了3斤白菜花了5.4元
"""
# 要求提取 (1、黄瓜、8) (2、葡萄、13.5) (3、白菜、5.4)


for line in content.split("\n"):
    # 正则中使用 () 进行分组
    pattern = r"(\d)斤(.*)花了(\d+(\.\d+)?)元"
    result = re.search(pattern, line)
    if result:
        # print(result.groups())
        print(f"{result.group(1)}\t{result.group(2)}\t{result.group(3)}")
