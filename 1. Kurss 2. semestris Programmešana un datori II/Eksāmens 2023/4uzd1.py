import random


def start_izloze():
    # pirmo reiz piecu lodīšu izlozi
    b = set()
    for i in range(5):
        a = random.randint(1, 49)
    while a in b:
        a = random.randint(1, 49)
    b.add(a)
    return b


def again_izloze(b):
    # atkārtots vienas lodītes lozēšana un pievieno to izlozēto lodīšu kopai
    a = random.randint(1, 49)
    while a in b:
        a = random.randint(1, 49)
    b.add(a)
    return b


lod_janis = start_izloze()  # Janisa lodites
lod_peter = start_izloze()  # pēterīša lodites
laimests = 1024
meginajumi = 1
kopigas_lodes = lod_janis.intersection(lod_peter)  # kopigas
# ja uzreiz visi 7 ir vienadi tad 1024
if len(kopigas_lodes) == 7:
    laimests = laimests
    meginajumi = meginajumi
else:
    # Ja kopigas kopas garums nav 7, tad lozesim atkal 
    while len(kopigas_lodes) < 7:
        again_izloze(lod_janis)
        again_izloze(lod_peter)
        kopigas_lodes = lod_janis.intersection(lod_peter)
    else: 
        i = len(lod_janis) - 7 
        meginajumi = i + meginajumi
        laimests = laimests / 2**i # dalam ar kapinataju

if laimests < 1: #meginajumi > 10 or laimests :
    laimests = 0
    print("Spēle tiek pārtraukta! Tika izdarīti vairāk nekā 10 mēģinājumi!\n")

print(meginajumi, "mēģinājumi tika izdarīti.")
print("Jānīša visas izvilktas lodītes:")
print(lod_janis)
print("Pēterīša visas izvilktas lodītes:")
print(lod_peter)
print("Kopīgās lodītes:")
print(kopigas_lodes)
print("Laimests:")
print(laimests, "EUR")