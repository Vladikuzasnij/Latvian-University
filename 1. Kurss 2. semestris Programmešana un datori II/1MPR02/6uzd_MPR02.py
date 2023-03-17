# Programmas nosaukums: Rekursija. Pitagora koks.
# 6. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter
import math


logs = tkinter.Tk()
canvas = tkinter.Canvas(logs, bg="white", height=1000, width=1000)
canvas.pack()


def zimet_pitagora_koku(x, y, garums, lenkis, rekursijas_skaits):
    # Uzzīme Pitagora koku noteiktā vietā, izmēra un tas tiek zimēts rekursīvi "rekursijas_skaits" reizes.
    # x - x koordināta pirmā nogriežņa sākumam
    # y - y koordināta pirmā nogriežņa beigām
    # garums - garums pirmām nogriežņim. Tāda veidā tiek regulēts Pitagora koka izmērs
    # lenkis - leņķis grādos pirmām nogriežņim ar "zēmi"
    # rekursijas_skaits - rekursijas skaits. Maksimālais skaits pēc kurā zimēšana beigsies
    if rekursijas_skaits > 0:
        # print(lenkis)
        x1 = x + garums * math.cos(math.radians(lenkis))
        y1 = y - garums * math.sin(math.radians(lenkis))
        canvas.create_line(x, y, x1, y1)

        zimet_pitagora_koku(x1, y1, garums * math.sqrt(2) / 2, lenkis - 45, rekursijas_skaits - 1)
        zimet_pitagora_koku(x1, y1, garums * math.sqrt(2) / 2, lenkis + 45, rekursijas_skaits - 1)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


zimet_pitagora_koku(500, 800, 200, 90, 12)

logs.mainloop()
