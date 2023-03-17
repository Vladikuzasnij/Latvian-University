# Programmas nosaukums: 7. uzd MPR8
# 7. uzdevums MPR8
# Uzdevuma formulējums: Uzzīmēt saules starus.
# Versija 1.0

import tkinter
from tkinter import ttk

def paradit():

    for x in range (0, 500, 25):   
        kanva.create_line(0, 0, x, 500, width=4, fill="yellow") # no 0 līdz 45 grādiem
    
    for y in range (500, 0, -25):   
        kanva.create_line(0, 0, 500, y, width=4, fill="yellow") # no 45 grādiem līdz 90 grā○diem
    
    
def notirit():
    kanva.delete("all") # notirisanai
    
logs = tkinter.Tk()
logs.geometry("700x600")

kanva = tkinter.Canvas(logs, bg="white", height=500, width=500)
kanva.place(x=100, y=10)
poga1= ttk.Button(logs, text="Parādīt", command=paradit)
poga1.place(x=10,y=10)
poga2 = ttk.Button(logs, text="Notīrīt", command=notirit)
poga2.place(x=10, y=50)

logs.mainloop()