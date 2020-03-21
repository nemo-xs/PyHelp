#
# * формирование списка из ряда введенных чисел и их сумма
# a = (int(i) for i in input().split())
# print(sum(a))

# // Или так, если дано сколько будет введено чисел на разных строках:
# n = int(input())
# print(sum(int(input()) for i in range(n)))

# // Или так, чтобы было понятней
# n = int(input())
# lst = [int(input()) for i in range(n)]
# x = sum(lst)
# print(x)

# *Подсчет длины окружности и площади круга и их сравнение
# import math as ma
# pi = ma.pi
# r = float(input("Введите радиус круга >"))

# S = int(pi * r**2)
# L = int(2 * pi * r)

# print(S)
# print(L)

# while (S > L):
#     S = int(pi * r**2)
#     L = int(2 * pi * r)
#     r = r - 0.01
# print("Радиус равен ", int(r))

# if S > L:
#     print("Площадь круга больше длины окружности"),
# else:
#     print("Длина окружности больше площади круга")

# * код для подстановки правильных окончаний в предложение

# a = 114
# if (a % 10 == 1 or a % 100 == 21) and (a % 100 != 11):
#     print(a, "програмист")
# elif ((a % 10 == 2 or a % 100 == 22 or a % 10 == 3 or a % 100 == 23
#        or a % 10 == 4 or a % 100 == 24) and a % 100 != 12 and a % 100 != 13
#       and a % 100 != 14):
#     print(a, "програмиста")
# else:
#     print(a, "програмистов")

# * Преобразование строки в числовой массив и разделение массива на 2 части
# a = "123456"
# result = [int(item) for item in a]

# print(result)
# sum1 = sum(result[0:3])
# print(sum1)
# sum2 = sum(result[3:6])
# print(sum2)

# * Подсчет букв и их архивирование типа АААаааBBccc = A3a3B2c3
# s = "AaajjjBBBgggs"
# i = 0
# n = 0
# x = 0
# s10 = ""
# while i + 1 <= len(s):
#     while i + 1 < len(s):
#         if s[i] == s[i + 1]:
#             i += 1
#         else:
#             break
#     if i + 1 == len(s):
#         n = i - x + 1
#         s10 = s10 + s[i] + str(n)
#         break
#     elif i == x:
#         i += 1
#         s10 = s10 + s[i-1] + str(1)
#         x = i
#     else:
#         n = i - x + 1
#         s10 = s10 + s[i-1] + str(n)
#         i += 1
#         x = i
# print(s10)
# // Еще один вариант (не мой)
# genome = input()+' '
# s = 0
# n = genome[0]
# for i in genome:
#     if n != i:
#         print(n + str(s), end='')
#         s, n = 0, i
#     s += 1
# // И еще один, с другой записью, но по принципу предыдущего
# s, n = 0, input()+' '
# for i in n:
#     if n[0] != i:
#         print(n[0], s, end='', sep='')
#         s, n = 0, i
#     s += 1

# * Обратная расшифровка сжатой вверху строки (функция для файлов - отдельно)

# n = "A1a2j3B3g3"
# n += 'a'
# print(n)
# s = 0
# i = 0
# for i in n:
#     if i.isalpha():
#          print(n[0] * s, end='', sep='')
#          s = 0
#          n = i
#     elif i.isdigit():
#          s = s * 10 + int(i)

# * Принимает произвольную строку с числами и выводит те, которые повторяются
# a.sort()
# n = a[-1]
# for i in a:
#     if a[0] == a[-1]:
#         print(a[0])
#         break
#     elif a.count(i) == 1 or i == n:
#         pass
#     else:
#         print(i, end=' ')
#     n = i
# // другой вариант реализации, через сравнение в set
# a = [int(i) for i in input().split()]
# for i in set(a):
#     if a.count(i) > 1:
#         print(i, end=' ')
# // тоже самое, только короче
# s = input().split()
# print(*(i for i in set(s) if s.count(i) > 1))
# * Получая на входе число, печатает количесво знаков равное этому числу, с 1
# при этом каждый знак печатается столько раз какое это число
# a = int(input())
# ran = range(1, a)
# ran2 = []
# n = 0
# if a != 0 and a != 1:
#     for i in ran:
#         ran1 = [[i] * i for i in range(a-1)]
#     for i in ran1:
#         ran2 = ran2 + i
#     ran2 = [str(i) for i in ran2]
#     ran3 = " ".join(ran2)
#     while n < a:
#         for i in ran2:
#             if n < a:
#                 print(i, end=" ")
#             n += 1
# else:
#     print(a)
# // и тоже самое, вариант с форума:
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
# * функция преобразования внутри списка (здесь берет четные и делит на два)
# def modify_list(l):
#     ls = []
#     for i in l:
#         if i % 2 != 0:
#             pass
#         else:
#             ls = ls + [i // 2]
#     l.clear()
#     l.extend(ls)
#     print(l)
# // вариант реализации с форума:
# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]
# * функция принимающая словарь и значения и модифицирующая их
# def update_dictionary(d, key, value):
#     if key in d:
#     	d[key] += [value]
#     elif (key not in d) and (2*key in d):
#         d[2*key] += [value]
#     elif 2*key not in d:
#         d[2*key] = [value]
# // вариант с форума:
# def update_dictionary(d, key, value):
#     if key in d.keys():
#         d[key].append(value)
#     elif 2*key in d.keys():
#         d[2*key].append(value)
#     else:
#         d[2*key] = [value]
# // еще один, непонятный но очень короткий:
# def update_dictionary(d, key, value):
#     key += key * (key not in d)
#     d[key] = d.get(key, []) + [value]
# * подсчет количества == слов в строке, и их вывод слово:кол-во. без учета Аа
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
# // Более полное решение для файлов
# with open("dataset_3363_3.txt") as inf:
#     for line in inf:
#         line = line.strip()
# st = line
# s = st.lower().split()
# s.sort()
# di = {}
# for i in set(s):
#     di[i] = s.count(i)

# m = max(di.values())
# print(m)
# print([i for i, value in di.items() if value == m])

# * Ввод словаря и проверка соответствий с введенной строкой

# d = int(input())
# dic = {str(input()).lower() for i in range(d)}

# li = int(input())
# lib = [str(input()).lower() for i in range(li)]
# lib = " ".join(lib)
# lib = lib.split()
# lib = set(lib)

# for i in lib:
#     if i.lower() not in dic:
#         print(i)

# * Поход черепашки по координатам
# x = 0
# y = 0
# d = int(input())
# i = 0

# while i < d:
#     dic = [map(str, input().split())]
#     dic = dict(dic)
#     for key in dic:
#         if key == 'север':
#             y = y + int(dic[key])
#         elif key == 'восток':
#             x += int(dic[key])
#         elif key == 'юг':
#             y -= int(dic[key])
#         elif key == 'запад':
#             x -= int(dic[key])
#     i += 1

# print(x, y)

# // вариант с форума решений
# x, y = 0, 0
# for i in range(int(input())):
#     s = input().split()
#     x += int(s[1])*((s[0] == 'восток')-(s[0] == 'запад'))
#     y += int(s[1])*((s[0] == 'север')-(s[0] == 'юг'))
# print(x, y)

# // и еще один
# dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}

# for _ in range(int(input())):
#     key, value = input().split()
#     dict[key] += int(value)

# print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])

#  * Класс копилка, с ограничением по объему


# class MoneyBox:
#     def __init__(self, capacity):
#         self.count = 0
#         self.capacity = capacity

#     def can_add(self, v):
#         if self.count + int(v) > self.capacity:
#             return False
#         else:
#             return True

#     def add(self, v):
#         self.count += v


# money = MoneyBox(10)
# money.add(5)
# money.add(12)
# print(money.count)
