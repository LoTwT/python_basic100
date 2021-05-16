# 计算前 n 个数的平方和
def sum_of_square(number):
    result = 0
    for num in range(1, number + 1):
        result += num * num
    return result


print(f"sum of square 3: {sum_of_square(3)}")
print(f"sum of square 3: {sum_of_square(5)}")
print(f"sum of square 3: {sum_of_square(10)}")
