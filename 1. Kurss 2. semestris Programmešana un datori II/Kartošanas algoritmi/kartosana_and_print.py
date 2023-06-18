
import math


def naivais_augosa(a):
    n = len(a)
    for j in range(n - 1):
        min1 = a[j]
        imin = j
        for i in range(j + 1, n):
            print(f"Comparing elements at indexes {imin} and {i}: {a}")
            if min1 > a[i]:
                min1 = a[i]
                imin = i
        a[imin] = a[j]
        a[j] = min1
        print(f"After swap: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(naivais_augosa(a))


def naivais_dilstosa(a):
    n = len(a)
    for j in range(n - 1):
        min1 = a[j]
        imin = j
        for i in range(j + 1, n):
            print(f"Comparing elements at indexes {imin} and {i}: {a}")
            if min1 < a[i]:
                min1 = a[i]
                imin = i
        a[imin] = a[j]
        a[j] = min1
        print(f"After swap: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(naivais_dilstosa(a))


def burbulis_augosa(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            print(f"Comparing elements at indexes {j} and {j + 1}: {a[j]} and {a[j + 1]}, {a}")

            if a[j] > a[j + 1]:
                print(f"Swapping elements at indexes {j} and {j + 1}")
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"After swap: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(burbulis_augosa(a))

def burbulis_dilstosa(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            print(f"Comparing elements at indexes {j} and {j + 1}: {a[j]} and {a[j + 1]}, {a}")
            if a[j] < a[j + 1]:
                print(f"Swapping elements at indexes {j} and {j + 1}")
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"After swap: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(burbulis_dilstosa(a))

def burbulis_uzlabotais_augosa(a):
    n = len(a)
    i = n - 1
    paz = True
    while paz:
        paz = False
        for j in range(0, i):
            print(f"Comparing elements at indexes {j} and {j + 1}: {a[j]} and {a[j + 1]}, {a}")
            if a[j] > a[j + 1]:
                paz = True
                print(f"Swapping elements at indexes {j} and {j + 1}")
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"After swap: {a}")
        i = i - 1
    return a


#a = [5, 2, 8, 9, 1]
# print(burbulis_uzlabotais_augosa(a))

def burbulis_uzlabotais_dilstosa(a):
    n = len(a)
    i = n - 1
    paz = True
    while paz:
        paz = False
        for j in range(0, i):
            print(f"Comparing elements at indexes {j} and {j + 1}: {a[j]} and {a[j + 1]}, {a}")
            if a[j] < a[j + 1]:
                paz = True
                print(f"Swapping elements at indexes {j} and {j + 1}")
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"After swap: {a}")
        i = i - 1
    return a


#a = [5, 2, 8, 9, 1]
# print(burbulis_uzlabotais_dilstosa(a))

def atspole_augosa(a):
    n = len(a)
    for i in range(1, n):
        print(f"Element to insert at index {i}: {a[i]}")
        if a[i - 1] > a[i]:
            for j in range(i, 0, -1):
                print(f"Comparing elements at indexes {j-1} and {j}: {a[j-1]} and {a[j]}, {a}")
                if a[j - 1] > a[j]:
                    print(f"Swapping elements at indexes {j-1} and {j}")
                    a[j], a[j - 1] = a[j - 1], a[j]
                    print(f"After swap: {a}")
                else:
                    break
    return a


#a = [5, 2, 8, 9, 1]
# print(atspole_augosa(a))

def atspole_dilstosa(a):
    n = len(a)
    for i in range(1, n):
        print(f"Element to insert at index {i}: {a[i]}")
        if a[i - 1] < a[i]:
            for j in range(i, 0, -1):
                print(f"Comparing elements at indexes {j-1} and {j}: {a[j-1]} and {a[j]}, {a}")
                if a[j - 1] < a[j]:
                    print(f"Swapping elements at indexes {j-1} and {j}")
                    a[j], a[j - 1] = a[j - 1], a[j]
                    print(f"After swap: {a}")
                else:
                    break
    return a


#a = [5, 2, 8, 9, 1]
# print(atspole_dilstosa(a))


def ievietosana_augosa(a):
    n = len(a)
    for i in range(1, n):
        print(f"Element to insert at index {i}: {a[i]}")
        if a[i - 1] > a[i]:
            x = a[i]
            j = i
            while a[j - 1] > x:
                print(f"Comparing elements at indexes {j-1} and {j}: {a[j-1]} and {x}")
                print(f"Shifting element at index {j-1} to index {j}")
                a[j] = a[j - 1]
                j = j - 1
                print(f"After shift: {a}")
                if j == 0:
                    break
            a[j] = x
            print(f"Inserting element at index {j}: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(ievietosana_augosa(a))

def ievietosana_dilstosa(a):
    n = len(a)
    for i in range(1, n):
        print(f"Element to insert at index {i}: {a[i]}")
        if a[i - 1] < a[i]:
            x = a[i]
            j = i
            while a[j - 1] < x:
                print(f"Comparing elements at indexes {j-1} and {j}: {a[j-1]} and {x}")
                print(f"Shifting element at index {j-1} to index {j}")
                a[j] = a[j - 1]
                j = j - 1
                print(f"After shift: {a}")
                if j == 0:
                    break
            a[j] = x
            print(f"Inserting element at index {j}: {a}")
    return a


#a = [5, 2, 8, 9, 1]
# print(ievietosana_dilstosa(a))

def sella_augosa(a):
    n = len(a)
    solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
    while solis >= 1:
        for k in range(0, solis):
            for i in range(solis + k, n, solis):
                print(f"Element to insert at index {i}: {a[i]}")
                if a[i - solis] > a[i]:
                    x = a[i]
                    j = i
                    while a[j - solis] > x:
                        print(f"Comparing elements at indexes {j-solis} and {j}: {a[j-solis]} and {x}")
                        print(f"Shifting element at index {j-solis} to index {j}")
                        a[j] = a[j - solis]
                        j = j - solis
                        print(f"After shift: {a}")
                        if j == k:
                            break
                    a[j] = x
                    print(f"Inserting element at index {j}: {a}")
        solis = (solis - 1) // 3
    return a


#a = [5, 2, 8, 9, 1]
# print(sella_augosa(a))

def sella_dilstosa(a):
    n = len(a)
    solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
    while solis >= 1:
        for k in range(0, solis):
            for i in range(solis + k, n, solis):
                print(f"Element to insert at index {i}: {a[i]}")
                if a[i - solis] < a[i]:
                    x = a[i]
                    j = i
                    while a[j - solis] < x:
                        print(f"Comparing elements at indexes {j-solis} and {j}: {a[j-solis]} and {x}")
                        print(f"Shifting element at index {j-solis} to index {j}")
                        a[j] = a[j - solis]
                        j = j - solis
                        print(f"After shift: {a}")
                        if j == k:
                            break
                    a[j] = x
                    print(f"Inserting element at index {j}: {a}")
        solis = (solis - 1) // 3
    return a


#a = [5, 2, 8, 9, 1]
# print(sella_dilstosa(a))

def atrais_augosa(a, sv, bv):
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            print(f"Comparing elements at indexes {i} and {j}: {a[i]} and {a[j]}, {a}")
            if lv == (a[i] > a[j]):
                print(f"Swapping elements at indexes {i} and {j}")
                a[i], a[j] = a[j], a[i]
                print(f"After swap: {a}")
                i, j = j, i
                lv = not lv
                solis = -solis
            j = j + solis
        atrais_augosa(a, sv, i - 1)
        atrais_augosa(a, i + 1, bv)
    return a


#a = [5, 2, 8, 9, 1]
# print(atrais_augosa(a, 0, 4)) # начальный и конечный индекс


def atrais_dilstosa(a, sv, bv):
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            print(f"Comparing elements at indexes {i} and {j}: {a[i]} and {a[j]}, {a}")
            if lv == (a[i] < a[j]):  # Changed comparison to < for descending order
                print(f"Swapping elements at indexes {i} and {j}")
                a[i], a[j] = a[j], a[i]
                print(f"After swap: {a}")
                i, j = j, i
                lv = not lv
                solis = -solis
            j = j + solis
        atrais_dilstosa(a, sv, i - 1)
        atrais_dilstosa(a, i + 1, bv)
    return a


a = [5, 2, 8, 9, 1]
print(atrais_dilstosa(a, 0, 4))  # начальный и конечный индекс
