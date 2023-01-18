# Programmas nosaukums: 3. uzd MPR15
# 3. uzdevums MPR15
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, vai trīs taisnes, kuras uzdotas ar taišņu vienādojumiem, ir novietotas tā, ka tās veido trijstūri. Ja veido trijstūri, tad aprēķina tā laukumu. Taišņu vienādojumu ievades forma dota attēlā.
# Versija 1.0

# Loga atribūti

import tkinter as tk
from tkinter import * # bez šai rindai nestrādas rinda button['state'] = DISABLED
from tkinter import ttk

def vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2):
    SD = A1*B2 - A2*B1
    if SD == 0:
        return False
    else:
        return True
    
def triangle_area_in_coordinates(x1,y1, x2,y2, x3,y3):
    Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    if Area == 0:
        return False
    else:
        return Area

def two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dx = -C1*B2 + B1*C2
    x = Dx/D
    return x

def two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dy = -C2*A1 + A2*C1
    y = Dy/D
    return y

def triangle_area_in_coordinates(x1,y1, x2,y2, x3,y3):
    Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    if Area == 0:
        return False
    else:
        return Area
    
#--------------------------

'''
A1*x + B1*y + C1 = 0
A2*x + B2*y + C2 = 0
A3*x + B3*y + C3 = 0
'''

def is_realA1(event): # Pārbaudam vai entry e1 ir ierakstīts reāls skaitlīs, nevis parasta simbolu virkne
    global a
    try:
        float(e1.get()) # Pārbaude no e1 ņemsim simbolu virkni un pārbaudīsim vai to var pārveidot float
    except:
        if e1.get() == "":  # ja nekas nav ierakstīts
            e1.config(bg = "white") #  tad iekrasosīm baltā
            l_result.config(text = "") # nodzēsisim ieprēkšējo rezultātu, kuru mēs paradījam lietotājam (aprēķināto laukumu)
            a = False # tad globalais a ir False
        else:
            e1.config(bg = "red")
            l_result.config(text = "")
            a = False
    else:
        e1.config(bg = "white")
        a = True
    check() # Pārbaudam vai visiem entry ir ierakstīti reāli skaitli

def is_realB1(event):
    global b
    try:
        float(e2.get())
    except:
        if e2.get() == "":
            e2.config(bg = "white")
            l_result.config(text = "")
            b = False
        else:
            e2.config(bg = "red")
            l_result.config(text = "")
            b = False
    else:
        e2.config(bg = "white")
        b = True
    check()

def is_realC1(event):
    global c
    try:
        float(e3.get())
    except:
        if e3.get() == "":
            e3.config(bg = "white")
            l_result.config(text = "")
            c = False
        else:
            e3.config(bg = "red")
            l_result.config(text = "")
            c = False
    else:
        e3.config(bg = "white")
        c = True
    check()

def is_realA2(event):
    global d
    try:
        float(e4.get())
    except:
        if e4.get() == "":
            e4.config(bg = "white")
            l_result.config(text = "")
            d = False
        else:
            e4.config(bg = "red")
            l_result.config(text = "")
            d = False
    else:
        e4.config(bg = "white")
        d = True
    check()

def is_realB2(event):
    global e 
    try:
        float(e5.get())
    except:
        if e5.get() == "":
            e5.config(bg = "white")
            l_result.config(text = "")
            e = False
        else:
            e5.config(bg = "red")
            l_result.config(text = "")
            e = False
    else:
        e5.config(bg = "white")
        e = True
    check()
        
def is_realC2(event):
    global f
    try:
        float(e6.get())
    except:
        if e6.get() == "":
            e6.config(bg = "white")
            l_result.config(text = "")
            f = False
        else:
            e6.config(bg = "red")
            l_result.config(text = "")
            f = False
    else:
        e6.config(bg = "white")
        f = True
    check()
        
def is_realA3(event):
    global g
    try:
        float(e7.get())
    except:
        if e7.get() == "":
            e7.config(bg = "white")
            l_result.config(text = "")
            g = False
        else:
            e7.config(bg = "red")
            l_result.config(text = "")
            g = False
    else:
        e7.config(bg = "white") 
        g = True
    check()
        
def is_realB3(event):
    global h
    try:
        float(e8.get())
    except:
        if e8.get() == "":
            e8.config(bg = "white")
            l_result.config(text = "")
            h = False
        else:
            e8.config(bg = "red")
            l_result.config(text = "")
            h = False
    else:
        e8.config(bg = "white")
        h = True
    check()
        
            
def is_realC3(event):
    global j
    try:
        float(e9.get())
    except:
        if e9.get() == "":
            e9.config(bg = "white")
            l_result.config(text = "")
            j = False
        else:
            e9.config(bg = "red")
            l_result.config(text = "")
            j = False
    else:
        e9.config(bg = "white")
        j = True
    check()
    
#--------------------------

def check(): # Pārbaude
    if a and b and c and d and e and f and g and h and j: # Ja visos lodziņos ir ierakstīti reāli skaitļi
        button['state'] = ACTIVE # tad poga kļūst aktīva
    else:
        button['state'] = DISABLED # Ja kaut viena lodziņa nav ierakstīts reāls skaitļi, tad poga kļūst aktīva
        
#--------------------------

def paraditRezultatu(): # funkcija datu nolasīšanai un apstrādei
    
    '''
    A1*x + B1*y + C1 = 0
    A2*x + B2*y + C2 = 0
    A3*x + B3*y + C3 = 0
    '''
    
    A1 = float(e1.get()) 
    B1 = float(e2.get())
    C1 = float(e3.get())
    
    A2 = float(e4.get())
    B2 = float(e5.get())
    C2 = float(e6.get())
    
    A3 = float(e7.get())
    B3 = float(e8.get())
    C3 = float(e9.get())
    
    # Ja 1. - 2. taisnei ir kopīgs punkts un 2. - 3. taisnei ir kopīgs punkts un 1. - 3. taisnei ir kopīgs punkts, tad atrādīsim visus šos krustpunktu koordinātas
    # lai pēc tam atrisinātu laukumu trīsturim pēc koordinātam
    if vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2) and vai_taisnem_ir_kopigs_punkts(A2, B2, A3, B3) and vai_taisnem_ir_kopigs_punkts(A1, B1, A3, B3):
    
        x1 = two_line_interseption_point_coordinate_x(A1,B1,C1, A3,B3,C3) # atradisim x1 koordinatu
        y1 = two_line_interseption_point_coordinate_y(A1,B1,C1, A3,B3,C3) # atradisim y1 koordinatu
    
        x2 = two_line_interseption_point_coordinate_x(A2,B2,C2, A3,B3,C3) # atradisim x2 koordinatu
        y2 = two_line_interseption_point_coordinate_y(A2,B2,C2, A3,B3,C3) # atradisim y2 koordinatu
    
        x3 = two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2) # atradisim x3 koordinatu
        y3 = two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2) # atradisim y3 koordinatu
    
        S = triangle_area_in_coordinates(x1,y1, x2,y2, x3,y3) # trijstura laukums koordinātas
    
        if S != 0:
            l_result.config(text = "S = " + str(S)) # Izvadam rezultātu
        else: 
            l_result.config(text = "Neveidojas trijstūris.") # Ja laukums ir 0, tad tas ir gadījums, kad visas taisnēs krustojās vienā punktā
    else:
        l_result.config(text = "Neveidojas trijstūris.") # Ja kaut viena prasība neizpildās, tad neveidojas trījstūris 
    
# -----------------------------------

# Sākuma visi globālie mainīgie ir False. Viņi atbild par to, vai poga ( button = ttk.Button(logs, text="=", width=1, command=paraditRezultatu) ) 
# ir ieslēgta vai izslēgta

a = False
b = False
c = False
d = False
e = False
f = False
g = False
h = False
j = False

logs = tk.Tk()
logs.title("Taišņu veidotais laukums") # Programmas nosaukums
logs.geometry("600x300") 
l_result = ttk.Label(logs, text="")
l_result.place(x=80, y=200)


# etiķešu (uzrakstu) iezveide

# -----------------------

l_iekava = ttk.Label(logs, text="{", font = ("Calibri", 140))
l_iekava.place(x=-5, y=-20)

l1 = ttk.Label(logs, text="x + ")
l1.place(x=95, y=50)

l2 = ttk.Label(logs, text="y + ")
l2.place(x=170, y=50)

l0_1 = ttk.Label(logs, text=" =  0 ")
l0_1.place(x=245, y=50)

# -----------------------
# -----------------------
l3 = ttk.Label(logs, text="x + ")
l3.place(x=95, y=100)

l4 = ttk.Label(logs, text="y + ")
l4.place(x=170, y=100)

l0_2 = ttk.Label(logs, text=" =  0 ")
l0_2.place(x=245, y=100)
# -----------------------

l5 = ttk.Label(logs, text="x + ")
l5.place(x=95, y=150)

l6 = ttk.Label(logs, text="y + ")
l6.place(x=170, y=150)

l0_3 = ttk.Label(logs, text=" =  0 ")
l0_3.place(x=245, y=150)
# -----------------------

    
# ievades tektlodziņu izveide

# -----------------------
e1 = tk.Entry(logs, width = 6)
e1.bind("<KeyRelease>", is_realA1) # Izsaucam funkciju is_realA1
e1.place(x=50, y=50)

e2 = tk.Entry(logs, width = 6)
e2.bind("<KeyRelease>", is_realB1 )
e2.place(x=120, y=50)

e3 = tk.Entry(logs, width = 6)
e3.bind("<KeyRelease>", is_realC1 )
e3.place(x=200, y=50)
# -----------------------

# -----------------------
e4 = tk.Entry(logs, width = 6)
e4.bind("<KeyRelease>", is_realA2 )
e4.place(x=50, y=100)

e5 = tk.Entry(logs, width = 6)
e5.bind("<KeyRelease>", is_realB2 )
e5.place(x=120, y=100)

e6 = tk.Entry(logs, width = 6)
e6.bind("<KeyRelease>", is_realC2 )
e6.place(x=200, y=100)
# -----------------------

# -----------------------
e7 = tk.Entry(logs, width = 6)
e7.bind("<KeyRelease>", is_realA3 )
e7.place(x=50, y=150)

e8 = tk.Entry(logs, width = 6)
e8.bind("<KeyRelease>", is_realB3 )
e8.place(x=120, y=150)

e9 = tk.Entry(logs, width = 6)
e9.bind("<KeyRelease>", is_realC3 ) 
e9.place(x=200, y=150)
# -----------------------

button = ttk.Button(logs, text="Aprēķināt!", width=10, command=paraditRezultatu)
button.place(x=280, y=150) # novietojām pogu koordinātas x = 250 y = 150
button['state'] = DISABLED # pēc noklusējuma poga ir izslēgta

# Obligāta rindiņa, lai logs būtu redzāms visu laiku
logs.mainloop()