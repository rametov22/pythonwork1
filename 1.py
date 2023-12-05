import math
#1
a = float(input('а сторона квадрата: '))
print(f'периметр квадрата: {a * 4}')

#2
a = int(input('а сторона квадрата: '))
print(f'поверхность квадрата: {a ** 2}')

#3
a = int(input('а сторона прямоугольника: '))
b = int(input('b сторона прямоугольника: '))
print(f'поверхность прямоугольника: {a * b} периметр: {2 *(a+ b)}')

#4
d = int(input('диаметр круга: '))
print(f'длина круга {3.14 * d}')

#5
a = int(input('сторона куба: '))
print(f'обьем куба {a ** 3} поверхность {6 * a * a}')

#6
a = int(input('а сторона паралельпипеда'))
b = int(input('b сторона паралельпипеда'))
c = int(input('c сторона паралельпипеда'))
print(f'обьем {a * b * c} поверхность {2 * (a * b + b * c + a * c)}')

#7
r = int(input('радиус круг'))
print(f'длина {2 * math.pi * r} поверхность {math.pi * r ** 2}')

#8
a = int(input('число'))
b = int(input('число'))
print(f'среднеарифметик {(a + b // 2)}')

#9
a = int(input('число'))
b = int(input('число'))
print(f'среднегео {(a * b) ** 0.5}')

#10
a = int(input('num'))
b = int(input('num2'))
if a == 0 or b == 0:
    print('0 ga teng mas num')
print(f'yigindi {a + b} kopaytma {a * b} kv {a * a} {b * b}')

#11
a = int(input('num'))
b = int(input('num2'))
if a == 0 or b == 0:
    print('0 ga teng mas num')
print(f'yigindi {a + b} kopaytma {a * b} modul {abs(a)} {abs(b)}')

#12
a = int(input('katet1: '))
b = int(input('katet2: '))
c = math.sqrt(a ** 2 + b ** 2)
print(f'gipotenuza: {c} perimetr {a + b + c}')

#13
R1 = int(input('radius aylana 1'))
R2 = int(input('radisn aylana 2'))
s1 = 3.14 * R1
s2 = 3.14 * R2
s3 = 3.14 * (R1 - R2)
print(f'birinch yuza {s1} ikinch yuza {s2} ayirma {s3}')

#14
L = int(input('aylana uzunligi'))
R = L / (2 * math.pi)
S = math.pi * R ** 2
print(f'radius {R} yuza {S}')

#15
S = int(input('aylana yuzasi'))
d = math.sqrt(4 * S / math.pi)
R = d / 2
print(f'diametr {d} radius {R}')

#16
x1 = int(input('x birinchi nuqta'))
y1 = int(input('y birinchi nuqta'))
x2 = int(input('x ikinchi nuqta'))
y2 = int(input('y ikinchi nuqta'))
dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'ikki nuqta orasidagi masofa {dis}')

#17
xa, ya = map(float, input("Nuqta A koordinatalarini kiriting (x y): ").split())
xb, yb = map(float, input("Nuqta B koordinatalarini kiriting (x y): ").split())
xc, yc = map(float, input("Nuqta C koordinatalarini kiriting (x y): ").split())
AC = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
AB = math.sqrt((xc - xb) ** 2 + (yc - yb) ** 2)
summ = AC + AB
print(f'AC uzunligi {AC} AB uzunligi {AB} yigindi {summ}')

#18
x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 6

vec_ac = (x3 - x1, y3 - y1)
vec_bc = (x3 - x2, y3 - y2)

length_ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
length_bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
print(f'kesmalar kopaytmasi: {length_ac * length_bc}')

#19
x1, y1 = 1, 3
x2, y2 = 5, 1

a = abs(x2 - x1)
b = abs(y2 - y1)

perimetr = 2 * (a + b)

area = a * b
print(f'perimetr {perimetr} yuzasi {area}')

#20
x1, y1 = 1, 2
x2, y2 = 4, 6
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'masofa {distance}')

#21
x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 6

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

perimetr = a + b + c

area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

print(f'perimetr {perimetr} area {area}')

#22
a = int(input('первое число: '))
b = int(input('второе число: '))

a, b = b, a

print(f'a = {a} b = {b}')

#23
a = 4
b = 5
c = 6

temp = a
a = b
b = c
c = temp
print(f'a = {a} b = {b} c = {c}')

#24
a = 4
b = 5
c = 6

temp = a
a = c
c = b
b = temp
print(f'a = {a} b = {b} c = {c}')

#25
x = 2
y = 3 * x ** 6 - 6 * x ** 2 - 7
print(y)

#26
x = 4
y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
print(y)

#27
a = 5
print({a ** 2}, {a ** 4}, {a ** 8})

#28
a = 8
print({a ** 2}, {a ** 3}, {a ** 5}, {a ** 10}, {a ** 15})

#29
my_num = 45
angle_radians = my_num + math.pi / 180
print(f'gradus {my_num} teng radian{angle_radians}')

#30

angle_radians = 1.5
angle_degrees = angle_radians * 180 / math.pi
print(f'radian {angle_radians} teng gradus {angle_degrees}')

#31
temp_fahrenheit = 98.6

temp_celsius = (temp_fahrenheit - 32) * 5/9

print(f'farengeit {temp_fahrenheit} teng celciya {temp_celsius}')

#32
temp_celsius = 37.5

temp_fahrenheit = (temp_celsius * 9/5) + 32

print(f'celciya {temp_celsius} teng faregeit {temp_fahrenheit}')

#33
x = int(input("kg: "))
a = int(input("nech pul {} kg: ".format(x)))
n = int(input("kg somi (n): "))

cost_per_kg = a / x

total_cost = cost_per_kg * n
print("1 kg konfet: {:.2f} sum".format(cost_per_kg))
print("narhi {} kg konfetga: {:.2f} sum".format(n, total_cost))

#34
a = int(input('nech pul shokolad: '))
b = int(input('nech pul konfet: '))
roz = a - b

if roz > 0:
    print(f'1 kg shokolad 1 kg konfetdan {roz} sum qmat turadi')
elif roz < 0:
    print(f'1 kg konfet 1 kg shokoladan {abs(roz)} sum qmat turadi')
else:
    print('narxi bir xil')

#35

speed_lod = 100

speed_den = 50


time_lod = 4

time_den = 3

# Qayiqning yurgan yo'lini hisoblash
km_lod = speed_lod * time_lod
km_den = speed_den * time_den

next_ = km_lod - km_den

print(f"Qayiq yurgan yo'l: {km_lod} km")
print(f"Oqimga qarshi yurgan yo'l: {km_den} km")
print(f"Keyingi harakatlanish joyi: {next_} km")

#36

v1 = 50

v2 = 100

S = int(input("Masofa (km): "))

T = S / (v1 + v2)

print(f"Birinchi avtomobil {T} soatdan keyin ikkinchi avtomobildan uzoqlashadi.")


# 37

v1 = 50

v2 = 100

S = int(input("Boshlang'ich masofa (km): "))

T = S / (v1 + v2)

S_keyingi = T * (v1 + v2)

print(f"Birinchi avtomobil {T} soatdan keyin ikkinchi avtomobil bilan uzoqlashadi.")
print(f"Boshlang'ichdan keyin ular orasidagi masofa {S_keyingi} km bo'ladi.")



#38

a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

x = float(input("x ni kiriting: "))

y = a * x + b

print(f"Chiziqli tenglama {x} qiymatida y = {y}")

# 39

import math

a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
c = float(input("c ni kiriting: "))

D = b**2 - 4*a*c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Tenglama haqiqiy yechimlari: x1 = {x1}, x2 = {x2}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    x1 = complex(real_part, imag_part)
    x2 = complex(real_part, -imag_part)
    print(f"Tenglama kompleks yechimlari: x1 = {x1}, x2 = {x2}")


# 40

a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
e = float(input("e ni kiriting: "))
c = float(input("c ni kiriting: "))
d = float(input("d ni kiriting: "))
f = float(input("f ni kiriting: "))

det = a*d - b*c
det_x = e*d - b*f
det_y = a*f - e*c

x = det_x / det
y = det_y / det
    
print(f"Tenglamalar sistemasi yechimlari: x = {x}, y = {y}")
