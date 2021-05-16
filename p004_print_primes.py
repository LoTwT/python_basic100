# 判断一个数是否为素数
def is_prime(number):
    if number in (1, 2):
        return True
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


# 打印区间内所有素数
def print_primes(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(f"{number} is a prime")


print_primes(11, 25)
