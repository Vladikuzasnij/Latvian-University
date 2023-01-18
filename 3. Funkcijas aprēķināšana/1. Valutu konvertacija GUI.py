# Programmas nosaukums: Valūtu konvertācija (GUI)
# 4. uzdevums (PU1)
# Uzdevuma formulējums: Izveidot programmu, kura konvertē EUR -> USD un USD -> EUR ar GUI.
# Programmas autors: Vladislavs Babaņins
# Versija 4.0

# 1 USD = 1.0129647 EUR
# 1.00 EUR = 0.98715628 USD

from tkinter import * # Importējam tkinter moduli

root = Tk() # Tkinter (lai izmantotu to komandas)


root.title("Valūtu konvertācija") # Windows "loga" nosaukums

# EUR => USD #

upper_text = Label(root, text="Valūtu konvertācija") # Teksta "Valūtu konvertācija" definēšana
upper_text.grid(row=0, column=2) # Rāda tekstu 0 rinda, 2 kolonnā

EUR_label = Label(root, text="EUR") # Teksta "EUR" definēšana
EUR_label.grid(row=0, column=1) # Rāda tekstu 0 rinda, 1 kolonnā

USD_label = Label(root, text="USD") # Teksta "EUR" definēšana
USD_label.grid(row=0, column=3) # Rāda tekstu 0 rinda, 3 kolonnā

Input_EUR=Entry(root) # Input definēšana (EUR input)
Input_EUR.insert(0, "EUR vērtība") # 0, "EUR vērtība" - tas kas ir pēc noklusējuma uzreiz ir uzrakstīts ailītē
Input_EUR.get() # Lai "saņemtu" kas bija ierakstīts ailītē
Input_EUR.grid(row=2, column=1) # Rāda input EUR (ailīte) 2. rinda, 1. kolonnā


def Click_on_right(): # Definējam komandu EUR -> USD
    Fuction_EUR_to_USD = Label(root, text=str(float(Input_EUR.get())*0.98715628) + " USD").grid(row=3, column=1) # Valūtu konvertācija. Paņemam EUR vertību no INPUT (kas lietotājs ir uzrakstījis). Rezultāta paradīšana 3. rindā un 1. kolonnā ar "USD" tekstu

# EUR => USD #



# USD => EUR #

Input_USD=Entry(root) # Input definēšana (USD input)
Input_USD.insert(0, "USD vērtība") # 0, "USD vērtība" - tas kas ir pēc noklusējuma uzreiz ir uzrakstīts ailītē
Input_USD.get() # Lai "saņemtu" kas bija ierakstīts ailītē
Input_USD.grid(row=2, column=3)  # Rāda input (ailīte) EUR 2. rinda, 3. kolonnā


def Click_on_left(): # Definējam komandu USD -> EUR
    Fuction_USD_to_EUR = Label(root, text=str(float(Input_USD.get())*1.0129647) + " EUR" ).grid(row=3, column=3)  # Valūtu konvertācija. Paņemam USD vertību no INPUT (kas lietotājs ir uzrakstījis). Rezultāta paradīšana 3. rindā un 3. kolonnā ar "EUR" tekstu


Kurss = Label(root, text="1.00 EUR = 0.98715628 USD\n1.00 USD = 1.0129647 EUR") # Kursa vērtība uz ekrāna (parasts teksts)
Kurss.grid(row=4, column=2) # Definēts, kur šis teksts atrodas


Button_right = Button(root, text="EUR -> USD", command=Click_on_right) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta (EUR -> USD)
Button_right.grid(row=2, column=2) # Parādam, kur poga tiks attēlota

Button_left = Button(root, text="USD -> EUR", command=Click_on_left) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta (USD -> EUR)
Button_left.grid(row=3, column=2) # Parādam, kur poga tiks attēlota

# USD => EUR #


root.mainloop()