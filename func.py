# 1
# def PowerA3(x):
#     return x ** 3
#
# A = 2.5
# B = 3.7
# C = 1.8
#
# D = 4
# E = 5
#
# result_A = PowerA3(A)
# result_B = PowerA3(B)
# result_C = PowerA3(C)
#
# result_D = PowerA3(D)
# result_E = PowerA3(E)
#
# print(f"A ning 3-darajasi: {result_A}")
# print(f"B ning 3-darajasi: {result_B}")
# print(f"C ning 3-darajasi: {result_C}")
#
# print(f"D ning 3-darajasi: {result_D}")
# print(f"E ning 3-darajasi: {result_E}")

# 2
# def PowerA234(x):
#     result2 = x ** 2
#     result3 = x ** 3
#     result4 = x ** 4
#     return result2, result3, result4
#
# A = 2.5
# B = 3.7
# C = 1.8
#
# result2_A, result3_A, result4_A = PowerA234(A)
# result2_B, result3_B, result4_B = PowerA234(B)
# result2_C, result3_C, result4_C = PowerA234(C)
#
# print(f"A ning 2-darajasi: {result2_A}")
# print(f"A ning 3-darajasi: {result3_A}")
# print(f"A ning 4-darajasi: {result4_A}")
#
# print(f"B ning 2-darajasi: {result2_B}")
# print(f"B ning 3-darajasi: {result3_B}")
# print(f"B ning 4-darajasi: {result4_B}")
#
# print(f"C ning 2-darajasi: {result2_C}")
# print(f"C ning 3-darajasi: {result3_C}")
# print(f"C ning 4-darajasi: {result4_C}")

# 3
# import math
#
#
# def MEAN(x, y):
#     arifmetik_mean = (x + y) / 2
#
#     geometrik_mean = math.sqrt(x * y)
#
#     return arifmetik_mean, geometrik_mean
#
#
# A = 2.5
# B = 3.7
# C = 1.8
# D = 4.2
#
# mean_AB = MEAN(A, B)
# arifmetik_mean_AB, geometrik_mean_AB = mean_AB
# print(f"(A, B) juftligi: Ortacha arifmetik = {arifmetik_mean_AB}, Ortacha geometrik = {geometrik_mean_AB}")
#
#
# mean_AC = MEAN(A, C)
# arifmetik_mean_AC, geometrik_mean_AC = mean_AC
# print(f"(A, C) juftligi: Ortacha arifmetik = {arifmetik_mean_AC}, Ortacha geometrik = {geometrik_mean_AC}")
#
#
# mean_AD = MEAN(A, D)
# arifmetik_mean_AD, geometrik_mean_AD = mean_AD
# print(f"(A, D) juftligi: Ortacha arifmetik = {arifmetik_mean_AD}, Ortacha geometrik = {geometrik_mean_AD}")

# 4
# import math
#
#
# def Triangle(side):
#     # Perimetr
#     perimeter = 3 * side
#
#     # Yuzasi (Heron formula)
#     semi_perimeter = perimeter / 2
#     area = math.sqrt(semi_perimeter * (semi_perimeter - side) ** 2)
#
#     return perimeter, area
#
#
# # Tomon uzunligi
# side_length = 5
#
# # Triangle funksiyasini chaqirib natijalarni olish
# perimeter, area = Triangle(side_length)
#
# # Natijalarni ekranga chiqaramiz
# print(f"Teng tomonli uchburchak: Tomon uzunligi = {side_length}")
# print(f"Perimetri: {perimeter}")
# print(f"Yuzasi: {area}")

# 5
# def RectPS(x1, y1, x2, y2):
#     # Tomon uzunliklari
#     side1 = abs(x2 - x1)
#     side2 = abs(y2 - y1)
#
#     # Perimetr
#     perimeter = 2 * (side1 + side2)
#
#     # Yuzasi
#     area = side1 * side2
#
#     return perimeter, area
#
# # Qarama-qarshi uchlar koordinatalari
# x1, y1 = 2, 3
# x2, y2 = 6, 7
#
# # RectPS funksiyasini chaqirib natijalarni olish
# perimeter, area = RectPS(x1, y1, x2, y2)
#
# # Natijalarni ekranga chiqaramiz
# print(f"Tog'ri tortburchak: Qarama-qarshi uchlar ({x1}, {y1}), ({x2}, {y2})")
# print(f"Perimetri: {perimeter}")
# print(f"Yuzi: {area}")

# 6
# def DigitCountSum(number):
#     # Sonning raqamlari soni
#     digit_count = len(str(number))
#
#     # Sonning raqamlari yig'indisi
#     digit_sum = sum(int(digit) for digit in str(number))
#
#     return digit_count, digit_sum
#
# # Sonlar
# a = 123
# b = 4567
# c = 89123
#
# # a, b, c sonlarining raqamlari soni va yig'indisini hisoblash
# count_a, sum_a = DigitCountSum(a)
# count_b, sum_b = DigitCountSum(b)
# count_c, sum_c = DigitCountSum(c)
#
# # Natijalarni ekranga chiqaramiz
# print(f"a soni: Raqamlari soni = {count_a}, Raqamlari yig'indisi = {sum_a}")
# print(f"b soni: Raqamlari soni = {count_b}, Raqamlari yig'indisi = {sum_b}")
# print(f"c soni: Raqamlari soni = {count_c}, Raqamlari yig'indisi = {sum_c}")

# 7
# def InvertDigit(number):
#     inverted_number = int(''.join(sorted(str(number), reverse=True)))
#     return inverted_number
#
# a = 123
# b = 4567
# c = 89123
#
# inverted_a = InvertDigit(a)
# inverted_b = InvertDigit(b)
# inverted_c = InvertDigit(c)
#
# print(f"a soni: Teskari tartibda chiqarilgan son = {inverted_a}")
# print(f"b soni: Teskari tartibda chiqarilgan son = {inverted_b}")
# print(f"c soni: Teskari tartibda chiqarilgan son = {inverted_c}")

# 8
# def AddRightDigit(K, R):
#     result_number = K * 10 + R
#     return result_number
#
# K = int(input("Butun musbat son K ni kiriting: "))
# R = int(input("Qo'shiladigan raqam R ni kiriting (1 <= R <= 9): "))
#
# result = AddRightDigit(K, R)
#
# print(f"Natija: {result}")

# 9
# def AddLeftDigit(K, R):
#     result_number = int(str(R) + str(K))
#     return result_number
#
# K = int(input("Butun musbat son K ni kiriting: "))
# R = int(input("Qo'shiladigan raqam R ni kiriting (1 <= R <= 9): "))
#
# result = AddLeftDigit(K, R)
#
# print(f"Natija: {result}")

# 10
# def Swap(a, b, c, d):
#     a, b = b, a
#
#     c, d = d, c
#
#     return a, b, c, d
#
#
# A = 2
# B = 5
# C = 8
# D = 10
#
# result_A, result_B, result_C, result_D = Swap(A, B, C, D)
#
# print(f"A va B qiymatlari almashtirilgan: A = {result_A}, B = {result_B}")
# print(f"C va D qiymatlari almashtirilgan: C = {result_C}, D = {result_D}")

# 11
# def Minmax(X, Y):
#     if X < Y:
#         print(f"Kichik: {X}, Katta: {Y}")
#     else:
#         print(f"Kichik: {Y}, Katta: {X}")
#
#
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# c = int(input("c ni kiriting: "))
# d = int(input("d ni kiriting: "))
#
# Minmax(a, b)
# Minmax(b, c)
# Minmax(c, d)
# Minmax(a, d)

# 12
# def Sortinc3(A, B, C):
#     if A > B:
#         A, B = B, A
#     if A > C:
#         A, C = C, A
#     if B > C:
#         B, C = C, B
#
#     return A, B, C
#
#
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting: "))
#
# result_A, result_B, result_C = Sortinc3(A, B, C)
#
# print(f"A, B, C sonlari osish tartibida joylashtirilgan: {result_A}, {result_B}, {result_C}")

# 13
# def SortDec3(A, B, C):
#     if C > B:
#         C, B = B, C
#     if C > A:
#         C, A = A, C
#     if B > A:
#         B, A = A, B
#     return A, B, C
#
#
# A = int(input('A ni kiriting'))
# B = int(input('B ni kiriting'))
# C = int(input('C ni kiriting'))
#
# result_A, result_B, result_C = SortDec3(A, B, C)
# print(f'A, B, C kamayish tartibida joylashtirilgan: {result_A}, {result_B}, {result_C}')

# 14
# def ShiftRight3(A, B, C):
#     temp = A
#     A = C
#     C = B
#     B = temp
#
#     return A, B, C
#
#
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting: "))
#
# result_A, result_B, result_C = ShiftRight3(A, B, C)
#
# print(f"ShiftRight3 natijasi: {result_A}, {result_B}, {result_C}")

# 15
# def ShiftLeft3(A, B, C):
#     temp = C
#     C = A
#     A = B
#     B = temp
#
#     return A, B, C
#
# A = int(input('A ni kiriting'))
# B = int(input('B ni kiriting'))
# C = int(input('C ni kiriting'))
#
# result_A, result_B, result_C = ShiftLeft3(A, B, C)
# print(f'ShiftLeft3 natijasi: {result_A}, {result_B}, {result_C}')

# 16
# def ishora(x):
#     if x < 0:
#         return -1
#     elif x > 0:
#         return 1
#     else:
#         return 0
#
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
#
# result = ishora(a) + ishora(b)
#
# print(f"ishora(a) + ishora(b) = {result}")

# 17
# def ildizlar(A, B, C):
#     D = B**2 - 4*A*C
#
#     if D > 0:
#         x1 = (-B + D**0.5) / (2*A)
#         x2 = (-B - D**0.5) / (2*A)
#         return "Ikkita haqiqiy ildiz mavjud:", x1, x2
#     elif D == 0:
#         x = -B / (2*A)
#         return "Bitta haqiqiy ildiz mavjud:", x
#     else:
#         return "Haqiqiy ildiz mavjud emas."
#
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# C = float(input("C ni kiriting: "))
#
# result = ildizlar(A, B, C)
#
# print(result)

# 18
# def doira_yuzi(radius, pi=3.1415):
#
#     area = pi * radius**2
#     return area
#
# pi_value = float(input("Pi o'zgaruvchisini kiriting (pi = 3.1415): "))
# radius_1 = float(input("1-doira radiusini kiriting: "))
# radius_2 = float(input("2-doira radiusini kiriting: "))
# radius_3 = float(input("3-doira radiusini kiriting: "))
#
# area_1 = doira_yuzi(radius_1, pi_value)
# area_2 = doira_yuzi(radius_2, pi_value)
# area_3 = doira_yuzi(radius_3, pi_value)
#
# print(f"1-doira yuzi: {area_1}")
# print(f"2-doira yuzi: {area_2}")
# print(f"3-doira yuzi: {area_3}")

# 19
# def RingS(R1, R2, pi=3.1415):
#
#     area = pi * (R1**2 - R2**2)
#     return area
#
# pi_value = float(input("Pi o'zgaruvchisini kiriting (pi = 3.1415): "))
# radius_1 = float(input("Birinchi aylananing radiusini kiriting (R1): "))
# radius_2 = float(input("Ikkinchi aylananing radiusini kiriting (R2): "))
#
# result = RingS(radius_1, radius_2, pi_value)
#
# print(f"Aylananing ustma-ust tushmagan qismining yuzasi: {result}")

# 20
# import math
#
# def TriangleP(A, B):
#
#     P = A + B + math.sqrt(A**2 + B**2)
#     return P
#
# katet_A = float(input("Katet A ni kiriting: "))
# katet_B = float(input("Katet B ni kiriting: "))
#
# result = TriangleP(katet_A, katet_B)
#
# print(f"Togri burchakli uchburchakning perimetri: {result}")

# 21
# def SumRange(A, B, C):
#     if A > B:
#         return 0
#     else:
#         return sum(range(A, B + 1)) + sum(range(B, C + 1))
#
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting: "))
#
# result = SumRange(A, B, C)
#
# print(f"{A} dan {B} gacha va {B} dan {C} gacha sonlar yigindisi: {result}")

# 22
# def Calc(A, B, Op):
#     if Op == 1:
#         result = A - B
#     elif Op == 2:
#         result = A * B
#     elif Op == 3:
#         if B != 0:
#             result = A / B
#         else:
#             return "Nolga bo'lish mumkin emas"
#     elif Op == 4:
#         result = A + B
#     else:
#         return "Noto'g'ri amal tanlang"
#
#     if result.is_integer():
#         return int(result)
#
#     return result
#
#
# A = float(input("A ni kiriting: "))
# B = float(input("B ni kiriting: "))
# Op = int(input("Amalni tanlang (1 - ayirish, 2 - kopaytirish, 3 - bolish, 4 - qo'shish): "))
#
# result = Calc(A, B, Op)
#
# print(f"Natija: {result}")

# 23
# def Quarter(X, Y):
#     if X > 0 and Y > 0:
#         return "I-chorak"
#     elif X < 0 and Y > 0:
#         return "II-chorak"
#     elif X < 0 and Y < 0:
#         return "III-chorak"
#     elif X > 0 and Y < 0:
#         return "IV-chorak"
#     else:
#         return "Nuqta o'chirilgan choraklarda yo'q"
#
# X = int(input("X ni kiriting: "))
# Y = int(input("Y ni kiriting: "))
#
# result = Quarter(X, Y)
#
# print(f"(X, Y) nuqta {result}da joylashgan")

# 24
# def Even(K):
#     return K % 2 == 0
#
# K_1 = int(input("1-sonni kiriting: "))
# K_2 = int(input("2-sonni kiriting: "))
# K_3 = int(input("3-sonni kiriting: "))
#
# result_1 = Even(K_1)
# result_2 = Even(K_2)
# result_3 = Even(K_3)
#
# print(f"{K_1} juftmi? {result_1}")
# print(f"{K_2} juftmi? {result_2}")
# print(f"{K_3} juftmi? {result_3}")

# 25
# def IsSquare(K):
#     return K > 0 and (int(K**0.5))**2 == K
#
# K_1 = int(input("1-sonni kiriting: "))
# K_2 = int(input("2-sonni kiriting: "))
# K_3 = int(input("3-sonni kiriting: "))
#
# result_1 = IsSquare(K_1)
# result_2 = IsSquare(K_2)
# result_3 = IsSquare(K_3)
#
# print(f"{K_1} kvadratmi? {result_1}")
# print(f"{K_2} kvadratmi? {result_2}")
# print(f"{K_3} kvadratmi? {result_3}")

# 26
# def IsPower5(K):
#     if K <= 0:
#         return False
#
#     while K > 1:
#         if K % 5 != 0:
#             return False
#         K /= 5
#
#     return True
#
# for i in range(1, 6):
#     result = IsPower5(i)
#     print(f"{i} soni 5 ning darajasi: {result}")

# 27
# def IsPowerN(K, N):
#     if K <= 0:
#         return False
#
#     while K % N == 0:
#         K /= N
#
#     return K == 1
#
#
# N = int(input("N ni kiriting: "))
#
# for i in range(1, 6):
#     result = IsPowerN(i, N)
#     print(f"{i} soni {N} ning darajasi: {result}")

# 28
# def IsPrime(N):
#     if N <= 1:
#         return False
#     for i in range(2, int(N**0.5) + 1):
#         if N % i == 0:
#             return False
#     return True
#
# # k sonini foydalanuvchi tomonidan kiritish
# k = int(input("k ni kiriting: "))
#
# # 5 ta son uchun IsPrime funksiyasini chaqirib natijalarni olish
# for i in range(1, 6):
#     result = IsPrime(i)
#     print(f"{i} soni tubmi? {result}")

# 29
# def DigitCount(K):
#     return len(str(K))
#
# # 5 ta son uchun DigitCount funksiyasini chaqirib natijalarni olish
# for i in range(1, 6):
#     result = DigitCount(i)
#     print(f"{i} sonining raqamlari soni: {result}")

# 30
# def DigitN(K, N):
#     str_K = str(K)
#     if abs(N) > len(str_K):
#         return -1
#
#     return int(str_K[N - 1])
#
#
# # K1, K2, K3 sonlarini va N raqamini foydalanuvchi tomonidan kiritish
# K1 = int(input("K1 ni kiriting: "))
# K2 = int(input("K2 ni kiriting: "))
# K3 = int(input("K3 ni kiriting: "))
# N = int(input("N ni kiriting: "))
#
# # DigitN funksiyasini chaqirib natijalarni olish
# result_K1 = DigitN(K1, N)
# result_K2 = DigitN(K2, N)
# result_K3 = DigitN(K3, N)
#
# # Natijalarni ekranga chiqarish
# print(f"{K1} sonining {N}-raqami: {result_K1}")
# print(f"{K2} sonining {N}-raqami: {result_K2}")
# print(f"{K3} sonining {N}-raqami: {result_K3}")

# 31
# def IsPalindrome(N):
#     str_N = str(N)
#     return str_N == str_N[::-1]
#
# # 5 ta son uchun IsPalindrome funksiyasini chaqirib natijalarni olish
# for i in range(1, 6):
#     result = IsPalindrome(i)
#     print(f"{i} soni palindrommi? {result}")

# 32
# import math
#
# def DegToRad(D):
#     return math.radians(D)
#
# # 3 ta burchakning qiymatlarini foydalanuvchi tomonidan kiritish
# D1 = float(input("Birinchi burchakni kiriting (0 < D < 360): "))
# D2 = float(input("Ikkinchi burchakni kiriting (0 < D < 360): "))
# D3 = float(input("Uchinchi burchakni kiriting (0 < D < 360): "))
#
# # DegToRad funksiyasini chaqirib natijalarni olish
# result_D1 = DegToRad(D1)
# result_D2 = DegToRad(D2)
# result_D3 = DegToRad(D3)
#
# # Natijalarni ekranga chiqarish
# print(f"{D1} gradusning radianga qiymati: {result_D1} radian")
# print(f"{D2} gradusning radianga qiymati: {result_D2} radian")
# print(f"{D3} gradusning radianga qiymati: {result_D3} radian")

# 33
# import math
#
# def RadToDeg(R):
#     return math.degrees(R)
#
# # 3 ta burchakning qiymatlarini foydalanuvchi tomonidan kiritish
# R1 = float(input("Birinchi burchakni kiriting: "))
# R2 = float(input("Ikkinchi burchakni kiriting: "))
# R3 = float(input("Uchinchi burchakni kiriting: "))
#
# # RadToDeg funksiyasini chaqirib natijalarni olish
# result_R1 = RadToDeg(R1)
# result_R2 = RadToDeg(R2)
# result_R3 = RadToDeg(R3)
#
# # Natijalarni ekranga chiqarish
# print(f"{R1} radianning gradusdagi qiymati: {result_R1} gradus")
# print(f"{R2} radianning gradusdagi qiymati: {result_R2} gradus")
# print(f"{R3} radianning gradusdagi qiymati: {result_R3} gradus")

# 34
# def Fact(N):
#     if N == 0 or N == 1:
#         return 1
#     else:
#         return N * Fact(N - 1)
#
# # 3 ta son uchun Fact funksiyasini chaqirib natijalarni olish
# for i in range(1, 4):
#     result = Fact(i)
#     print(f"{i} ning faktoriali: {result}")

# 35
# def Fact2(N):
#     if N <= 0:
#         return 1
# 
#     result = 1
#     for i in range(N, 0, -2):
#         result *= i
# 
#     return result
# 
# 
# # 3 ta son uchun Fact2 funksiyasini chaqirib natijalarni olish
# for i in range(1, 4):
#     result = Fact2(i)
#     print(f"{i} ning ikkilangan faktoriali: {result}")

# 36
# def Fib(N):
#     if N <= 0:
#         return "N kiritilgan qiymat noto'g'ri."
#
#     fib_sequence = [0, 1]
#     while len(fib_sequence) <= N:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#
#     return fib_sequence[N]
#
# # Funksiyani chaqirib natijalarni olish
# N = int(input("Fibonachchi sonlarining N - elementini kiriting: "))
# result = Fib(N)
#
# # Natijani ekranga chiqarish
# print(f"Fibonachchi sonlarining {N} - elementi: {result}")

# 37
# def Power1(A, B):
#     result = A ** B
#     return result
#
#
# A = int(input('A soni: '))
#
# B = int(input('B soni: '))
#
# rr = Power1(A, B)
# print(f'{A} ning {B} darajasi - {rr} ')

# 38
# def Power2(A, N, M, K):
#     if N < 0:
#         return "N kiritilgan qiymat noto'g'ri."
#
#     result_N = 1
#     result_M = 1
#     result_K = 1
#
#     for i in range(abs(N)):
#         result_N *= A
#
#     for i in range(M):
#         result_M *= A
#
#     for i in range(K):
#         result_K *= A
#
#     return result_N, result_M, result_K
#
# # Funksiyani chaqirib natijalarni olish
# A = float(input("A sonini kiriting: "))
# N = int(input("N darajasini kiriting: "))
# M = int(input("M darajasini kiriting: "))
# K = int(input("K darajasini kiriting: "))
#
# result_N, result_M, result_K = Power2(A, N, M, K)
#
# # Natijani ekranga chiqarish
# print(f"{A}^{N} = {result_N}")
# print(f"{A}^{M} = {result_M}")
# print(f"{A}^{K} = {result_K}")

# 39
# def Power1(A, B):
#     result = 1
#     for _ in range(abs(B)):
#         result *= A
#     return result
#
# def Power2(A, N):
#     result = 1
#     for _ in range(abs(N)):
#         result *= A
#     return result
#
# def Power3(A, N):
#     if N % 1 == 0:
#         return Power2(A, int(N))
#     else:
#         return Power1(A, N)
#
# # Funksiyani chaqirib natijani olish
# A = float(input("A sonini kiriting: "))
# N = float(input("N sonini kiriting: "))
#
# result = Power3(A, N)
#
# # Natijani ekranga chiqarish
# print(f"{A}^{N} = {result}")

# 40
# def Exp1(x, e):
#     result = 1.0
#     term = 1.0
#     n = 1
#
#     while abs(term) > e:
#         term *= x / n
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = Exp1(x, e)
#
# # Natijani ekranga chiqarish
# print(f"Exp1({x}, {e}) = {result}")

# 41
# import math
#
# def sin1(x, e):
#     result = x
#     term = x
#     n = 1
#
#     while abs(term) > e:
#         term *= -1 * x**2 / ((2 * n) * (2 * n + 1))
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = sin1(x, e)
#
# # Natijani ekranga chiqarish
# print(f"sin1({x}, {e}) = {result}")

# 42
# import math
#
# def cos1(x, e):
#     result = 1
#     term = 1
#     n = 1
#
#     while abs(term) > e:
#         term *= -1 * x**2 / ((2 * n - 1) * (2 * n))
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = cos1(x, e)
#
# # Natijani ekranga chiqarish
# print(f"cos1({x}, {e}) = {result}")

# 43
# def Ln1(x, e):
#     if abs(x) >= 1:
#         return "x ning moduli 1 dan kichik bo'lishi kerak."
#
#     result = 0
#     term = x
#     n = 1
#
#     while abs(term) > e:
#         term *= -1 * x * n / (n + 1)
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = Ln1(x, e)
#
# # Natijani ekranga chiqarish
# print(f"Ln1({x}, {e}) = {result}")

# 44
# def Arctg1(x, e):
#     if abs(x) >= 1:
#         return "x ning moduli 1 dan kichik bo'lishi kerak."
#
#     result = 0
#     term = x
#     n = 1
#
#     while abs(term) > e:
#         term *= -1 * x**2 * (2 * n - 1) / ((2 * n + 1) * n)
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = Arctg1(x, e)
#
# # Natijani ekranga chiqarish
# print(f"Arctg1({x}, {e}) = {result}")

# 45
# import math
#
# def Power4(x, a, e):
#     if abs(x) >= 1:
#         return "x ning moduli 1 dan kichik bo'lishi kerak."
#
#     result = 1
#     term = a * x
#     n = 1
#
#     while abs(term) > e:
#         term *= -1 * x * (a - n + 1) / n
#         result += term
#         n += 1
#
#     return result
#
# # Funksiyani chaqirib natijani olish
# x = float(input("x sonini kiriting: "))
# a = float(input("a sonini kiriting: "))
# e = float(input("e sonini kiriting: "))
#
# result = Power4(x, a, e)
#
# # Natijani ekranga chiqarish
# print(f"Power4({x}, {a}, {e}) = {result}")

# 46
# def EKUB(A, B, C, D):
#     def EKUB2(x, y):
#         while y:
#             x, y = y, x % y
#         return x
#
#     ekub_ab = EKUB2(A, B)
#     ekub_ac = EKUB2(ekub_ab, C)
#     ekub_ad = EKUB2(ekub_ac, D)
#
#     return ekub_ad
#
# # Funksiyani chaqirib natijani olish
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# C = int(input("C sonini kiriting: "))
# D = int(input("D sonini kiriting: "))
#
# result = EKUB(A, B, C, D)
#
# # Natijani ekranga chiqarish
# print(f"EKUB({A}, {B}, {C}, {D}) = {result}")

# 47
# def EKUB(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# def Frac1(a, b, c, d):
#     ekub_bd = EKUB(b, d)
#
#     p1 = a * (d // ekub_bd)
#     p2 = c * (b // ekub_bd)
#
#     q = b * (d // ekub_bd)
#
#     return p1 + p2, q
#
# # Funksiyani chaqirib natijani olish
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))
# d = int(input("d sonini kiriting: "))
#
# result_p, result_q = Frac1(a, b, c, d)
#
# # Natijani ekranga chiqarish
# print(f"Frac1({a}, {b}, {c}, {d}) = ({result_p}, {result_q})")

# 48
# def EKUB(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# def EKUK(A, B):
#     return A * B // EKUB(A, B)
#
# # Funksiyani chaqirib natijani olish
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# result = EKUK(A, B)
#
# # Natijani ekranga chiqarish
# print(f"EKUK({A}, {B}) = {result}")

# 49
# def EKUB(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# def EKUB3(A, B, C):
#     ekub_ab = EKUB(A, B)
#     ekub_ac = EKUB(A, C)
#     ekub_bc = EKUB(B, C)
#
#     return EKUB(ekub_ab, ekub_ac, ekub_bc)
#
# # Funksiyani chaqirib natijani olish
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# C = int(input("C sonini kiriting: "))
#
# result = EKUB3(A, B, C)
#
# # Natijani ekranga chiqarish
# print(f"EKUB3({A}, {B}, {C}) = {result}")

# 50
# def TimeToHMS(T):
#     # Soatni hisoblash
#     hours = T // 3600
#     # Qolgan sekundlar
#     remaining_seconds = T % 3600
#     # Minutni hisoblash
#     minutes = remaining_seconds // 60
#     # Qolgan sekundlar
#     seconds = remaining_seconds % 60
#
#     return hours, minutes, seconds
#
# # Funksiyani chaqirib natijani olish
# T = int(input("Sekundlarni kiriting: "))
#
# hours, minutes, seconds = TimeToHMS(T)
#
# # Natijani ekranga chiqarish
# print(f"{T} sekund = {hours:02d}:{minutes:02d}:{seconds:02d}")

# 51
# def IncTime(H, M, S, T):
#     # Berilgan soat, minut va sekundlarni sekundga aylantiramiz
#     total_seconds = H * 3600 + M * 60 + S
#     # Yangi total sekundlarni hisoblaymiz
#     new_total_seconds = total_seconds + T
#     # Yangi soatni hisoblash
#     new_hours = new_total_seconds // 3600
#     # Qolgan sekundlar
#     remaining_seconds = new_total_seconds % 3600
#     # Yangi minutni hisoblash
#     new_minutes = remaining_seconds // 60
#     # Yangi sekundlarni hisoblash
#     new_seconds = remaining_seconds % 60
#
#     return new_hours, new_minutes, new_seconds
#
# # Funksiyani chaqirib natijani olish
# H = int(input("Soatni kiriting: "))
# M = int(input("Minutni kiriting: "))
# S = int(input("Sekundni kiriting: "))
# T = int(input("Qancha sekundga oshirishni kiriting: "))
#
# new_hours, new_minutes, new_seconds = IncTime(H, M, S, T)
#
# # Natijani ekranga chiqarish
# print(f"{H:02d}:{M:02d}:{S:02d} + {T} sekund = {new_hours:02d}:{new_minutes:02d}:{new_seconds:02d}")

# 52
# def IsLeapYear(Y):
#     if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#         return True
#     else:
#         return False
#
# # Funksiyani chaqirib natijani olish
# years = [2020, 2021, 2022, 2023, 2024]
#
# for year in years:
#     result = IsLeapYear(year)
#     print(f"{year} yili kabisa yili: {result}")

# 53
# def IsLeapYear(Y):
#     # Yilni kabisa yiliga tekshirish
#     return (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0)
#
#
# def MonthDays(M, Y):
#     # Berilgan oyning kunlar soni
#     days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     # Kabisa yilni tekshirish
#     if IsLeapYear(Y):
#         days_in_month[2] = 29  # Kabisa yilda fevral oyining kunlari 29
#     return days_in_month[M]
#
#
# def DaysInMonths(Y):
#     # Berilgan yil uchun har bir oyda necha kunlar borligini hisoblash
#     days_in_January = MonthDays(1, Y)
#     days_in_February = MonthDays(2, Y)
#     days_in_March = MonthDays(3, Y)
#
#     return days_in_January, days_in_February, days_in_March
#
#
# # Funksiyani chaqirib natijani olish
# Y = int(input("Yilni kiriting: "))
#
# days_in_January, days_in_February, days_in_March = DaysInMonths(Y)
#
# # Natijani ekranga chiqarish
# print(f"{Y} yili uchun kunlar soni:\nJanuary: {days_in_January}\nFebruary: {days_in_February}\nMarch: {days_in_March}")

# 54
# def MonthDays(M, Y):
#     # Berilgan oyning kunlar soni
#     days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     # Kabisa yilni tekshirish
#     if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#         days_in_month[2] = 29  # Kabisa yilda fevral oyining kunlari 29
#     return days_in_month[M]
#
# def PrevDate(D, M, Y):
#     # Oldingi sanani aniqlash
#     if D == 1:
#         # Agar kiritilgan kun birinchi kun bo'lsa, oldingi sanaga o'tkazamiz
#         if M == 1:
#             # Agar kiritilgan oy yanvar bo'lsa, oldingi yilning dekabr oyiga o'tkazamiz
#             prev_month = 12
#             prev_year = Y - 1
#         else:
#             # Agar kiritilgan oy yanvar emas bo'lsa, oldingi oyni bir kamaytiramiz
#             prev_month = M - 1
#             prev_year = Y
#         prev_day = MonthDays(prev_month, prev_year)
#     else:
#         # Agar kiritilgan kun birinchi kun bo'lmasa, kunni bir kamaytiramiz
#         prev_day = D - 1
#         prev_month = M
#         prev_year = Y
#
#     return prev_day, prev_month, prev_year
#
# # Funksiyani chaqirib natijani olish
# D = int(input("Kunni kiriting: "))
# M = int(input("Oyini kiriting: "))
# Y = int(input("Yilni kiriting: "))
#
# prev_day, prev_month, prev_year = PrevDate(D, M, Y)
#
# # Natijani ekranga chiqarish
# print(f"{D:02d}/{M:02d}/{Y} dan oldingi sanasi: {prev_day:02d}/{prev_month:02d}/{prev_year}")

# 55
# def MonthDays(M, Y):
#     # Berilgan oyning kunlar soni
#     days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     # Kabisa yilni tekshirish
#     if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#         days_in_month[2] = 29  # Kabisa yilda fevral oyining kunlari 29
#     return days_in_month[M]
#
# def NextDate(D, M, Y):
#     # Keyingi sanani aniqlash
#     days_in_month = MonthDays(M, Y)
#
#     if D == days_in_month:
#         # Agar kiritilgan kun birinchi kun bo'lsa, keyingi sanaga o'tkazamiz
#         if M == 12:
#             # Agar kiritilgan oy dekabr bo'lsa, keyingi yilning yanvar oyiga o'tkazamiz
#             next_month = 1
#             next_year = Y + 1
#         else:
#             # Agar kiritilgan oy dekabr emas bo'lsa, keyingi oyni bir oshiramiz
#             next_month = M + 1
#             next_year = Y
#         next_day = 1
#     else:
#         # Agar kiritilgan kun birinchi kun bo'lmasa, kunni bir oshiramiz
#         next_day = D + 1
#         next_month = M
#         next_year = Y
#
#     return next_day, next_month, next_year
#
# # Funksiyani chaqirib natijani olish
# D = int(input("Kunni kiriting: "))
# M = int(input("Oyini kiriting: "))
# Y = int(input("Yilni kiriting: "))
#
# next_day, next_month, next_year = NextDate(D, M, Y)
#
# # Natijani ekranga chiqarish
# print(f"{D:02d}/{M:02d}/{Y} dan keyingi sanasi: {next_day:02d}/{next_month:02d}/{next_year}")

# 56
# import math
#
# def Leng(X1, Y1, X2, Y2):
#     # Berilgan nuqtalarni orasidagi masofani hisoblash
#     distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#     return distance
#
# # Nuqtalarni olish
# X1 = float(input("A nuqta x qiymatini kiriting: "))
# Y1 = float(input("A nuqta y qiymatini kiriting: "))
# X2 = float(input("B nuqta x qiymatini kiriting: "))
# Y2 = float(input("B nuqta y qiymatini kiriting: "))
#
# # Funksiyani chaqirib natijani olish
# result = Leng(X1, Y1, X2, Y2)
#
# # Natijani ekranga chiqarish
# print(f"Masofa: {result}")

# 57
# import math
#
# def Leng(X1, Y1, X2, Y2):
#     # Berilgan nuqtalarni orasidagi masofani hisoblash
#     distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#     return distance
#
# def Perim(XA, YA, XB, YB, XC, YC):
#     # Uchburchak perimetri hisoblanadi
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     perimeter = AB + BC + CA
#     return perimeter
#
# # Nuqtalarni olish
# XA = float(input("A nuqta x qiymatini kiriting: "))
# YA = float(input("A nuqta y qiymatini kiriting: "))
# XB = float(input("B nuqta x qiymatini kiriting: "))
# YB = float(input("B nuqta y qiymatini kiriting: "))
# XC = float(input("C nuqta x qiymatini kiriting: "))
# YC = float(input("C nuqta y qiymatini kiriting: "))
#
# # Funksiyani chaqirib natijani olish
# result = Perim(XA, YA, XB, YB, XC, YC)
#
# # Natijani ekranga chiqarish
# print(f"Uchburchak perimetri: {result}")

# 58
# import math
#
# def Leng(X1, Y1, X2, Y2):
#     # Berilgan nuqtalarni orasidagi masofani hisoblash
#     distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#     return distance
#
# def Perim(XA, YA, XB, YB, XC, YC):
#     # Uchburchak perimetri hisoblanadi
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     perimeter = AB + BC + CA
#     return perimeter
#
# def Area(XA, YA, XB, YB, XC, YC):
#     # Uchburchak yuzasi hisoblanadi
#     s = Perim(XA, YA, XB, YB, XC, YC) / 2
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))
#     return area
#
# # Nuqtalarni olish
# XA = float(input("A nuqta x qiymatini kiriting: "))
# YA = float(input("A nuqta y qiymatini kiriting: "))
# XB = float(input("B nuqta x qiymatini kiriting: "))
# YB = float(input("B nuqta y qiymatini kiriting: "))
# XC = float(input("C nuqta x qiymatini kiriting: "))
# YC = float(input("C nuqta y qiymatini kiriting: "))
#
# # Funksiyani chaqirib natijani olish
# result = Area(XA, YA, XB, YB, XC, YC)
#
# # Natijani ekranga chiqarish
# print(f"Uchburchak yuzasi: {result}")

# 59
# import math
#
# def Leng(X1, Y1, X2, Y2):
#     # Berilgan nuqtalarni orasidagi masofani hisoblash
#     distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#     return distance
#
# def Area(XA, YA, XB, YB, XC, YC):
#     # Uchburchak yuzasi hisoblanadi
#     s = (Leng(XA, YA, XB, YB) + Leng(XB, YB, XC, YC) + Leng(XC, YC, XA, YA)) / 2
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))
#     return area
#
# def Dist(Xa, Ya, Xb, Yb, Xp, Yp):
#     # P nuqtadan AB kesmaga tushirilgan balandlik hisoblanadi
#     Spab = Area(Xa, Ya, Xb, Yb, Xp, Yp)
#     AB = Leng(Xa, Ya, Xb, Yb)
#
#     distance = 2 * Spab / AB
#     return distance
#
# # Nuqtalarni olish
# Xa = float(input("A nuqta x qiymatini kiriting: "))
# Ya = float(input("A nuqta y qiymatini kiriting: "))
# Xb = float(input("B nuqta x qiymatini kiriting: "))
# Yb = float(input("B nuqta y qiymatini kiriting: "))
# Xp = float(input("P nuqta x qiymatini kiriting: "))
# Yp = float(input("P nuqta y qiymatini kiriting: "))
#
# # Funksiyani chaqirib natijani olish
# result = Dist(Xa, Ya, Xb, Yb, Xp, Yp)
#
# # Natijani ekranga chiqarish
# print(f"P nuqtadan AB, BC, AC kesmaga tushirilgan balandlik: {result}")

# 60
# import math
#
# def Dist(Xa, Ya, Xb, Yb, Xp, Yp):
#     # P nuqtadan AB kesmaga tushirilgan balandlik hisoblanadi
#     Spab = Area(Xa, Ya, Xb, Yb, Xp, Yp)
#     AB = Leng(Xa, Ya, Xb, Yb)
#
#     distance = 2 * Spab / AB
#     return distance
#
# def Leng(X1, Y1, X2, Y2):
#     # Berilgan nuqtalarni orasidagi masofani hisoblash
#     distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#     return distance
#
# def Area(XA, YA, XB, YB, XC, YC):
#     # Uchburchak yuzasi hisoblanadi
#     s = (Leng(XA, YA, XB, YB) + Leng(XB, YB, XC, YC) + Leng(XC, YC, XA, YA)) / 2
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     area = math.sqrt(s * (s - AB) * (s - BC) * (s - CA))
#     return area
#
# def Heights(Xa, Ya, Xb, Yb, Xc, Yc, hA, hB, hC):
#     # Uchburchak tomonlariga tushurilgan balandliklarni hisoblash
#     ha = Dist(Xb, Yb, Xc, Yc, Xa, Ya)
#     hb = Dist(Xa, Ya, Xc, Yc, Xb, Yb)
#     hc = Dist(Xa, Ya, Xb, Yb, Xc, Yc)
#
#     # Berilgan balandliklarni foydalanuvchiga chiqarish
#     print(f"A nuqta uchun balandlik: {hA}, Hisoblangan balandlik: {ha}")
#     print(f"B nuqta uchun balandlik: {hB}, Hisoblangan balandlik: {hb}")
#     print(f"C nuqta uchun balandlik: {hC}, Hisoblangan balandlik: {hc}")
#
# # Nuqtalarni olish
# Xa = float(input("A nuqta x qiymatini kiriting: "))
# Ya = float(input("A nuqta y qiymatini kiriting: "))
# Xb = float(input("B nuqta x qiymatini kiriting: "))
# Yb = float(input("B nuqta y qiymatini kiriting: "))
# Xc = float(input("C nuqta x qiymatini kiriting: "))
# Yc = float(input("C nuqta y qiymatini kiriting: "))
# hA = float(input("A nuqta uchun balandlikni kiriting: "))
# hB = float(input("B nuqta uchun balandlikni kiriting: "))
# hC = float(input("C nuqta uchun balandlikni kiriting: "))
#
# # Funksiyani chaqirib natijani olish
# Heights(Xa, Ya, Xb, Yb, Xc, Yc, hA, hB, hC)
