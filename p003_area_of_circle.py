# 计算圆的面积
import math


def compute_area_of_circle(r):
    return round(math.pi * r * r, 2)


print(f"area is 2: {compute_area_of_circle(2)}")
print(f"area is 3.14: {compute_area_of_circle(3.14)}")
print(f"area is 6.78: {compute_area_of_circle(6.78)}")
