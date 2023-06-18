# 1.uzd.

'''
ВВодите слова и выводит их в обратной последовательности (?)
но нужно ли в обратной?
возможно подвох и она неправильно написала программу
останавливается при XXX

ievadi: mama
ievadi vardi papa
ievadi vardi XXX
papa mama 

проблема программы
если вначале в самом XXX то всё равно дальше пойдёт

РЕКУРСИВНО ДЕЛАЕТ
'''

"""
#Original

def vardi(x):
    txt = ""
    y = input("ievadi vardi ")
    if y == "XXX":
        txt += x + " "
        return txt
    else:
        txt = vardi(y)
        txt += x + " "
        return txt


x = input("ievadi: ")
print(vardi(x))
"""

# модифицированная, если ввести XXX то ничего не выведет. Рекурсивная также.
# ВОЗВРАЩАЕТ В ОБРАТНОМ ПОРЯДКЕ (!) (так как у оригинала было, но можно вписать XXX и всё ок будет.


def words(x):
    sv = ""
    y = input("Ievadiet vārdu ==> ")
    if y == "XXX":
        sv = sv + x + " "
        return sv
    else:
        sv = words(y)
        sv = sv + x + " "
        return sv


x = ""
print(words(x))


"""
#Original zamena peremennih nazvanij

def words(x):
    sv = ""
    y = input("Ievadiet vardu ==> ")
    if y == "XXX":
        sv += x + " "
        return sv
    else:
        sv = words(y)
        sv += x + " "
        return sv


x = input("ievadi: ")
print(words(x))
"""

# --------------


'''
# модифицированная, если ввести XXX то ничего не выведет. Рекурсивная также.
# ВОЗВРАЩАЕТ В ПЕРВИЧНОМ ПОРЯДКЕ (!)


def words(x):
    sv = ""
    y = input("Ievadiet vārdu ==> ")
    if y == "XXX":
        sv = sv + x + " "
        return sv
    else:
        sv = words(y)
        sv = x + " " + sv
        return sv


x = ""
print(words(x))
'''
