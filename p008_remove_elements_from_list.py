# 从列表中移除多个元素
def remove_elements_from_list(origin_list, delete_list):
    for item in delete_list:
        origin_list.remove(item)
    return origin_list


origin_list = [3, 5, 7, 9, 11, 13]
delete_list = [7, 11]
print(f"origin_list: {origin_list}, delete_list: {delete_list}, result: {remove_elements_from_list(origin_list, delete_list)}")

origin_list = [3, 5, 7, 9, 11, 13]
delete_list = [7, 11]
# 列表推导式
data = [item for item in origin_list if item not in delete_list]
print(
    f"origin_list: {origin_list}, delete_list: {delete_list}, result: {data}")
