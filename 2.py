# 1
# L = int(input('uzunlik sm: '))
# M = L // 100
# print(f'{L} sm = {M} metr')
#
# 2
# M = int(input('ogirlik kg: '))
# T = M // 1000
# print(f'{M} kg = {T} t')
#
# 3
# B = int(input('Fayl Bayti: '))
# Kb = B // 1024
# print(f'{B} bayt = {Kb} kb')
#
# 4
# A = int(input('a ni kiriting: '))
# B = int(input('b ni kiriting'))
#
# sum = A // B
# print(f'a kesmani b kesmaga {sum} marta joylashtirish mm')
#
# 5
# A = int(input('a ni kiriting: '))
# B = int(input('b ni kiriting'))
#
# dnt = A % B
#
# print(f'a kesmada joylashmagan uzunlig {dnt}')
#
# 6
# num_ = int(input('ikki xonali son: '))
# teens = num_ // 10
# ones = num_ % 10
# print(f'onlik {teens} birlik {ones}')
#
# 7
# num_ = int(input('ikki xonali son: '))
# teens = num_ // 10
# ones = num_ % 10
# sum = teens + ones
# print(f'raqamlari yigindisi {sum}')
#
# 8
# num_ = int(input('ikki xonali son: '))
# teens = num_ // 10
# ones = num_ % 10
# for_ = ones * 10 + teens
# print(f'{num_} aylantirilgan holati {for_}')
#
# 9
# num_ = int(input('uch xonali son: '))
# hon = num_ // 100
# print(f'{num_} 100 xonadigi soni {hon}')

# 10
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# print(f'{num_} sonida birlik xonasidagi son {ones} onlik honasidagi son {teens}')

# 11
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# sum = hon + teens + ones
# print(f'{num_} raqamlarini yigindisi {sum}')

# 12
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# for_ = ones * 100 + teens * 10 + hon
# print(f'{num_} sonini aylantirilgan holati {for_}')

# 13
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# for_ = teens * 100 + ones * 10 + hon
# print(f'birinchi soni onga olish {for_}')
#
# 14
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# for_ = ones * 100 + hon * 10 + teens
# print(f'ohirhi sonni chapga olish {for_}')

# 15
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# for_ = teens * 100 + hon * 10 + ones
# print(f'on lik bn yuzlikni almashtirish {for_}')

# 16
# num_ = int(input('uch xonali son: '))
# ones = num_ % 10
# teens = num_ // 10 % 10
# hon = num_ // 100
# for_ = hon * 100 + ones * 10 + teens
# print(f'onlik bn birlikni almashtirish {for_}')

# 17
# num_ = int(input('son 999 dan koproq: '))
# hon = num_ // 100 % 10
# print(f'{num_} minlik honadagi yuzlik soni {hon}')

# 18
# num_ = int(input('son 999 dan koproq: '))
# min_ = num_ // 1000
# print(f'{num_} da minlik son {min_}')

# 19
# sec = int(input('kun boshidan necha sekund otdi: '))
# min_ = sec // 60
# print(f'agar kun boshdan {sec} sec otkan bosa bu {min_} min otdi dgani')

# 20
# sec = int(input('kun boshidan necha sekund otdi: '))
# oc_ = sec / 3600
# print(f'agar kun boshdan {sec} sec otkan bosa bu {oc_} soat otdi dgani')

# 21
# sec = int(input('kun boshidan necha sekund otdi: '))
# min_ = sec // 60
# qol_ = sec % 60
# print(f'kun boshdan {min_} min, {qol_} sec otdi')

# 22
# sec = int(input('kun boshidan necha sekund otdi: '))
# s = sec // 3600
# qol_ = sec % 3600
# print(f'kun boshdan {s} soat, {qol_} sec otdi')

# 23
# sec = int(input('kun boshdan necha sekund otdi: '))
# s = sec // 3600
# min_ = (sec % 3600) // 60
# new_sec = sec % 60
# print(f'kun boshdan {s} soat, {min_} minut, {new_sec} sec otdi')

# 24
# K = int(input('1-365 gacha son: '))
#
# week_day = (K) % 7
#
# week_days = ('Yakshamba', 'Dushamba', 'Seshamba', 'Chorshamba', 'Payshamba', 'Juma', 'Shamba')
#
# print(f'{K}-kun {week_days[week_day]} ga togri keladi')

# 25

# K = int(input('1-365 gacha son: '))
#
# week_day = (K - 4) % 7
#
# week_days = ('Yakshamba', 'Dushamba', 'Seshamba', 'Chorshamba', 'Payshamba', 'Juma', 'Shamba')
#
# print(f'{K}-kun {week_days[week_day]} ga togri keladi')

# 26
#
# K = int(input('1-365 gacha son: '))
#
# week_day = (K) % 7
#
# week_days = ('Dushamba', 'Seshamba', 'Chorshamba', 'Payshamba', 'Juma', 'Shamba', 'Yakshamba',)
#
# print(f'{K}-kun {week_days[week_day]} ga togri keladi')

# 27

# K = int(input('1-365 gacha son: '))
#
# week_day = (K - 2) % 7
#
# week_days = ('Dushamba', 'Seshamba', 'Chorshamba', 'Payshamba', 'Juma', 'Shamba', 'Yakshamba',)
#
# print(f'{K}-kun {week_days[week_day]} ga togri keladi')

# 28
# N = int(input('yanvar birinchi kuni qaysi haftadan boshlanadi sonda(1-7): '))
# K = int(input('1-365 gacha son: '))
#
# week_day = ((K - 1) + (N - 1)) % 7 + 1
#
# week_days = ('Dushamba', 'Seshamba', 'Chorshamba', 'Payshamba', 'Juma', 'Shamba', 'Yakshamba',)
#
# print(f'{K}-kun {week_days[week_day - 1]} ga togri keladi')

# 29
#
# def kv(A, B, C):
#     if A < C or B < C:
#         print("bunaqa razmerli kvadrat bu togri tortburchakka sigmidi")
#         return
#
#     sum_kv = (A // C) * (B // C)
#
#     kv_ = A * B - sum_kv * C * C
#
#     # Выводим результат
#     print(f"kvadratlan soni: {sum_kv}")
#     print(f"joylashmay qolgan qismi: {kv_}")
#
# # Пример использования
# A = int(input("A tomoni togri torburchak: "))
# B = int(input("B tomoni togri torburchak: "))
# C = int(input("C tomoni kvadrat: "))
#
# kv(A, B, C)

# 30
#
# def determine_year(year):
#     century = (year - 1) // 100 + 1
#     return century
#
#
# # Пример использования
# year = int(input("Введите год: "))
# century = determine_year(year)
# print(f"{year} год входит в {century} столетие.")
