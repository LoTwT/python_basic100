# 计算列表数字的和
def sum_of_list(list_instance):
    result = 0
    for param in list_instance:
        result += param
    return result


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(f"sum of {list1}: {sum_of_list(list1)}")
print(f"sum of {list2}: {sum_of_list(list2)}")

# 使用内置的 sum() 函数
print(f"sum of {list1}: {sum(list1)}")
print(f"sum of {list2}: {sum(list2)}")
