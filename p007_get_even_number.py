# 返回范围内所有偶数
def get_even_number(start, end):
    result = []
    for number in range(start, end+1):
        if number % 2 == 0:
            result.append(number)
    return result


start = 4
end = 15
print(f"start={start}, end={end}, even number: {get_even_number(start, end)}")

# 列表推导式
data = [num for num in range(start, end) if num % 2 == 0]
print(f"start={start}, end={end}, even number: {data}")
