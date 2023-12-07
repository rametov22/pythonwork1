# 1
# num_ = int(input('целое число: '))
#
# if num_ > 0:
#     num_ += 1
#     print(num_)
# else:
#     print(num_)

# 2
# num_ = int(input('целое число: '))
# if num_ > 0:
#     num_ += 1
#     print(num_)
# else:
#     num_ -= 2
#     print(num_)

# 3
# num_ = int(input('целое число: '))
# if num_ > 0:
#     num_ += 1
#     print(num_)
# elif num_ < 0:
#     num_ -= 2
#     print(num_)
# else:
#     num_ += 10
#     print(num_)

# 4
# a = int(input('число: '))
# b = int(input('число: '))
# c = int(input('число: '))
# if a and b and c > 0:
#     print('3')
# elif a and b > 0 and c < 0 or a and c > 0 and b < 0 or b and c > 0 and a < 0:
#     print('2')
# elif a > 0 and b and c < 0 or b > 0 and a and c < 0 or c > 0 and b and a < 0:
#     print('1')
# else:
#     print('0')

# 5
# a = int(input('число: '))
# b = int(input('число: '))
# c = int(input('число: '))
# if a and b and c > 0:
#     print('musbat 3, manfiy 0')
# elif a and b > 0 and c < 0 or a and c > 0 and b < 0 or b and c > 0 and a < 0:
#     print('musbat 2, manfiy 1')
# elif a > 0 and b and c < 0 or b > 0 and a and c < 0 or c > 0 and b and a < 0:
#     print('musbat 1, manfiy 2')
# else:
#     print('musbat 0, manfiy 3')

# 6
# a = int(input('число: '))
# b = int(input('число: '))
# c = int(input('число: '))
# if a > b and c:
#     print(f'kottasi {a}')
# elif b > a and c:
#     print(f'kottasi {b}')
# elif c > a and b:
#     print(f'kottasi {c}')
# else:
#     print(None)

# 7
# a = int(input('son: '))
# b = int(input('son2: '))
# if a > b:
#     print(b)
# else:
#     print(a)

# 8
# a = int(input('son: '))
# b = int(input('son2: '))
# if a > b:
#     print(a, b)
# else:
#     print(b, a)

# 9
# A = int(input('sonA: '))
# B = int(input('sonB: '))
# if A > B:
#     A, B = B, A
#     print(A, B)
# else:
#     print(A, B)

# 10
# A = int(input('sonA: '))
# B = int(input('sonB: '))
# if A == B:
#     print(A, B)
# elif A != B:
#     A += B
#     print(A)

# 11
# A = int(input('sonA: '))
# B = int(input('sonB: '))
# if A > B:
#     print(A)
# elif B > A:
#     A = B
#     print(A)
# else:
#     print('0')

# 12
# a = int(input('son'))
# b = int(input('son'))
# c = int(input('son'))
# if a < b and c:
#     print(a)
# elif b < a and c:
#     print(b)
# elif c < a and b:
#     print(c)
# else:
#     print(None)

# 13
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
# if a > b and a < c or a < b and a > c:
#     print(a)
# elif b > a and b < c or b < a and b > c:
#     print(b)
# elif c > a and c < b or c < a and c > b:
#     print(c)
# else:
#     print(None)

# 14
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
# if a < b and c and b < c:
#     print(a, b, c)
# elif b < a and c and a < c:
#     print(b, a, c)
# elif c < a and b and a < b:
#     print(c, a, b)
# elif a < b and c and c < b:
#     print(a, c, b)
# elif b < a and c and c < a:
#     print(b, c, a)
# elif c < a and b and b < a:
#     print(c, b, a)

# 15
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
# if a + b > a + c and a + b > b + c:
#     print(a + b)
# elif a + c > a + b and a + c > b + c:
#     print(a + c)
# elif b + c > a + b and b + c > a + c:
#     print(b + c)
# else:
#     print(None)

# 16
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
#
# if a < b < c:
#     a *= 2
#     b *= 2
#     c *= 2
#     print(a, b, c)
# else:
#     a = -a
#     b = -b
#     c = -c
#     print(a, b, c)
#

# 17
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
#
# if a < b < c or a > b > c:
#     a *= 2
#     b *= 2
#     c *= 2
#     print(a, b, c)
# else:
#     a = -a
#     b = -b
#     c = -c
#     print(a, b, c)

# 18
# a = int(input('son1: '))
# b = int(input('son2: '))
# c = int(input('son3: '))
# if a == b:
#     result = c
#     position = 'c'
# elif a == c:
#     result = b
#     position = 'b'
# else:
#     result = a
#     position = 'a'
# print(f'qolgan son {result} tartib raqami {position}')

# 19
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
# d = int(input("Введите число d: "))
#
# if a == b == c:
#     result = d
#     position = "d"
# elif a == b == d:
#     result = c
#     position = "c"
# elif a == c == d:
#     result = b
#     position = "b"
# else:
#     result = a
#     position = "a"
#
# print(f"qolgan son {result} tartib raqami {position}.")

# 20
# import math
# ax, ay = map(float, input("Введите координаты точки A (через пробел): ").split())
# bx, by = map(float, input("Введите координаты точки B (через пробел): ").split())
# cx, cy = map(float, input("Введите координаты точки C (через пробел): ").split())
#
# distance_AB = math.sqrt((bx - ax)**2 + (by - ay)**2)
# distance_AC = math.sqrt((cx - ax)**2 + (cy - ay)**2)
#
# if distance_AB < distance_AC:
#     closest_point = "B"
#     closest_distance = distance_AB
# else:
#     closest_point = "C"
#     closest_distance = distance_AC
#
# print(f"Точка {closest_point} ближайшая к точке A, расстояние между ними: {closest_distance}")

# 21
# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))
#
# # Проверяем положение точки
# if x == 0 and y == 0:
#     print(0)
# elif x == 0:
#     print(2)
# elif y == 0:
#     print(1)
# else:
#     print(3)

# 22
# x = float(input("Введите координату x: "))
# y = float(input("Введите координату y: "))
#
# if x > 0 and y > 0:
#     print("Точка находится в первой координатной четверти.")
# elif x < 0 and y > 0:
#     print("Точка находится во второй координатной четверти.")
# elif x < 0 and y < 0:
#     print("Точка находится в третьей координатной четверти.")
# elif x > 0 and y < 0:
#     print("Точка находится в четвёртой координатной четверти.")
# else:
#     print("Точка не находится в координатных четвертях.")

# 23
# x1, y1 = map(float, input("Введите координаты первого конца (x1 y1): ").split())
# x2, y2 = map(float, input("Введите координаты второго конца (x2 y2): ").split())
# x3, y3 = map(float, input("Введите координаты третьего конца (x3 y3): ").split())
#
# x4 = x2 + (x2 - x1)
# y4 = y1 + (y2 - y1)
#
# print(f"Координаты четвертого конца: ({x4}, {y4})")

# 24
# import math
#
# def f(x):
#     if x > 0:
#         return 2 * math.sin(x)
#     else:
#         return x - 6
#
#
# x_value = float(input("Введите значение x: "))
# result = f(x_value)
# print(f"f({x_value}) = {result}")

# 25
# def f(x):
#     if x < -2 or x > 2:
#         return x * 2
#     else:
#         return -3 * x
#
#
# x_value = float(input("Введите значение x: "))
# result = f(x_value)
# print(f"f({x_value}) = {result}")

# 26
# def f(x):
#     if x <= 0:
#         return -x
#     elif 0 < x < 2:
#         return x ** 2
#     elif x >= 2:
#         return 4
#     else:
#         return x
#
#
# x_value = float(input("Введите значение x: "))
# result = f(x_value)
# print(f"f({x_value}) = {result}")

# 27
# def f(x):
#     if x < 0:
#         return 0
#     elif x % 2 == 0:
#         return 1
#     else:
#         return -1
#
#
# x_value = float(input("Введите значение x: "))
# result = f(x_value)
# print(f"f({x_value}) = {result}")

# 28
# year = int(input("Введите год: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} год - високосный. Всего 366 дней.")
# else:
#     print(f"{year} год - невисокосный. Всего 365 дней.")

# 29
# number = int(input("Введите целое число: "))
#
# if number > 0 and number % 2 != 0:
#     print(f"{number} - musbat toq son.")
# elif number > 0 and number % 2 == 0:
#     print(f'{number} - musbat juft son')
# elif number < 0 and number % 2 != 0:
#     print(f'{number} - manfiy toq son')
# elif number < 0 and number % 2 == 0:
#     print(f"{number} - manfiy juft son.")
# elif number == 0:
#     print(f"{number} - son nolga teng.")
# else:
#     print(f"{number} - osmondan olingan son.")

# 30
# number = int(input("Введите число от 1 до 999: "))
#
# # Проверка и вывод результата
# if 1 <= number <= 9:
#     print(f"{number} - однозначное число.")
# elif 10 <= number <= 99:
#     if number % 2 == 0:
#         print(f"{number} - четное двузначное число.")
#     else:
#         print(f"{number} - нечетное двузначное число.")
# elif 100 <= number <= 999:
#     if number % 2 == 0:
#         print(f"{number} - четное трехзначное число.")
#     else:
#         print(f"{number} - нечетное трехзначное число.")
# else:
#     print("Число не находится в заданном диапазоне.")
