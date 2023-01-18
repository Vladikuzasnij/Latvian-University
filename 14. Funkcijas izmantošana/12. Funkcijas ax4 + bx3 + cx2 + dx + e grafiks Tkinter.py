# Programmas nosaukums: 4. uzd MPR14
# 4. uzdevums MPR14
# Uzdevuma formulējums: Sastādīt programmu, kas koordinātu plaknē uzzīmē funkcijas y = ax^4 + bx^3 + cx^2 + dx + e grafiku. Koeficientus ievada lietotājs. Lietotājam jāparedz atsevišķa procedūra koordinātu plaknes uzzīmēšanai un funkcijas grafika konstruēšanai, kā ar funkcija dotās funkcijas vērtības aprēķināšanai.
# Versija 1.0

import tkinter
from tkinter import ttk
from tkinter import *

def enable_button(): # Aktīve pogu "Parādīt funkciju"
        poga3['state'] = ACTIVE
        
def disable_button(): # Dizaktīve pogu "Parādīt funkciju"
        poga3['state'] = DISABLED
        
def paradit(): # funkcija koodinātu zīmēšanai
        
        enable_button()
        kanva.configure(bg='AliceBlue')

        kanva.create_line(150,350,850,350, arrow="last", fill="gray")
        kanva.create_text(847, 330, text="X", anchor = "nw")

        kanva.create_line(500, 0, 500, 700, arrow="first", fill="gray")
        kanva.create_text(507, 0, text= "Y", anchor="nw")

        # Y ass

        for i in range (175, 826, 25): #Y ASS
                kanva.create_line(i, 347, i, 353, fill="gray")

        for i in range(-13,0): # minusiem uz Y
                kanva.create_text(505, 341 - i*25, text = str(i), anchor = "nw", fill= "gray")

        for i in range(1,14): # minusiem uz X
                kanva.create_text(505, 341 - i*25, text = str(i), anchor = "nw", fill= "gray")

        # X ass

        for i in range (25, 676,25) : # X ASS
                kanva.create_line(497, i, 503, i, fill="gray")

        for i in range(-13,0): # minusiem uz X
                kanva.create_text(490 + i*25, 330, text = str(i), anchor = "nw", fill= "gray")

        for i in range(1, 14): # plusiem uz X
                kanva.create_text(496 + i*25, 330, text = str(i), anchor = "nw", fill= "gray")

def get_point(a,b,c,d,e,x):
        return a*x*x*x*x + b*x*x*x + c*x*x + d*x + e # return funkcijas vērību punktā x

def zimesana(x1,y1,x2,y2): # grafiku zimēšanai. Savieno divus punktus ar nogriežņi
        kanva.create_line(x1, y1, x2, y2)

def funkcijas_vertibas(a,b,c,d,e,x,y,x1,y1):
        
        for i in range (175, 825):
                x = (i - 500)/25
                y = get_point(a,b,c,d,e,x) # Funkcija
                x2 = i
                y2 = 350-y*25
                zimesana(x1,y1,x2,y2)
                x1=x2
                y1=y2  

#-------------------------------------------#

def funkcija_get(): # funkcija noteic pirmas funkcijas vērtības un paņēm no ievadisanas laukumiem ievaditus datus
        
        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())
        d = float(e4.get())
        e = float(e5.get())

        x = (175 - 500)/25
        y = get_point(a,b,c,d,e,x) # Funkcija
        x1 = 175
        y1 = 350-y*25
        funkcijas_vertibas(a,b,c,d,e,x,y,x1,y1)

def notirit(): # funkcija satura dzēšanai
        
        kanva.configure(bg='white')
        kanva.delete("all")
        disable_button()

# Loga atribūti

logs = tkinter.Tk()
logs.geometry("860x710")

# Kanvas novietošana

kanva = tkinter.Canvas(logs, bg="white", height=710, width=860)
kanva.place(x=0, y=0)

# Pogas

poga1= ttk.Button(logs, text="Parādit", command=paradit)
poga1.place(x=10, y=10)

poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

poga3= ttk.Button(logs, text="Parādit funkciju", state = 'disabled', command=funkcija_get)
poga3.place(x=10, y=85)

# Ievadisanas laukumi

e1 = ttk.Entry(logs)
e1.place(x=120, y=20, width=30)

e2 = ttk.Entry(logs)
e2.place(x=195, y=20, width=30)

e3 = ttk.Entry(logs)
e3.place(x=270, y=20, width=30)

e4 = ttk.Entry(logs)
e4.place(x=340, y=20, width=30)

e5 = ttk.Entry(logs)
e5.place(x=400, y=20, width=30)

# Etiketes

l0 = ttk.Label(logs, text="y = ")
l0.place(x=92, y=20)

l1 = ttk.Label(logs, text="x^4 +")
l1.place(x=155, y=20)

l2 = ttk.Label(logs, text="x^3 +")
l2.place(x=233, y=20)

l3 = ttk.Label(logs, text="x^2 +")
l3.place(x=305, y=20)

l4 = ttk.Label(logs, text="x +")
l4.place(x=377, y=20)

# Obligāta rindiņa, lai logs būtu redzāms visu laiku

logs.mainloop()
