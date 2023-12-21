# 1
# n = int(input("n ni kiriting: "))
#
# massiv = [2 * i + 1 for i in range(n)]
#
# print("Massiv:", massiv)
#
# 2
# n = int(input("n ni kiriting: "))
#
# massiv = [2 ** i for i in range(n)]
#
# print("Massiv:", massiv)
#
# 3
# n = int(input("n ni kiriting: "))
# A = int(input("A ni kiriting: "))
# D = int(input("D ni kiriting: "))
#
# massiv = [A + i * D for i in range(n)]
#
# print("Massiv:", massiv)
#
# 4
# n = int(input("Natural son kiriting: "))
# A = int(input("Dastlabki hadni kiriting: "))
# D = int(input("O'sishini kiriting: "))
#
# # Massivni hosil qilish
# massiv = [A * D ** i for i in range(n)]
#
# # Massivni chiqarish
# print("Massiv:", massiv)
#
#
# 5
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib
#
#
# n = int(input("Natural son kiriting: "))
#
# # Massivni hosil qilish
# massiv = fibonacci(n)
#
# # Massivni chiqarish
# print("Massiv:", massiv)
#
#
# 6
# def generate_sequence(n, A, B):
#     sequence = [A, B]
#     for i in range(2, n):
#         sequence.append(sum(sequence[:i]))
#     return sequence
#
#
# n = int(input("Natural son kiriting (n > 2): "))
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
#
# # Massivni hosil qilish
# massiv = generate_sequence(n, A, B)
#
# # Massivni chiqarish
# print("Massiv:", massiv)
#
#
# 7
# def teskari_tartibda_chiqarish(massiv):
#     reversed_massiv = massiv[::-1]
#     print("Massiv teskari tartibda:", reversed_massiv)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Massivni teskari tartibda chiqarish
# teskari_tartibda_chiqarish(massiv)
#
#
# # 8
# def toqlar_va_ularning_indekslari(massiv):
#     toqlar = [element for element in massiv if element % 2 != 0]
#     toqlar_indekslari = [i for i, element in enumerate(massiv) if element % 2 != 0]
#
#     print("Toqlar: ", toqlar)
#     print("Toqlar indekslari: ", toqlar_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Toqlar va ularning indekslarini chiqarish
# toqlar_va_ularning_indekslari(massiv)
#
#
# # 9
# def juftlar_va_ularning_indekslari(massiv):
#     juftlar = [element for element in massiv if element % 2 == 0]
#     juftlar_indekslari = sorted([i for i, element in enumerate(massiv) if element % 2 == 0])
#
#     print("Juftlar: ", juftlar)
#     print("Juftlar indekslari (kamayish tartibida): ", juftlar_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Juftlar va ularning indekslarini chiqarish
# juftlar_va_ularning_indekslari(massiv)
#
#
# # 10
#
# def juftlar_va_ularning_indekslari(massiv):
#     juftlar = [element for element in massiv if element % 2 == 0]
#     juftlar_indekslari = sorted([i for i, element in enumerate(massiv) if element % 2 == 0])
#
#     print("Juftlar: ", juftlar)
#     print("Juftlar indekslari (o'sish tartibida): ", juftlar_indekslari)
#
#
# def toqlar_va_ularning_indekslari(massiv):
#     toqlar = [element for element in massiv if element % 2 != 0]
#     toqlar_indekslari = sorted([i for i, element in enumerate(massiv) if element % 2 != 0], reverse=True)
#
#     print("Toqlar: ", toqlar)
#     print("Toqlar indekslari (kamayish tartibida): ", toqlar_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Juftlar va ularning indekslarini chiqarish
# juftlar_va_ularning_indekslari(massiv)
#
# # Toqlar va ularning indekslarini chiqarish
# toqlar_va_ularning_indekslari(massiv)
#
#
# # 11
#
# def karralilar(massiv, k):
#     karralilar_indekslari = [i for i, element in enumerate(massiv) if i % k == 0]
#     karralilar_sonlari = [massiv[i] for i in karralilar_indekslari]
#
#     print(f"Massivdagi {k}-ga karrali elementlar: ", karralilar_sonlari)
#     print(f"Ularning indekslari: ", karralilar_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # K ni olish
# k = int(input("K ni kiriting (1 dan kichik, n dan katta): "))
#
# # Karralilar va ularning indekslarini chiqarish
# karralilar(massiv, k)
#
#
# # 12
#
# def juft_sonlar(massiv):
#     juftlar = [element for element in massiv if element % 2 == 0]
#     juft_sonlar_soni = len(juftlar)
#     juft_sonlar_yigindisi = sum(juftlar)
#     eng_katta_juft_son = max(juftlar)
#     orta_qiymat = sum(juftlar) / juft_sonlar_soni
#     teskari_indekslar = list(range(len(massiv) - 1, -1, -2))
#
#     print("Massivdagi juft sonlar miqdori:", juft_sonlar_soni)
#     print("Massivdagi juft sonlarining yigindisi:", juft_sonlar_yigindisi)
#     print("Massivdagi eng katta juft son:", eng_katta_juft_son)
#     print("Massivdagi juft sonlarining orta qiymati:", orta_qiymat)
#     print("Massivdagi juft sonlarining teskari tartibdagi indekslari:", teskari_indekslar)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting (n juft son bolishi kerak): "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Juft sonlar bilan bog'liq ma'lumotlarni chiqarish
# juft_sonlar(massiv)
#
#
# # 13
#
# def toq_sonlar(massiv):
#     toqlar = [element for element in massiv if element % 2 != 0]
#     toq_sonlar_soni = len(toqlar)
#     toq_sonlar_yigindisi = sum(toqlar)
#     eng_katta_toq_son = max(toqlar)
#     orta_qiymat = sum(toqlar) / toq_sonlar_soni
#     teskari_indekslar = list(range(len(massiv) - 1, -1, -2))
#
#     print("Massivdagi toq sonlar miqdori:", toq_sonlar_soni)
#     print("Massivdagi toq sonlarining yigindisi:", toq_sonlar_yigindisi)
#     print("Massivdagi eng katta toq son:", eng_katta_toq_son)
#     print("Massivdagi toq sonlarining orta qiymati:", orta_qiymat)
#     print("Massivdagi toq sonlarining teskari tartibdagi indekslari:", teskari_indekslar)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting (n toq son bolishi kerak): "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Toq sonlar bilan bog'liq ma'lumotlarni chiqarish
# toq_sonlar(massiv)
#
#
# # 14
#
# def juft_va_toq_indekslari(massiv):
#     juft_indekslari = [i for i in range(len(massiv)) if i % 2 == 0]
#     toq_indekslari = [i for i in range(len(massiv)) if i % 2 != 0]
#
#     print("Massivdagi juft indekslilar:", juft_indekslari)
#     print("Massivdagi toq indekslilar:", toq_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Juft va toq indekslilarini chiqarish
# juft_va_toq_indekslari(massiv)
#
#
# # 15
#
#
# def juft_va_toq_indekslari(massiv):
#     juft_indekslari = [i for i in range(len(massiv)) if i % 2 == 0]
#     toq_indekslari = [i for i in range(len(massiv)) if i % 2 != 0]
#
#     print("Massivdagi juft indekslilar:", juft_indekslari)
#     print("Massivdagi toq indekslilar:", toq_indekslari)
#
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# massiv = []
#
# for i in range(n):
#     element = int(input(f"{i + 1}-elementni kiriting: "))
#     massiv.append(element)
#
# # Juft va toq indekslilarini chiqarish
# juft_va_toq_indekslari(massiv)
#
#
# # 16
#
# def massiv_tuzish(n):
#     massiv = list(range(1, n + 1))
#     print(f"{n} ta elementdan tashkil topgan massiv: {massiv}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# massiv_tuzish(n)
#
#
# # 17
#
# def massiv_chiqarish(n):
#     massiv = list(range(1, n + 1))
#     print(f"Massiv elementlari: {massiv}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# massiv_chiqarish(n)
#
#
# # 18
#
# def massiv_tahlili(massiv):
#     if len(massiv) < 2:
#         print(0)
#     else:
#         massiv.sort()
#         birinchi_kichik = massiv[1]
#         print(birinchi_kichik)
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     massiv_tahlili(massiv)
#
#
# # 19
#
# def indeksni_chiqar(massiv):
#     if len(massiv) < 2:
#         print(0)
#     else:
#         eng_katta = max(massiv[0], massiv[-1])
#         eng_kichik = min(massiv[0], massiv[-1])
#
#         eng_katta_indeks = massiv.index(eng_katta)
#         eng_kichik_indeks = massiv.index(eng_kichik)
#
#         print(f"Eng katta elementning indeksi: {eng_katta_indeks}")
#         print(f"Eng kichik elementning indeksi: {eng_kichik_indeks}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     indeksni_chiqar(massiv)
#
#
# #    20
#
# def yigindini_chiqar(massiv, k, l):
#     if 0 <= k <= l < len(massiv):
#         yigindi = sum(massiv[k:l + 1])
#         print(f"Indekslar {k} va {l} orasidagi elementlar yig'indisi: {yigindi}")
#     else:
#         print("Noto'g'ri indekslar kiritildi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     k = int(input("k ni kiriting (0 <= k <= l < n): "))
#     l = int(input("l ni kiriting (0 <= k <= l < n): "))
#
#     yigindini_chiqar(massiv, k, l)
#
#
# # 21
#
# def yigindini_chiqar(massiv, k, l):
#     if 0 <= k <= l < len(massiv):
#         yigindi = sum(massiv[k:l + 1])
#         print(f"Indekslar {k} va {l} orasidagi elementlar yig'indisi: {yigindi}")
#     else:
#         print("Noto'g'ri indekslar kiritildi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     k = int(input("k ni kiriting (0 <= k <= l < n): "))
#     l = int(input("l ni kiriting (0 <= k <= l < n): "))
#
#     yigindini_chiqar(massiv, k, l)
#
#
# # 22
#
# def tashqari_yigindini_chiqar(massiv, K, L):
#     if 0 <= K <= L < len(massiv):
#         tashqari_yigindi = sum(massiv[:K] + massiv[L + 1:])
#         print(f"Indekslar {K} va {L} orasidagi elementlar tashqarisidagi yig'indi: {tashqari_yigindi}")
#     else:
#         print("Noto'g'ri indekslar kiritildi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     K = int(input("K ni kiriting (0 <= K <= L < N): "))
#     L = int(input("L ni kiriting (0 <= K <= L < N): "))
#
#     tashqari_yigindini_chiqar(massiv, K, L)
#
#
# # 24
#
# def arifmetik_progressiya_mi(massiv):
#     n = len(massiv)
#
#     if n <= 2:
#         print(0)  # Massivda kamida uchta element bo'lishi kerak
#         return
#
#     d = massiv[1] - massiv[0]  # Arifmetik progressiya oraliq
#     for i in range(2, n):
#         if massiv[i] - massiv[i - 1] != d:
#             print(0)  # Massiv arifmetik progressiya emas
#             return
#
#     print(d)  # Massiv arifmetik progressiya, ayirmani chiqaramiz
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     arifmetik_progressiya_mi(massiv)
#
#
# # 25
#
# def geometrik_progressiya_mi(massiv):
#     n = len(massiv)
#
#     if n <= 2:
#         print(n)  # Massivda kamida uchta element bo'lishi kerak
#         return
#
#     r = massiv[1] / massiv[0]  # Geometrik progressiya o'rni
#     for i in range(2, n):
#         if massiv[i] / massiv[i - 1] != r:
#             print(n)  # Massiv geometrik progressiya emas, maxrajni chiqaramiz
#             return
#
#     maxraj = massiv[-1] * (r ** (n - 1))
#     print(maxraj)  # Massiv geometrik progressiya, maxrajni chiqaramiz
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     geometrik_progressiya_mi(massiv)
#
#
# # 26
#
#
# def ketma_ketlik_tekshir(massiv):
#     n = len(massiv)
#
#     for i in range(1, n - 1):
#         if (massiv[i - 1] % 2 == 0 and massiv[i] % 2 == 0) or (massiv[i - 1] % 2 == 1 and massiv[i] % 2 == 1):
#             print(0)  # Ketma-ketlik bajarilgan
#             return
#
#     print(i)  # Ketma-ketlikni buzgan birinchi elementning indeksi
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     ketma_ketlik_tekshir(massiv)
#
#
# # 27
#
# def ketma_ketlik_tekshir(massiv):
#     n = len(massiv)
#
#     for i in range(1, n - 1):
#         if (massiv[i - 1] > 0 and massiv[i] > 0) or (massiv[i - 1] < 0 and massiv[i] < 0):
#             print(0)  # Ketma-ketlik bajarilgan
#             return
#
#     print(i)  # Ketma-ketlikni buzgan birinchi elementning indeksi
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     ketma_ketlik_tekshir(massiv)
#
#
# # 28
#
#
# def kichigini_aniqlovchi(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     kichig = float('inf')  # Boshlang'ich qiymat kichik deb tanlanadi
#
#     for i in range(0, n, 2):  # Juft indeksli elementlarni tekshiramiz
#         if massiv[i] < kichig:
#             kichig = massiv[i]
#
#     if kichig == float('inf'):
#         print("Juft indeksli elementlar topilmadi.")
#     else:
#         print(f"Juft indeksli elementlari orasidan kichigi: {kichig}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     kichigini_aniqlovchi(massiv)
#
#
# # 29
#
# def kattasini_aniqlovchi(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     katta = float('-inf')  # Boshlang'ich qiymat katta deb tanlanadi
#
#     for i in range(1, n, 2):  # Toq indeksli elementlarni tekshiramiz
#         if massiv[i] > katta:
#             katta = massiv[i]
#
#     if katta == float('-inf'):
#         print("Toq indeksli elementlar topilmadi.")
#     else:
#         print(f"Toq indeksli elementlari orasidan kattasi: {katta}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     kattasini_aniqlovchi(massiv)
#
#
# # 30
#
# def ong_qoshinisi_aniqla(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     katta_element_indeksi = 0
#     katta_element_qiymati = massiv[0]
#
#     for i in range(1, n):
#         if massiv[i] > katta_element_qiymati:
#             katta_element_qiymati = massiv[i]
#             katta_element_indeksi = i
#
#     print(f"O'ng qo'shinisidan katta elementning indeksi: {katta_element_indeksi}")
#     print(f"O'ng qo'shinisidan katta element qiymati: {katta_element_qiymati}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     ong_qoshinisi_aniqla(massiv)
#
#
# # 31
#
# def chap_qoshinisi_aniqla(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     katta_element_indekslar = []
#     katta_element_qiymati = massiv[0]
#
#     for i in range(1, n):
#         if massiv[i] > katta_element_qiymati:
#             katta_element_qiymati = massiv[i]
#             katta_element_indekslar = [i]
#         elif massiv[i] == katta_element_qiymati:
#             katta_element_indekslar.append(i)
#
#     if not katta_element_indekslar:
#         print("Chap qo'shinisidan katta element topilmadi.")
#     else:
#         print(f"Chap qo'shinisidan katta elementlarining indekslari (kamayish tartibida): {katta_element_indekslar}")
#         print(f"Chap qo'shinisidan katta element qiymati: {katta_element_qiymati}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     chap_qoshinisi_aniqla(massiv)
#
#
# # 32
#
# def lokal_minimum_indeksi(massiv):
#     n = len(massiv)
#
#     if n < 3:
#         print("Massivda kamida uch element bo'lishi kerak.")
#         return
#
#     for i in range(1, n - 1):
#         if massiv[i] < massiv[i - 1] and massiv[i] < massiv[i + 1]:
#             print(f"Birinchi uchragan lokal minimum elementning indeksi: {i}")
#             return
#
#     print("Lokal minimum topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 3:
#     print("Massivda kamida uch element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     lokal_minimum_indeksi(massiv)
#
#
# # 33
#
# def oxirgi_lokal_maksimum_indeksi(massiv):
#     n = len(massiv)
#
#     if n < 3:
#         print("Massivda kamida uch element bo'lishi kerak.")
#         return
#
#     for i in range(n - 2, 0, -1):
#         if massiv[i] > massiv[i - 1] and massiv[i] > massiv[i + 1]:
#             print(f"Oxirgi lokal maksimum elementning indeksi: {i}")
#             return
#
#     print("Lokal maksimum topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 3:
#     print("Massivda kamida uch element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     oxirgi_lokal_maksimum_indeksi(massiv)
#
#
# # 34
# def lokal_minimum_kattasini_aniqla(massiv):
#     n = len(massiv)
#
#     if n < 3:
#         print("Massivda kamida uch element bo'lishi kerak.")
#         return
#
#     katta_element_indeksi = None
#
#     for i in range(1, n - 1):
#         if massiv[i] < massiv[i - 1] and massiv[i] < massiv[i + 1]:
#             if katta_element_indeksi is None or massiv[i] > massiv[katta_element_indeksi]:
#                 katta_element_indeksi = i
#
#     if katta_element_indeksi is not None:
#         print(f"Lokal minimumlari orasidan katta elementning indeksi: {katta_element_indeksi}")
#         print(f"Lokal minimumlari orasidan katta element qiymati: {massiv[katta_element_indeksi]}")
#     else:
#         print("Lokal minimum topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 3:
#     print("Massivda kamida uch element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     lokal_minimum_kattasini_aniqla(massiv)
#
#
# # 35
#
# def lokal_maksimum_kichigini_aniqla(massiv):
#     n = len(massiv)
#
#     if n < 3:
#         print("Massivda kamida uch element bo'lishi kerak.")
#         return
#
#     kichig_element_indeksi = None
#
#     for i in range(1, n - 1):
#         if massiv[i] > massiv[i - 1] and massiv[i] > massiv[i + 1]:
#             if kichig_element_indeksi is None or massiv[i] < massiv[kichig_element_indeksi]:
#                 kichig_element_indeksi = i
#
#     if kichig_element_indeksi is not None:
#         print(f"Lokal maksimumlari orasidan kichigi elementning indeksi: {kichig_element_indeksi}")
#         print(f"Lokal maksimumlari orasidan kichigi element qiymati: {massiv[kichig_element_indeksi]}")
#     else:
#         print("Lokal maksimum topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 3:
#     print("Massivda kamida uch element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     lokal_maksimum_kichigini_aniqla(massiv)
#
#
# # 36
#
# def lokal_minimum_maksimum_bolmagan_kattasini_aniqla(massiv):
#     n = len(massiv)
#
#     if n < 3:
#         print("Massivda kamida uch element bolishi kerak.")
#         return
#
#     katta_element_indeksi = None
#     for i in range(1, n - 1):
#         if (massiv[i] <= massiv[i - 1] and massiv[i] <= massiv[i + 1]) or (
#                 massiv[i] >= massiv[i - 1] and massiv[i] >= massiv[i + 1]):
#             if katta_element_indeksi is None or massiv[i] > massiv[katta_element_indeksi]:
#                 katta_element_indeksi = i
#
#     if katta_element_indeksi is not None:
#         print(f"Lokal minimum yoki maksimum bolmagan elementning indeksi: {katta_element_indeksi}")
#         print(f"Lokal minimum yoki maksimum bolmagan elementning qiymati: {massiv[katta_element_indeksi]}")
#     else:
#         print("Lokal minimum yoki maksimum bolmagan element topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 3:
#     print("Massivda kamida uch element bolishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     lokal_minimum_maksimum_bolmagan_kattasini_aniqla(massiv)
#
#
# # 37
#
# def monoton_osuvchi_oraliqlar_soni(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     monoton_osuvchi_oraliqlar_son = 1
#
#     for i in range(1, n):
#         if massiv[i] > massiv[i - 1]:
#             monoton_osuvchi_oraliqlar_son += 1
#
#     print(f"Massivda monoton o'suvchi oraliqlar soni: {monoton_osuvchi_oraliqlar_son}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     monoton_osuvchi_oraliqlar_soni(massiv)
#
#
# # 38
#
# def monoton_oraliqlar_soni(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     monoton_oraliqlar_son = 1
#
#     for i in range(1, n):
#         if massiv[i] != massiv[i - 1]:
#             monoton_oraliqlar_son += 1
#
#     print(f"Massivda monoton oraliqlar soni: {monoton_oraliqlar_son}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     monoton_oraliqlar_soni(massiv)
#
#
# # 39
#
# def monoton_oraliqlar_soni(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     monoton_oraliqlar_son = 1
#
#     for i in range(1, n):
#         if massiv[i] != massiv[i - 1]:
#             monoton_oraliqlar_son += 1
#
#     print(f"Massivda monoton oraliqlar soni: {monoton_oraliqlar_son}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     monoton_oraliqlar_soni(massiv)
#
#
# # 40
#
# def eng_yaqin_element(massiv, R):
#     n = len(massiv)
#
#     if n == 0:
#         print("Massiv bo'sh.")
#         return
#
#     eng_yaqin = massiv[0]
#
#     for element in massiv:
#         if abs(element - R) < abs(eng_yaqin - R):
#             eng_yaqin = element
#
#     print(f"Massivda {R} soniga eng yaqin element: {eng_yaqin}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# massiv = []
# for i in range(n):
#     element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#     massiv.append(element)
#
# R = int(input("Qidirish uchun R ni kiriting: "))
#
# eng_yaqin_element(massiv, R)
#
#
# # 41
#
# def eng_katta_yigindisi_2_ta_qoshini(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     eng_katta_1, eng_katta_2 = float('-inf'), float('-inf')
#
#     for i in range(n):
#         if massiv[i] > eng_katta_1:
#             eng_katta_2 = eng_katta_1
#             eng_katta_1 = massiv[i]
#         elif massiv[i] > eng_katta_2:
#             eng_katta_2 = massiv[i]
#
#     print(
#         f"Massiv elementlari orasidan yig'indisi eng katta bo'ladigan 2 ta qo'shini elementlar: {eng_katta_1} va {eng_katta_2}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     eng_katta_yigindisi_2_ta_qoshini(massiv)
#
#
# # 42
#
# def eng_yaqin_yigindi_2_qoshini(massiv, R):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     eng_yaqin_1, eng_yaqin_2 = float('inf'), float('inf')
#
#     for i in range(n):
#         if abs(massiv[i] - R) < abs(eng_yaqin_1 - R):
#             eng_yaqin_2 = eng_yaqin_1
#             eng_yaqin_1 = massiv[i]
#         elif abs(massiv[i] - R) < abs(eng_yaqin_2 - R):
#             eng_yaqin_2 = massiv[i]
#
#     print(
#         f"Massiv elementlari orasidan {R} soniga yig'indisi eng yaqin bo'ladigan 2 ta qo'shini elementlar: {eng_yaqin_1} va {eng_yaqin_2}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     R = int(input("Qidirish uchun R ni kiriting: "))
#
#     eng_yaqin_yigindi_2_qoshini(massiv, R)
#
#
# # 43
#
# def tartibla_va_sonlar(massiv):
#     n = len(massiv)
#
#     if n < 1:
#         print("Massivda kamida bir element bo'lishi kerak.")
#         return
#
#     massiv.sort()
#
#     unikal_qiymatlar = []
#     sonlar = []
#
#     current_qiymat = massiv[0]
#     current_son = 1
#
#     for i in range(1, n):
#         if massiv[i] == current_qiymat:
#             current_son += 1
#         else:
#             unikal_qiymatlar.append(current_qiymat)
#             sonlar.append(current_son)
#             current_qiymat = massiv[i]
#             current_son = 1
#
#     unikal_qiymatlar.append(current_qiymat)
#     sonlar.append(current_son)
#
#     for i in range(len(unikal_qiymatlar)):
#         print(f"{unikal_qiymatlar[i]} soni: {sonlar[i]} ta")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 1:
#     print("Massivda kamida bir element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     tartibla_va_sonlar(massiv)
#
#
# # 45
#
# def eng_yaqin_qoshni_indeks(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     eng_yaqin_indekslar = []
#
#     for i in range(1, n):
#         if abs(massiv[i] - massiv[i - 1]) == 1:
#             eng_yaqin_indekslar.append(i - 1)
#             eng_yaqin_indekslar.append(i)
#
#     if eng_yaqin_indekslar:
#         print(f"Bir biriga eng yaqin qo'shnilar indekslari: {eng_yaqin_indekslar}")
#     else:
#         print("Bir biriga eng yaqin qo'shnilar topilmadi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     eng_yaqin_qoshni_indeks(massiv)
#
#
# # 46
#
#
# def eng_yaqin_yigindi_2_element(massiv, R):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     massiv.sort()
#
#     eng_yaqin_1, eng_yaqin_2 = massiv[0], massiv[1]
#
#     for i in range(n - 1):
#         if abs(massiv[i] + massiv[i + 1] - R) < abs(eng_yaqin_1 + eng_yaqin_2 - R):
#             eng_yaqin_1, eng_yaqin_2 = massiv[i], massiv[i + 1]
#
#     print(
#         f"Massiv elementlari orasidan {R} soniga yig'indisi eng yaqin bo'ladigan 2 ta elementlar: {eng_yaqin_1} va {eng_yaqin_2}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     R = int(input("Qidirish uchun R ni kiriting: "))
#
#     eng_yaqin_yigindi_2_element(massiv, R)
#
#
# # 47
#
#
# def eng_yaqin_yigindi_2_element(massiv, R):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     massiv.sort()
#
#     eng_yaqin_1, eng_yaqin_2 = massiv[0], massiv[1]
#
#     for i in range(n - 1):
#         if abs(massiv[i] + massiv[i + 1] - R) < abs(eng_yaqin_1 + eng_yaqin_2 - R):
#             eng_yaqin_1, eng_yaqin_2 = massiv[i], massiv[i + 1]
#
#     print(
#         f"Massiv elementlari orasidan {R} soniga yig'indisi eng yaqin bo'ladigan 2 ta elementlar: {eng_yaqin_1} va {eng_yaqin_2}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     R = int(input("Qidirish uchun R ni kiriting: "))
#
#     eng_yaqin_yigindi_2_element(massiv, R)
#
#
# # 48
#
# def eng_kop_qatnashgan_element_son(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     kop_qatnashgan_element_son = 1
#     jami_kop_qatnashgan_element_son = 1
#
#     for i in range(1, n):
#         if massiv[i] == massiv[i - 1]:
#             kop_qatnashgan_element_son += 1
#         else:
#             kop_qatnashgan_element_son = 1
#
#         if kop_qatnashgan_element_son > jami_kop_qatnashgan_element_son:
#             jami_kop_qatnashgan_element_son = kop_qatnashgan_element_son
#
#     print(f"Massivda eng ko'p qatnashgan bir xil qiymatli element soni: {jami_kop_qatnashgan_element_son}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     eng_kop_qatnashgan_element_son(massiv)
#
#
# # 49
#
# def orin_almashtirilgan_mi(massiv):
#     n = len(massiv)
#
#     for i in range(n):
#         if massiv[i] != i + 1:
#             print(f"Birinchi uchragan nojuz kiritilgan elementning indeksi: {i}")
#             return
#
#     print("1 dan n gacha bo'lgan sonlarning o'rin almashtirilishi mavjud emas, shuning uchun 0 chiqarildi.")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# massiv = []
# for i in range(n):
#     element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#     massiv.append(element)
#
# orin_almashtirilgan_mi(massiv)
#
#
# # 50
#
# def ong_qoshni_katta_son(massiv):
#     n = len(massiv)
#
#     if n < 2:
#         print("Massivda kamida ikkita element bo'lishi kerak.")
#         return
#
#     katta_son = massiv[1]
#
#     for i in range(2, n, 2):
#         if massiv[i] > katta_son:
#             katta_son = massiv[i]
#
#     print(f"Massiv elementlari orasidan o'ng qo'shnisidan katta bo'lgan son: {katta_son}")
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivni nechta elementdan tashkil qilmoqchisiz? "))
# if n < 2:
#     print("Massivda kamida ikkita element bo'lishi kerak.")
# else:
#     massiv = []
#     for i in range(n):
#         element = int(input(f"Massivning {i + 1}-elementini kiriting: "))
#         massiv.append(element)
#
#     ong_qoshni_katta_son(massiv)
#
#
# # 51
#
# def almashtir_va_chiqar(a, b):
#     print("Almashtirilgan massivlar:")
#     print("a:", b)
#     print("b:", a)
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivlar a va b uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# b = []
#
# print("Massiv a uchun elementlarni kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# print("Massiv b uchun elementlarni kiriting:")
# for i in range(n):
#     element = int(input(f"b[{i}]: "))
#     b.append(element)
#
# almashtir_va_chiqar(a, b)
#
#
# # 52
#
# def hosil_qil(a):
#     n = len(a)
#     b = []
#
#     for i in range(n):
#         if a[i] < 5:
#             b.append(2)
#         else:
#             b.append(a[i] / 2)
#
#     return b
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = float(input(f"a[{i}]: "))
#     a.append(element)
#
# b = hosil_qil(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
#
#
# # 53
#
# def hosil_qil(a, b):
#     n = len(a)
#     c = []
#
#     for i in range(n):
#         c.append(a[i] * b[i])
#
#     return c
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massivlar uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# b = []
#
# print("Massiv a elementlarini kiriting:")
# for i in range(n):
#     element = float(input(f"a[{i}]: "))
#     a.append(element)
#
# print("Massiv b elementlarini kiriting:")
# for i in range(n):
#     element = float(input(f"b[{i}]: "))
#     b.append(element)
#
# c = hosil_qil(a, b)
#
# print("C massiv hosil qilindi:")
# print("c:", c)
#
#
# # 54
#
# def hosil_qil_va_chiqar(a):
#     b = [x for x in a if x % 2 == 0]
#     print("B massiv hosil qilindi:")
#     print("b:", b)
#     print("B massiv elementlari soni:", len(b))
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# hosil_qil_va_chiqar(a)
#
#
# # 55
#
# def toq_indekslar(a):
#     n = len(a)
#     i = 1  # toq indekslarni hisoblash uchun boshlang'ich qiymat
#
#     while i < n:
#         print(f"Toq indeks: {i}, Qiymat: {a[i]}")
#         i += 2  # Har ikki qadamda bir toq indeksga o'tamiz
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# toq_indekslar(a)
#
#
# # 56
#
# def hosil_qil_va_chiqar(a):
#     n = len(a)
#     b = [a[i] ** 3 for i in range(2, n, 3)]  # 3 ga karrali indekslardan tashkil topgan b massiv
#
#     print("B massiv hosil qilindi:")
#     print("b:", b)
#     print("B massiv elementlari soni:", len(b))
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# hosil_qil_va_chiqar(a)
#
#
# # 57
#
# def hosil_qil_va_chiqar(a):
#     n = len(a)
#     b = []
#
#     # Juft indeksdagi elementlarni qo'shish
#     for i in range(0, n, 2):
#         b.append(a[i])
#
#     # Toq indeksdagi elementlarni qo'shish
#     for i in range(1, n, 2):
#         b.append(a[i])
#
#     print("B massiv hosil qilindi:")
#     print("b:", b)
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# hosil_qil_va_chiqar(a)
#
#
# # 58
#
# def hosil_qil_a(a):
#     n = len(a)
#     b = []
#
#     for i in range(n):
#         if a[i] < 2:
#             b.append(a[i] * 2)
#         else:
#             b.append(a[i] // 2)
#
#     return b
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = hosil_qil_a(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
#
#
# # 59
#
# def hosil_qil_a(a):
#     n = len(a)
#     b = [sum(a[:i + 1]) / (i + 1) for i in range(n)]
#
#     return b
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = hosil_qil_a(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
#
#
# # 60
#
# def hosil_qil_a(a):
#     n = len(a)
#     b = [sum(a[k:]) for k in range(n)]
#
#     return b
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = hosil_qil_a(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
#
#
# # 61
#
# def hosil_qil_a(a):
#     n = len(a)
#     b = [(sum(a[k:]) / (n - k)) for k in range(n)]
#
#     return b
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = hosil_qil_a(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
#
#
# # 62
#
# def hosil_qil_b_va_c(a):
#     b = [element for element in a if element > 0]  # Musbat elementlardan tashkil topgan b massiv
#     c = [element for element in a if element < 0]  # Manfiy elementlardan tashkil topgan c massiv
#
#     return b, c
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b, c = hosil_qil_b_va_c(a)
#
# print("B massiv hosil qilindi:")
# print("b:", b)
# print("B massiv elementlari soni:", len(b))
#
# print("C massiv hosil qilindi:")
# print("c:", c)
# print("C massiv elementlari soni:", len(c))
#
#
# # 63
#
# def hosil_qil_c(a, b):
#     c = sorted(a + b)
#     return c
#
#
# # Foydalanuvchi kiritadi
# n = 5  # Massivlar uchun sababi 5 ta elementli
# m = 10  # C massivi uchun sababi 10 ta elementli
#
# a = []
# print("Massiv a elementlarini o'sish tartibida kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = []
# print("Massiv b elementlarini o'sish tartibida kiriting:")
# for i in range(n):
#     element = int(input(f"b[{i}]: "))
#     b.append(element)
#
# c = hosil_qil_c(a, b)
#
# print("C massiv hosil qilindi:")
# print("c:", c)
#
#
# # 64
#
# def hosil_qil_c(a, b, c):
#     combined = a + b + c
#     result = sorted(combined)[:10]
#     return result
#
#
# # Foydalanuvchi kiritadi
# n = 10  # Har bir massiv uchun sababi 10 ta elementli
#
# a = []
# print("Massiv a elementlarini o'sish tartibida kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# b = []
# print("Massiv b elementlarini o'sish tartibida kiriting:")
# for i in range(n):
#     element = int(input(f"b[{i}]: "))
#     b.append(element)
#
# c = []
# print("Massiv c elementlarini o'sish tartibida kiriting:")
# for i in range(n):
#     element = int(input(f"c[{i}]: "))
#     c.append(element)
#
# result_c = hosil_qil_c(a, b, c)
#
# print("C massiv hosil qilindi:")
# print("c:", result_c)
#
#
# # 65
#
# def orttirish(a, k):
#     for i in range(len(a)):
#         a[i] += k
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# k = int(input("Qo'shiladigan sonni kiriting: "))
#
# orttirish(a, k)
#
# print("A massiv hosil qilindi:")
# print("a:", a)
#
#
# # 66
#
# def orttirish_juft_songa(a):
#     juft_songlar = [element for element in a if element % 2 == 0]
#
#     if juft_songlar:
#         birinchi_juft_son = juft_songlar[0]
#         index = a.index(birinchi_juft_son)
#
#         a[index] += 2
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# orttirish_juft_songa(a)
#
# print("A massiv hosil qilindi:")
# print("a:", a)
#
#
# # 67
#
# def orttirish_toq_songa(a):
#     toq_songlar = [element for element in a if element % 2 != 0]
#
#     if toq_songlar:
#         oxirgi_toq_son = toq_songlar[-1]
#         index = a.index(oxirgi_toq_son)
#
#         a[index] += 2
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# orttirish_toq_songa(a)
#
# print("A massiv hosil qilindi:")
# print("a:", a)
#
#
# # 68
#
# def almashtirish(a):
#     if len(a) < 2:
#         return a
#
#     eng_kichik_index = a.index(min(a))
#     eng_katta_index = a.index(max(a))
#
#     a[eng_kichik_index], a[eng_katta_index] = a[eng_katta_index], a[eng_kichik_index]
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# almashtirish(a)
#
# print("A massiv hosil qilindi:")
# print("a:", a)
#
#
# # 69
#
# def almashtirish(a):
#     if len(a) < 6 or len(a) % 2 != 0:
#         return a
#
#     n = len(a)
#     birinchi_index = 0
#     ikkinchi_index = 2
#     uchinchi_index = 4
#
#     a[birinchi_index], a[ikkinchi_index], a[uchinchi_index] = a[uchinchi_index], a[birinchi_index], a[ikkinchi_index]
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# if n % 2 != 0 or n < 6:
#     print("Juft son kiritilgan va kamida 6 elementdan iborat bo'lishi kerak.")
# else:
#     a = []
#     print("Massiv elementlarini kiriting:")
#     for i in range(n):
#         element = int(input(f"a[{i}]: "))
#         a.append(element)
#
#     almashtirish(a)
#
#     print("A massiv hosil qilindi:")
#     print("a:", a)
#
#
# # 70
# def almashtirish(a):
#     if len(a) < 2 or len(a) % 2 != 0:
#         return a
#
#     n = len(a)
#     yarmi = n // 2
#     a[:yarmi], a[yarmi:] = a[yarmi:], a[:yarmi]
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# if n % 2 != 0 or n < 2:
#     print("Juft son kiritilgan va kamida 2 elementdan iborat bo'lishi kerak.")
# else:
#     a = []
#     print("Massiv elementlarini kiriting:")
#     for i in range(n):
#         element = int(input(f"a[{i}]: "))
#         a.append(element)
#
#     almashtirish(a)
#
#     print("A massiv hosil qilindi:")
#     print("a:", a)
#
# # 71
#
# def teskari_tartib(a):
#     a.sort(reverse=True)
#
#
# # Foydalanuvchi kiritadi
# n = int(input("Massiv uchun nechta elementdan tashkil qilmoqchisiz? "))
#
# a = []
# print("Massiv elementlarini kiriting:")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
#
# teskari_tartib(a)
#
# print("A massiv teskari tartibda joylashtirildi:")
# print("a:", a)

# 72
# n = int(input("n ni kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# k = int(input("k ni kiriting: "))
# h = int(input("h ni kiriting: "))
#
# # Massivning a[k] va a[h] elementlari orasidagi qiymatlarni almashtirish
# temp = a[k]
# a[k] = a[h]
# a[h] = temp
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan massiv:", a)

# 73
# n = int(input("n ni kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# k = int(input("k ni kiriting: "))
# h = int(input("h ni kiriting: "))
#
# # a[k] va a[h] elementlarisiz massivni chiqarish
# print("a[k] elementi:", a[k])
# print("a[h] elementi:", a[h])
#
# # O'zgartirilgan massivni chiqarish
# print("Massiv:", a)

# 74
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Eng kichik va eng katta elementlarni indekslarni topish
# kichik_indeks = a.index(min(a))
# katta_indeks = a.index(max(a))
#
# # Almashtirishsiz massivni chiqarish
# print("Almashtirishsiz Massiv:", a)
#
# # Eng kichik va eng katta elementlarni olish
# kichik_element = a[kichik_indeks]
# katta_element = a[katta_indeks]
#
# # Eng kichik va eng katta elementlar orasidagi qiymatlarni nolga almashtirish
# a[kichik_indeks] = 0
# a[katta_indeks] = 0
#
# # O'zgartirilgan massivni chiqarish
# print(f"Eng kichik element: {kichik_element}")
# print(f"Eng katta element: {katta_element}")
# print("Almashtirilgan Massiv:", a)

# 75
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Eng kichik va eng katta elementlarni topish
# kichik_indeks = a.index(min(a))
# katta_indeks = a.index(max(a))
#
# # Eng kichik va eng katta elementlarni teskari tartibda almashtirish
# a[kichik_indeks], a[katta_indeks] = a[katta_indeks], a[kichik_indeks]
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 76
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Barcha lokal maksimumlarni nolga aylantirish
# for i in range(1, n - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         a[i] = 0
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 77
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Barcha lokal minimumlarni kvadratga oshirish
# for i in range(1, n - 1):
#     if a[i] < a[i - 1] and a[i] < a[i + 1]:
#         a[i] = a[i] ** 2
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 78
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning har bir elementini, uning ong qoshnisi bilan orta arifmetigiga almashtirish
# for i in range(n - 1):
#     a[i] = (a[i] + a[i + 1]) / 2
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 79
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni bir qadam ongga siljitish
# for i in range(n - 1):
#     a[i] = a[i + 1]
#
# # Oxirgi elementni 0 ga tenglash
# a[-1] = 0
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 80
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni bir qadam chapga siljitish
# for i in range(n - 1, 0, -1):
#     a[i] = a[i - 1]
#
# # Birinchi elementni 0 ga tenglash
# a[0] = 0
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 81
# n = int(input("Massiv uzunligini kiriting: "))
# k = int(input("k ni kiriting (1 <= k < n): "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni k ta orin ongga siljitish
# for i in range(n - k):
#     a[i] = a[i + k]
#
# # Oxirgi k ta elementni 0 ga tenglash
# for i in range(n - k, n):
#     a[i] = 0
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 82
# n = int(input("Massiv uzunligini kiriting: "))
# k = int(input("k ni kiriting (1 <= k < n): "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni k ta orin chapga siljitish
# for i in range(n - k):
#     a[i + k] = a[i]
#
# # Birinchi k ta elementni 0 ga tenglash
# for i in range(k):
#     a[i] = 0
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 83
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni 1 ta orin ongga siklik siljitish
# temp = a[0]  # Birinchi elementni saqlash
# for i in range(n - 1):
#     a[i] = a[i + 1]
# a[-1] = temp  # Oxirgi elementga birinchi elementni qiymatini o'tkazish
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 84
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivni bir qadam chapga siklik siljitish
# temp = a[-1]  # Oxirgi elementni saqlash
# for i in range(n - 1, 0, -1):
#     a[i] = a[i - 1]
# a[0] = temp  # Birinchi elementga oxirgi elementni qiymatini o'tkazish
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 85
# n = int(input("Massiv uzunligini kiriting: "))
# k = int(input("k ni kiriting (1 <= k <= 4; k < n): "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Yordamchi massivni hosil qilish
# yordamchi_massiv = a[-k:] + a[:-k]
#
# # Yordamchi massivni massivga o'tkazish
# a = yordamchi_massiv
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 86
# n = int(input("Massiv uzunligini kiriting: "))
# k = int(input("k ni kiriting (1 <= k <= 4; k < n): "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Yordamchi massivni hosil qilish
# yordamchi_massiv = a[-k:] + a[:-k]
#
# # Yordamchi massivni massivga o'tkazish
# a = yordamchi_massiv
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 87
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning dastlabki elementini boshqa joylashtirish
# first_element = a[0]
# a = sorted(a)
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 88
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning oxirgi elementini boshqa joylashtirish
# last_element = a[-1]
# a = sorted(a[:-1]) + [last_element]
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 89
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Qonuniyatni buzib turgan elementni topish
# violator = None
# for i in range(n - 1):
#     if a[i] > a[i + 1]:
#         violator = i
#         break
#
# # Agar qonuniyatni buzib turgan element topilgan bo'lsa, uni o'sish tartibida joylashtirish
# if violator is not None:
#     a.sort()
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 90
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k ni kiriting
# k = int(input("O'chiriladigan element indeksini kiriting (0 <= k < n): "))
#
# # Massivdan k indeksiga teng bolgan elementni o'chirish
# if 0 <= k < n:
#     del a[k]
#     print("O'chirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")

# 91
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k va m ni kiriting
# k = int(input("O'chiriladigan boshlang'ich indeksni kiriting (0 <= k < n): "))
# m = int(input("O'chiriladigan oxirgi indeksni kiriting (k < m < n): "))
#
# # Massivdan k dan m gacha bo'lgan elementlarni o'chirish
# if 0 <= k < m < n:
#     del a[k:m+1]
#     print(f"O'chirilgan Massivning elementlari soni: {len(a)}")
#     print("O'chirilgan Massivning elementlari:", a)
# else:
#     print("Noto'g'ri kiritildi. k va m indekslari massivning chegaralarida bo'lishi kerak.")

# 92
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Toqlarini ochirish
# even_elements = [a[i] for i in range(0, n, 2)]
#
# print(f"Toqlarini ochirilgan Massivning elementlari soni: {len(even_elements)}")
# print("Toqlarini ochirilgan Massivning elementlari:", even_elements)

# 93
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Juft indekslilarini ochirish
# odd_elements = a[1::2]
#
# print(f"Juft indekslilarini ochirilgan Massivning elementlari soni: {len(odd_elements)}")
# print("Juft indekslilarini ochirilgan Massivning elementlari:", odd_elements)

# 94
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Toq indekslilarini ochirish
# even_elements = a[0::2]
#
# print(f"Toq indekslilarini ochirilgan Massivning elementlari soni: {len(even_elements)}")
# print("Toq indekslilarini ochirilgan Massivning elementlari:", even_elements)

# 95
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Qoshnilarni ochirish
# unique_elements = []
# for element in a:
#     if a.count(element) == 1:
#         unique_elements.append(element)
#
# print(f"Qoshnilarni ochirilgan Massivning elementlari soni: {len(unique_elements)}")
# print("Qoshnilarni ochirilgan Massivning elementlari:", unique_elements)

# 96
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Bir xil qiymatga ega bolgan elementlarni topish
# unique_elements = set()
# duplicates = set()
#
# for element in a:
#     if element in unique_elements:
#         duplicates.add(element)
#     else:
#         unique_elements.add(element)
#
# # Birinchi uchragani qoldirish
# result = [element for element in a if element not in duplicates or a.index(element) == a.index(duplicates.pop())]
#
# print(f"Bir xil qiymatga ega bolgan elementlarni ochirilgan Massivning elementlari soni: {len(result)}")
# print("Bir xil qiymatga ega bolgan elementlarni ochirilgan Massivning elementlari:", result)

# 97
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Bir xil qiymatga ega bolgan elementlarni topish
# unique_elements = set()
# duplicates = set()
#
# for element in a:
#     if element in unique_elements:
#         duplicates.add(element)
#     else:
#         unique_elements.add(element)
#
# # Oxirgi uchragani qoldirish
# result = [element for element in a if element not in duplicates or a[::-1].index(element) == a[::-1].index(duplicates.pop())]
#
# print(f"Bir xil qiymatga ega bolgan elementlarni ochirilgan Massivning elementlari soni: {len(result)}")
# print("Bir xil qiymatga ega bolgan elementlarni ochirilgan Massivning elementlari:", result)

# 98
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # 3 marta yoki undan kam uchragan elementlarni topish
# unique_elements = set()
# triplicates = set()
#
# for element in a:
#     if a.count(element) >= 3:
#         triplicates.add(element)
#     else:
#         unique_elements.add(element)
#
# # 3 martadan kam uchraganlarni ochirish
# result = [element for element in a if element not in triplicates]
#
# print(f"3 martadan kam uchraganlarini ochirilgan Massivning elementlari soni: {len(result)}")
# print("3 martadan kam uchraganlarini ochirilgan Massivning elementlari:", result)

# 99
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # 2 marta yoki undan kop uchragan elementlarni topish
# unique_elements = set()
# duplicates = set()
#
# for element in a:
#     if a.count(element) >= 2:
#         duplicates.add(element)
#     else:
#         unique_elements.add(element)
#
# # 2 martadan kop uchraganlarni ochirish
# result = [element for element in a if element not in duplicates]
#
# print(f"2 martadan kop uchraganlarini ochirilgan Massivning elementlari soni: {len(result)}")
# print("2 martadan kop uchraganlarini ochirilgan Massivning elementlari:", result)

# 100
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # 2 marta uchragan elementlarni topish
# unique_elements = set()
# duplicates = set()
#
# for element in a:
#     if a.count(element) >= 2:
#         duplicates.add(element)
#     else:
#         unique_elements.add(element)
#
# # 2 martadan uchraganlarni ochirish
# result = [element for element in a if element not in duplicates or a.index(element) == a.index(duplicates.pop())]
#
# print(f"2 martadan uchraganlarini ochirilgan Massivning elementlari soni: {len(result)}")
# print("2 martadan uchraganlarini ochirilgan Massivning elementlari:", result)

# 101
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k ni kiriting
# k = int(input("Qoshuvshini o'zgartirish kerak bo'lgan element indeksini kiriting (0 <= k < n): "))
#
# # Massivda k indeksiga teng bo'lgan elementdan oldin kelgan elementni nolga teng qilish
# if 0 <= k < n:
#     a[k - 1] = 0
#     print("O'zgartirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")

# 102
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k ni kiriting
# k = int(input("Qoshuvshini o'zgartirish kerak bo'lgan element indeksini kiriting (0 <= k < n): "))
#
# # Massivda k indeksiga teng bo'lgan elementdan keyin kelgan elementni nolga teng qilish
# if 0 <= k < n - 1:
#     a[k + 1] = 0
#     print("O'zgartirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")

# 103
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Eng kichik va eng katta elementlarni topish
# min_element_index = a.index(min(a))
# max_element_index = a.index(max(a))
#
# # Qiymati nolga teng bo'lgan elementlarni qo'shish
# a[min_element_index - 1] = 0
# a[max_element_index + 1] = 0
#
# print("O'zgartirilgan Massiv:", a)

# 104
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k ni va m ni kiriting
# k = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan element indeksini kiriting (0 <= k < n): "))
# m = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan elementlar sonini kiriting (1 <= m <= 10): "))
#
# # Massivda k indeksiga teng bo'lgan elementdan oldin, qiymati nolga teng bo'lgan m ta elementni qo'shish
# if 0 <= k < n - 1:
#     for i in range(k + 1, min(k + 1 + m, n)):
#         a[i] = 0
#     print("O'zgartirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")

# 105
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k va m ni kiriting
# k = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan element indeksini kiriting (0 <= k < n): "))
# m = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan elementlar sonini kiriting (1 <= m <= 10): "))
#
# # Massivda k indeksiga teng bo'lgan elementdan keyin, qiymati nolga teng bo'lgan m ta elementni qo'shish
# if 0 <= k < n - 1:
#     for i in range(k + 1, min(k + 1 + m, n)):
#         a[i] = 0
#     print("O'zgartirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # k va m ni kiriting
# k = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan element indeksini kiriting (0 <= k < n): "))
# m = int(input("Qo'shuvshini o'zgartirish kerak bo'lgan elementlar sonini kiriting (1 <= m <= 10): "))
#
# # Massivda k indeksiga teng bo'lgan elementdan keyin, qiymati nolga teng bo'lgan m ta elementni qo'shish
# if 0 <= k < n - 1:
#     for i in range(k + 1, min(k + 1 + m, n)):
#         a[i] = 0
#     print("O'zgartirilgan Massiv:", a)
# else:
#     print("Noto'g'ri kiritildi. k indeksi massivning chegaralarida bo'lishi kerak.")

# 106
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning juft indeksli elementlarini qo'shish
# for i in range(0, n, 2):
#     a[i] += a[i + 1]
#
# print("O'zgartirilgan Massiv:", a)

# 107
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning toq indeksli elementlarini 2 marta qo'shish
# for i in range(1, n, 2):
#     a[i] += a[i - 1]
#
# print("O'zgartirilgan Massiv:", a)

# 108
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Har bir musbat elementdan oldin, qiymati nolga teng element qo'shish
# for i in range(n):
#     if a[i] > 0:
#         a.insert(i, 0)
#         n += 1  # Massiv uzunligini yangilash
#
# print("O'zgartirilgan Massiv:", a)

# 109
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Har bir manfiy elementdan keyin, qiymati nolga teng element qo'shish
# for i in range(n):
#     if a[i] < 0:
#         a.insert(i + 1, 0)
#         n += 1  # Massiv uzunligini yangilash
#
# print("O'zgartirilgan Massiv:", a)

# 110
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning juft indeksli elementlarini qo'shish
# for i in range(0, n, 2):
#     a[i] += a[i + 1]
#
# print("O'zgartirilgan Massiv:", a)

# 111
# n = int(input("Massiv uzunligini kiriting: "))
#
# # Massivni hosil qilish
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Massivning toq indeksli elementlarini 2 marta qo'shish
# for i in range(1, n, 2):
#     a[i] += a[i - 1]
#
# print("O'zgartirilgan Massiv:", a)

# 112
# def pufaksimon_saralash(massiv):
#     n = len(massiv)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if massiv[i] > massiv[j]:
#                 # Almashtirish
#                 massiv[i], massiv[j] = massiv[j], massiv[i]
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Pufaksimon saralash algoritmi orqali massivni osish tartibida chiqarish
# pufaksimon_saralash(a)
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 113
# def selection_sort(massiv):
#     n = len(massiv)
#     for i in range(n):
#         eng_kichik_indeks = i
#         for j in range(i + 1, n):
#             if massiv[j] < massiv[eng_kichik_indeks]:
#                 eng_kichik_indeks = j
#
#         # Almashtirish
#         massiv[i], massiv[eng_kichik_indeks] = massiv[eng_kichik_indeks], massiv[i]
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Oddiy tanlash (selection sort) algoritmi orqali massivni osish tartibida chiqarish
# selection_sort(a)
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 114
# def insertion_sort(massiv):
#     n = len(massiv)
#     for i in range(1, n):
#         key = massiv[i]
#         j = i - 1
#
#         # Tartiblangan elementlar orasiga joylashish
#         while j >= 0 and key < massiv[j]:
#             massiv[j + 1] = massiv[j]
#             j -= 1
#
#         massiv[j + 1] = key
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Oddiy qo'shish (insertion sort) algoritmi orqali massivni osish tartibida chiqarish
# insertion_sort(a)
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 115
# def insertion_sort(massiv):
#     n = len(massiv)
#     for i in range(1, n):
#         key = massiv[i]
#         j = i - 1
#
#         # Tartiblangan elementlar orasiga joylashish
#         while j >= 0 and key < massiv[j]:
#             massiv[j + 1] = massiv[j]
#             j -= 1
#
#         massiv[j + 1] = key
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# a = [int(input(f"a[{i}] ni kiriting: ")) for i in range(n)]
#
# # Oddiy qo'shish (insertion sort) algoritmi orqali massivni osish tartibida chiqarish
# insertion_sort(a)
#
# # O'zgartirilgan massivni chiqarish
# print("O'zgartirilgan Massiv:", a)

# 116
# def seriyalarni_analiz_qil(a):
#     n = len(a)
#     seriyalar = []
#     uzunliklar = []
#     elementlar = []
#
#     i = 0
#     while i < n:
#         seriya_uzunligi = 1
#         while i < n - 1 and a[i] == a[i + 1]:
#             seriya_uzunligi += 1
#             i += 1
#
#         seriyalar.append(a[i])
#         uzunliklar.append(seriya_uzunligi)
#         elementlar.append(a[i])
#         i += 1
#
#     return seriyalar, uzunliklar, elementlar
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Seriyalarni aniqlab olish
# seriyalar, uzunliklar, elementlar = seriyalarni_analiz_qil(A)
#
# # B va C massivlarini hosil qilish
# B = uzunliklar
# C = elementlar
#
# # Chiqarish
# print("A Massivi:", A)
# print("B Massivi:", B)
# print("C Massivi:", C)

# 117
# def seriyalarni_analiz_qil(a):
#     n = len(a)
#     seriyalar = []
#     uzunliklar = []
#     elementlar = []
#
#     i = 0
#     while i < n:
#         seriya_uzunligi = 1
#         while i < n - 1 and a[i] == a[i + 1]:
#             seriya_uzunligi += 1
#             i += 1
#
#         seriyalar.append(a[i])
#         uzunliklar.append(seriya_uzunligi)
#         elementlar.append(a[i])
#         i += 1
#
#     return seriyalar, uzunliklar, elementlar
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Seriyalarni aniqlab olish
# seriyalar, uzunliklar, elementlar = seriyalarni_analiz_qil(A)
#
# # B va C massivlarini hosil qilish
# B = uzunliklar
# C = elementlar
#
# # Chiqarish
# print("A Massivi:", A)
# print("B Massivi (seriyalar uzunligi):", B)
# print("C Massivi (seriyani tashkil qilgan element qiymati):", C)

# 118
# def seriyadan_keyin_nol_qoshish(massiv):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         new_massiv.append(massiv[i])
#         new_massiv.append(0)
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Har bir seriyadan keyin qiymati 0 ga teng bo'lgan element qo'shish
# B = seriyadan_keyin_nol_qoshish(A)
#
# # Chiqarish
# print("A Massivi:", A)
# print("B Massivi:", B)

# 119
# def seriyaga_element_qoshish(massiv, element):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         new_massiv.append(massiv[i])
#         new_massiv.append(element)
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Qo'shiladigan elementni olish
# element = int(input("Qo'shiladigan elementni kiriting: "))
#
# # Har bir seriyaga bir element qo'shish
# B = seriyaga_element_qoshish(A, element)
#
# # Chiqarish
# print("A Massivi:", A)
# print("B Massivi (Har bir seriyaga bir element qo'shilgan):", B)

# 120
# def seriyani_bir_elementga_kamaytirish(massiv, element):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         if i % 2 == 0:
#             # Juft indekslilarni seriya uzunligini kamaytirish uchun boshqarish
#             new_massiv.extend([element] * (massiv[i] - 1))
#         else:
#             # Toq indekslilarni boshqa seriyalarga qo'shish
#             new_massiv.append(massiv[i])
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Kamaytirish uchun elementni olish
# element = int(input("Kamaytirish uchun elementni kiriting: "))
#
# # Massivni kamaytirish
# B = seriyani_bir_elementga_kamaytirish(A, element)
#
# # Chiqarish
# print("A Massivi:", A)
# print("B Massivi (Seriyalarni bir elementga kamaytirilgan):", B)

# 121
# def k_seriya_uzunligini_oshirish(massiv, k):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         if i % 2 == 0 and massiv[i] <= k:
#             # Juft indekslilarni K - seriyasi uzunligini 2 marta oshirish uchun boshqarish
#             new_massiv.extend([massiv[i]] * 2)
#         else:
#             # Toq indekslilarni boshqa seriyalarga qo'shish
#             new_massiv.append(massiv[i])
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # K - seriyasi uzunligini 2 marta oshirish
# K = int(input("K - seriyasi uzunligini kiriting (K > 0): "))
# if K > 0:
#     B = k_seriya_uzunligini_oshirish(A, K)
#     print("B Massivi (K - seriyasi uzunligini 2 marta oshirilgan):", B)
# else:
#     print("K ni 0 dan katta kiriting.")

# 122
# def k_seriyaning_ochirish(massiv, k):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         if i % 2 == 0 and massiv[i] <= k:
#             # Juft indekslilarni K - seriyasini ochirish uchun boshqarish
#             pass
#         else:
#             # Toq indekslilarni boshqa seriyalarga qo'shish
#             new_massiv.append(massiv[i])
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # K - seriyasini ochirish
# K = int(input("K - seriyasini kiriting (K > 0): "))
# if K > 0:
#     B = k_seriyaning_ochirish(A, K)
#     print("B Massivi (K - seriyasini ochirilgan):", B)
# else:
#     print("K ni 0 dan katta kiriting.")

# 123
# def k_seriyaning_ornini_almashtirish(massiv, k):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         if i % 2 == 0 and massiv[i] <= k:
#             # Juft indekslilarni K - seriyasi ornini almashtirish uchun boshqarish
#             if i > 0 and massiv[i] > massiv[i - 1]:
#                 new_massiv.append(massiv[i - 1])
#             else:
#                 new_massiv.append(massiv[i])
#         else:
#             # Toq indekslilarni boshqa seriyalarga qo'shish
#             new_massiv.append(massiv[i])
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # K - seriyasi bilan birinchi seriyasi ornini almashtirish
# K = int(input("K - seriyasini kiriting (K > 1): "))
# if K > 1:
#     B = k_seriyaning_ornini_almashtirish(A, K)
#     print("B Massivi (K - seriyasi bilan birinchi seriyasi ornini almashtirilgan):", B)
# else:
#     print("K ni 1 dan katta kiriting.")

# 124
# def k_seriyaning_oxirgi_ornini_almashtirish(massiv, k):
#     n = len(massiv)
#     new_massiv = []
#
#     for i in range(n):
#         if i % 2 == 0 and massiv[i] <= k:
#             # Juft indekslilarni K - seriyasi bilan oxirgi seriyasi ornini almashtirish uchun boshqarish
#             if i < n - 1 and massiv[i] > massiv[i + 1]:
#                 new_massiv.append(massiv[i + 1])
#             else:
#                 new_massiv.append(massiv[i])
#         else:
#             # Toq indekslilarni boshqa seriyalarga qo'shish
#             new_massiv.append(massiv[i])
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # K - seriyasi bilan oxirgi seriyasi ornini almashtirish
# K = int(input("K - seriyasini kiriting (K > 1): "))
# if K > 1:
#     B = k_seriyaning_oxirgi_ornini_almashtirish(A, K)
#     print("B Massivi (K - seriyasi bilan oxirgi seriyasi ornini almashtirilgan):", B)
# else:
#     print("K ni 1 dan katta kiriting.")

# 125
# def seriyalarni_nolga_almashtir(massiv, K):
#     n = len(massiv)
#     new_massiv = []
#
#     i = 0
#     while i < n:
#         # Seriyani topish
#         seriya_uzunligi = 0
#         while i + seriya_uzunligi < n and seriya_uzunligi < K:
#             seriya_uzunligi += 1
#
#         # Seriya uzunligi K dan kichik bo'lsa, bitta elementni nolga almashtirish
#         if seriya_uzunligi < K:
#             new_massiv.append(0)
#         else:
#             new_massiv.extend(massiv[i:i + seriya_uzunligi])
#
#         i += seriya_uzunligi
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Uzunligi K dan kichik seriyalarni nolga almashtirish
# K = int(input("Uzunligi K dan kichik seriyalarni nolga almashtirish uchun K ni kiriting (K > 1): "))
# if K > 1:
#     B = seriyalarni_nolga_almashtir(A, K)
#     print("B Massivi (Uzunligi K dan kichik seriyalarni nolga almashtirilgan):", B)
# else:
#     print("K ni 1 dan katta kiriting.")

# 126
# def uzunlik_K_seriyalarini_nolga_almashtirish(massiv, K):
#     n = len(massiv)
#     new_massiv = []
#
#     i = 0
#     while i < n:
#         # Seriyani topish
#         seriya_uzunligi = 0
#         while i + seriya_uzunligi < n and seriya_uzunligi < K:
#             seriya_uzunligi += 1
#
#         # Seriya uzunligi K ga teng bo'lsa, bitta elementni nolga almashtirish
#         if seriya_uzunligi == K:
#             new_massiv.append(0)
#         else:
#             new_massiv.extend(massiv[i:i + seriya_uzunligi])
#
#         i += seriya_uzunligi
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Uzunligi K ga teng seriyalarni nolga almashtirish
# K = int(input("Uzunligi K ga teng seriyalarni nolga almashtirish uchun K ni kiriting (K > 1): "))
# if K > 1:
#     B = uzunlik_K_seriyalarini_nolga_almashtirish(A, K)
#     print("B Massivi (Uzunligi K ga teng seriyalarni nolga almashtirilgan):", B)
# else:
#     print("K ni 1 dan katta kiriting.")

# 127
# def seriyalarni_nolga_almashtir(massiv, K):
#     n = len(massiv)
#     new_massiv = []
#
#     i = 0
#     while i < n:
#         # Seriyani topish
#         seriya_uzunligi = 0
#         while i + seriya_uzunligi < n and seriya_uzunligi < K:
#             seriya_uzunligi += 1
#
#         # Seriya uzunligi K dan katta bo'lsa, bitta elementni nolga almashtirish
#         if seriya_uzunligi >= K:
#             new_massiv.extend([0] * seriya_uzunligi)
#         else:
#             new_massiv.extend(massiv[i:i + seriya_uzunligi])
#
#         i += seriya_uzunligi
#
#     return new_massiv
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Uzunligi K dan katta seriyalarni nolga almashtirish
# K = int(input("Uzunligi K dan katta seriyalarni nolga almashtirish uchun K ni kiriting (K > 1): "))
# if K > 1:
#     B = seriyalarni_nolga_almashtir(A, K)
#     print("B Massivi (Uzunligi K dan katta seriyalarni nolga almashtirilgan):", B)
# else:
#     print("K ni 1 dan katta kiriting.")

# 128
# def seriyaga_element_qoshish(massiv, yangi_element):
#     if not massiv:
#         # Massiv bo'sh bo'lsa, yangi elementni massivga qo'shamiz
#         massiv.append(yangi_element)
#     else:
#         # Massiv bo'sh bo'lmasa, birinchi uchragan seriyaga yangi elementni qo'shamiz
#         massiv[0].append(yangi_element)
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Yangi elementni olish
# yangi_element = int(input("Yangi elementni kiriting: "))
#
# # Seriyaga yangi elementni qo'shish
# seriyaga_element_qoshish(A, yangi_element)
#
# # Yangilangan massivni chiqarish
# print("Yangilangan Massiv:", A)

# 129
# def oxirgi_seriyaga_element_qoshish(massiv, yangi_element):
#     if not massiv:
#         # Massiv bo'sh bo'lsa, yangi seriyani boshlash
#         massiv.append([yangi_element])
#     else:
#         # Massiv bo'sh bo'lmasa, oxirgi seriyaga yangi elementni qo'shamiz
#         massiv[-1].append(yangi_element)
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Yangi elementni olish
# yangi_element = int(input("Yangi elementni kiriting: "))
#
# # Oxirgi seriyaga yangi elementni qo'shish
# oxirgi_seriyaga_element_qoshish(A, yangi_element)
#
# # Yangilangan massivni chiqarish
# print("Yangilangan Massiv:", A)

# 130
# def barcha_seriyalarga_element_qoshish(massiv, yangi_element):
#     if not massiv:
#         # Massiv bo'sh bo'lsa, yangi seriyani boshlash
#         massiv.append([yangi_element])
#     else:
#         # Massiv bo'sh bo'lmasa, barcha seriyalarga yangi elementni qo'shamiz
#         for seriya in massiv:
#             seriya.append(yangi_element)
#
# # Massivni olish
# n = int(input("Massiv uzunligini kiriting: "))
# A = [int(input(f"A[{i}] ni kiriting: ")) for i in range(n)]
#
# # Yangi elementni olish
# yangi_element = int(input("Yangi elementni kiriting: "))
#
# # Barcha seriyalarga yangi elementni qo'shish
# barcha_seriyalarga_element_qoshish(A, yangi_element)
#
# # Yangilangan massivni chiqarish
# print("Yangilangan Massiv:", A)
