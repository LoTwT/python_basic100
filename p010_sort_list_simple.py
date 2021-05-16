# 简单列表排序

# 升序 改变原列表
origin_list = [20, 40, 30, 50, 10]
origin_list.sort()
print(f"升序 改变原列表: {origin_list}")
# 降序 改变原列表
origin_list = [20, 40, 30, 50, 10]
origin_list.sort(reverse=True)
print(f"降序 改变原列表: {origin_list}")
# 升序 不改变原列表
origin_list = [20, 40, 30, 50, 10]
result_list = sorted(origin_list)
print(f"升序 不改变原列表, origin_list: {origin_list}, result_list: {result_list}")
# 降序 不改变原列表
origin_list = [20, 40, 30, 50, 10]
result_list = sorted(origin_list, reverse=True)
print(f"降序 不改变原列表, origin_list: {origin_list}, result_list: {result_list}")
