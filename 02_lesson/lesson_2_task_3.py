import math

def square(side):
    return math.ceil(side *2)

side = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")