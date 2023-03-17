# Programmas nosaukums: Četras aritmētiskās darbības ar daļskaitļiem.
# 3. uzdevums (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē četras aritmētiskās darbības ar daļskaitļiem. Piespiežot pogu =, tiek parbaudeādīts rezultāts atbilstoši, tai darbības zīmei, kas redzama uz pogas.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter # Importējam tkinter moduli


def mainit_zimi():
    cetras_zimes_mainisana_plus_minus_reizinat_dalit(button)


def cetras_zimes_mainisana_plus_minus_reizinat_dalit(ee):
    index = zimes_veidi.index(ee['text'])
    ee.config(text=zimes_veidi[(index + 1) % 4])


def saskaitit(dala_1, dala_2):
    saucejs = dala_1[1] * dala_2[1]
    skaititajs = dala_1[0] * dala_2[1] + dala_1[1] * dala_2[0]
    return (skaititajs, saucejs)


def atnemt(dala_1, dala_2):
    saucejs = dala_1[1] * dala_2[1]
    skaititajs = dala_1[0] * dala_2[1] - dala_1[1] * dala_2[0]
    return (skaititajs, saucejs)


def reizinat(dala_1, dala_2):
    skaititajs = dala_1[0] * dala_2[0]
    saucejs = dala_1[1] * dala_2[1]
    return (skaititajs, saucejs)


def dalit(dala_1, dala_2):
    skaititajs = dala_1[0] * dala_2[1]
    saucejs = dala_1[1] * dala_2[0]
    return (skaititajs, saucejs)


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def result():

    label_skaititajs_result.config(text="")
    label_saucejs_result.config(text="")
    label_minus.config(text="")
    dala_1 = (int(input_skaititajs_1.get()), int(input_saucejs_1.get()))
    dala_2 = (int(input_skaititajs_2.get()), int(input_saucejs_2.get()))

    index = zimes_veidi.index(button['text'])

    if dala_1[0] > 0 and dala_2[0] > 0 and dala_1[1] > 0 and dala_2[1] > 0:
        minus = ""

        if index == 0:
            finals = saskaitit(dala_1, dala_2)
        elif index == 1:
            finals = atnemt(dala_1, dala_2)
            if finals[0] < 0:
                finals = (abs(finals[0]), finals[1])
                minus = "-"
        elif index == 2:
            finals = reizinat(dala_1, dala_2)
        else:
            finals = dalit(dala_1, dala_2)
        gcdala_1 = gcd(finals[0], finals[1])

        label_skaititajs_result.config(text=str(finals[0] // gcdala_1))
        label_saucejs_result.config(text=str(finals[1] // gcdala_1))
        label_minus.config(text=minus)


def is_int_skaititajs_1(event):
    global parbaude_skaititajs_1
    parbaude = input_skaititajs_1.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        if input_skaititajs_1.get() == "": # ja nekas nav ierakstīts
            input_skaititajs_1.config(bg="white") #  tad iekrasosīm baltā
            submit_button['state'] = tkinter.DISABLED
            parbaude_skaititajs_1 = False # tad globalais parbaude_skaititajs_1 ir False
        else:
            input_skaititajs_1.config(bg="red")
            submit_button['state'] = tkinter.DISABLED
            parbaude_skaititajs_1 = False
    else:
        input_skaititajs_1.config(bg="white")
        parbaude_skaititajs_1 = True
    check() # Pārbaudam vai visiem entry ir ierakstīti reāli skaitli


def is_int_skaititajs_2(event):
    global parbaude_skaititajs_2
    parbaude = input_skaititajs_2.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        if input_skaititajs_2.get() == "":
            input_skaititajs_2.config(bg="white")
            submit_button['state'] = tkinter.DISABLED
            parbaude_skaititajs_2 = False
        else:
            input_skaititajs_2.config(bg="red")
            submit_button['state'] = tkinter.DISABLED
            parbaude_skaititajs_2 = False
    else:
        input_skaititajs_2.config(bg="white")
        parbaude_skaititajs_2 = True
    check()


def is_int_saucejs_1(event):
    global parbaude_saucejs_1
    parbaude = input_saucejs_1.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        if input_saucejs_1.get() == "":
            input_saucejs_1.config(bg="white")
            submit_button['state'] = tkinter.DISABLED
            parbaude_saucejs_1 = False
        else:
            input_saucejs_1.config(bg="red")
            submit_button['state'] = tkinter.DISABLED
            parbaude_saucejs_1 = False
    else:
        input_saucejs_1.config(bg="white")
        parbaude_saucejs_1 = True
    check()


def is_int_saucejs_2(event):
    global parbaude_saucejs_2
    parbaude = input_saucejs_2.get()
    try:

        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        if input_saucejs_2.get() == "":
            input_saucejs_2.config(bg="white")
            submit_button['state'] = tkinter.DISABLED
            parbaude_saucejs_2 = False
        else:
            input_saucejs_2.config(bg="red")
            submit_button['state'] = tkinter.DISABLED
            parbaude_saucejs_2 = False
    else:
        input_saucejs_2.config(bg="white")
        parbaude_saucejs_2 = True
    check()


def check(): # Pārbaude
    if parbaude_skaititajs_1 and parbaude_skaititajs_2 and parbaude_saucejs_1 and parbaude_saucejs_2: # Ja visos lodziņos ir ierakstīti reāli skaitļi
        submit_button['state'] = tkinter.ACTIVE # tad poga kļūst aktīva
    else:
        submit_button['state'] = tkinter.DISABLED # Ja kaut viena lodziņa nav ierakstīts reāls skaitļi, tad poga kļūst aktīva


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk() # Tkinter (lai izmantotu to komandas)
logs.geometry("230x185") # Loga izmēra definalsēšana
logs.title("Darbības ar daļskaitļiem.") # Windows "loga" nosaukums

zimes_veidi = ("+", "-", "x", ":")

# Labels
label_dalisanas_zime_1 = tkinter.Label(logs, text="―", font=("Arial", 25)) #
label_dalisanas_zime_1.place(x=19, y=50)

label_dalisanas_zime_2 = tkinter.Label(logs, text="―", font=("Arial", 25)) #
label_dalisanas_zime_2.place(x=71, y=50)

label_dalisanas_zime_3 = tkinter.Label(logs, text="―", font=("Arial", 25)) #
label_dalisanas_zime_3.place(x=159, y=50)

label_skaititajs_result = tkinter.Label(logs, text="", width=3)
label_skaititajs_result.place(x=166, y=52)

label_saucejs_result = tkinter.Label(logs, text="", width=3)
label_saucejs_result.place(x=166, y=80)

label_minus = tkinter.Label(logs, text="", width=0, font=("Arial", 25))
label_minus.place(x=136, y=50)


input_skaititajs_1 = tkinter.Entry(logs, width=3)
input_skaititajs_1.bind("<KeyRelease>", is_int_skaititajs_1)
input_skaititajs_1.place(x=28, y=52)

input_skaititajs_2 = tkinter.Entry(logs, width=3)
input_skaititajs_2.bind("<KeyRelease>", is_int_skaititajs_2)
input_skaititajs_2.place(x=80, y=52)


input_saucejs_1 = tkinter.Entry(logs, width=3)
input_saucejs_1.bind("<KeyRelease>", is_int_saucejs_1)
input_saucejs_1.place(x=28, y=80)

input_saucejs_2 = tkinter.Entry(logs, width=3)
input_saucejs_2.bind("<KeyRelease>", is_int_saucejs_2)
input_saucejs_2.place(x=80, y=80)


submit_button = tkinter.Button(logs, text="=", width=20, bd=1, command=result)
submit_button.place(x=103, y=65, width=25) # Parādam, kur poga tiks attēlota
submit_button['state'] = tkinter.DISABLED  # pēc noklusējuma poga ir izslēgta

button = tkinter.Button(logs, text="+", width=20, bd=1, command=mainit_zimi)
button.place(x=53, y=65, width=25) # Parādam, kur poga tiks attēlota

parbaude_skaititajs_1 = False
parbaude_skaititajs_2 = False
parbaude_saucejs_1 = False
parbaude_saucejs_2 = False

logs.mainloop() # Obligāta rindiņa, lai logs butu redzāms visu laiku
