def decofile(intext, outext):
    """ Декодер шифрованных по алгоритму А1 строк """
    with open(intext) as inf:
        for line in inf:
            line = line.strip()
    n = line
    n += 'a'
    print(n)
    res = ''
    s = 0
    for i in n:
        if i.isalpha():
            res = res + (n[0] * s)
            s = 0
            n = i
        elif i.isdigit():
            s = s * 10 + int(i)

    with open(outext, 'w') as ouf:
        ouf.write(res)
        ouf.write(str())


def decotext(stroka):
    stroka += 'a'
    n = stroka
    s = 0
    i = 0
    res = ''
    for i in n:
        if i.isalpha():
            res = res + (n[0] * s)
            s = 0
            n = i
        elif i.isdigit():
            s = s * 10 + int(i)
    return res


# * Заготовка под функцию кодирования/декодирования через ключ --------------
# ish = str(input())
# key = str(input())
# cod = str(input())
# decod = str(input())

# # ish = ('a', 'b', 'c', 'd')
# # key = ('*', 'd', '%', '#')
# # cod = ("a", "b", 'a', 'c', 'a', 'b', 'a', 'd', 'a', 'b', 'a')
# # decod = ('#', '*', '%', '*', 'd', '*', '%')

# coder = ''
# decoder = ''
# for i in cod:
#     # ish.index(i)
#     coder += key[ish.index(i)]
# print(coder)

# for i in decod:
#     decoder += ish[key.index(i)]
# print(decoder)
# ----------------------------------------------------------------------------