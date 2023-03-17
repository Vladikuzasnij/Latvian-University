# Programmas nosaukums: 5. uzd MPR8
# 5. uzdevums MPR8
# Uzdevuma formulējums: Uzzīmēt žogu visu vienā krāsā.
# Versija 1.0

import tkinter
from tkinter import ttk

def zogs():

    x=20 # sakotnejas vertibas
    y=20
    
    for x in range (20, 550, 30):

        kanva.create_line(x,y, x-10, y+10, x-10, y+200, x+10, y+200, x+10, y+10, x, y, width=2, fill="blue") # latiņas ar ciklu
        
# ------------------------------------------------------------

    kanva.create_line(10,70, 0, 70, width=1, fill="blue")
    kanva.create_line(10,100, 0, 100, width=1, fill="blue") # pirmas četras usiņas
    
    kanva.create_line(10,150, 0, 150, width=1, fill="blue")
    kanva.create_line(10,180, 0, 180, width=1, fill="blue")


    for x in range (1, 20, 1):
        kanva.create_line(10+30*x, 70, 0+30*x, 70, width=1, fill="blue")
        kanva.create_line(10+30*x, 100, 0+30*x, 100, width=1, fill="blue") # usiņas ar ciklu
    
        kanva.create_line(10+30*x, 150, 0+30*x, 150, width=1, fill="blue")
        kanva.create_line(10+30*x, 180, 0+30*x, 180, width=1, fill="blue")


   
def notirit():
    kanva.delete("all") # notirisanai
    
logs = tkinter.Tk()
logs.geometry("700x600")

kanva = tkinter.Canvas(logs, bg="white", height=500, width=500)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Žogs", command=zogs)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()