
import random
import numpy as np


def parveide_sv_to_mas(sv, m):
    # Transformē simbolu virkni par masīvu ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    # sv - simbolu virkne, kura sastāv no cipariem
    # m - garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    n = len(sv)
    a = np.arange(m)
    for i in range(n):
        a[i] = int(sv[-i - 1])
    for i in range(n, m):
        a[i] = 0
    return a


def parveide_mas_to_sv(a):
    # Transformē masīvu par simbolu virkni. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
    # a - viendimensijas masīvs
    n = len(a)
    sv = ""
    for i in range(n):
        sv = str(a[i]) + sv

    try:  # try/except gadījumam ja 0 + 0
        while sv[0] == "0":
            sv = sv[1:]
        return sv

    except IndexError:  # Tas ir nepieciešams gadījumam ja lietotājs ievadīs 0 + 0 = 0.
        return "0"  # bez šim rindām būtu kļūda, kad 0 + 0


def get_sub(a, b):
    # Atņem masīvu a no b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) atņemšanai. Atgriež simbolu virkni bez nullem priekšā
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs
    if str(a) == str(b):
        return "0"

    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        n = n1
    else:
        n = n2
    m1 = parveide_sv_to_mas(a, n)
    m2 = parveide_sv_to_mas(b, n)
    m3 = numpy.zeros(n, dtype=numpy.int_)

    for i in range(-1, -n1, -1):
        if m1[i] < m2[i]:
            m1[i - 1] = m1[i - 1] - 1
            m1[i] = m1[i] + 10

    for i in range(n):
        m3[i] = m1[i] - m2[i]

    a = parveide_mas_to_sv(m3)
    a = a[::-1]
    a = remove_front_zeros(a)
    return a


def remove_front_zeros(s):
    # Atgriež simbolu virkni bez nullem priekšā
    # s - simbolu virkne, kura sastav no cipariem, potenciāli ar nullēm priekšā
    i = 0
    while i < len(s) - 1 and s[i] == '0':
        i += 1
    s = s[i:]
    return s


def get_sum(a, b):
    # Saskaita masīvu a un b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) saskaitīšanu
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs
    a = a[::-1]
    b = b[::-1]
    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        n = n1
    else:
        n = n2
    m1 = parveide_sv_to_mas(a, n)
    m2 = parveide_sv_to_mas(b, n)
    m3 = np.zeros(n + 1, dtype=np.int_)

    s = 0
    for i in range(n):
        s = s + m1[i] + m2[i]
        m3[i] = s % 10
        s = s // 10
    m3[n] = s

    return parveide_mas_to_sv(m3)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------

#a = parveide_sv_to_mas(a, len(a))
#b = parveide_sv_to_mas(b, len(b))
#print(saskaitisana(a, b))


def get_array_from_string(string):
    return np.array([int(char) for char in string], dtype=int)


def array_to_int(arr):
    if isinstance(arr, np.ndarray):
        return int(''.join(map(str, arr)))
    else:
        return arr


def get_mul(a, b):
    # Multiplies array a and b using long multiplication
    # a - one-dimensional array
    # b - one-dimensional array

    a = a[::-1]
    b = b[::-1]

    m = np.zeros(len(a) + len(b), dtype=int)

    for i in range(len(a)):
        for j in range(len(b)):
            m[i + j] += int(a[i]) * int(b[j])
            m[i + j + 1] += m[i + j] // 10
            m[i + j] %= 10

    # Remove leading zeros
    while len(m) > 1 and m[-1] == 0:
        m = m[:-1]

    return m[::-1]


def karatsuba(num1, num2):
    if len(num1) < 10 or len(num2) < 10:
        return get_mul(num1, num2)

    n = max(len(num1), len(num2))

    half = n // 2

    num1_high = num1[:half]
    num1_low = num1[half:]

    num2_high = num2[:half]
    num2_low = num2[half:]

    ac = array_to_int(karatsuba(num1_high, num2_high))
    bd = array_to_int(karatsuba(num1_low, num2_low))
    ad_plus_bc = array_to_int(karatsuba(get_sum(num1_high, num1_low), get_sum(num2_high, num2_low))) - ac - bd

    prod = ac * 10**(2 * half) + ad_plus_bc * 10**half + bd
    #prod = ac * 10**(2 * half) + ad_plus_bc * 10**half + bd

    return prod


def input_big_number():
    return input("Please enter a big number: ")


'''
# Test examples
num1_str = input_big_number()
num2_str = input_big_number()

num1_arr = get_array_from_string(num1_str)
num2_arr = get_array_from_string(num2_str)

# Print the result of Karatsuba multiplication
kara = karatsuba(num1_arr, num2_arr)
print("Karatsuba multiplication result: ", kara)
sumer = int(num1_str) * int(num2_str)
print(int(num1_str) * int(num2_str))
if int(sumer) == int(kara):
    print("OK")
elif int(sumer) != int(kara):
    print("FALSE")
'''

# for i in range(1233, 10000):
#    for j in range(4300, 10000):

for i in range(5555555555555555, 555555555555555555555555555555555):  # 50000, 1000000
    for j in range(5555555555555555, 555555555555555555555555555555555):  # 50000, 1000000
        num1_str = str(i)
        num2_str = str(j)
        num1_arr = get_array_from_string(num1_str)
        num2_arr = get_array_from_string(num2_str)
        kara = karatsuba(num1_arr, num2_arr)
        print("Karatsuba multiplication result: ", array_to_int(kara))
        ok = i * j
        print("prosto:", ok)
        if array_to_int(kara) == ok:
            print(str(i) + " * " + str(j))
            print(str(ok) + " = " + str(array_to_int(kara)))
            print("OK")
        elif array_to_int(kara) != ok:
            print(str(i) + " * " + str(j))
            print(str(ok) + " != " + str(array_to_int(kara)))
            print("ERROR")


'''
for i in range(50000, 1000000):
    for j in range(50000, 1000000):
        num1_str = str(i)
        num2_str = str(j)
        num1_arr = get_array_from_string(num1_str)
        num2_arr = get_array_from_string(num2_str)
        kara = karatsuba(num1_arr, num2_arr)
        print("Karatsuba multiplication result: ", array_to_int(kara))
        ok = i * j
        print("prosto:", ok)
        if array_to_int(kara) == ok:
            print("OK")
        elif array_to_int(kara) != ok:
            print("ERROR")
'''

'''
def get_string_from_array(array):
    string = ""
    for i in range(len(array)):
        string += str(array[i])
    return string


def get_new_number_as_string():
    lidz = random.randint(1000, 2000)
    n1 = ""
    for i in range(lidz):
        n1 += chr(random.randint(48, 57))
    return n1


def make_adjusted(num, n):
    result = np.zeros(n, dtype=int)
    i = 0
    while (i < n):
        if (i < n - len(num)):
            result[i] = 0
        else:
            result[i] = num[i - (n - len(num))]
        i += 1
    return result


for i in range(10):
    num1 = get_new_number_as_string()
    num2 = get_new_number_as_string()

    if not num1.isnumeric() or not num2.isnumeric():
        print("Beidzam sadarbību")
        quit()

    num1 = get_array_from_string(str(num1))
    num2 = get_array_from_string(str(num2))

    if len(num1) < len(num2):
        num1 = make_adjusted(num1, len(num2))
    elif len(num2) < len(num1):
        num2 = make_adjusted(num2, len(num1))

    result = karatsuba(num1, num2)
    result2 = get_mul(num1, num2)

    print(result)
    print(result2)
'''
