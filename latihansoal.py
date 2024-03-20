# # kota = ["bandung", "jakarta", "tangerang", "bekasi"]
# # provinsi = ["jawa barat", "DKI"]
# # for index, indonesia in enumerate(kota):
# #     print(index,kota)
# #
# # # for i in range(dari berapa, sampe berapa):
# #
# # #soal latihan
# # #10 9 8 7 6 5 4 3 2 1
# # #1 3 5 7 9 11 13 15 17
# #
# # for i in range(10, 0, -1):
# #     print(i, end = "")
# #
# #
# # for a in range(1,20,+2):
# #     print(a)
# #
# # ## 3. 25 20 15 10 5 0
# # for b in range(30,0,-5):
# #     print(b)
# #
# # #4. 2 4 8 16 32 64 128 256 512 1024
# #
# # c = 2
# # for i in range(10):
# #     print(c)
# #     c*=2
# #
# # # 1 3 5 7 9 11 13 15 17 19
# # a=1
# # for i in range(10):
# #     print(a)
# #     a+=2
#
# # 1 2 4 7 11 16 22 29 37 46
# a = 1
# b = 1
# for i in range(10):
#     print(a)
#     a += b
#     b += 2
#
# # soalke 3
# a = -5
# b = 3
# for i in range(10):
#     print(a)
#     a += b
#     b += 3
#
# #soal ke 4
# a = 1
# b = 0
# c = 3
# for i in range(10):
#     print(a)
#     a += b
#     b += 1
#
# #soalke5
# #semua bentuk for bisa dipindahkan ke while, tapi tidak semua while bisa dipindahkan ke for
# a = 1
# b = 1
# c = 3
# for i in range(10):
#     print(a)
#     a += b
#     b += 1
#
# #latihan soal while
# a = 1
# for i in range(3):
#     print(a, "aku cinta indonesia")
#     a += 2
#


#soal 1
a = 1
max = 3
x = 0
while (x<max):
    print(a, "aku cinta indonesia")
    x += 1
    a += 2

#soal ke 2
# 2 4 7 11 16 22
a = 2
b = 2
for i in range(6):
    print(a, end=" ")
    a += b
    b += 1

#soal 3)
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
a = 1
b = 1
print()
for i in range(3):
    print(a, "x", b, "=", b)
    b += 1

# soal 4
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
a = 7
b = 6
c = 42 #atau c = a*b
for i in range(5):
    print(a, "x", b, "=", c)
    b += 1
    c = a * b

# soal 5
# * * * *
# * * * *
# * * * *

a = "* * * *"
b = 1
for i in range(3):
    print(a)
    b += 1

# soal 6
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
baris = 3
kolom = 4
for i in range(1, baris +1):
    for j in range( kolom):
        print(i,end='')
    print()

# soal 7
# 1 1 2 3 5 8 13 21 34 55
a = 1
b = 1
c = b
for i in range(10):
    print(a, end = " ")
    c = a + b
    a = b
    b = c


#soal 8
# 1 2 3 6 11 20 37 68 125 230
a = 1
b = 2
c = 3
print()
print(a, end=" ")
print(b, end =" ")
print(c, end =" ")
for i in range(7):
    d = a + b + c
    print(d, end = " ")
    a = b
    b = c
    c = d

#soal 9
# 1 1 1 1
# 1 1 1
# 1 1
# 1
baris = 4
kolom = 4
print()
for i in range(baris):
    print()
    for j in range(kolom - i):
        print('1', end=" ")

#soal 10
# 2 3 2 3 2
# 3 2 3 2
# 2 3 2
# 3 2
# 2
print()
for i in range(5):
    print()
    for j in range(5,i,-1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(3, end=" ")
            else:
                print(2, end=" ")
        else :
            if j % 2 == 1:
                print(3, end=" ")
            else :
                print(2, end=" ")















