# Programmas nosaukums: Karšu kavas izdali
# 4. uzdevums (1MPR10_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē kāršu kavas uzdali 4 spēlētājiem pa 6 kārtīm katram spēlētajam
# un paziņo, kādas kārtis katrs spēlētajs ir saņemis.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

# ♣ ♦ ♥ ♠
# 2 3 4 5 6 7 8 9 10 J Q K A

import random


def karsu_izdale_n_speletajiem_pa_m_kartim(n, m):
    # Atgriež simbolu virknī šāda veidā ar spēlētaju kārtu un viņa kārtem:
    # 1.spēlētājs: ♦6 ♦5 ♠J ♠5 ♠8 ♣A
    # 2.spēlētājs: ♦8 ♠9 ♥6 ♠4 ♣9 ♥Q
    # 3.spēlētājs: ♠7 ♣7 ♠6 ♦10 ♠K ♥4
    # ...
    # n.spēlētajs: ...
    # To vajag print'ēt atsevišķi print(karsu_izdale_n_speletajiem_pa_m_kartim(4, 6))

    # n - int - spēlētaju skaits (naturāls skaitlis)
    # m - int - karšu skaits (naturāls skaitlis)

    a = set(("♣", "♦", "♥", "♠"))
    b = set(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))

    c = set()

    for i in a:
        for j in b:
            c.add(i + j)

    res = ""
    for i in range(1, n + 1):
        sv = str(i) + ".spēlētājs:"
        for j in range(m):
            sv = sv + " " + c.pop()
        res = res + sv + "\n"
    return res


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


print("Kāršu kavas izdale 4 spēlētājiem pa 6 kārtīm katram spēlētājam:\n")
print(karsu_izdale_n_speletajiem_pa_m_kartim(4, 6))
