# Programmas nosaukums: 6. uzd MPR8
# 6. uzdevums MPR8
# Uzdevuma formulējums: Uzzīmēt rūtiņu lapu. Visi nogriežņi vienā krāsā.
# Versija 1.0

import tkinter
from tkinter import ttk

def paradit():
    
    for x in range (100, 9000, 100):   
        kanva.create_rectangle(x, 0, x, 1000, width=1, fill="blue")
    
    for y in range (100, 9000, 100):   
        kanva.create_rectangle(0, y, 1000, y, width=1, fill="blue")    
        
    
def notirit():
    kanva.delete("all") # notirisanai
    
logs = tkinter.Tk()
logs.geometry("1000x1000")

kanva = tkinter.Canvas(logs, bg="white", height=1000, width=1000)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Parādīt", command=paradit)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()