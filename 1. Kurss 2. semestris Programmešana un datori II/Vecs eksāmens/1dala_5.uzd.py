'''
через множества 10 шариков с такими то номерами
берём 6 шариков промуреванных от 0 до 9
'''


import random

kopa = set()  # sākotnēji tukša izvikto lodīšu kopa

for i in range(6):
    ran = random.randint(0, 9)
    while ran in kopa:  # ja lodīte jau ir kopā kopa, tad ģenerē jaunu lodītes numuru
        ran = random.randint(0, 9)
    kopa.add(ran)
    print(str(i + 1) + ". izvilktās lodītes numurs:", ran)
