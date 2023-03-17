# Programmas nosaukums: Četras aritmētiskās darbības ar daļskaitļiem.
# Papilduzdevums 1 (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē četras aritmētiskās darbības ar daļskaitļiem. Piespiežot pogu =, tiek parādīts rezultāts atbilstoši, tai darbības zīmei, kas redzama uz pogas.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter # Importējam tkinter moduli

# ----------- Pirmās daļas pārbaudīšāna --------------


def is_skaititajs_1_mazaks_saucejs_1(a1, d1):
    global parbaude_skaititajam_1
    if a1 <= d1:
        parbaude_skaititajam_1 = True
    else:
        parbaude_skaititajam_1 = False


def is_skaititajs_2_mazaks_saucejs_2(b1, e1):
    global parbaude_skaititajam_2
    if b1 <= e1:
        parbaude_skaititajam_2 = True
    else:
        parbaude_skaititajam_2 = False


def is_pareizs_vesela_dala_1():
    global parbaude_veselais_1
    parbaude = input_veselais_1.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
    except:
        parbaude_veselais_1 = False
    else:
        parbaude_veselais_1 = True


def is_pareizs_skaititajs_1():
    global parbaude_skaititajam_1, parbaude_saucejam_1

    parbaude = input_skaititajs_1.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
    except:
        parbaude_skaititajam_1 = False
    else:
        a1 = input_skaititajs_1.get()
        d1 = input_skaititajs_2.get()
        is_skaititajs_1_mazaks_saucejs_1(a1, d1)


def is_pareizs_saucejs_1():
    global parbaude_skaititajam_1, parbaude_saucejam_1
    parbaude = input_skaititajs_2.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        parbaude_saucejam_1 = False

    else:
        d1 = input_skaititajs_2.get()
        a1 = input_skaititajs_1.get()
        is_skaititajs_1_mazaks_saucejs_1(a1, d1)
        parbaude_saucejam_1 = True


# ---------------------------------------------------
# ----------- Otrās daļas pārbaudīšāna --------------


def is_pareiza_vesela_dala_2():
    global parbaude_veselais_2
    parbaude = input_veselais_2.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
    except:
        parbaude_veselais_2 = False

    else:
        parbaude_veselais_2 = True


def is_pareizs_skaititajs_2():
    global parbaude_skaititajam_2
    parbaude = input_saucejs_1.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
    except:
        parbaude_skaititajam_2 = False
    else:
        b1 = input_saucejs_1.get()
        e1 = input_saucejs_2.get()
        is_skaititajs_2_mazaks_saucejs_2(b1, e1)


def is_pareizs_saucejs_2():
    global parbaude_skaititajam_2, parbaude_saucejam_2
    parbaude = input_saucejs_2.get()
    try:
        parbaude = int(parbaude)
        parbaude = math.sqrt(parbaude)
        parbaude = 1 / parbaude
    except:
        parbaude_saucejam_2 = False
    else:
        if input_saucejs_2.get() < input_saucejs_1.get():
            parbaude_skaititajam_2 = False
        else:
            parbaude_skaititajam_2 = True
            parbaude_saucejam_2 = True


# -------------------------


def check():
    if parbaude_skaititajam_1 and parbaude_skaititajam_2 and parbaude_saucejam_1 and parbaude_saucejam_2 and parbaude_veselais_1 and parbaude_veselais_2: # Ja visos lodziņos ir ierakstīti reāli skaitļi
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# --------- Funkcijas reķināšanai ---------


def mainit_zimi():
    cetras_zimes_mainisana_plus_minus_reizinat_dalit(button)


def cetras_zimes_mainisana_plus_minus_reizinat_dalit(ee):
    index = zimes_veidi.index(ee['text'])
    ee.config(text=zimes_veidi[(index + 1) % 4])


def saskaitit(d1, d2):
    saucejs = d1[1] * d2[1]
    skaititajs = d1[0] * d2[1] + d1[1] * d2[0]
    return (skaititajs, saucejs)


def atnemt(d1, d2):
    saucejs = d1[1] * d2[1]
    skaititajs = d1[0] * d2[1] - d1[1] * d2[0]
    return (skaititajs, saucejs)


def reizinat(d1, d2):
    skaititajs = d1[0] * d2[0]
    saucejs = d1[1] * d2[1]
    return (skaititajs, saucejs)


def dalit(d1, d2):
    skaititajs = d1[0] * d2[1]
    saucejs = d1[1] * d2[0]
    return (skaititajs, saucejs)


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def result():
    is_pareizs_vesela_dala_1()
    is_pareizs_skaititajs_1()
    is_pareizs_saucejs_1()

    is_pareiza_vesela_dala_2()
    is_pareizs_skaititajs_2()
    is_pareizs_saucejs_2()

    if check():
        result2()
    else:
        label_error.config(text="Nepareizi ievadīti dati kāda no lodziņiem!")
        label_vesels_skaitlis_result.config(text="")
        label_skaititajs_result.config(text="")
        label_saucejs_result.config(text="")
        label_dalisanas_zime_3.config(text="")

        parbaude_veselais_1 = False
        parbaude_skaititajam_1 = False
        parbaude_saucejam_1 = False

        parbaude_veselais_2 = False
        parbaude_skaititajam_2 = False
        parbaude_saucejam_2 = False


def result2():
    label_error.config(text="")
    minus = ""
    index = zimes_veidi.index(button['text'])

    label_skaititajs_result.config(text="")
    label_saucejs_result.config(text="")
    label_minus.config(text="")

    d1 = [int(input_veselais_1.get()), int(input_skaititajs_1.get()), int(input_skaititajs_2.get())] # 1 - vesela daļa, 2 - skaititajs, 3 - saucejs
    d2 = [int(input_veselais_2.get()), int(input_saucejs_1.get()), int(input_saucejs_2.get())] # 1 - vesela daļa, 2 - skaititajs, 3 - saucejs

    d1[1] = d1[0] * d1[2] + d1[1]
    d2[1] = d2[0] * d2[2] + d2[1]

    neista_dala1 = (d1[1], d1[2]) # konvērtē uz neīstu daļu 1.daļu. Nav veselas daļas
    neista_dala2 = (d2[1], d2[2]) # konvērtē uz neīstu daļu 2.daļu. Nav veselas daļas

    if index == 0:
        finals = saskaitit(neista_dala1, neista_dala2)

    elif index == 1:

        finals = atnemt(neista_dala1, neista_dala2)
        if finals[0] < 0:
            finals = (abs(finals[0]), finals[1])
            minus = "-"

    elif index == 2:
        neista_dala1_list = list(neista_dala1)
        neista_dala1_list[0] = d1[0] * neista_dala1[1] + neista_dala1[0]
        neista_dala1 = tuple(neista_dala1)
        finals = reizinat(neista_dala1, neista_dala2)

    else:
        finals = dalit(neista_dala1, neista_dala2)

    gcd1 = gcd(finals[0], finals[1]) # Daļas saīsināšānai

    if gcd1 == 0:
        label_vesels_skaitlis_result.config(text="undef") # Dalīšana ar 0
        label_skaititajs_result.config(text="")
        label_saucejs_result.config(text="")
        label_dalisanas_zime_3.config(text="")

    else:
        parbaude_skaititajam_1 = finals[0] // gcd1
        parbaude_skaititajam_2 = finals[1] // gcd1
        list_dala_beigas = [0, parbaude_skaititajam_1, parbaude_skaititajam_2]

        if list_dala_beigas[2] == 0:
            label_vesels_skaitlis_result.config(text="undef")
            label_skaititajs_result.config(text="")
            label_saucejs_result.config(text="")
            label_dalisanas_zime_3.config(text="")

        else:
            vesela_dala = list_dala_beigas[1] // list_dala_beigas[2]
            skaititajs = list_dala_beigas[1] % list_dala_beigas[2]
            saucejs = list_dala_beigas[2]
            list_dala_beigas = (vesela_dala, skaititajs, saucejs)

            label_vesels_skaitlis_result.config(text=str(vesela_dala))
            label_skaititajs_result.config(text=str(skaititajs))
            label_saucejs_result.config(text=str(saucejs))

            label_minus.config(text=minus)
            label_dalisanas_zime_3.config(text="―", font=("Arial", 25))

            # ----- Testēšanai -----
            #print("Finālas daļas veselā daļa: " + str(list_dala_beigas[0]))
            #print("Finālas daļas skaitītājs: " + str(list_dala_beigas[1]))
            #print("Finālas daļas saucējs: " + str(list_dala_beigas[2]))
            # ----- Testēšanai -----

            if list_dala_beigas[1] == 0 and list_dala_beigas[2] != 0: # Ja ir 0 skaitītāja un nav 0 saucēja, tad nerakstam daļsvītru un nodzēsam vērtības
                label_skaititajs_result.config(text="")
                label_saucejs_result.config(text="")
                label_dalisanas_zime_3.config(text="")

            elif vesela_dala == 0: # Ja vesela daļā ir 0, tad nav jēgas to rakstīt.
                label_vesels_skaitlis_result.config(text="")

    parbaude_veselais_1 = False
    parbaude_skaititajam_1 = False
    parbaude_saucejam_1 = False

    parbaude_veselais_2 = False
    parbaude_skaititajam_2 = False
    parbaude_saucejam_2 = False

    for widget in logs.winfo_children():
            if isinstance(widget, tkinter.Entry):  # Ja tas ir entry widgets
                widget.delete(0, 'end') # tad nodzes visus entry

# --------- Funkcijas reķināšanai ---------


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk() # Tkinter (lai izmantotu to komandas)
logs.geometry("230x185") # Loga izmēra definēšana
logs.title("Daļskaitļi") # Windows "loga" nosaukums


# Labels dalīšanas zīmes
label_dalisanas_zime_1 = tkinter.Label(logs, text="―", font=("Arial", 25)) #
label_dalisanas_zime_1.place(x=19, y=50)

label_dalisanas_zime_2 = tkinter.Label(logs, text="―", font=("Arial", 25)) #
label_dalisanas_zime_2.place(x=91, y=50)

label_dalisanas_zime_3 = tkinter.Label(logs, text="", font=("Arial", 25)) #
label_dalisanas_zime_3.place(x=159, y=50)

# Rezultāts
label_vesels_skaitlis_result = tkinter.Label(logs, text="", width=3)
label_vesels_skaitlis_result.place(x=156, y=65)

label_skaititajs_result = tkinter.Label(logs, text="", width=3)
label_skaititajs_result.place(x=176, y=52)

label_saucejs_result = tkinter.Label(logs, text="", width=3)
label_saucejs_result.place(x=176, y=80)

label_error = tkinter.Label(logs, text="", width=0)
label_error.place(x=5, y=10)

# Munis priekšā
label_minus = tkinter.Label(logs, text="", width=0, font=("Arial", 25))
label_minus.place(x=150, y=50)

# Entry logi
input_veselais_1 = tkinter.Entry(logs, width=3)
input_veselais_1.place(x=2, y=65)

input_skaititajs_1 = tkinter.Entry(logs, width=3)
input_skaititajs_1.place(x=28, y=52)

input_saucejs_1 = tkinter.Entry(logs, width=3)
input_saucejs_1.place(x=100, y=52)

input_veselais_2 = tkinter.Entry(logs, width=3)
input_veselais_2.place(x=77, y=65)

input_skaititajs_2 = tkinter.Entry(logs, width=3)
input_skaititajs_2.place(x=28, y=80)

input_saucejs_2 = tkinter.Entry(logs, width=3)
input_saucejs_2.place(x=100, y=80)

# -----------------------------------------

# Rezultāta poga "="
submit_button = tkinter.Button(logs, text="=", width=20, bd=1, command=result) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta
submit_button.place(x=123, y=65, width=25) # Parādam, kur poga tiks attēlota


# Mainīt zīmi poga (+, -, x, :)
zimes_veidi = ("+", "-", "x", ":")
button = tkinter.Button(logs, text="+", width=20, bd=1, command=mainit_zimi) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta
button.place(x=53, y=65, width=25) # Parādam, kur poga tiks attēlota

parbaude_veselais_1 = False
parbaude_skaititajam_1 = False
parbaude_saucejam_1 = False

parbaude_veselais_2 = False
parbaude_skaititajam_2 = False
parbaude_saucejam_2 = False

logs.mainloop()
