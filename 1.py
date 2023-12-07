# 1
# A = int(input('цисло: '))
# if A > 0:
#     print(True)
# else:
#     print(False)
#
# 2
# A = int(input('цисло: '))
# if A % 2 == 1:
#     print(True)
# else:
#     print(False)

# 3
# A = int(input('цисло: '))
# if A % 2 == 0:
#     print(True)
# else:
#     print(False)

# 4
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A > 2 and B <= 3:
#     print(True)
# else:
#     print(False)

# 5
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A >= 0 or B < 2:
#     print(True)
# else:
#     print(False)

# 6
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A <= B and B <= C:
#     print(True)
# else:
#     print(False)

# 7
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
#
# if B < A and B > C or B > A and B < C:
#     print(True)
# else:
#     print(False)

# 8
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A % 2 == 1 and B % 2 == 1:
#     print(True)
# else:
#     print(False)

# 9
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A % 2 == 1 and B % 2 == 1 or A % 2 == 1 or B % 2 == 1:
#     print(True)
# else:
#     print(False)

# 10
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A % 2 == 1 and B % 2 == 0 or B % 2 == 1 and A % 2 == 0:
#     print(True)
# else:
#     print(False)

# 11
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# if A % 2 == 1 and B % 2 == 1 or A % 2 == 0 and B % 2 == 0:
#     print(True)
# else:
#     print(False)

# 12
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A > 0 and B > 0 and C > 0:
#     print(True)
# else:
#     print(False)

# 13
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A > 0 or B > 0 or C > 0:
#     print(True)
# else:
#     print(False)

# 14
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A > 0 and B < 0 and C < 0 or A < 0 and B > 0 and C < 0 or A < 0 and B < 0 and C > 0:
#     print(True)
# else:
#     print(False)

# 15
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A > 0 and B > 0 and C < 0 or A > 0 and B < 0 and C > 0 or A < 0 and B > 0 and C > 0:
#     print(True)
# else:
#     print(False)

# 16
# A = int(input('число: '))
# if A > 9 and A < 100 and A % 2 == 0:
#     print(True)
# else:
#     print(False)

# 17
# A = int(input('число: '))
# if A > 99 and A < 1000 and A % 2 == 1:
#     print(True)
# else:
#     print(False)

# 18
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
# if A == B or A == C or B == C:
#     print(True)
# else:
#     print(False)

# 19
# A = int(input('число 1: '))
# B = int(input('число 2: '))
# C = int(input('число 3: '))
#
# if A == -B or A == -C or B == -C:
#     print(True)
# else:
#     print(False)

# 20
# A = int(input('трехзначное число: '))
# ones = A % 10
# teens = A // 10 % 10
# huns = A // 100
# if ones != teens and ones != huns and teens != huns:
#     print(True)
# else:
#     print(False)

# 21
# A = int(input('трехзначное число: '))
# ones = A % 10
# teens = A // 10 % 10
# huns = A // 100
# if huns < teens and huns < ones and teens < ones:
#     print(True)
# else:
#     print(False)

# 22
# A = int(input('трехзначное число: '))
# ones = A % 10
# teens = A // 10 % 10
# huns = A // 100
# if huns < teens and huns < ones and teens < ones or huns > teens and huns > ones and teens > ones:
#     print(True)
# else:
#     print(False)

# 23
# A = int(input('трехзначное число: '))
# ones = A % 10
# teens = A // 10 % 10
# huns = A // 100
# if huns == ones:
#     print(True)
# else:
#     print(False)

# 24
# A = float(input("Введите коэффициент A (A должно быть отлично от нуля): "))
# B = float(input("Введите коэффициент B: "))
# C = float(input("Введите коэффициент C: "))
#
# D = B**2 - 4*A*C
#
# if D > 0:
#     print("Квадратное уравнение имеет два действительных корня.")
# elif D == 0:
#     print("Квадратное уравнение имеет один действительный корень.")
# else:
#     print("Квадратное уравнение не имеет действительных корней.")

# 25
# x = int(input('x число: '))
# y = int(input('y число: '))
# if x < 0 and y > 0:
#     print(True)
# else:
#     print(False)

# 26
# x = int(input('x число: '))
# y = int(input('y число: '))
# if x > 0 and y < 0:
#     print(True)
# else:
#     print(False)

# 27
# x = int(input('x число: '))
# y = int(input('y число: '))
# if x < 0 and (y > 0 or y < 0):
#     print(True)
# else:
#     print(False)

# 28
# x = int(input('x число: '))
# y = int(input('y число: '))
# if x > 0 and y > 0 or x < 0 and y < 0:
#     print(True)
# else:
#     print(False)

# 29
# x = float(input("Введите координату x точки: "))
# y = float(input("Введите координату y точки: "))
# x1 = float(input("Введите координату x1 верхней левой вершины: "))
# y1 = float(input("Введите координату y1 верхней левой вершины: "))
# x2 = float(input("Введите координату x2 правой нижней вершины: "))
# y2 = float(input("Введите координату y2 правой нижней вершины: "))
#
# if (x1 <= x <= x2) and (y1 >= y >= y2):
#     print(True)
# else:
#     print(False)

# 30
# a = int(input("Введите длину стороны a: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
#
# if a == b == c:
#     print(True)
# else:
#     print(False)

# 31
# a = int(input("Введите длину стороны a: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
#
# if a == b:
#     print(True)
# else:
#     print(False)

# 32
# a = int(input("Введите длину стороны a: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
#
# if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#     print(True)
# else:
#     print(False)

# 33
# a = int(input("Введите длину стороны a: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
#
# if a + b > c and b + c > a and a + c > b:
#     print(True)
# else:
#     print(False)

# 34
# x = int(input('x координата доски: '))
# y = int(input('y координата доски: '))
#
# if (x + y) % 2 == 0:
#     print("Заданная область (", x, ",", y, ") белая.")
# else:
#     print("Заданная область (", x, ",", y, ") черная.")

# 35
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# color1 = (x1 + y1) % 2
#
# color2 = (x2 + y2) % 2
#
# if color1 == color2:
#     print("Данные области имеют одинаковый цвет.")
# else:
#     print("Данные области имеют разный цвет.")

# 36
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# color1 = (x1 + y1) % 2
#
# color2 = (x2 + y2) % 2
#
# if color1 == color2:
#     print("Душа может путешествовать с одного поля на другое.")
# else:
#     print("Душа не может путешествовать с одного поля на другое.")

# 37
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print("Царь может перейти с одного поля на другое за один марш.")
# else:
#     print("Царь не может перейти с одного поля на другое за один марш.")

# 38
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# if abs(x1 - x2) == abs(y1 - y2):
#     print("Слон может пройти с одного поля на другое за одну прогулку.")
# else:
#     print("Слон не может пройти с одного поля на другое за одну прогулку.")

# 39
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
#     print("Ферзь может пройти с одного поля на другое за одну прогулку.")
# else:
#     print("Ферзь не может пройти с одного поля на другое за одну прогулку.")

# 40
# x1 = int(input("Введите координату x1 (от 1 до 8): "))
# y1 = int(input("Введите координату y1 (от 1 до 8): "))
#
# x2 = int(input("Введите координату x2 (от 1 до 8): "))
# y2 = int(input("Введите координату y2 (от 1 до 8): "))
#
# dx = abs(x1 - x2)
# dy = abs(y1 - y2)
#
# if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
#     print("Конь может пройти с одного поля на другое за одну прогулку.")
# else:
#     print("Конь не может пройти с одного поля на другое за одну прогулку.")
