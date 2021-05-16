# 计算阶乘
def calc_factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

print(f"3 的阶乘 = {calc_factorial(3)}")
print(f"6 的阶乘 = {calc_factorial(6)}")
print(f"100 的阶乘 = {calc_factorial(100)}")