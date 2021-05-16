# 列表去重
def get_unique_list(origin_list):
    result = []
    for item in origin_list:
        if item not in result:
            result.append(item)
    return result


origin_list = [10, 20, 30, 10, 20]
print(
    f"origin_list: {origin_list}, unique_list: {get_unique_list(origin_list)}")

# 利用 set
print(
    f"origin_list: {origin_list}, unique_list: {list(set(origin_list))}")
