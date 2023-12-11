# 1
# A = int(input("A musbat son: "))
# B = int(input("B musbat son: "))
#
# while A <= B:
#     print("A B dan kotta bosin.")
#     A = int(input("A musbat son: "))
#     B = int(input("B musbat son: "))
#
# remainder = A % B
#
# empty_part = B - remainder
#
# print(f"A ni pustoy joyi: {empty_part}")

# 2
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
#
# while A <= 0 or B <= 0:
#     print("Xatolik: Sonlar musbat bo'lishi kerak.")
#     A = int(input("A ni qaytadan kiriting: "))
#     B = int(input("B ni qaytadan kiriting: "))
#
# a_kesma = set(range(0, A + 1, A))
#
# b_kesma = set(range(0, B + 1, B))
#
# common_elements = a_kesma.intersection(b_kesma)
#
# print(f"A usunlikdagi kesmada B kesmadan {len(common_elements)} ta joylashishi mumkin.")

# 3
# N = int(input("N ni kiriting: "))
# K = int(input("K ni kiriting: "))
#
# while N <= 0 or K <= 0:
#     print("Xatolik: Sonlar musbat bo'lishi kerak.")
#     N = int(input("N ni qaytadan kiriting: "))
#     K = int(input("K ni qaytadan kiriting: "))
# M = N
# S = K
# while M >= S:
#     M -= S
#
# qoldiq = N / K % 1
# butun_qism = N // K
#
# # Natijani chiqarish
# print(f"{N} ni {K} ga bolgandagi qoldiq: {qoldiq}")
# print(f"{N} ni {K} ga bolgandagi butun qismi: {butun_qism}")

# 4
# n = int(input("n sonini kiriting: "))
#
# daraja = 3
# daraja_topildi = False
# i = 1
#
# while i < n:
#     i *= daraja
#     if i == n:
#         daraja_topildi = True
#         break
#
# if daraja_topildi:
#     print("3-ning darajasi")
# else:
#     print("3-ning darajasi emas")

# 5
# n = int(input("n sonini kiriting: "))
#
# daraja = 2
# k = 0
#
# while n % daraja == 0:
#     n //= daraja
#     k += 1
#
# if n == 1:
#     print(f"{n} soni {daraja} ning {k}-darajasi")
# else:
#     print(f"{n} soni {daraja} ning darajasi emas")

# 6
# n = int(input("n sonini kiriting: "))
#
# n_daraja = 1
#
# while n > 0:
#     n_daraja *= n
#     n -= 2
#
# print(f"{n}!! = {n_daraja}")

# 7
# n = int(input("n sonini kiriting: "))
# k = 0
# while n > k:
#     for i in range(1, n + 1):
#         if i ** 2 > n:
#             i **= 2
#             k = i
#             print(k)
#             break

# 8
# n = int(input("n ni kiriting: "))
#
# k = 1
# while k**2 <= n:
#     k += 1
#
# k -= 1
# print(f"Eng katta butun k: {k}")

# 9
# n = int(input("n ni kiriting: "))
#
# k = 1
# while 3 * k < n:
#     k += 1
#
# k -= 1
# print(f"Eng kichik butun k: {k}")

# 10
# n = int(input("n ni kiriting: "))
#
# k = 1
# while 3 ** k <= n:
#     k += 1
#
# k -= 1
# print(f"Eng katta butun k: {k}")

# 11
# n = int(input("n ni kiriting: "))
#
# k = 1
# total = 0
#
# while total < n:
#     total += k
#     k += 1
#
# print(f"Eng kichik k: {k - 1}")
# print(f"1 dan {k - 1} gacha bo'lgan yig'indi: {total}")

# 12
# n = int(input("n ni kiriting: "))
#
# k = 1
# total = 0
#
# while total + k <= n:
#     total += k
#     k += 1
#
# print(f"Eng katta k: {k - 1}")
# print(f"1 dan {k - 1} gacha bo'lgan yig'indi: {total}")

# 13
# a = float(input("a ni kiriting: "))
#
# k = 1
# total = 0.0
#
# while total < a:
#     total += 1 / k
#     k += 1
#
# print(f"Eng kichik k: {k - 1}")
# print(f"1 + 1/2 + 1/3 + ... + 1/{k-1} gacha bo'lgan yig'indi: {total}")

# 14
# a = float(input("a ni kiriting: "))
#
# k = 1
# total = 0.0
#
# while total + 1 / k <= a:
#     total += 1 / k
#     k += 1
#
# print(f"Eng katta k: {k - 1}")
# print(f"1 + 1/2 + 1/3 + ... + 1/{k-1} gacha bo'lgan yig'indi: {total}")

# 15
# S = float(input("Boshlang'ich summani kiriting: "))
# p = float(input("Foizni kiriting (0 < p < 25): "))
#
# # Qancha martadan keyin summa 2 marta kop bolishi kerakligini hisoblash
# k = 0
# while S < 2:
#     S *= (1 + p / 100)
#     k += 1
#
# print(f"Keyin boshlang'ich summa 2 martadan ko'p bo'ladi, {k} oyda.")
# print(f"Bankda hosil bo'lgan summa: {S}")


# 16
# initial_distance = 10
# p = float(input("Yuqoridagi kunga nisbatan foizni kiriting (0 < p < 50): "))
# target_distance = 200
#
# current_distance = initial_distance
# days = 1
#
# while current_distance < target_distance:
#     current_distance += current_distance * p / 100
#     days += 1
#
# print(f"Jami kunlar soni: {days}")
# print(f"Jami yugurgan masofa: {current_distance} km")

# 17
# n = int(input("n ni kiriting: "))
# m = int(input("m ni kiriting: "))
#
# qoldiq = n - m * (n // m)
# butun_qism = (n - qoldiq) // m
#
# print(f"{n} ni {m} ga bo'lib, butun qismi: {butun_qism}, qoldiq: {qoldiq}")

# 18
# n = int(input("Butun sonni kiriting: "))
#
# reverse_n = 0
#
# while n > 0:
#     last_digit = n % 10
#     reverse_n = reverse_n * 10 + last_digit
#     n //= 10
#
# print(f"Berilgan sonning teskari tartibi: {reverse_n}")

# 19
# n = int(input("Butun sonni kiriting: "))
#
# sum_of_digits = 0
# count_of_digits = 0
#
# while n > 0:
#     last_digit = n % 10
#     sum_of_digits += last_digit
#     count_of_digits += 1
#     n //= 10
#
# print(f"Raqamlar yig'indisi: {sum_of_digits}")
# print(f"Raqamlar soni: {count_of_digits}")

# 20
# n = int(input("Butun sonni kiriting: "))
#
# has_two = False
#
# while n > 0:
#     last_digit = n % 10
#     if last_digit == 2:
#         has_two = True
#         break
#     n //= 10
#
# if has_two:
#     print("Berilgan son ichida 2 raqami bor.")
# else:
#     print("Berilgan son ichida 2 raqami yo'q.")

# 21
# n = int(input("Butun sonni kiriting: "))
#
# has_odd_digit = False
#
# while n > 0:
#     last_digit = n % 10
#     if last_digit % 2 != 0:
#         has_odd_digit = True
#         break
#     n //= 10
#
# if has_odd_digit:
#     print("Berilgan son ichida toq raqam bor.")
# else:
#     print("Berilgan son ichida toq raqam yo'q.")

# 22
# n = int(input("Butun sonni kiriting: "))
#
# is_prime = True
#
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#
# if is_prime:
#     print(f"{n} tub son.")
# else:
#     print(f"{n} tub son emas.")

# 23
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
# result = gcd(a, b)
#
# print(f"{a} va {b} sonlarining eng katta umumiy boluvchisi: {result}")

# 24
# n = int(input("Butun sonni kiriting: "))
#
# def is_fibonacci(number):
#     a, b = 0, 1
#     while b < number:
#         a, b = b, a + b
#     return b == number
#
# if is_fibonacci(n):
#     print(f"{n} Fibonachi sonlari orasida bor.")
# else:
#     print(f"{n} Fibonachi sonlari orasida yo'q.")

# 25
# n = int(input("Butun sonni kiriting: "))
#
# def find_first_fibonacci_greater_than_n(target):
#     a, b = 0, 1
#     while b <= target:
#         a, b = b, a + b
#     return b
#
# result = find_first_fibonacci_greater_than_n(n)
#
# print(f"{n} dan katta bolgan birinchi Fibonachi soni: {result}")

# 26
# n = int(input("Butun sonni kiriting: "))
#
# def find_fibonacci_numbers_around_n(target):
#     a, b = 0, 1
#     while b <= target:
#         a, b = b, a + b
#     return b - a, b
#
# prev_fibonacci, next_fibonacci = find_fibonacci_numbers_around_n(n)
#
# print(f"{n} dan bir oldingi Fibonachi soni: {prev_fibonacci}")
# print(f"{n} dan bir keyingi Fibonachi soni: {next_fibonacci}")

# 27
# n = int(input("Butun sonni kiriting: "))
#
# def find_fibonacci_index(target):
#     a, b = 0, 1
#     index = 0
#     while a < target:
#         a, b = b, a + b
#         index += 1
#     return index if a == target else -1
#
# result = find_fibonacci_index(n)
#
# if result != -1:
#     print(f"{n} soni Fibonachi ketma-ketligining {result}-xadi.")
# else:
#     print(f"{n} soni Fibonachi ketma-ketligida yo'q.")

# 28
# e = float(input("e ni kiriting: "))
#
# a = 2
# k = 2
#
# while a < e:
#     a = 2 + 1 / a
#     k += 1
#
# print(f"{e} ga yaqin bo'lgan ketma-ketlik xadi {k}-xadda.")

# 29
# e = float(input("e ni kiriting: "))
#
# a1 = 1
# a2 = 2
# k = 3
#
# while True:
#     ak = (a1 + 2 * a2) / 3
#     print(f"a{k} = {ak}, a{k-1} = {a2}")
#     if abs(ak - a2) < e:
#         break
#     a1, a2 = a2, ak
#     k += 1
#
# print(f"Eng kichik k: {k}")

# 30
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting: "))
#
# count_of_squares = 0
#
# while A >= C and B >= C:
#     A -= C
#     B -= C
#     count_of_squares += 1
#
# print(f"Tortburchak ichida tomoni {C} bolgan kvadratdan {count_of_squares} ta sig'di.")
