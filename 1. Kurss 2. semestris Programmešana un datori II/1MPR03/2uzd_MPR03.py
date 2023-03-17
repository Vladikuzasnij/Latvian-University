# Programmas nosaukums: Serpinska paklājs.
# 2. uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido Serpinska paklāju, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import tkinter


def zimet_serpinska_paklaju(x, y, izmers):
    # Uzzīmē Serpinska paklāju
    # x - kreisa augšēja koordināta x Serpinska paklājam
    # y - kreisa augšēja koordināta y Serpinska paklājam
    if izmers < 5:
        kanva.create_rectangle(x, y, x + izmers, y + izmers, fill="black", outline="")
    else:
        maz_izmers = izmers / 3
        zimet_serpinska_paklaju(x, y, maz_izmers)
        zimet_serpinska_paklaju(x + maz_izmers, y, maz_izmers)
        zimet_serpinska_paklaju(x + 2 * maz_izmers, y, maz_izmers)
        zimet_serpinska_paklaju(x, y + maz_izmers, maz_izmers)
        zimet_serpinska_paklaju(x + 2 * maz_izmers, y + maz_izmers, maz_izmers)
        zimet_serpinska_paklaju(x, y + 2 * maz_izmers, maz_izmers)
        zimet_serpinska_paklaju(x + maz_izmers, y + 2 * maz_izmers, maz_izmers)
        zimet_serpinska_paklaju(x + 2 * maz_izmers, y + 2 * maz_izmers, maz_izmers)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
logs.geometry("1000x1000")
logs.title("Rekursija")
kanva = tkinter.Canvas(logs, width=1000, height=1000, bg="white")
kanva.pack()

zimet_serpinska_paklaju(100, 100, 800)

logs.mainloop()
