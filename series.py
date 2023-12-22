# 1
# def yigindi_hisobla(sonlar):
#     yigindi = sum(sonlar)
#     return yigindi
#
# sonlar = [float(x) for x in input("Haqiqiy sonlarni vergul bilan kiriting: ").split(',')]
#
# yigindi = yigindi_hisobla(sonlar)
# print(f"Kiritilgan sonlar yig'indisi: {yigindi}")

# 2
# def kopaytma_hisobla(sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
#
# sonlar = [float(x) for x in input("Haqiqiy sonlarni vergul bilan kiriting: ").split(',')]
#
# kopaytma = kopaytma_hisobla(sonlar)
# print(f"Kiritilgan sonlar kopaytmasi: {kopaytma}")

# 3
# def orta_arifmetik_hisobla(sonlar):
#     if len(sonlar) == 0:
#         return None
#     orta_arifmetik = sum(sonlar) / len(sonlar)
#     return orta_arifmetik
#
# sonlar = [float(x) for x in input("Haqiqiy sonlarni vergul bilan kiriting: ").split(',')]
#
# orta_arifmetik = orta_arifmetik_hisobla(sonlar)
# if orta_arifmetik is not None:
#     print(f"Kiritilgan sonlar orta arifmetigi: {orta_arifmetik}")
# else:
#     print("Kiritilgan sonlar ro'yxati bo'sh.")

# 4
# def yigindini_kopaytmasini_hisobla(n, sonlar):
#     if n == 0 or len(sonlar) != n:
#         return None, None
#
#     yigindi = sum(sonlar)
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#
#     return yigindi, kopaytma
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [float(x) for x in input(f"{n} ta haqiqiy sonni vergul bilan kiriting: ").split(',')]
#
# yigindi, kopaytma = yigindini_kopaytmasini_hisobla(n, sonlar)
#
# if yigindi is not None and kopaytma is not None:
#     print(f"Kiritilgan sonlar yig'indisi: {yigindi}")
#     print(f"Kiritilgan sonlar kopaytmasi: {kopaytma}")
# else:
#     print("Noto'g'ri ma'lumot kiritildi. Iltimos, to'g'ri ma'lumot kiriting.")

# 5
# def butun_qismlar_va_ularning_yigindisini_hisobla(n, sonlar):
#     if n == 0 or len(sonlar) != n:
#         return None, None
#
#     butun_qismlar = sum(int(x) for x in sonlar)
#     butun_qismlar_yigindisi = sum(int(x) for x in map(lambda x: str(x).split('.')[1], sonlar) if '.' in str(x))
#
#     return butun_qismlar, butun_qismlar_yigindisi
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [float(x) for x in input(f"{n} ta haqiqiy sonni vergul bilan kiriting: ").split(',')]
#
# butun_qismlar, butun_qismlar_yigindisi = butun_qismlar_va_ularning_yigindisini_hisobla(n, sonlar)
#
# if butun_qismlar is not None and butun_qismlar_yigindisi is not None:
#     print(f"Kiritilgan sonlarning faqat butun qismlari yig'indisi: {butun_qismlar}")
#     print(f"Kiritilgan sonlarning butun qismlarining yig'indisi: {butun_qismlar_yigindisi}")
# else:
#     print("Noto'g'ri ma'lumot kiritildi. Iltimos, to'g'ri ma'lumot kiriting.")

# 6
# def kasr_qismlar_va_kopaytmasini_hisobla(n, sonlar):
#     if n == 0 or len(sonlar) != n:
#         return None, None
#
#     kasr_qismlar = [float('0.' + str(x).split('.')[1]) for x in sonlar]
#     kasr_qismlar_kopaytma = 1
#     for qism in kasr_qismlar:
#         kasr_qismlar_kopaytma *= qism
#
#     return kasr_qismlar, kasr_qismlar_kopaytma
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [float(x) for x in input(f"{n} ta haqiqiy sonni vergul bilan kiriting: ").split(',')]
#
# kasr_qismlar, kasr_qismlar_kopaytma = kasr_qismlar_va_kopaytmasini_hisobla(n, sonlar)
#
# if kasr_qismlar is not None and kasr_qismlar_kopaytma is not None:
#     print(f"Kiritilgan sonlarning faqat kasr qismlari: {kasr_qismlar}")
#     print(f"Kiritilgan sonlarning kasr qismlarining kopaytmasi: {kasr_qismlar_kopaytma}")
# else:
#     print("Noto'g'ri ma'lumot kiritildi. Iltimos, to'g'ri ma'lumot kiriting.")

# 7
# def yaxlitlangan_yigindini_chiqar(n, sonlar):
#     yaxlitlangan_sonlar = [round(x) for x in sonlar]
#     yigindi = sum(yaxlitlangan_sonlar)
#
#     print("Kiritilgan haqiqiy sonlar:")
#     for i in range(n):
#         print(f"{sonlar[i]:.2f} -> {yaxlitlangan_sonlar[i]}")
#
#     print(f"Yaxlitlangan sonlar yig'indisi: {yigindi}")
#
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [float(x) for x in input(f"{n} ta haqiqiy sonni vergul bilan kiriting: ").split(',')]
#
# yaxlitlangan_yigindini_chiqar(n, sonlar)

# 8
# def juft_sonlarni_chiqar(n, sonlar):
#     juft_sonlar = [son for son in sonlar if son % 2 == 0]
#
#     print("Kiritilgan butun sonlar:")
#     for i in range(n):
#         print(f"Son {i + 1}: {sonlar[i]}")
#
#     print("\nJuft sonlar:")
#     for i, son in enumerate(juft_sonlar):
#         print(f"Son {i + 1}: {son}")
#
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# juft_sonlarni_chiqar(n, sonlar)

# 9
# def toq_sonlarni_chiqar(n, sonlar):
#     toq_sonlar = [son for son in sonlar if son % 2 != 0]
#
#     print("Kiritilgan butun sonlar:")
#     for i in range(n):
#         print(f"Son {i + 1}: {sonlar[i]}")
#
#     print("\nToq sonlar:")
#     for i, son in enumerate(toq_sonlar):
#         print(f"Son {i + 1}: {son}")
#
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# toq_sonlarni_chiqar(n, sonlar)

# 10
# def musbat_sonlarni_analiz_qil(n, sonlar):
#     musbat_sonlar_mavjudmi = any(son > 0 for son in sonlar)
#
#     print("Kiritilgan butun sonlar:")
#     for i in range(n):
#         print(f"Son {i + 1}: {sonlar[i]}")
#
#     print(f"\nMusbat sonlar mavjudmi: {musbat_sonlar_mavjudmi}")
#
#
# n = int(input("n natural sonini kiriting: "))
#
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# musbat_sonlarni_analiz_qil(n, sonlar)

# 11
# def kichik_sonlarni_analiz_qil(n, k, sonlar):
#     kichik_sonlar_mavjudmi = any(son < k for son in sonlar)
#
#     print(f"Kiritilgan butun sonlar, k={k}:")
#     for i in range(n):
#         print(f"Son {i + 1}: {sonlar[i]}")
#
#     print(f"\nKichik sonlar mavjudmi: {kichik_sonlar_mavjudmi}")
#
#
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# kichik_sonlarni_analiz_qil(n, k, sonlar)

# 12
# def noldan_ayri_butun_son(toplam):
#     if toplam % 10 == 0:
#         return 0
#     elif toplam > 0:
#         return 10 - toplam % 10
#     else:
#         return abs(toplam) % 10
#
# toplam = int(input("Noldan iborat bo'lmagan butun sonlar toplamini kiriting: "))
#
# noldan_ayri_son = noldan_ayri_butun_son(toplam)
#
# print(f"Kiritilgan sonning o'zi: {toplam}")
# print(f"Aniqlangan son: {noldan_ayri_son}")

# 13
# def musbat_juft_sonlarni_yigindi(n, toplam):
#     if toplam % 2 != 0 or toplam <= 0:
#         print(0)
#         return
#
#     juft_sonlar_yigindisi = 0
#     for i in range(n):
#         if i % 2 == 0 and toplam > 0:
#             juft_sonlar_yigindisi += i
#
#     print(juft_sonlar_yigindisi)
#
#
# # Butun sonlarni olish
# n = int(input("Noldan iborat bo'lmagan butun sonlar toplamini kiriting: "))
# toplam = int(input(f"{n} ta butun sonni kiriting: "))
#
# # Musbat juft sonlarni yigindini chiqarish
# musbat_juft_sonlarni_yigindi(n, toplam)

# 14
# def kichik_sonni_aniqla(k, toplam):
#     if k <= 0 or toplam % k == 0:
#         print(0)
#         return
#
#     kichik_son = k - (toplam % k)
#     print(kichik_son)
#
#
# # Butun sonlarni olish
# k = int(input("K butun sonini kiriting: "))
# toplam = int(input("Noldan iborat bo'lmagan butun sonlar toplamini kiriting: "))
#
# # K dan kichik bo'lgan sonni aniqlash va chiqarish
# kichik_sonni_aniqla(k, toplam)

# 15
# def kattasi_nomerini_aniqla(k, toplam):
#     if k <= 0 or toplam % k == 0:
#         print(0)
#         return
#
#     katta_son_nomeri = toplam // k + 1
#     print(katta_son_nomeri)
#
#
# # Butun sonlarni olish
# k = int(input("K butun sonini kiriting: "))
# toplam = int(input("Noldan iborat bo'lmagan butun sonlar toplamini kiriting: "))
#
# # K dan katta bo'lgan birinchi sonning raqamini aniqlash va chiqarish
# kattasi_nomerini_aniqla(k, toplam)

# 16
# def kattasi_nomerini_aniqla(k, toplam):
#     if k <= 0 or toplam % k == 0:
#         print(0)
#         return
#
#     katta_son_nomeri = toplam // k
#     print(katta_son_nomeri)
#
#
# # Butun sonlarni olish
# k = int(input("K butun sonini kiriting: "))
# toplam = int(input("Noldan iborat bo'lmagan butun sonlar toplamini kiriting: "))
#
# # K dan katta bo'lgan oxirgi sonning raqamini aniqlash va chiqarish
# kattasi_nomerini_aniqla(k, toplam)

# 17
# def sonlarni_chiqar(B, sonlar):
#     print(f"B = {B}")
#     print("Kiritilgan sonlar:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}")
#
# # B ni olish
# B = float(input("B haqiqiy sonini kiriting: "))
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Sonlarni B bilan birga chiqarish
# sonlarni_chiqar(B, sonlar)

# 18
# def bir_xil_qiymatlilarni_chiqar(n, sonlar):
#     bir_xil_qiymatlilar = set()
#
#     print("Kiritilgan butun sonlar:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}")
#         bir_xil_qiymatlilar.add(son)
#
#     print("\nHar xil qiymatli elementlar:")
#     for qiymat in bir_xil_qiymatlilar:
#         print(qiymat)
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting (n > 2): "))
# while n <= 2:
#     print("n soni 2 dan katta bo'lishi kerak.")
#     n = int(input("n natural sonini kiriting (n > 2): "))
#
# # Butun sonlarni olish
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Bir xil qiymatlilarni chiqarish
# bir_xil_qiymatlilarni_chiqar(n, sonlar)

# 19
# def chap_qoshni_kichiklari_va_sonlar(n, sonlar):
#     chap_qoshni_kichiklari = sorted(sonlar)
#     sonlar = sorted(sonlar, reverse=True)
#
#     print("Kiritilgan butun sonlar:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}")
#
#     print("\nChap qoshni kichiklari:")
#     for kichik in chap_qoshni_kichiklari:
#         print(kichik)
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Butun sonlarni olish
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Chap qoshni kichiklari va sonlarini chiqarish
# chap_qoshni_kichiklari_va_sonlar(n, sonlar)

# 20
# def ong_qoshni_kichiklari_va_sonlar(n, sonlar):
#     ong_qoshni_kichiklari = sorted(sonlar, reverse=True)
#
#     print("Kiritilgan butun sonlar:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}")
#
#     print("\nOng qoshni kichiklari:")
#     for kichik in ong_qoshni_kichiklari:
#         print(kichik)
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Butun sonlarni olish
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Ong qoshni kichiklari va sonlarini chiqarish
# ong_qoshni_kichiklari_va_sonlar(n, sonlar)

# 21
# def osish_tartibida_bool(n, sonlar):
#     is_osish = all(sonlar[i] <= sonlar[i + 1] for i in range(n - 1))
#     print(is_osish)
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Osish tartibida bo'lishni tekshirish va natijani chiqarish
# osish_tartibida_bool(n, sonlar)

# 22
# def tartibni_tekshir(n, sonlar):
#     tartib_buzilgan = any(sonlar[i] > sonlar[i + 1] for i in range(n - 1))
#
#     if tartib_buzilgan:
#         print(sonlar.index(max(sonlar)) + 1)
#     else:
#         print(0)
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Tartibni tekshirish va natijani chiqarish
# tartibni_tekshir(n, sonlar)

# 23
# def arra_shaklida_bool(n, sonlar):
#     is_arra_shaklida = all((sonlar[i] < sonlar[i + 1] and sonlar[i] < sonlar[i + 2]) or
#                            (sonlar[i] > sonlar[i + 1] and sonlar[i] > sonlar[i + 2])
#                            for i in range(n - 2))
#
#     if is_arra_shaklida:
#         print(0)
#     else:
#         print(sonlar.index(max(sonlar)) + 1)
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Arra shaklida bo'lishni tekshirish va natijani chiqarish
# arra_shaklida_bool(n, sonlar)

# 24
# def oxirgi_2_ta_nol_orasidagi_yigindi(n, sonlar):
#     nol_indekslari = [i for i, son in enumerate(sonlar) if son == 0]
#
#     if len(nol_indekslari) >= 2:
#         oxirgi_2_ta_nol_orasidagi_yigindi = sum(sonlar[nol_indekslari[-2] + 1: nol_indekslari[-1]])
#         print(f"Oxirgi 2 ta nol orasidagi sonlar yig'indisi: {oxirgi_2_ta_nol_orasidagi_yigindi}")
#     else:
#         print("Kamida 2 ta nol mavjud emas.")
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Butun sonlarni olish
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Oxirgi 2 ta nol orasidagi sonlarni yig'indisini chiqarish
# oxirgi_2_ta_nol_orasidagi_yigindi(n, sonlar)

# 25
# def birinchi_va_oxirgi_nol_orasidagi_yigindi(n, sonlar):
#     nol_indekslari = [i for i, son in enumerate(sonlar) if son == 0]
#
#     if len(nol_indekslari) >= 2:
#         birinchi_nol_indeksi = nol_indekslari[0]
#         oxirgi_nol_indeksi = nol_indekslari[-1]
#
#         yigindi = sum(sonlar[birinchi_nol_indeksi + 1: oxirgi_nol_indeksi])
#         print(f"Birinchi va oxirgi nol orasidagi sonlar yig'indisi: {yigindi}")
#     else:
#         print("Kamida 2 ta nol mavjud emas.")
#
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Butun sonlarni olish
# sonlar = [int(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Birinchi va oxirgi nol orasidagi sonlarni yig'indisini chiqarish
# birinchi_va_oxirgi_nol_orasidagi_yigindi(n, sonlar)

# 26
# def daraja_chiqar(n, k, sonlar):
#     daraja_sonlar = [son ** k for son in sonlar]
#
#     print(f"{k}-darajali sonlar:")
#     for i, daraja in enumerate(daraja_sonlar):
#         print(f"Son {i + 1}^{k} = {daraja}")
#
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # k-darajali sonlarni chiqarish
# daraja_chiqar(n, k, sonlar)

# 27
# def darajalarni_chiqar(n, sonlar):
#     print("Kiritilgan sonlar va ularning darajalari:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}^{i + 1} = {son ** (i + 1)}")
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Darajalarni chiqarish
# darajalarni_chiqar(n, sonlar)

# 28
# def darajalarni_chiqar(n, sonlar):
#     print("Kiritilgan sonlar va ularning darajalari:")
#     for i, son in enumerate(sonlar):
#         print(f"Son {i + 1}: {son}^{n - i} = {son ** (n - i)}")
#
# # n ni olish
# n = int(input("n natural sonini kiriting: "))
#
# # Haqiqiy sonlarni olish
# sonlar = [float(input(f"Son {i + 1}: ")) for i in range(n)]
#
# # Darajalarni chiqarish
# darajalarni_chiqar(n, sonlar)

# 29
# def yigindini_chiqar(n, k, toplamlar):
#     barcha_sonlar = [son for toplam in toplamlar for son in toplam]
#
#     print(f"Barcha sonlar yig'indisi: {barcha_sonlar}")
#
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # Barcha sonlar yig'indisini chiqarish
# yigindini_chiqar(n, k, toplamlar)

# 30
# def yigindini_chiqar(n, k, toplamlar):
#     for i, toplam in enumerate(toplamlar):
#         print(f"Toplam {i + 1} elementlari yig'indisi: {sum(toplam)}")
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # Har bir toplam uchun elementlar yig'indisini chiqarish
# yigindini_chiqar(n, k, toplamlar)

# 31
# def ikkita_soni_bor_toplamni_chiqar(n, k, toplamlar):
#     for i, toplam in enumerate(toplamlar):
#         if 2 in toplam:
#             print(f"Toplam {i + 1} soni: {toplam}")
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # 2 soni bor bolgan toplamlarning sonini chiqarish
# ikkita_soni_bor_toplamni_chiqar(n, k, toplamlar)

# 32
# def birinchi_uchragan_2sonni_turgan_nomerni_chiqar(n, k, toplamlar):
#     for i, toplam in enumerate(toplamlar):
#         for j in range(len(toplam) - 2):
#             if toplam[j] == 2 and toplam[j + 1] == 2:
#                 print(f"Toplam {i + 1} uchragan birinchi 2 soni turgan nomer: {j + 1}")
#                 break
#     else:
#         print("Har bir toplamda uchragan birinchi 2 son topilmadi.")
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # Birinchi uchragan 2 sonni turgan nomerni chiqarish
# birinchi_uchragan_2sonni_turgan_nomerni_chiqar(n, k, toplamlar)

# 33
# def oxirgi_uchragan_2sonni_turgan_nomerni_chiqar(n, k, toplamlar):
#     for i, toplam in enumerate(toplamlar):
#         for j in range(len(toplam) - 2):
#             if toplam[j] == 2 and toplam[j + 1] == 2:
#                 nomer = j + 1
#         else:
#             if nomer is not None:
#                 print(f"Toplam {i + 1} oxirgi uchragan 2 soni turgan nomer: {nomer}")
#             else:
#                 print(f"Toplam {i + 1} uchragan 2 son topilmadi.")
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # Oxirgi uchragan 2 sonni turgan nomerni chiqarish
# oxirgi_uchragan_2sonni_turgan_nomerni_chiqar(n, k, toplamlar)

# 34
# def toplamlar_elementlari_yigindisini_chiqar(n, k, toplamlar):
#     for i, toplam in enumerate(toplamlar):
#         if toplam.count(2) == 2:
#             yigindi = sum(toplam)
#             print(f"Toplam {i + 1} elementlari yig'indisi: {yigindi}")
#         else:
#             print(f"Toplam {i + 1} uchragan 2 son topilmadi. 0")
#
# # n va k ni olish
# n = int(input("n natural sonini kiriting: "))
# k = int(input("k natural sonini kiriting: "))
#
# # Butun sonlarni olish
# toplamlar = [list(map(int, input(f"Toplam {i + 1} ({k} ta son): ").split())) for i in range(n)]
#
# # Har bir toplam uchun qiyidagi vazifani bajarish
# toplamlar_elementlari_yigindisini_chiqar(n, k, toplamlar)

# 35
# def toplam_elementlarini_chiqar(k):
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun elementlarni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#         print(f"Toplam {i + 1} elementlari: {elementlar}")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun elementlarni kiritish va chiqarish
# toplam_elementlarini_chiqar(k)

# 36
# def osuvchi_bolgan_toplamlarni_chiqar(k):
#     osuvchi_bolgan_toplamlar = []
#
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun kamida 2 ta elementni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#
#         if len(elementlar) >= 2:
#             osuvchi_bolgan_toplamlar.append(sum(elementlar))
#         else:
#             print(f"Toplam {i + 1} uchun kamida 2 ta element kiritilmadi. 0")
#
#     print(f"O'suvchi bolgan toplamlar sonlari: {osuvchi_bolgan_toplamlar}")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun kamida 2 ta elementni kiritish va chiqarish
# osuvchi_bolgan_toplamlarni_chiqar(k)

# 37
# def osuvchi_kamayuvchi_toplamlarni_chiqar(k):
#     osuvchi_toplamlar = []
#     kamayuvchi_toplamlar = []
#
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun kamida 2 ta elementni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#
#         if len(elementlar) >= 2:
#             if elementlar[0] > elementlar[1]:
#                 osuvchi_toplamlar.append(sum(elementlar))
#             elif elementlar[0] < elementlar[1]:
#                 kamayuvchi_toplamlar.append(sum(elementlar))
#             else:
#                 print(f"Toplam {i + 1} uchun kamida 2 ta bir xil element kiritildi. 0")
#         else:
#             print(f"Toplam {i + 1} uchun kamida 2 ta element kiritilmadi. 0")
#
#     print(f"O'suvchi bolgan toplamlar sonlari: {osuvchi_toplamlar}")
#     print(f"Kamayuvchi bolgan toplamlar sonlari: {kamayuvchi_toplamlar}")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun kamida 2 ta elementni kiritish va chiqarish
# osuvchi_kamayuvchi_toplamlarni_chiqar(k)

# 38
# def osuvchi_kamayuvchi_toplamlarni_chiqar(k):
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun kamida 2 ta elementni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#
#         if len(elementlar) >= 2:
#             if elementlar[0] > elementlar[1]:
#                 print(f"Toplam {i + 1} elementlari osuvchi. 1")
#             elif elementlar[0] < elementlar[1]:
#                 print(f"Toplam {i + 1} elementlari kamayuvchi. -1")
#             else:
#                 print(f"Toplam {i + 1} elementlari osuvchi ham kamayuvchi ham bo'lmasa. 0")
#         else:
#             print(f"Toplam {i + 1} uchun kamida 2 ta element kiritilmadi. 0")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun kamida 2 ta elementni kiritish va chiqarish
# osuvchi_kamayuvchi_toplamlarni_chiqar(k)

# 39
# def arrasimon_toplamlarni_chiqar(k):
#     arrasimon_toplamlar = []
#
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun kamida 3 ta elementni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#
#         if len(elementlar) == 3:
#             arrasimon_toplamlar.append(sum(elementlar))
#         else:
#             print(f"Toplam {i + 1} uchun kamida 3 ta element kiritilmadi. 0")
#
#     print(f"Arrasimon bo'lgan toplamlar sonlari: {arrasimon_toplamlar}")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun kamida 3 ta elementni kiritish va chiqarish
# arrasimon_toplamlarni_chiqar(k)

# 40
# def arrasimon_yoki_qonuniyatni_buzgan_element_tartibini_chiqar(k):
#     for i in range(k):
#         print(f"Toplam {i + 1} uchun kamida 3 ta elementni kiriting:")
#         elementlar = []
#         while True:
#             element = int(input("Element (0 bilan tugatish uchun 0 ni kiriting): "))
#             if element == 0:
#                 break
#             elementlar.append(element)
#
#         if len(elementlar) == 3:
#             if elementlar[0] * elementlar[1] != elementlar[2]:
#                 print(f"Toplam {i + 1} elementlari arrasimon. Son: {sum(elementlar)}")
#             else:
#                 print(f"Toplam {i + 1} elementlari arrasimon emas. Qonuniyati buzgan element tartib raqami: {sorted(range(3), key=lambda x: elementlar[x])}")
#         else:
#             print(f"Toplam {i + 1} uchun kamida 3 ta element kiritilmadi. 0")
#
# # k ni olish
# k = int(input("k natural sonini kiriting: "))
#
# # Har bir toplam uchun kamida 3 ta elementni kiritish va chiqarish
# arrasimon_yoki_qonuniyatni_buzgan_element_tartibini_chiqar(k)
