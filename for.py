# 1
# k = int(input('число: '))
# n = int(input('сколько раз: '))
# if n > 0:
#     for i in range(n):
#         print(k)
# else:
#     print('n больще 0')

# 2
# a = int(input('число а: '))
# b = int(input('число b: '))
#
# for i in range(a, b + 1):
#     print(i)
#
# print(f'a = {a}, b = {b}')
# print(f'chiqarilgan sonlar soni {b - a + 1}')

# 3
# a = int(input('число a: '))
# b = int(input('число b: '))
#
# for i in range(b, a, - 1):
#     print(i, end=" ")
#
# print(f'chiqarilgan sonlar soni {b - a + 1}')

# 4
# sum_ = int(input('цена кг конфет: '))
# for i in range(1, 11):
#     print(f'{i}kg стоит сум {i * sum_}')

# 5
# sum_ = int(input('цена кг конфет: '))
# price = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# for i in price:
#     new_price = sum_ * i
#     print(f"{i} kg konfet narxi: ${new_price:.2f}")

# 6
# sum_ = int(input('цена кг конфет: '))
# price = [1.2, 1.4, 1.6, 1.8, 2]
# for i in price:
#     new_price = sum_ * i
#     print(f'{i} kg konfet narxi: {new_price}')

# 7
# a = int(input('число: '))
# b = int(input('число: '))
# if a < b:
#     total = 0
#     for i in range(a, b + 1):
#         total += i
#         print(total)

# 8
# a = int(input('число: '))
# b = int(input('число: '))
# if a < b:
#     total = 1
#     for i in range(a, b + 1):
#         total *= i
#         print(total)

# 9
# a = int(input('число: '))
# b = int(input('число: '))
# if a < b:
#     total = 0
#     for i in range(a, b + 1):
#         i **= 2
#         total += i
#         print(total)

# 10
# n = int(input('число: '))
#
# if n <= 0:
#     print("n должен быть больше 0")
# else:
#     S = 0
#     for i in range(1, n + 1):
#         S += 1 / i
#
#     print(f"S = {S}")

# 11
# n = int(input("число: "))
#
# if n <= 0:
#     print("n должен быть больше 0.")
# else:
#     S = 0
#     for i in range(n, 2 * n + 1):
#         S += i ** 2
#
#     print(f"S = {S}")

# 12
# n = int(input("число: "))
#
# if n <= 0:
#     print("n должен быть больше 0")
# else:
#     S = 1.0
#     for i in range(1, n + 1):
#         S *= 1.0 + i / 10.0
#
#     print(f"S = {S}")

# 13
# n = int(input("n butun sonini kiriting: "))
#
# if n <= 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     S = 0
#     sign = 1
#     for i in range(1, n + 1):
#         S += sign * i / 10.0
#         sign *= -1
#
#     print(f"S = {S}")

# 14
# n = int(input("n butun sonini kiriting: "))
#
# if n <= 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     result = 0
#     for i in range(1, n + 1):
#         result += (2 * i - 1)
#
#     print(f"{n} gacha bo'lgan sonlar kvadratlari yig'indisi: {result}")

# 15
# a = float(input("a haqiqiy sonini kiriting: "))
# n = int(input("n butun sonini kiriting: "))
#
# result = 1.0
#
# for _ in range(n):
#     result *= a
#
# print(f"{a} ning {n}-darajasi: {result}")

# 16
# a = float(input("a haqiqiy sonini kiriting: "))
# n = int(input("n butun sonini kiriting: "))
#
# for i in range(n + 1):
#     result = a ** i
#     print(f"{a} ning {i}-darajasi: {result}")

# 17
# a = int(input("a haqiqiy sonini kiriting: "))
# n = int(input("n butun sonini kiriting: "))
#
# result = 0
#
# for i in range(n + 1):
#     result += a ** i
#     print(f"{a} ning {i}-darajasi: {a ** i}")
#
# print(f"Yig'indi: {result}")

# 18
# a = float(input("a haqiqiy sonini kiriting: "))
# n = int(input("n butun sonini kiriting: "))
#
# result = 0
#
# for i in range(n + 1):
#     result += ((-1) ** i) * (a ** i)
#     print(f"{a} ning {i}-darajasi: {((-1) ** i) * (a ** i)}")
#
# print(f"Yig'indi: {result}")

# 19
# n = int(input("n butun sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     factorial_result = 1
#
#     for i in range(1, n + 1):
#         factorial_result *= i
#
#     print(f"{n}! = {factorial_result}")

# 20
# n = int(input("n butun sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     total = 0
#     factorial = 1
#
#     for i in range(1, n + 1):
#         factorial *= i
#         total += factorial
#
#     print(f"Yig'indi: {total}")

# 21
# import math
#
# n = int(input("n butun sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     total = 0
#     factorial = 1
#
#     for i in range(n + 1):
#         if i != 0:
#             factorial *= i
#             total += 1 / factorial
#
#     total += 1
#
#     print(f"Yig'indi: {total}")
#     print(f"Natijaning yaqinlashgan qiymati: {math.exp(1)}")

# 22
# import math
#
# n = int(input("n butun sonini kiriting: "))
# x = float(input("x haqiqiy sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     total = 0
#     term = 1
#
#     for i in range(1, n + 1):
#         term *= x / i
#         total += term
#
#     total += 1
#
#     print(f"Yig'indi: {total}")
#     print(f"Natijaning yaqinlashgan qiymati: {math.exp(x)}")

# 23
# import math
#
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
# def compute_term(x, n):
#     return ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
#
# n = int(input("n butun sonini kiriting: "))
# x = float(input("x haqiqiy sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     total = 0
#
#     for i in range(n + 1):
#         total += compute_term(x, i)
#
#     print(f"Yig'indi: {total}")
#     print(f"Natijaning yaqinlashgan qiymati: {math.sin(x)}")

# 24
# import math
#
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
# def compute_term(x, n):
#     return ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
#
# n = int(input("n butun sonini kiriting: "))
# x = float(input("x haqiqiy sonini kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat butun soni bo'lishi kerak.")
# else:
#     total = 0
#
#     for i in range(n + 1):
#         total += compute_term(x, i)
#
#     print(f"Yig'indi: {total}")
#     print(f"Natijaning yaqinlashgan qiymati: {math.cos(x)}")

# 25
# n = int(input("n butun sonini kiriting (n > 0): "))
# x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))
#
# if n <= 0 or abs(x) >= 1:
#     print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
# else:
#     total = 0
#
#     for i in range(1, n + 1):
#         total += ((-1) ** (i - 1)) * (x ** i) / i
#
#     print(f"Yig'indi: {total}")

# 26
# n = int(input("n butun sonini kiriting (n > 0): "))
# x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))
#
# if n <= 0 or abs(x) >= 1:
#     print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
# else:
#     total = 0
#
#     for i in range(n + 1):
#         total += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
#
#     print(f"Yig'indi: {total}")

# 27
# import math
#
# n = int(input("n butun sonini kiriting (n > 0): "))
# x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))
#
# if n <= 0 or abs(x) >= 1:
#     print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
# else:
#     total = x
#     term = 1
#
#     for i in range(1, n + 1):
#         term *= (2 * i - 1) * x / ((2 * i) * (2 * i + 1))
#         total += term
#
#     print(f"Yig'indi: {total}")

# 28
# import math
#
# n = int(input("n butun sonini kiriting (n > 0): "))
# x = float(input("|x| < 1 bo'lishi kerak, x ni kiriting: "))
#
# if n <= 0 or abs(x) >= 1:
#     print("Noto'g'ri kiritish. n > 0 va |x| < 1 bo'lishi kerak.")
# else:
#     total = 1
#     term = 1
#
#     for i in range(1, n + 1):
#         term *= ((-1) ** (i - 1)) * (2 * i - 1) * x / math.prod(range(2, 2 * i + 1, 2))
#         total += term
#
#     print(f"Yig'indi: {total}")

# 29
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# n = int(input("n ni kiriting: "))
#
# if n < 0:
#     print("Noto'g'ri kiritish. n musbat bo'lishi kerak.")
# else:
#     interval = B - A
#     step = interval / n
#
#     print(f'["[{A}, {B}|"] kesmada {n} ta kesma bor:')
#     for i in range(n):
#         start_point = A + i * step
#         end_point = A + (i + 1) * step
#         print(f'[{start_point}, {end_point}]')

# 30
# import math
#
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# n = int(input("n ni kiriting: "))
#
# if n < 1:
#     print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
# else:
#     interval = B - A
#     step = interval / n
#
#     print(f'["[{A}, {B}]"] kesmada {n} ta kesma bor:')
#     for i in range(n + 1):
#         x = A + i * step
#         f_x = 1 - math.sin(x)
#         print(f'F({x}) = {f_x}')

# 31
# n = int(input("n butun sonini kiriting: "))
#
# A = 2  # dastlabki qiymat
# for k in range(1, n + 1):
#     print(f"A{k} = {A}")
#     A = 2 + 1 / A

# 32
# n = int(input("n butun sonini kiriting: "))
#
# A = 1  # dastlabki qiymat
# for k in range(1, n + 1):
#     print(f"A{k} = {A}")
#     A = (A + 1) / k

# 33
# n = int(input("n butun sonini kiriting (n > 1): "))
#
# if n <= 1:
#     print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
# else:
#     fib_sequence = [1, 1]
#
#     for k in range(3, n + 1):
#         fk = fib_sequence[-2] + fib_sequence[-1]
#         fib_sequence.append(fk)
#
#     print(f"Fibonacci ketma-ketlikning dastlabki {n} ta hadlari:")
#     for i, fk in enumerate(fib_sequence, start=1):
#         print(f"F{i} = {fk}")

# 34
# n = int(input("n butun sonini kiriting (n > 1): "))
#
# if n <= 1:
#     print("Noto'g'ri kiritish. n 1 dan katta bo'lishi kerak.")
# else:
#     A_sequence = [1, 2]
#
#     for k in range(3, n + 1):
#         Ak = (A_sequence[-2] + 2 * A_sequence[-1]) / 3
#         A_sequence.append(Ak)
#
#     print(f"Ketma-ketlikning dastlabki {n} ta hadlari:")
#     for i, Ak in enumerate(A_sequence, start=1):
#         print(f"A{i} = {Ak}")

# 35
# n = int(input("n butun sonini kiriting (n > 2): "))
#
# if n <= 2:
#     print("Noto'g'ri kiritish. n 2 dan katta bo'lishi kerak.")
# else:
#     A_sequence = [1, 2, 3]
#
#     for k in range(4, n + 1):
#         Ak = A_sequence[-1] + A_sequence[-2] - 2 * A_sequence[-3]
#         A_sequence.append(Ak)
#
#     print(f"Ketma-ketlikning dastlabki {n} ta hadlari:")
#     for i, Ak in enumerate(A_sequence, start=1):
#         print(f"A{i} = {Ak}")

# 36
# N = int(input("N butun sonini kiriting: "))
# K = int(input("K butun sonini kiriting: "))
#
# if N < 1 or K < 1:
#     print("Noto'g'ri kiritish. N va K 1 dan katta bo'lishi kerak.")
# else:
#     total = sum(i ** K for i in range(1, N + 1))
#     print(f"Yig'indi: {total}")

# 37
# N = int(input("N butun sonini kiriting: "))
#
# if N < 1:
#     print("Noto'g'ri kiritish. N 1 dan katta bo'lishi kerak.")
# else:
#     total = sum(i ** i for i in range(1, N + 1))
#     print(f"Yig'indi: {total}")

# 38
# N = int(input("N butun sonini kiriting: "))
#
# if N < 1:
#     print("Noto'g'ri kiritish. N 1 dan katta bo'lishi kerak.")
# else:
#     total = sum(i ** (N - i + 1) for i in range(1, N + 1))
#     print(f"Yig'indi: {total}")

# 39
# A = int(input("A butun sonini kiriting: "))
# B = int(input("B butun sonini kiriting (A dan katta bo'lishi kerak): "))
#
# if A >= B:
#     print("Noto'g'ri kiritish. B A dan katta bo'lishi kerak.")
# else:
#     for i in range(A, B + 1):
#         for _ in range(i):
#             print(i)

# 40
# A = int(input("A butun sonini kiriting: "))
# B = int(input("B butun sonini kiriting (A dan katta bo'lishi kerak): "))
#
# if A >= B:
#     print("Noto'g'ri kiritish. B A dan katta bo'lishi kerak.")
# else:
#     for i in range(A, B + 1):
#         for _ in range(i):
#             print(i)
