# Programmas nosaukums: 2.uzdevums ar determinanta metodi ar GUI.
# PU1 (MPR5) 2.uzdevums
# Uzdevuma formulējums: Izveidot programmu, kas pieprasa ievadīt lineāras vienādojumu sistēmas koeficientu vērtības un paziņo tās atrisinājumu skaitu. Uzdevums jāatrisina, izmantojot determinantu metodi un ar koeficientu proporciju salīdzināšanas metodi. Ar GUI.
# Programmas autors: Vladislavs Babaņins
# Versija 4.6

import math

from tkinter import * # Importējam tkinter moduli

root = Tk() # Tkinter (lai izmantotu to komandas)

root.geometry("230x185") # Loga izmēra definēšana
root.title("Lineāras vienādojumu sistēma") # Windows "loga" nosaukums


# Labels

Label_x1 = Label(root, text="x  + ") # 
Label_x1.place(x=50, y=50) #

Label_y1 = Label(root, text=" y = ") # 
Label_y1.place(x=100, y=50) #

Label_x2 = Label(root, text="x  + ") # 
Label_x2.place(x=50, y=80) #

Label_y2 = Label(root, text=" y = ") # 
Label_y2.place(x=100, y=80) #

# Tukšie "Label", lai varētu ievadīt un mainīt to saturošo informāciju

l1 = Label(root, text="")
l1.place(x=65, y=140)

# 1. vienādojums

Input_a=Entry(root, width=3)
 
Input_a.place(x=28,y=52)

Input_b=Entry(root, width=3)
 
Input_b.place(x=80,y=52) 

Input_c=Entry(root, width=3)
 
Input_c.place(x=130,y=52) 

# 2. vienādojums

Input_d=Entry(root, width=3)

Input_d.place(x=28,y=80)

Input_e=Entry(root, width=3)
Input_e.place(x=80,y=80)

Input_f=Entry(root, width=3)
Input_f.place(x=130,y=80)

def Result():
    
    l1.config(text = "")
    
    a=float(Input_a.get())
    b=float(Input_b.get())
    c=float(Input_c.get())
    d=float(Input_d.get())
    e=float(Input_e.get())
    f=float(Input_f.get())
    
    D=a*e-b*d
    Dx=c*e-b*f
    Dy=a*f-c*d
    
    
    if D==0 and (Dx !=0 or Dy !=0) :
        l1.config(text = "Nav atrisinājumu")

    if D==0 and Dx == 0 and Dy==0 :
        l1.config(text = "Bezgalīgi daudz atrisinājumu") 

        
    if D!=0:
    
        x=Dx/D
        y=Dy/D
        
        l1.config(text = "x = "+str(x) + "\ny = " + str(y))



Submit_button = Button(root, text="Rezultāts", command=Result) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta
Submit_button.place(x=50, y=110, width=80) # Parādam, kur poga tiks attēlota





root.mainloop() # Obligāta rindiņa, lai logs butu redzāms visu laiku