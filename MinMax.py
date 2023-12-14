# 1
# nums = input("Sonlar to'plamini kiriting (bo'sh joy bilan ajrating): ")
# nums = nums.split()
#
# my_num = [int(num) for num in nums]
#
# if len(my_num) == 0:
#     print("To'plam bo'sh.")
# else:
#     max_num = min_num = my_num[0]
#
#     for i in my_num:
#         if i > max_num:
#             max_num = i
#         elif i < min_num:
#             min_num = i
#
#     print(f"Eng katta son: {max_num}")
#     print(f"Eng kichik son: {min_num}")

# 2
# n = int(input("n ni kiriting: "))
#
# eng_kichik_yuzasi = float('inf')
#
# for i in range(n):
#     a = int(input(f"{i + 1}-tortburchakning tomonini kiriting (a): "))
#     b = int(input(f"{i + 1}-tortburchakning boshqa tomonini kiriting (b): "))
#
#     yuzasi = a * b
#
#     if yuzasi < eng_kichik_yuzasi:
#         eng_kichik_yuzasi = yuzasi
#
# if eng_kichik_yuzasi != float('inf'):
#     print(f"Eng kichik yuzali to'rtburchakning yuzasi: {eng_kichik_yuzasi}")
# else:
#     print("To'plam bo'sh.")

# 3
# n = int(input("n ni kiriting: "))
#
# eng_katta_perimetr = 0
#
# for i in range(n):
#     a = int(input(f"{i + 1}-tortburchakning tomonini kiriting (a): "))
#     b = int(input(f"{i + 1}-tortburchakning boshqa tomonini kiriting (b): "))
#
#     perimetr = 2 * (a + b)
#
#     if perimetr > eng_katta_perimetr:
#         eng_katta_perimetr = perimetr
#
# if eng_katta_perimetr != 0:
#     print(f"Eng katta perimetrga ega bo'lgan to'rtburchakning perimetri: {eng_katta_perimetr}")
# else:
#     print("To'plam bo'sh.")

# 4
# n = int(input("n ni kiriting: "))
#
# eng_kichik = float('inf')
# eng_kichik_orni = None
#
# for i in range(n):
#     son = int(input(f"{i + 1}-sonni kiriting: "))
#
#     if son < eng_kichik:
#         eng_kichik = son
#         eng_kichik_orni = i + 1
#
# if eng_kichik_orni is not None:
#     print(f"Eng kichik element: {eng_kichik}")
#     print(f"Eng kichik elementning o'rnini: {eng_kichik_orni}")
# else:
#     print("To'plam bo'sh.")

# 5
# n = int(input("n ni kiriting: "))
#
# eng_katta_zichlik = 0
# eng_katta_zichlik_indeksi = None
#
# for i in range(n):
#     m = int(input(f"{i+1}-elementning og'irlikni kiriting (m): "))
#     v = int(input(f"{i+1}-elementning hajmini kiriting (v): "))
#
#     zichlik = m / v
#
#     if zichlik > eng_katta_zichlik:
#         eng_katta_zichlik = zichlik
#         eng_katta_zichlik_indeksi = i + 1
#
# if eng_katta_zichlik_indeksi is not None:
#     print(f"Eng katta zichlik: {eng_katta_zichlik}")
#     print(f"Eng katta zichlikning indeksi: {eng_katta_zichlik_indeksi}")
# else:
#     print("To'plam bo'sh.")

# 6
# N = int(input("N ni kiriting: "))
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     eng_kichik, eng_katta = birinchi, birinchi
#     tartib_raqami_kichik, tartib_raqami_katta = 1, 1
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element < eng_kichik:
#             eng_kichik = element
#             tartib_raqami_kichik = i
#         elif element >= eng_katta:
#             eng_katta = element
#             tartib_raqami_katta = i
#
#     print(f"Birinchi uchragan eng kichik element tartib raqami: {tartib_raqami_kichik}")
#     print(f"Ohirgi uchragan eng katta element tartib raqami: {tartib_raqami_katta}")
# else:
#     print("To'plam bo'sh.")

# 7
# N = int(input("N ni kiriting: "))
#
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     eng_kichik, eng_katta = birinchi, birinchi
#     tartib_raqami_kichik, tartib_raqami_katta = 1, 1
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element > eng_katta:
#             eng_katta = element
#             tartib_raqami_katta = i
#         elif element < eng_kichik:
#             eng_kichik = element
#             tartib_raqami_kichik = i
#
#     print(f"birinchi uchragan eng katta element {tartib_raqami_katta}")
#     print(f"birinchi uchragan eng kichik element {tartib_raqami_kichik}")

# 8
# N = int(input("N ni kiriting: "))
#
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     eng_kichik, eng_kichik_tartib_raqam = birinchi, 1
#     oxirgi = birinchi
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element < eng_kichik:
#             eng_kichik = element
#             eng_kichik_tartib_raqam = i
#
#         oxirgi = element
#
#     print(f"Birinchi uchragan eng kichik element tartib raqami: {eng_kichik_tartib_raqam}")
#     print(f"Oxirgi uchragan eng kichik element tartib raqami: {N}")
# else:
#     print("To'plam bo'sh.")

# 9
# N = int(input("N ni kiriting: "))
#
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     eng_katta, eng_katta_tartib_raqam = birinchi, 1
#     oxirgi = birinchi
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element > eng_katta:
#             eng_katta = element
#             eng_katta_tartib_raqam = i
#
#         oxirgi = element
#
#     print(f"Birinchi uchragan eng katta element tartib raqami: {eng_katta_tartib_raqam}")
#     print(f"Oxirgi uchragan eng katta element tartib raqami: {N}")
# else:
#     print("To'plam bo'sh.")

# 10
# N = int(input("N ni kiriting: "))
#
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     tartib_raqam = 1
#     ekstremal = birinchi
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element > ekstremal or element < ekstremal:
#             ekstremal = element
#             tartib_raqam = i
#
#     print(f"Birinchi uchragan ekstremal element tartib raqami: {tartib_raqam}")
# else:
#     print("To'plam bo'sh.")

# 11
# N = int(input("N ni kiriting: "))
#
# if N > 0:
#     birinchi = int(input("1-elementni kiriting: "))
#     tartib_raqam = 1
#     ekstremal = birinchi
#
#     for i in range(2, N + 1):
#         element = int(input(f"{i}-elementni kiriting: "))
#
#         if element >= ekstremal or element <= ekstremal:
#             ekstremal = element
#             tartib_raqam = i
#
#     print(f"Oxirgi uchragan ekstremal element tartib raqami: {tartib_raqam}")
# else:
#     print("To'plam bo'sh.")

# 12
# N = int(input("N ni kiriting: "))
#
# eng_kichik_musbat = float('inf')
# tartib_raqami = None
#
# for i in range(1, N + 1):
#     son = int(input(f"{i}-elementni kiriting: "))
#     if son > 0 and son < eng_kichik_musbat:
#         eng_kichik_musbat = son
#         tartib_raqami = i
#
# if tartib_raqami is not None:
#     print(f"Eng kichik musbat sonning tartib raqami: {tartib_raqami}")
# else:
#     print("Musbat son topilmadi yoki to'plam bo'sh.")

# 13
# N = int(input("N ni kiriting: "))
#
# eng_kichik_musbat = float('inf')
#
# for i in range(1, N + 1):
#     son = int(input(f"{i}-elementni kiriting: "))
#     if son > 0 and son < eng_kichik_musbat:
#         eng_kichik_musbat = son
#
# if eng_kichik_musbat != float('inf'):
#     print(f"Eng kichik musbat son: {eng_kichik_musbat}")
# else:
#     print("Musbat son topilmadi yoki to'plam bo'sh.")

# 14
# B = int(input("B ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-sonni kiriting: ")) for i in range(10)]
#
# eng_kichik_tartib_raqam = None
# for i, son in enumerate(toplam):
#     if son > B:
#         if eng_kichik_tartib_raqam is None or son < toplam[eng_kichik_tartib_raqam]:
#             eng_kichik_tartib_raqam = i
#
# if eng_kichik_tartib_raqam is not None:
#     print(f"B sonidan katta bo'lgan, eng kichik elementning tartib raqami: {eng_kichik_tartib_raqam + 1}")
# else:
#     print("Berilgan to'plamda B sonidan katta son topilmadi: 0 0")

# 15
# B = int(input("B ni kiriting: "))
# C = int(input("C ni kiriting (C > B): "))
#
# toplam = [int(input(f"{i + 1}-sonni kiriting: ")) for i in range(10)]
#
# eng_katta_tartib_raqam = None
# for i, son in enumerate(toplam):
#     if B < son < C:
#         if eng_katta_tartib_raqam is None or son > toplam[eng_katta_tartib_raqam]:
#             eng_katta_tartib_raqam = i
#
# if eng_katta_tartib_raqam is not None:
#     print(f"(B, C) oraliqdagi eng katta elementning tartib raqami: {eng_katta_tartib_raqam + 1}")
# else:
#     print("(B, C) oraliqda son topilmadi: 0 0")

# 16
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# eng_kichik = float('inf')
# birinchi_uchragan = 0
#
# for i, son in enumerate(toplam):
#     if son < eng_kichik:
#         eng_kichik = son
#         birinchi_uchragan = i + 1
#
# print(f"Birinchi uchragan eng kichik elementgacha bo'lgan elementlar soni: {birinchi_uchragan}")

# 17
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# eng_katta = float('-inf')
# oxirgi_uchragan_turuvchi = 0
#
# for i in range(N - 1, 0, -1):
#     if toplam[i] > eng_katta:
#         eng_katta = toplam[i]
#         oxirgi_uchragan_turuvchi = i + 1
#
# print(f"Oxirgi uchragan eng katta elementdan keyin turgan elementlar soni: {oxirgi_uchragan_turuvchi}")

# 18
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N > 1:
#     birinchi_uchragan = toplam[0]
#     oxirgi_uchragan = toplam[N - 1]
#
#     if birinchi_uchragan > oxirgi_uchragan:
#         eng_katta = birinchi_uchragan
#         eng_katta_tartib_raqam = 1
#     else:
#         eng_katta = oxirgi_uchragan
#         eng_katta_tartib_raqam = N
#
#     for i in range(1, N - 1):
#         if toplam[i] > eng_katta:
#             eng_katta = toplam[i]
#             eng_katta_tartib_raqam = i + 1
#
#     print(f"Birinchi va oxirgi uchragan eng katta element orasida turgan elementlar soni: {eng_katta_tartib_raqam}")
# else:
#     print("To'plamda faqat bitta element mavjud: 0")

# 19
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N > 0:
#     eng_kichik = min(toplam)
#     eng_kichik_tartib_raqam = toplam.index(eng_kichik) + 1
#
#     print(f"To'plamdagi eng kichik element tartib raqami: {eng_kichik_tartib_raqam}")
# else:
#     print("To'plam bo'sh.")

# 20
# N = int(input("N ni kiriting: "))
#
# # To'plamni olish
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N > 1:
#     eng_kichik = float('inf')
#     eng_katta = float('-inf')
#     eng_kichik_tartib_raqam = None
#     eng_katta_tartib_raqam = None
#
#     for i in range(N):
#         if toplam[i] < eng_kichik:
#             eng_kichik = toplam[i]
#             eng_kichik_tartib_raqam = i + 1
#
#         if toplam[i] > eng_katta:
#             eng_katta = toplam[i]
#             eng_katta_tartib_raqam = i + 1
#
#     print(f"To'plamdagi eng kichik element tartib raqami: {eng_kichik_tartib_raqam}")
#     print(f"To'plamdagi eng katta element tartib raqami: {eng_katta_tartib_raqam}")
# else:
#     print("To'plamda faqat bitta element mavjud: 0 0")

# 21
# N = int(input("N ni kiriting (N > 2): "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# eng_katta = max(toplam)
# eng_kichik = min(toplam)
# toplam.remove(eng_katta)
# toplam.remove(eng_kichik)
#
# ortacha_qiymat = sum(to'plam) / len(toplam)
#
# print(f"To'plamning ortacha qiymati: {ortacha_qiymat}")

# 22
# N = int(input("N ni kiriting (N > 2): "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N >= 2:
#     eng_kichik1 = min(toplam)
#     toplam.remove(eng_kichik1)
#     eng_kichik2 = min(toplam)
#
#     print(f"To'plamdagi eng kichik 2 ta qiymat: {eng_kichik1} {eng_kichik2}")
# else:
#     print("N soni 2 dan kichik bo'lishi kerak.")

# 23
# N = int(input("N ni kiriting (N > 3): "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N >= 3:
#     eng_katta1 = max(toplam)
#     toplam.remove(eng_katta1)
#     eng_katta2 = max(toplam)
#     toplam.remove(eng_katta2)
#     eng_katta3 = max(toplam)
#
#     print(f"To'plamdagi eng katta 3 ta qiymat: {eng_katta1} {eng_katta2} {eng_katta3}")
# else:
#     print("N soni 3 dan kichik bo'lishi kerak.")

# 24
# N = int(input("N ni kiriting (N > 1): "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N > 1:
#     eng_katta_yigindi = float('-inf')
#
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             yigindi = toplam[i] + toplam[j]
#             if yigindi > eng_katta_yigindi:
#                 eng_katta_yigindi = yigindi
#
#     print(f"Ikkita qo'shni son yigindisining eng katta qiymati: {eng_katta_yigindi}")
# else:
#     print("N soni 1 dan katta bo'lishi kerak.")

# 25
# N = int(input("N ni kiriting (N > 1): "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# if N > 1:
#     eng_kichik_kopaytma = float('inf')
#     eng_kichik_indekslar = None
#
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             kopaytma = toplam[i] * toplam[j]
#             if kopaytma < eng_kichik_kopaytma:
#                 eng_kichik_kopaytma = kopaytma
#                 eng_kichik_indekslar = (i + 1, j + 1)
#
#     print(f"Ko'paytmasi eng kichik bo'ladigan ikkita qo'shni element indekslari: {eng_kichik_indekslar}")
# else:
#     print("N soni 1 dan katta bo'lishi kerak.")

# 26
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# maksimal_son = float('-inf')
# juft_son_topilmadi = True
#
# for i in range(N - 1):
#     if toplam[i] % 2 == 0 and toplam[i + 1] % 2 == 0:
#         juft_son_topilmadi = False
#         maksimal_son = max(maksimal_son, toplam[i], toplam[i + 1])
#
# if juft_son_topilmadi:
#     print(0)
# else:
#     print(f"Ketma-ket kelaigan juft elementlar maksimal soni: {maksimal_son}")

# 27
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# max_ketma_ket_oraliq_boshlangan_indeks = 0
# max_ketma_ket_oraliq_uzunlik = 1
# current_ketma_ket_oraliq_boshlangan_indeks = 0
# current_ketma_ket_oraliq_uzunlik = 1
#
# for i in range(1, N):
#     if toplam[i] == toplam[i - 1]:
#         current_ketma_ket_oraliq_uzunlik += 1
#     else:
#         current_ketma_ket_oraliq_boshlangan_indeks = i
#         current_ketma_ket_oraliq_uzunlik = 1
#
#     if current_ketma_ket_oraliq_uzunlik > max_ketma_ket_oraliq_uzunlik:
#         max_ketma_ket_oraliq_boshlangan_indeks = current_ketma_ket_oraliq_boshlangan_indeks
#         max_ketma_ket_oraliq_uzunlik = current_ketma_ket_oraliq_uzunlik
#
# if max_ketma_ket_oraliq_uzunlik > 1:
#     max_ketma_ket_oraliq_son = toplam[max_ketma_ket_oraliq_boshlangan_indeks]
#     print(f"Bir xil sonlar ketma-ketligi eng uzun bo'ladigan oraliq boshlangan element indeksi: {max_ketma_ket_oraliq_boshlangan_indeks + 1}")
#     print(f"Bir xil sonlar ketma-ketligidagi elementlar soni: {max_ketma_ket_oraliq_son}")
# else:
#     print("Bir xil sonlar ketma-ketligi topilmadi.")

# 28
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# max_ketma_ket_oraliq_boshlangan_indeks = 0
# max_ketma_ket_oraliq_uzunlik = 1
# current_ketma_ket_oraliq_boshlangan_indeks = 0
# current_ketma_ket_oraliq_uzunlik = 1
#
# for i in range(1, N):
#     if toplam[i] == toplam[i - 1]:
#         current_ketma_ket_oraliq_uzunlik += 1
#     else:
#         current_ketma_ket_oraliq_boshlangan_indeks = i
#         current_ketma_ket_oraliq_uzunlik = 1
#
#     if current_ketma_ket_oraliq_uzunlik > max_ketma_ket_oraliq_uzunlik:
#         max_ketma_ket_oraliq_boshlangan_indeks = current_ketma_ket_oraliq_boshlangan_indeks
#         max_ketma_ket_oraliq_uzunlik = current_ketma_ket_oraliq_uzunlik
#
# if max_ketma_ket_oraliq_uzunlik > 1:
#     max_ketma_ket_oraliq_son = toplam[max_ketma_ket_oraliq_boshlangan_indeks]
#     print(f"Bir sonni ketma-ketligi eng uzun bo'ladigan oraliq boshlangan element indeksi: {max_ketma_ket_oraliq_boshlangan_indeks + 1}")
#     print(f"Bir sonni ketma-ketligidagi elementlar soni: {max_ketma_ket_oraliq_son}")
# else:
#     print(0)

# 29
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# maksimal_son = float('-inf')
# juft_son_topilmadi = True
#
# for i in range(N - 1):
#     if toplam[i] % 2 == 0 and toplam[i + 1] % 2 == 0:
#         juft_son_topilmadi = False
#         kichik_son = min(toplam[i], toplam[i + 1])
#         maksimal_son = max(maksimal_son, kichik_son)
#
# if juft_son_topilmadi:
#     print(0)
# else:
#     print(f"Ketma-ket keladigan eng kichik elementlarning maksimal soni: {maksimal_son}")
#

# 30
# N = int(input("N ni kiriting: "))
#
# toplam = [int(input(f"{i + 1}-elementni kiriting: ")) for i in range(N)]
#
# minimal_son = float('inf')
# juft_son_topilmadi = True
#
# for i in range(N - 1):
#     if toplam[i] % 2 == 0 and toplam[i + 1] % 2 == 0:
#         juft_son_topilmadi = False
#         katta_son = max(toplam[i], toplam[i + 1])
#         minimal_son = min(minimal_son, katta_son)
#
# if juft_son_topilmadi:
#     print(0)
# else:
#     print(f"Ketma-ket keladigan eng katta elementlarning minimal soni: {minimal_son}")
