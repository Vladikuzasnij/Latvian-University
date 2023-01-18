# Programmas nosaukums: 2. uzd MPR9
# 2. uzdevums MPR9
# Uzdevuma formulējums: Uzzimēt attēlā redzamo līniju, ja zināms, ka tā uzdota polārajās koordinātās r = a*cos(6*alpha). Parametra a vērtibu ievada lietotājs, bet leņķis a pieder [0;2Pi] 
# Versija 1.0

# Import
import math
import tkinter
from tkinter import ttk

def paradit(): # funkcija zīmēšanai kanvā
    
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


def linija():
    
    x0 = 500
    y0 = 350
    a = float(e1.get())
    b = 2*x0+a/25
    x1 = x0 + a/25
    y1 = y0
    
    # Līnija
    for i in range (1, 3600, 1):
        
        f = i/1800*math.pi
        x = a*math.cos(6*f)*math.cos(f)
        
        y = a*math.cos(6*f)*math.sin(f)
        y2 = -y*25 + y0
        x2 = x*25 + x0
        
        kanva.create_line(x1,y1,x2,y2)
        x1=x2
        y1=y2


def notirit(): # funkcija kanvas satura dzēšanai
    kanva.delete("all")
    
# Logs
logs = tkinter.Tk()
logs.geometry("860x710")

# Kanva
kanva = tkinter.Canvas(logs, bg="white", height=710, width=860)
kanva.place(x=0, y=0)


# Pogu definēšana
poga1= ttk.Button(logs, text="Parādit", command=paradit)
poga1.place(x=10, y=10)

poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

poga3= ttk.Button(logs, text="Parādit līniju", command=linija)
poga3.place(x=10, y=150)


# Etiketes
l0 = ttk.Label(logs, text="r = a*cos(6*f) ")
l0.place(x=7, y=100)

l1 = ttk.Label(logs, text="a = ")
l1.place(x=7, y=120)


# Entry
e1 = ttk.Entry(logs)
e1.place(x=30, y=120, width=30)


# Obligāta rindiņa
logs.mainloop()