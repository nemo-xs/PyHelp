def max3(z, a):   # значения здесь - могут быть условные (как неизвестные) или
    if z > a:     # известными. Они никак не связаны с конкретными переменными
        return z,   # вернуть
    else:           # "Иначе"" (его можно вообще убирать - лишний оператор)
        return a


# print(max3("ab", "bc"))   # Параметры берутся из памяти (последние значения,)
# # или можно их прописывать числами, или любыми сравниваемыми значениями
# # непосредственно здесь, в скобках (если прописать x и y - возьмет из памяти)


def hello1(name1="World"):
    print("Hi", name1)


hello1()