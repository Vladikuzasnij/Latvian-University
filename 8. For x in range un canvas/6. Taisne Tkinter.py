# Programmas nosaukums: 3. uzd MPR8
# 3. uzdevums MPR8
# Uzdevuma formulējums: Novilkt taisnes nogriezni.
# Versija 1.0

import tkinter
from tkinter import ttk

def paradit():
    kanva.create_line(10,10,200,200)   # zīmēšanai
    
def notirit():
    kanva.delete("all") # notīrīsanai
    
logs = tkinter.Tk()
logs.geometry("700x600")

kanva = tkinter.Canvas(logs, bg="white", height=500, width=500)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Parādīt", command=paradit)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()