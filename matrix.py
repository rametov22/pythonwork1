# 1
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# matrix = [[10 * i for i in range(n)] for i in range(m)]
#
# for row in matrix:
#     print(row)

# 2
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[5 * j for j in range(n)] for i in range(m)]
#
# # Natijani chiqarish
# for row in matrix:
#     print(row)

# 3
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# row_sum = int(input("Har bir ustun uchun m ta sondan iborat yig'indini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[row_sum * j for j in range(n)] for i in range(m)]
#
# # Natijani chiqarish
# for row in matrix:
#     print(row)

# # 4
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# column_sum = int(input("Har bir satri uchun n ta sondan iborat yig'indini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[column_sum * i for j in range(n)] for i in range(m)]
#
# # Natijani chiqarish
# for row in matrix:
#     print(row)

# 5
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# row_sum = int(input("Birinchi satri uchun m ta sondan iborat yig'indini kiriting: "))
# d = int(input("Arifmetik progressiyada qo'shiladigan d sonini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = []
#
# for i in range(m):
#     row = [row_sum * j for j in range(n)]
#     matrix.append(row)
#     row_sum += d
#
# # Natijani chiqarish
# for row in matrix:
#     print(row)

# 6
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# row_sum = int(input("Birinchi satri uchun m ta sondan iborat yig'indini kiriting: "))
# q = int(input("Geometrik progressiyada ko'paytiriladigan q sonini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = []
#
# for i in range(m):
#     row = [row_sum * q**j for j in range(n)]
#     matrix.append(row)
#     row_sum *= q
#
# # Natijani chiqarish
# for row in matrix:
#     print(row)

# 7
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# k = int(input("K satrini kiriting (0 dan {0} gacha): ".format(m - 1)))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # K-satrini chiqarish
# print("K-satr: ", matrix[k])

# 8
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
# k = int(input("K ustunini kiriting (0 dan {0} gacha): ".format(n - 1)))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # K-ustunini chiqarish
# print("K-ustun: ", [matrix[i][k] for i in range(m)])

# 9
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # 2 ga karrali satrlarni chiqarish
# for i in range(0, m, 2):
#     print(matrix[i])

# 10
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # Toq indeksli ustunlarni chiqarish
# for i in range(1, n, 2):
#     print([matrix[j][i] for j in range(m)])

# 11
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # Elementlarni chiqarish
# for i in range(m):
#     if i % 2 == 0:
#         print(matrix[i])
#     else:
#         print(matrix[i][::-1])

# 12
# m = int(input("M qiymatini kiriting: "))
# n = int(input("N qiymatini kiriting: "))
#
# # Matritsa hosil qilish
# matrix = [[i * n + j for j in range(n)] for i in range(m)]
#
# # Elementlarni chiqarish
# for j in range(n):
#     if j % 2 == 0:
#         print([matrix[i][j] for i in range(m)])
#     else:
#         print([matrix[i][j] for i in range(m)][::-1])

# 13
# M = int(input("Matritsa o'lchamini kiriting (M): "))
#
# matrix = [[i * M + j for j in range(M)] for i in range(M)]
#
# for i in range(M):
#     print(matrix[i])
#
# print(matrix[0])
# print([matrix[i][-1] for i in range(1, M)])
# print(matrix[M-1][:-1])
# print([matrix[i][-2::-1] for i in range(M-2, 0, -1)])
# print([matrix[-1][0]])

# 14
# M = int(input("Matritsa o'lchamini kiriting (M): "))
#
# # M x M olchamli matritsa hosil qilish
# matrix = [[i * M + j for j in range(M)] for i in range(M)]
#
# # Matritsaning elementlarini chiqarish (burchak hosil qilgan tartibda)
# for i in range(M):
#     print(matrix[i])  # birinchi ustunning barcha elementlari
#
# print([matrix[i][-1] for i in range(1, M)])  # oxirgi satrning barcha elementlari
#
# for i in range(1, M):
#     print([matrix[i][j] for j in range(M-2, -1, -1)])  # ikkinchi ustunning qolgan elementlari
#
# print([matrix[-2-i][::-1] for i in range(M-2)])  # oxirdan bir oldingi satrning qolgan elementlari
#
# print([matrix[0][-1]])  # xakazo, oxirida A0, M-1 element

# 15
# N = int(input("Matritsa o'lchamini kiriting (N): "))
#
# # NxN olchamli matritsa hosil qilish
# matrix = [[0] * N for _ in range(N)]
#
# counter = 1
#
# # Matritsa elementlariga sonlarni joylash
# for layer in range(N // 2 + N % 2):
#     for j in range(layer, N - layer):
#         matrix[layer][j] = counter
#         counter += 1
#
#     for i in range(layer + 1, N - layer):
#         matrix[i][N - layer - 1] = counter
#         counter += 1
#
#     for j in range(N - layer - 2, layer - 1, -1):
#         matrix[N - layer - 1][j] = counter
#         counter += 1
#
#     for i in range(N - layer - 2, layer, -1):
#         matrix[i][layer] = counter
#         counter += 1
#
# # Matritsani ekranga chiqarish
# for row in matrix:
#     print(row)

# 16
# N = int(input("Matritsa o'lchamini kiriting (N): "))
#
# # NxN olchamli matritsa hosil qilish
# matrix = [[0] * N for _ in range(N)]
#
# counter = 1
#
# # Matritsa elementlariga sonlarni joylash
# for layer in range(N // 2 + N % 2):
#     for j in range(layer, N - layer):
#         matrix[layer][j] = counter
#         counter += 1
#
#     for i in range(layer + 1, N - layer):
#         matrix[i][N - layer - 1] = counter
#         counter += 1
#
#     for j in range(N - layer - 2, layer - 1, -1):
#         matrix[N - layer - 1][j] = counter
#         counter += 1
#
#     for i in range(N - layer - 2, layer, -1):
#         matrix[i][layer] = counter
#         counter += 1
#
# # Matritsani ekranga chiqarish
# for row in matrix:
#     print(row)

# 17
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
# k = int(input("K - satrini kiriting (0 dan {0} gacha): ".format(m - 1)))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # K - satri elementlarini yig'indisi
# s_sum = sum(matrix[k])
#
# # K - satri elementlarini kopaytmasi
# s_product = 1
# for element in matrix[k]:
#     s_product *= element
#
# # Natijani chiqarish
# print("K - satri elementlarining yig'indisi:", s_sum)
# print("K - satri elementlarining kopaytmasi:", s_product)

# 18
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
# k = int(input("K - ustunini kiriting (0 dan {0} gacha): ".format(n - 1)))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # K - ustuni elementlarining yig'indisi
# s_sum = sum(matrix[i][k] for i in range(m))
#
# # K - ustuni elementlarining kopaytmasi
# s_product = 1
# for i in range(m):
#     s_product *= matrix[i][k]
#
# # Natijani chiqarish
# print("K - ustuni elementlarining yig'indisi:", s_sum)
# print("K - ustuni elementlarining kopaytmasi:", s_product)

# 19
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satri elementlarini yig'indisi
# row_sums = [sum(matrix[i]) for i in range(m)]
#
# # Natijani chiqarish
# for i in range(m):
#     print("Satri {} elementlarining yig'indisi: {}".format(i, row_sums[i]))

# 20
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuni elementlarining kopaytmasi
# column_products = [1] * n
#
# for j in range(n):
#     for i in range(m):
#         column_products[j] *= matrix[i][j]
#
# # Natijani chiqarish
# for j in range(n):
#     print("Ustun {} elementlarining kopaytmasi: {}".format(j, column_products[j]))

# 21
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satri uchun toq indeks ustunlarining orta arifmetigi
# for i in range(m):
#     row = matrix[i]
#     odd_columns = [row[j] for j in range(1, n, 2)]
#
#     if len(odd_columns) > 0:
#         average = sum(odd_columns) / len(odd_columns)
#         print("Satri {} uchun toq indeks ustunlarining orta arifmetigi: {}".format(i, average))
#     else:
#         print("Satri {} uchun toq indeks ustunlarining orta arifmetigi: Satri uchun toq indeks ustuni yo'q".format(i))

# 22
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuni uchun 2 ga karrali satrlarning yig'indisi
# for j in range(n):
#     column = [matrix[i][j] for i in range(0, m, 2)]
#     sum_of_even_rows = sum(column)
#     print("Ustun {} uchun 2 ga karrali satrlarning yig'indisi: {}".format(j, sum_of_even_rows))

# 23
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satrning eng kichik elementini chiqarish
# for i in range(m):
#     min_element = min(matrix[i])
#     print("Satri {} eng kichik elementi: {}".format(i, min_element))

# 24
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuning eng katta elementini chiqarish
# for i in range(m):
#     max_element = max(matrix[i])
#     print("Ustun {} eng katta elementi: {}".format(i, max_element))

# 25
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Matritsa har bir satri elementlarini yig'indisi
# max_row_sum = 0
# max_row_index = 0
#
# for i in range(m):
#     row_sum = sum(matrix[i])
#     if row_sum > max_row_sum:
#         max_row_sum = row_sum
#         max_row_index = i
#
# # Natijani chiqarish
# print("Eng katta yig'indi satri indeksi:", max_row_index)
# print("Eng katta yig'indi:", max_row_sum)

# 26
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuning elementlarining kopaytmasi
# min_column_product = float('inf')
# min_column_index = 0
#
# for j in range(n):
#     column_product = 1
#     for i in range(m):
#         column_product *= matrix[i][j]
#
#     if column_product < min_column_product:
#         min_column_product = column_product
#         min_column_index = j
#
# # Natijani chiqarish
# print("Eng kichik kopaytma ustuni indeksi:", min_column_index)
# print("Eng kichik kopaytma:", min_column_product)

# 27
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satri elementlarini yig'indisi va eng kichik yig'indining indeksi
# min_row_sum = float('inf')
# min_row_index = 0
#
# for i in range(m):
#     row_sum = sum(matrix[i])
#
#     if row_sum < min_row_sum:
#         min_row_sum = row_sum
#         min_row_index = i
#
# # Natijani chiqarish
# print("Eng kichik yig'indi satri indeksi:", min_row_index)
# print("Eng kichik yig'indi:", min_row_sum)

# 28
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuning elementlarining yig'indisi va eng kichik element
# max_column_sum = float('-inf')
# min_column_element = float('inf')
# min_column_index = 0
#
# for j in range(n):
#     column_sum = sum(matrix[i][j] for i in range(m))
#
#     if column_sum > max_column_sum:
#         max_column_sum = column_sum
#         min_column_index = j
#
#     min_element = min(matrix[i][j] for i in range(m))
#     if min_element < min_column_element:
#         min_column_element = min_element
#
# # Natijani chiqarish
# print("Eng katta yig'indi ustuni indeksi:", min_column_index)
# print("Eng kichik element ustuni:", min_column_element)

# 29
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satri uchun, shu satri orta arifmetigidan kichik bo'lgan elementlar soni
# for i in range(m):
#     row = matrix[i]
#     average = sum(row) / n
#
#     count = sum(1 for element in row if element < average)
#
#     print("Satri {} uchun, shu satri orta arifmetigidan kichik bo'lgan elementlar soni: {}".format(i, count))

# 30
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustun uchun, shu ustun orta arifmetigidan katta bo'lgan elementlar soni
# for j in range(n):
#     column = [matrix[i][j] for i in range(m)]
#     average = sum(column) / m
#
#     count = sum(1 for element in column if element > average)
#
#     print("Ustun {} uchun, shu ustun orta arifmetigidan katta bo'lgan elementlar soni: {}".format(j, count))

# 31
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Matritsa barcha elementlarini orta arifmetigiga qarab, eng yaqin satri va ustunni topish
# global_average = sum(sum(row) for row in matrix) / (m * n)
#
# min_row_difference = float('inf')
# min_row_index = 0
#
# min_column_difference = float('inf')
# min_column_index = 0
#
# for i in range(m):
#     row_average = sum(matrix[i]) / n
#     row_difference = abs(global_average - row_average)
#
#     if row_difference < min_row_difference:
#         min_row_difference = row_difference
#         min_row_index = i
#
# for j in range(n):
#     column_average = sum(matrix[i][j] for i in range(m)) / m
#     column_difference = abs(global_average - column_average)
#
#     if column_difference < min_column_difference:
#         min_column_difference = column_difference
#         min_column_index = j
#
# # Natijani chiqarish
# print("Matritsa barcha elementlarining orta arifmetigi:", global_average)
# print("Eng yaqin satri:", min_row_index)
# print("Eng yaqin ustun:", min_column_index)

# 32
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir satri uchun musbat va manfiy elementlar sonini hisoblash
# for i in range(m):
#     positive_count = sum(1 for element in matrix[i] if element > 0)
#     negative_count = sum(1 for element in matrix[i] if element < 0)
#
#     # Agar musbat va manfiy elementlar soni teng bo'lsa
#     if positive_count == negative_count and positive_count > 0:
#         print("Birinchi uchragan satri:", i)
#         break
# else:
#     # Agar birinchi uchragan satri topilmasa
#     print("Bunday satr yo'q")

# 33
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Har bir ustuni uchun musbat va manfiy elementlar sonini hisoblash
# for j in range(n):
#     positive_count = sum(1 for i in range(m) if matrix[i][j] > 0)
#     negative_count = sum(1 for i in range(m) if matrix[i][j] < 0)
#
#     # Agar musbat va manfiy elementlar soni teng bo'lsa
#     if positive_count == negative_count and positive_count > 0:
#         last_column = j
#         break
# else:
#     # Agar bunday ustun topilmagan bo'lsa
#     print("Bunday ustun yo'q")
# else:
# # Agar birinchi uchragan satri topilmasa
# print("Oxirgi ustun:", last_column)

# 34
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Oxirgi juft sonlardan iborat bolgan satrni aniqlash
# last_even_row = None
#
# for i in range(m):
#     row = matrix[i]
#     if all(element % 2 == 0 for element in row):
#         last_even_row = i
#
# # Natijani chiqarish
# if last_even_row is not None:
#     print("Oxirgi juft sonlardan iborat bolgan satr:", last_even_row)
# else:
#     print("Bunday satr yo'q")

# 35
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Faqat juft sonlardan iborat bolgan birinchi ustunni aniqlash
# first_even_column = None
#
# for j in range(n):
#     column = [matrix[i][j] for i in range(m)]
#     if all(element % 2 == 0 for element in column):
#         first_even_column = j
#         break
#
# # Natijani chiqarish
# if first_even_column is not None:
#     print("Faqat juft sonlardan iborat bolgan birinchi ustun:", first_even_column)
# else:
#     print("Bunday ustun yo'q")

# 36
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Massivning har xil satrlari oxshash bo'lgan birinchi satrga oxshash bolgan satrlarning sonini aniqlash
# first_duplicate_row = None
#
# for i in range(m):
#     row = matrix[i]
#     for j in range(i + 1, m):
#         if matrix[j] == row:
#             first_duplicate_row = i
#             break
#     if first_duplicate_row is not None:
#         break
#
# # Natijani chiqarish
# if first_duplicate_row is not None:
#     print("Massivning har xil satrlari oxshash bo'lgan birinchi satrga oxshash bolgan satrlar soni:", first_duplicate_row)
# else:
#     print("Bunday satr yo'q")

# 37
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Massivning har xil ustunlari oxshash bo'lgan oxirgi ustunga oxshash bolgan ustunlarning sonini aniqlash
# last_duplicate_column = None
#
# for j in range(n):
#     column = [matrix[i][j] for i in range(m)]
#     for k in range(j + 1, n):
#         if [matrix[i][k] for i in range(m)] == column:
#             last_duplicate_column = j
#             break
#     if last_duplicate_column is not None:
#         break
#
# # Natijani chiqarish
# if last_duplicate_column is not None:
#     print("Massivning har xil ustunlari oxshash bo'lgan oxirgi ustunga oxshash bolgan ustunlar soni:", last_duplicate_column)
# else:
#     print("Bunday ustun yo'q")

# 38
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Elementlari har xil bo'lgan satrlarni aniqlash
# duplicate_rows = []
#
# for i in range(m):
#     row = matrix[i]
#     if row not in duplicate_rows and matrix.count(row) > 1:
#         duplicate_rows.append(row)
#
# # Natijani chiqarish
# if duplicate_rows:
#     print("Elementlari har xil bo'lgan satrlar soni:", len(duplicate_rows))
# else:
#     print("Bunday satr yo'q")

# 39
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Elementlari har xil bo'lgan ustunlarni aniqlash
# duplicate_columns = []
#
# for j in range(n):
#     column = [matrix[i][j] for i in range(m)]
#     if column not in duplicate_columns and matrix.count(column) > 1:
#         duplicate_columns.append(column)
#
# # Natijani chiqarish
# if duplicate_columns:
#     print("Elementlari har xil bo'lgan ustunlar soni:", len(duplicate_columns))
# else:
#     print("Bunday ustun yo'q")

# 40
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Elementlari har xil bo'lgan ustunlarni aniqlash
# max_count = 0
# common_elements = []
#
# for i in range(m):
#     for j in range(n):
#         current_element = matrix[i][j]
#         current_count = sum(1 for row in matrix for element in row if element == current_element)
#
#         if current_count > max_count:
#             max_count = current_count
#             common_elements = [current_element]
#         elif current_count == max_count and current_element not in common_elements:
#             common_elements.append(current_element)
#
# # Natijani chiqarish
# if common_elements:
#     print("Bir xil elementlar soni eng ko'p bo'lgan elementlar:", common_elements)
# else:
#     print("Bunday element yo'q")

# 41
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = [[int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)] for i in range(m)]
#
# # Elementlari har xil bo'lgan ustunlarni aniqlash
# max_count = 0
# common_elements = []
# common_column = None
#
# for j in range(n):
#     column = [matrix[i][j] for i in range(m)]
#     current_count = sum(1 for col in matrix if col == column)
#
#     if current_count > max_count:
#         max_count = current_count
#         common_elements = column
#         common_column = j
#
# # Natijani chiqarish
# if common_elements:
#     print(f"Bir xil elementlar soni eng ko'p bo'lgan birinchi ustun (ustun {common_column}):", common_elements)
# else:
#     print("Bunday ustun yo'q")

# 42
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = []
# for i in range(m):
#     row = [int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)]
#     matrix.append(row)
#
# # Elementlari osish tartibida kiritilgan satrlar sonini aniqlash
# sorted_rows = sorted(matrix)
#
# if sorted_rows == matrix:
#     print("Elementlari osish tartibida kiritilgan satrlar soni: {}".format(m))
# else:
#     print("Elementlari osish tartibida kiritilgan satrlar yo'q")

# 43
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = []
# for i in range(m):
#     row = [int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)]
#     matrix.append(row)
#
# # Elementlari kamayish tartibida kiritilgan ustunlar sonini aniqlash
# sorted_columns = [list(column) for column in zip(*sorted(zip(*matrix)))]
#
# if sorted_columns == matrix:
#     print("Elementlari kamayish tartibida kiritilgan ustunlar soni: {}".format(n))
# else:
#     print("Elementlari kamayish tartibida kiritilgan ustunlar yo'q")

# 44
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = []
# for i in range(m):
#     row = [int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)]
#     matrix.append(row)
#
# # Elementlari kamayish tartibida kiritilgan satrlar orasidan eng kichik qiymatni aniqlash
# min_value = float('inf')
#
# for i in range(1, m):
#     if matrix[i] < matrix[i - 1]:
#         min_value = min(min(matrix[i]), min_value)
#
# # Natijani chiqarish
# if min_value != float('inf'):
#     print("Elementlari kamayish tartibida kiritilgan satrlar orasidan eng kichik qiymat:", min_value)
# else:
#     print(0)

# 45
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = []
# for i in range(m):
#     row = [int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)]
#     matrix.append(row)
#
# # Elementlari kamayish tartibida kiritilgan ustunlar orasidan eng katta qiymatni aniqlash
# max_value = float('-inf')
#
# for j in range(1, n):
#     if all(matrix[i][j] >= matrix[i][j - 1] for i in range(m)):
#         max_value = max(max(matrix[i][j] for i in range(m)), max_value)
#
# # Natijani chiqarish
# if max_value != float('-inf'):
#     print("Elementlari kamayish tartibida kiritilgan ustunlar orasidan eng katta qiymat:", max_value)
# else:
#     print(0)

# 46
# m = int(input("Matritsa yuqori o'lchamini kiriting (m): "))
# n = int(input("Matritsa chap o'lchamini kiriting (n): "))
#
# # Matritsa hosil qilish
# matrix = []
# for i in range(m):
#     row = [int(input("matrix[{}][{}]: ".format(i, j))) for j in range(n)]
#     matrix.append(row)
#
# # Ozi turgan satrda eng kattasi va ozi turgan ustunda eng kichigi bo'lgan elementni aniqlash
# result = 0
#
# for i in range(m):
#     max_in_row = max(matrix[i])
#     min_in_column = min(matrix[i][j] for j in range(n))
#
#     if matrix[i][matrix[i].index(max_in_row)] == min_in_column:
#         result = matrix[i][matrix[i].index(max_in_row)]
#         break
#
# # Natijani chiqarish
# print(result)

# 47
#
# def almashuvuv(matritsa, k1, k2):
#     # Matritsa elementlarini almashuvish
#     for i in range(len(matritsa)):
#         matritsa[i][k1], matritsa[i][k2] = matritsa[i][k2], matritsa[i][k1]
#
#
# # Matritsani tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # k1 va k2 ni tanlash
# k1 = 0
# k2 = 2
#
# # almashuvuvni amalga oshirish
# almashuvuv(matritsa, k1, k2)
#
# # Natijani chop etish
# for row in matritsa:
#     print(row)
#
#
# # 48
#
# def ustunlarni_chiqar(matritsa, k1, k2):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # To'g'ri k1 va k2 qiymatlari berilganligini tekshirish
#     if 0 <= k1 < k2 < n:
#         # Ustunlarni chiqarish
#         for i in range(m):
#             del matritsa[i][k1:k2 + 1]
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Noto'g'ri k1 va k2 qiymatlari berilgan.")
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # k1 va k2 ni tanlash
# k1 = 1
# k2 = 2
#
# # Ustunlarni chiqarishni amalga oshirish
# ustunlarni_chiqar(matritsa, k1, k2)
#
#
# # 49
#
# def element_almashuv(matritsa):
#     m = len(matritsa)
#     c = len(matritsa[0])
#
#     for i in range(m):
#         # Har bir satr uchun eng kichik va eng katta elementlarni topish
#         eng_kichik = min(matritsa[i])
#         eng_katta = max(matritsa[i])
#
#         # Eng kichik va eng katta elementlarni almashuvish
#         eng_kichik_index = matritsa[i].index(eng_kichik)
#         eng_katta_index = matritsa[i].index(eng_katta)
#
#         matritsa[i][eng_kichik_index], matritsa[i][eng_katta_index] = matritsa[i][eng_katta_index], matritsa[i][
#             eng_kichik_index]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # Elementlarni almashuvishni amalga oshirish
# element_almashuv(matritsa)
#
#
# # 50
#
# def element_almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     for j in range(n):
#         # Har bir ustun uchun eng kichik va eng katta elementlarni topish
#         ustun_elements = [matritsa[i][j] for i in range(m)]
#         eng_kichik = min(ustun_elements)
#         eng_katta = max(ustun_elements)
#
#         # Eng kichik va eng katta elementlarni o'rinlarini topish
#         eng_kichik_index = ustun_elements.index(eng_kichik)
#         eng_katta_index = ustun_elements.index(eng_katta)
#
#         # Eng kichik va eng katta elementlarni almashuvish
#         matritsa[eng_kichik_index][j], matritsa[eng_katta_index][j] = matritsa[eng_katta_index][j], \
#                                                                       matritsa[eng_kichik_index][j]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # Elementlarni almashuvishni amalga oshirish
# element_almashuv(matritsa)
#
#
# # 51
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Har bir ustun uchun eng kichik va eng katta elementlarni topish
#     eng_kichik = min([min(row) for row in matritsa])
#     eng_katta = max([max(row) for row in matritsa])
#
#     # Eng kichik va eng katta elementlarni joylashgan satrlarni topish
#     eng_kichik_satr = [i for i, row in enumerate(matritsa) if eng_kichik in row]
#     eng_katta_satr = [i for i, row in enumerate(matritsa) if eng_katta in row]
#
#     # Eng kichik va eng katta elementlarni joylashgan satrlarni almashuvish
#     for i in range(n):
#         matritsa[eng_kichik_satr[0]][i], matritsa[eng_katta_satr[0]][i] = matritsa[eng_katta_satr[0]][i], \
#                                                                           matritsa[eng_kichik_satr[0]][i]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 52
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Har bir ustun uchun eng kichik va eng katta elementlarni topish
#     eng_kichik = min([min(row) for row in matritsa])
#     eng_katta = max([max(row) for row in matritsa])
#
#     # Eng kichik va eng katta elementlarni joylashgan ustunlarni topish
#     eng_kichik_ustun = [j for j in range(n) if eng_kichik in [matritsa[i][j] for i in range(m)]]
#     eng_katta_ustun = [j for j in range(n) if eng_katta in [matritsa[i][j] for i in range(m)]]
#
#     # Eng kichik va eng katta elementlarni joylashgan ustunlarni almashuvish
#     for i in range(m):
#         matritsa[i][eng_kichik_ustun[0]], matritsa[i][eng_katta_ustun[0]] = matritsa[i][eng_katta_ustun[0]], \
#                                                                             matritsa[i][eng_kichik_ustun[0]]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 53
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Dastlabki ustunni tanlash
#     dastlabki_ustun = matritsa[0]
#
#     # Faqat musbat elementlarni olish
#     musbatlar = [element for element in dastlabki_ustun if element > 0]
#
#     # Agar musbat elementlar mavjud bo'lsa, ularni joylashgan eng oxirgi ustunni topish
#     if musbatlar:
#         eng_oxirgi_ustun_index = matritsa.index([musbatlar[-1]])
#
#         # Eng oxirgi ustunni olish
#         eng_oxirgi_ustun = matritsa[eng_oxirgi_ustun_index]
#
#         # Eng oxirgi ustunni dastlabki ustun bilan almashuvish
#         matritsa[0], matritsa[eng_oxirgi_ustun_index] = eng_oxirgi_ustun, dastlabki_ustun
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, -7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 54
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Oxirgi ustunni tanlash
#     oxirgi_ustun = matritsa[-1]
#
#     # Faqat manfiy elementlarni olish
#     manfiylar = [element for element in oxirgi_ustun if element < 0]
#
#     # Agar manfiy elementlar mavjud bo'lsa, ularni joylashgan eng birinchi ustunni topish
#     if manfiylar:
#         eng_birinchi_ustun_index = matritsa.index([manfiylar[0]])
#
#         # Eng birinchi ustunni olish
#         eng_birinchi_ustun = matritsa[eng_birinchi_ustun_index]
#
#         # Eng birinchi ustunni oxirgi ustun bilan almashuvish
#         matritsa[-1], matritsa[eng_birinchi_ustun_index] = eng_birinchi_ustun, oxirgi_ustun
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, -7, 5],
#     [2, 8, 4],
#     [1, 6, 9]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 55
#
# def yarim_almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Teng yarimdan yuqorisini va pastini topish
#     yuqori_yarim = matritsa[:m // 2]
#     pastki_yarim = matritsa[m // 2:]
#
#     # Teng yarimni va pastki yarimni almashuvish
#     matritsa[:m // 2], matritsa[m // 2:] = pastki_yarim, yuqori_yarim
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
#
# # almashuvishni amalga oshirish
# yarim_almashuv(matritsa)
#
#
# # 56
#
# def chap_ong_almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Teng yonidan chap va ong qismini topish
#     chap_qisim = [row[:n // 2] for row in matritsa]
#     ong_qisim = [row[n // 2:] for row in matritsa]
#
#     # Teng yonini va ong qismini almashuvish
#     for i in range(m):
#         matritsa[i][:n // 2], matritsa[i][n // 2:] = ong_qisim[i], chap_qisim[i]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # almashuvishni amalga oshirish
# chap_ong_almashuv(matritsa)
#
#
# # 57
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Matritsani 4 qisimiga bo'lish
#     chap_tuqori = [row[:n // 2] for row in matritsa[:m // 2]]
#     ong_yuqori = [row[n // 2:] for row in matritsa[:m // 2]]
#     chap_past = [row[:n // 2] for row in matritsa[m // 2:]]
#     ong_past = [row[n // 2:] for row in matritsa[m // 2:]]
#
#     # 1-va va 4-qisimlarni almashuvish
#     for i in range(m // 2):
#         matritsa[i][:n // 2], matritsa[i + m // 2][n // 2:] = ong_past[i], chap_tuqori[i]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 58
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Matritsani 4 qisimiga bo'lish
#     chap_yuqori = [row[:n // 2] for row in matritsa[:m // 2]]
#     ong_yuqori = [row[n // 2:] for row in matritsa[:m // 2]]
#     chap_past = [row[:n // 2] for row in matritsa[m // 2:]]
#     ong_past = [row[n // 2:] for row in matritsa[m // 2:]]
#
#     # 2-va va 3-qisimlarni almashuvish
#     for i in range(m // 2):
#         matritsa[i + m // 2][:n // 2], matritsa[i][:n // 2] = ong_past[i], chap_past[i]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 59
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     for i in range(m // 2):
#         if i % 2 == 0:
#             matritsa[i], matritsa[m - i - 1] = matritsa[m - i - 1], matritsa[i]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 60
#
# def almashuv(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     for j in range(n // 2):
#         if j % 2 == 0:
#             for i in range(m):
#                 matritsa[i][j], matritsa[i][n - j - 1] = matritsa[i][n - j - 1], matritsa[i][j]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # almashuvishni amalga oshirish
# almashuv(matritsa)
#
#
# # 61
#
# def satr_ochir(matritsa, k):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if 0 <= k < m:
#         del matritsa[k]
#     else:
#         print("Xatolik: Noto'g'ri k qiymati")
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# k = 2  # O'chirilayotgan satr indeksi
# satr_ochir(matritsa, k)
#
#
# # 62
#
# def ustun_ochir(matritsa, k):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if 0 <= k < n:
#         for i in range(m):
#             del matritsa[i][k]
#     else:
#         print("Xatolik: Noto'g'ri k qiymati")
#
#
# # Natijani chop etish
# for row in matritsa:
#     print(row)
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# k = 2  # O'chirilayotgan ustun indeksi
# ustun_ochir(matritsa, k)
#
#
# # 63
#
# def kichik_satrni_ochir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if m > 1:
#         # Eng kichik elementni topish
#         eng_kichik_element = matritsa[0][0]
#         for i in range(m):
#             for j in range(n):
#                 if matritsa[i][j] < eng_kichik_element:
#                     eng_kichik_element = matritsa[i][j]
#
#         # Eng kichik elementni joylashgan satrni o'chirish
#         for i in range(m):
#             if eng_kichik_element in matritsa[i]:
#                 del matritsa[i]
#                 break
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Matritsa faqat bitta satrni o'z ichiga olishi mumkin emas")
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, 2, 3, 4],
#     [1, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# kichik_satrni_ochir(matritsa)
#
#
# # 64
#
# def katta_ustunni_ochir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if n > 1:
#         # Eng katta elementni topish
#         eng_katta_element = matritsa[0][0]
#         for i in range(m):
#             for j in range(n):
#                 if matritsa[i][j] > eng_katta_element:
#                     eng_katta_element = matritsa[i][j]
#
#         # Eng katta elementni joylashgan ustunni o'chirish
#         for j in range(n):
#             if eng_katta_element in [matritsa[i][j] for i in range(m)]:
#                 for i in range(m):
#                     del matritsa[i][j]
#                 break
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Matritsa faqat bitta ustunni o'z ichiga olishi mumkin emas")
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, 2, 3, 4],
#     [1, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# katta_ustunni_ochir(matritsa)
#
#
# # 65
#
# def musbat_ustun_ochir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Faqat musbat elementlardan tashkil topgan birinchi uchragan ustunni o'chirish
#     for j in range(n):
#         if all(matritsa[i][j] > 0 for i in range(m)):
#             for i in range(m):
#                 del matritsa[i][j]
#             break
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, -2, 3, 4],
#     [1, 6, 7, 8],
#     [9, 10, 11, -12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# musbat_ustun_ochir(matritsa)
#
#
# # 66
#
# def musbat_ustun_ochir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     print(musbat_ustun_ochir)
#
#
# # 67
#
# def musbat_ustunlarni_ochir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Faqat musbat elementlardan tashkil topgan barcha ustunlarni o'chirish
#     ustun_indekslari = [j for j in range(n) if all(matritsa[i][j] > 0 for i in range(m))]
#
#     # Ustunlarni o'chirish
#     for j in reversed(ustun_indekslari):
#         for i in range(m):
#             del matritsa[i][j]
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, -2, 3, 4],
#     [1, 6, 7, 8],
#     [9, 10, 11, -12],
#     [13, 14, 15, 16]
# ]
#
# # O'chirishni amalga oshirish
# musbat_ustunlarni_ochir(matritsa)
#
#
# # 68
#
# def qo_shish(matritsa, k):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if 0 <= k < m:
#         qo_shiladigan_satr = None
#
#         # Matritsadan k-satri oldindan elementlari qiymati teng bo'lgan satrni topish
#         for i in range(k):
#             if all(matritsa[i][j] == matritsa[k][j] for j in range(n)):
#                 qo_shiladigan_satr = matritsa[i]
#                 break
#
#         # Agar topilgan bo'lsa uni matritsaga qo'shish
#         if qo_shiladigan_satr:
#             matritsa.append(qo_shiladigan_satr)
#         else:
#             print(f"Xatolik: {k}-satri oldindan elementlari qiymati teng bo'lgan satr topilmadi")
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Xatolik: Noto'g'ri k qiymati")
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 3, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# k = 2  # Qo'shiladigan satr indeksi
# qo_shish(matritsa, k)
#
#
# # 69
#
# def qo_shish(matritsa, k):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     if 0 <= k < n:
#         qo_shiladigan_ustun = None
#
#         # Matritsadan k-ustunidan keyin elementlari qiymati birga teng bo'lgan ustunni topish
#         for j in range(k + 1, n):
#             if all(matritsa[i][j] == matritsa[i][k] for i in range(m)):
#                 qo_shiladigan_ustun = [matritsa[i][j] for i in range(m)]
#                 break
#
#         # Agar topilgan bo'lsa uni matritsaga qo'shish
#         if qo_shiladigan_ustun:
#             for i in range(m):
#                 matritsa[i].extend(qo_shiladigan_ustun)
#         else:
#             print(f"Xatolik: {k}-ustunidan keyin elementlari qiymati birga teng bo'lgan ustun topilmadi")
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Xatolik: Noto'g'ri k qiymati")
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 6, 8],
#     [9, 10, 10, 12],
#     [13, 14, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# k = 2  # Qo'shiladigan ustun indeksi
# qo_shish(matritsa, k)
#
#
# # 70
#
# def qo_shish(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     eng_katta_element = matritsa[0][0]
#     eng_katta_element_indeks = (0, 0)
#
#     # Matritsadan eng katta element va uning indeksini topish
#     for i in range(m):
#         for j in range(n):
#             if matritsa[i][j] > eng_katta_element:
#                 eng_katta_element = matritsa[i][j]
#                 eng_katta_element_indeks = (i, j)
#
#     # Eng katta elementni joylashgan satrni o'qib olamiz
#     eng_katta_element_satr_indeksi = eng_katta_element_indeks[0]
#
#     # Eng katta element joylashgan satrdan keyin yana shunday satrni qo'shish
#     qo_shiladigan_satr = matritsa[eng_katta_element_satr_indeksi][:]
#     matritsa.insert(eng_katta_element_satr_indeksi + 1, qo_shiladigan_satr)
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 9, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# qo_shish(matritsa)
#
#
# # 71
#
# def qo_shish(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     eng_kichik_element = matritsa[0][0]
#     eng_kichik_element_indeks = (0, 0)
#
#     # Matritsadan eng kichik element va uning indeksini topish
#     for i in range(m):
#         for j in range(n):
#             if matritsa[i][j] < eng_kichik_element:
#                 eng_kichik_element = matritsa[i][j]
#                 eng_kichik_element_indeks = (i, j)
#
#     # Eng kichik elementni joylashgan ustunni o'qib olamiz
#     eng_kichik_element_ustun_indeksi = eng_kichik_element_indeks[1]
#
#     # Eng kichik element joylashgan ustundan keyin yana shunday ustunni qo'shish
#     for i in range(m):
#         qo_shiladigan_ustun_element = matritsa[i][eng_kichik_element_ustun_indeksi]
#         matritsa[i].insert(eng_kichik_element_ustun_indeksi + 1, qo_shiladigan_ustun_element)
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 1, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# qo_shish(matritsa)
#
#
# # 72
#
# def qo_shish(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     qo_shiladigan_ustun_indeksi = -1
#
#     # Faqat musbat elementlardan tashkil topgan birinchi uchragan ustundan oldin elementlari qiymati birga teng bo'lgan ustunni topish
#     for j in range(1, n):
#         if all(matritsa[i][j] == matritsa[i][j - 1] for i in range(m)) and all(matritsa[i][j] > 0 for i in range(m)):
#             qo_shiladigan_ustun_indeksi = j
#             break
#
#     # Agar topilgan bo'lsa, uni matritsaga qo'shish
#     if qo_shiladigan_ustun_indeksi != -1:
#         for i in range(m):
#             qo_shiladigan_ustun_element = matritsa[i][qo_shiladigan_ustun_indeksi]
#             matritsa[i].insert(qo_shiladigan_ustun_indeksi, qo_shiladigan_ustun_element)
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Bunday ustun topilmadi. Matritsa o'zgarishsiz chiqariladi.")
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 2, 3, 4],
#     [5, 6, 6, 7, 8],
#     [9, 10, 10, 11, 12],
#     [13, 14, 15, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# qo_shish(matritsa)
#
#
# # 73
#
# def qo_shish(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     qo_shiladigan_ustun_indeksi = -1
#
#     # Faqat manfiy elementlardan tashkil topgan oxirgi ushragan ustundan keyin elementlari qiymati nolga teng bo'lgan ustunni topish
#     for j in range(n - 2, -1, -1):
#         if all(matritsa[i][j] == matritsa[i][j + 1] for i in range(m)) and all(matritsa[i][j] < 0 for i in range(m)):
#             qo_shiladigan_ustun_indeksi = j + 1
#             break
#
#     # Agar topilgan bo'lsa, uni matritsaga qo'shish
#     if qo_shiladigan_ustun_indeksi != -1:
#         for i in range(m):
#             qo_shiladigan_ustun_element = matritsa[i][qo_shiladigan_ustun_indeksi]
#             matritsa[i].insert(qo_shiladigan_ustun_indeksi, qo_shiladigan_ustun_element)
#
#         # Natijani chop etish
#         for row in matritsa:
#             print(row)
#     else:
#         print("Bunday ustun topilmadi. Matritsa o'zgarishsiz chiqariladi.")
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, -2, -2, 3, 4],
#     [5, 6, -6, -6, 7, 8],
#     [9, 10, -10, -10, 11, 12],
#     [13, 14, -15, -15, 15, 16]
# ]
#
# # Qo'shishni amalga oshirish
# qo_shish(matritsa)
#
#
# # 74
#
# def lokal_minimum(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     for i in range(1, m - 1):
#         for j in range(1, n - 1):
#             current_element = matritsa[i][j]
#
#             # Elementni barcha tomonlari bilan solishtiramiz
#             top_element = matritsa[i - 1][j]
#             bottom_element = matritsa[i + 1][j]
#             left_element = matritsa[i][j - 1]
#             right_element = matritsa[i][j + 1]
#
#             # Agar element barcha tomonlari bilan kichik bo'lsa, elementni nolga almashtiramiz
#             if current_element < top_element and current_element < bottom_element and \
#                     current_element < left_element and current_element < right_element:
#                 matritsa[i][j] = 0
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, 3, 2, 4, 5],
#     [2, 1, 0, 3, 2],
#     [8, 7, 1, 6, 3],
#     [4, 5, 2, 7, 4]
# ]
#
# # Lokal minimumlarni topish va nolga almashtirish
# lokal_minimum(matritsa)
#
#
# # 75
#
# def lokal_maksimum(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     for i in range(1, m - 1):
#         for j in range(1, n - 1):
#             current_element = matritsa[i][j]
#
#             # Elementni barcha tomonlari bilan solishtiramiz
#             top_element = matritsa[i - 1][j]
#             bottom_element = matritsa[i + 1][j]
#             left_element = matritsa[i][j - 1]
#             right_element = matritsa[i][j + 1]
#
#             # Agar element barcha tomonlari bilan katta bo'lsa, elementni nolga almashtiramiz
#             if current_element > top_element and current_element > bottom_element and \
#                     current_element > left_element and current_element > right_element:
#                 matritsa[i][j] = 0
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [5, 3, 2, 4, 5],
#     [2, 8, 0, 3, 2],
#     [8, 7, 9, 6, 3],
#     [4, 5, 2, 7, 4]
# ]
#
# # Lokal maksimumlarni topish va nolga almashtirish
# lokal_maksimum(matritsa)
#
#
# # 76
#
# def satrlarni_ozgartir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Matritsa satrlarini o'zgartirish
#     matritsa.sort(key=lambda row: row[n - 1])
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 1, 4, 2, 9],
#     [7, 6, 5, 8, 0],
#     [9, 2, 1, 5, 7],
#     [4, 0, 3, 6, 1]
# ]
#
# # Satrlarni o'zgartirish va natijani chop etish
# satrlarni_ozgartir(matritsa)
#
#
# # 77
#
# def ustunlarni_ozgartir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Matritsa ustunlarini o'zgartirish
#     transposed_matritsa = list(map(list, zip(*matritsa)))
#     transposed_matritsa.sort(key=lambda col: col[m - 1])
#
#     # Natijani chop etish
#     for row in list(map(list, zip(*transposed_matritsa))):
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 1, 4, 2, 9],
#     [7, 6, 5, 8, 0],
#     [9, 2, 1, 5, 7],
#     [4, 0, 3, 6, 1]
# ]
#
# # Ustunlarni o'zgartirish va natijani chop etish
# ustunlarni_ozgartir(matritsa)
#
#
# # 78
#
# def ustunlarni_ozgartir(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Matritsa ustunlarini o'zgartirish
#     transposed_matritsa = list(map(list, zip(*matritsa)))
#     transposed_matritsa.sort(key=lambda col: col[m - 1], reverse=True)
#
#     # Natijani chop etish
#     for row in list(map(list, zip(*transposed_matritsa))):
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 1, 4, 2, 9],
#     [7, 6, 5, 8, 0],
#     [9, 2, 1, 5, 7],
#     [4, 0, 3, 6, 1]
# ]
#
# # Ustunlarni o'zgartirish va natijani chop etish
# ustunlarni_ozgartir(matritsa)
#
#
# # 79
#
# def satrlarni_tartiblash(matritsa):
#     m = len(matritsa)
#     n = len(matritsa[0])
#
#     # Satrlarni minimal va maksimal elementlari o'sish tartibida bo'ladigan tartibda tartiblash
#     matritsa.sort(key=lambda row: (min(row), max(row)))
#
#     # Natijani chop etish
#     for row in matritsa:
#         print(row)
#
#
# # Matriksni tanlash
# matritsa = [
#     [3, 1, 4, 2, 9],
#     [7, 6, 5, 8, 0],
#     [9, 2, 1, 5, 7],
#     [4, 0, 3, 6, 1]
# ]
#
# # Satrlarni tartiblash va natijani chop etish
# satrlarni_tartiblash(matritsa)
#
#
# # 80
#
#
# def asosiy_dioganal_yigindisi(matritsa):
#     m = len(matritsa)
#     yigindi = 0
#
#     for i in range(m):
#         yigindi += matritsa[i][i]
#
#     return yigindi
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy dioganal elementlarni yig'indisini chiqarish
# yigindi = asosiy_dioganal_yigindisi(matritsa)
# print("Asosiy dioganal elementlarning yig'indisi:", yigindi)
#
#
# # 81
#
#
# def yordamchi_dioganal_orasining_arifmetigi(matritsa):
#     m = len(matritsa)
#     arifmetik_yigindi = 0
#
#     for i in range(m):
#         arifmetik_yigindi += matritsa[i][i]  # Asosiy diagonal element
#         arifmetik_yigindi += matritsa[i][m - i - 1]  # Yordamchi diagonal element
#
#     arifmetik_yigindi /= (2 * m)  # O'rta arifmetigi hisoblash
#
#     return arifmetik_yigindi
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Yordamchi diagonal elementlarning o'rta arifmetigini chiqarish
# arifmetik_yigindi = yordamchi_dioganal_orasining_arifmetigi(matritsa)
# print("Yordamchi diagonal elementlarning o'rta arifmetigi:", arifmetik_yigindi)
#
#
# # 82
#
# def diagonal_yigindisi(matritsa):
#     m = len(matritsa)
#     yigindilar = []
#
#     for i in range(m):
#         diagonal_element = matritsa[i][i]
#         yigindilar.append(diagonal_element)
#
#     return yigindilar
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning yig'indisini chiqarish
# yigindilar = diagonal_yigindisi(matritsa)
# for i, yigindisi in enumerate(yigindilar, start=1):
#     print(f"A[{i}] yig'indisi: {yigindisi}")
#
#
# # 83
#
# def diagonal_yigindisi(matritsa):
#     m = len(matritsa)
#     yigindilar = [0] * (2 * m - 1)
#
#     for i in range(m):
#         for j in range(m):
#             yigindilar[i + j] += matritsa[i][j]
#
#     return yigindilar
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning yig'indisini chiqarish
# yigindilar = diagonal_yigindisi(matritsa)
# for i, yigindisi in enumerate(yigindilar, start=1):
#     print(f"A[{i}] yig'indisi: {yigindisi}")
#
#
# # 84
#
# def diagonal_yigindisi(matritsa):
#     m = len(matritsa)
#     yigindilar = [0] * (2 * m - 1)
#
#     for i in range(m):
#         for j in range(m):
#             yigindilar[i + j] += matritsa[i][j]
#
#     return yigindilar
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning yig'indisini chiqarish
# yigindilar = diagonal_yigindisi(matritsa)
# for i, yigindisi in enumerate(yigindilar, start=1):
#     print(f"A[{i}] yig'indisi: {yigindisi}")
#
#
# # 85
#
# def eng_katta_diagonal_element(matritsa):
#     m = len(matritsa)
#     eng_katta_element = None
#
#     for i in range(m):
#         diagonal_element = matritsa[i][i]
#
#         if eng_katta_element is None or diagonal_element > eng_katta_element:
#             eng_katta_element = diagonal_element
#
#     return eng_katta_element
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning eng kattasini chiqarish
# eng_katta_element = eng_katta_diagonal_element(matritsa)
# print("Eng katta diagonal element:", eng_katta_element)
#
#
# # 86
#
# def eng_kichik_diagonal_element(matritsa):
#     m = len(matritsa)
#     eng_kichik_element = None
#
#     for i in range(m):
#         diagonal_element = matritsa[i][i]
#
#         if eng_kichik_element is None or diagonal_element < eng_kichik_element:
#             eng_kichik_element = diagonal_element
#
#     return eng_kichik_element
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning eng kichigini chiqarish
# eng_kichik_element = eng_kichik_diagonal_element(matritsa)
# print("Eng kichik diagonal element:", eng_kichik_element)
#
#
# # 87
#
# def eng_katta_diagonal_element(matritsa):
#     m = len(matritsa)
#     eng_katta_element = None
#
#     for i in range(m):
#         diagonal_element = matritsa[i][i]
#
#         if eng_katta_element is None or diagonal_element > eng_katta_element:
#             eng_katta_element = diagonal_element
#
#     return eng_katta_element
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonalga parallel bo'lgan har bir diagonal elementning eng kattasini chiqarish
# eng_katta_element = eng_katta_diagonal_element(matritsa)
# print("Eng katta diagonal element:", eng_katta_element)
#
#
# # 88
#
# def asosiy_diagonalni_nolga_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(i + 1, m):  # asosiy diagonalni pastdagi elementlar
#             matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonal va undan pastdagi elementlarni nolga almashtirish
# yangi_matritsa = asosiy_diagonalni_nolga_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 89
#
# def yordamchi_diagonalni_nolga_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(0, i):  # yordamchi diagonal va undan yuqoridagi elementlar
#             matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Yordamchi diagonal va undan yuqoridagi elementlarni nolga almashtirish
# yangi_matritsa = yordamchi_diagonalni_nolga_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
# 
# # 90
#
#
# def yordamchi_diagonalni_nolga_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(i, m):  # yordamchi diagonal va undan pastdagi elementlar
#             matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Yordamchi diagonal va undan pastdagi elementlarni nolga almashtirish
# yangi_matritsa = yordamchi_diagonalni_nolga_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 91
#
# def asosiy_diagonal_va_yuqoridagi_nolga_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(0, i + 1):  # asosiy diagonal va undan yuqoridagi elementlar
#             matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonal va undan yuqoridagi elementlarni nolga almashtirish
# yangi_matritsa = asosiy_diagonal_va_yuqoridagi_nolga_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 92
#
#
# def diagonal_va_undan_yuqoridagi_nolga_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(0, m):  # asosiy diagonal va yordamchi diagonal elementlari
#             if i == j or j < i:
#                 matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Asosiy diagonal va undan yuqoridagi elementlarni nolga almashtirish
# yangi_matritsa = diagonal_va_undan_yuqoridagi_nolga_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 93
#
# def h_shakli(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(m):
#             if i != m // 2 and j != m // 2:
#                 matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # "h" shakli bo'yalgan sohanini nolga almashtirish
# yangi_matritsa = h_shakli(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 94
#
# def i_shakli(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(m):
#             if i != j:
#                 matritsa[i][j] = 0
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # "i" shakli bo'yalgan sohanini nolga almashtirish
# yangi_matritsa = i_shakli(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 95
#
#
# def f_shakli(matritsa):
#     m = len(matritsa)
#     for i in range(m):
#         for j in range(m):
#             matritsa[i][j] = 0 if i + j == m - 1 else matritsa[i][j]
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # "f" shakli bo'yalgan sohanini nolga almashtirish
# yangi_matritsa = f_shakli(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 96
#
# def asosiy_diagonaldan_nisbatan_almashtir(matritsa):
#     m = len(matritsa)
#
#     for i in range(m):
#         for j in range(m):
#             matritsa[i][j] = matritsa[i][i]  # asosiy diagonal elementlariga nisbatan almashtirish
#
#     return matritsa
#
#
# # Matriksni tanlash
# matritsa = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# # Asosiy diagonalga nisbatan elementlarni almashtirish
# yangi_matritsa = asosiy_diagonaldan_nisbatan_almashtir(matritsa)
# for row in yangi_matritsa:
#     print(row)
#
#
# # 97
#
# def almashtir(matritsa):
#     m = len(matritsa)
#     for i in range(m):
#         matritsa[i][i], matritsa[i][m - i - 1] = matritsa[i][m - i - 1], matritsa[i][i]
#
#
# # Matritsaning o'lchamini olish
# m = int(input("Matritsa o'lchamini kiriting: "))
#
# # Matritsa elementlarini olish
# matritsa = []
# print(f"{m} x {m} matritsa elementlarini kiriting:")
# for _ in range(m):
#     qator = [int(x) for x in input().split()]
#     matritsa.append(qator)
#
# # Almashtiruvchi funksiyani chaqirish
# almashtir(matritsa)
#
# # Natijani chiqarish
# print("Almashtirilgan matritsa:")
# for qator in matritsa:
#     print(qator)
#
#
# # 98
#
# def buruvchi(matritsa):
#     m = len(matritsa)
#
#     # Transponatsiya
#     transponovan_matritsa = [[matritsa[j][i] for j in range(m)] for i in range(m)]
#
#     # Har bir qatorni teskari tartibda qo'yish
#     for i in range(m):
#         matritsa[i] = matritsa[i][::-1]
#
#     # Transponatsiyalangan matritsani teskari tartibda qo'yish
#     for i in range(m):
#         transponovan_matritsa[i] = transponovan_matritsa[i][::-1]
#
#     # Matritsaning o'zini teskari tartibda qo'yish
#     matritsa = matritsa[::-1]
#
#     return matritsa
#
#
# # Matritsaning o'lchamini olish
# m = int(input("Matritsa o'lchamini kiriting: "))
#
# # Matritsa elementlarini olish
# matritsa = []
# print(f"{m} x {m} matritsa elementlarini kiriting:")
# for _ in range(m):
#     qator = [int(x) for x in input().split()]
#     matritsa.append(qator)
#
# # Buruvchi funksiyani chaqirish
# natija = buruvchi(matritsa)
#
# # Natijani chiqarish
# print("Buruvchilangan matritsa:")
# for qator in natija:
#     print(qator)
#
#
# # 99
#
# def buruvchi(matritsa):
#     m = len(matritsa)
#
#     # Transponatsiya
#     transponovan_matritsa = [[matritsa[j][i] for j in range(m)] for i in range(m)]
#
#     # Har bir qatorni teskari tartibda qo'yish
#     for i in range(m):
#         matritsa[i] = matritsa[i][::-1]
#
#     # Transponatsiyalangan matritsani teskari tartibda qo'yish
#     for i in range(m):
#         transponovan_matritsa[i] = transponovan_matritsa[i][::-1]
#
#     # Matritsaning o'zini teskari tartibda qo'yish
#     matritsa = matritsa[::-1]
#
#     return transponovan_matritsa
#
#
# # Matritsaning o'lchamini olish
# m = int(input("Matritsa o'lchamini kiriting: "))
#
# # Matritsa elementlarini olish
# matritsa = []
# print(f"{m} x {m} matritsa elementlarini kiriting:")
# for _ in range(m):
#     qator = [int(x) for x in input().split()]
#     matritsa.append(qator)
#
# # Buruvchi funksiyani chaqirish
# natija = buruvchi(matritsa)
#
# # Natijani chiqarish
# print("90 ga soat strelkasiga qarama qarshi buruvchilangan matritsa:")
# for qator in natija:
#     print(qator)
#
#
# # 100
#
#
# def buruvchi(matritsa):
#     m = len(matritsa)
#
#     # Transponatsiya
#     transponovan_matritsa = [[matritsa[j][i] for j in range(m)] for i in range(m)]
#
#     # Matritsaning o'zini teskari tartibda qo'yish
#     matritsa = matritsa[::-1]
#
#     return transponovan_matritsa
#
#
# # Matritsaning o'lchamini olish
# m = int(input("Matritsa o'lchamini kiriting: "))
#
# # Matritsa elementlarini olish
# matritsa = []
# print(f"{m} x {m} matritsa elementlarini kiriting:")
# for _ in range(m):
#     qator = [int(x) for x in input().split()]
#     matritsa.append(qator)
#
# # Buruvchi funksiyani chaqirish
# natija = buruvchi(matritsa)
#
# # Natijani chiqarish
# print("90 ga soat strelkasiga bo'yicha buruvchilangan matritsa:")
# for qator in natija:
#     print(qator)





