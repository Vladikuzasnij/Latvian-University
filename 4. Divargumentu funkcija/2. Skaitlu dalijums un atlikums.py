# Programmas nosaukums: Skaitļu dalījums un atlikums
# 1. uzdevums (MPR4)
# Uzdevuma formulējums: Izveidot vienloga lietotni, kas nodrošina divu veselu skaitļu ievadi un pēc pogas piespiešanas paziņo šo skaitļu dalījumu un atlikumu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import tkinter
from tkinter import ttk

root = tkinter.Tk()

root.title("Skaitļu dalījums un atlikums")
root.geometry("220x100")

def Click_on_button():

    x=InputLeft.get()
    y=InputRight.get()
    
    z=int(x)//int(y)
    w=int(x)%int(y)
    
    Result.config(text = (str(z) + " atl. " + str(w)))
    
Poga=tkinter.Button(root, text="=", command=Click_on_button)
Poga.pack()
Poga.place(x=130, y=30, width=25, height=25)


DalisanasZime=tkinter.Label(root, text=":")


InputLeft=tkinter.Entry(root)

InputLeft.pack()
InputLeft.place(x=50, y=30, width=25, height=25)

DalisanasZime=tkinter.Label(root, text=":")
DalisanasZime.pack()
DalisanasZime.place(x=78, y=30)

InputRight=tkinter.Entry(root)

InputRight.pack()
InputRight.place(x=90, y=30, width=25, height=25)

Result = ttk.Label(root, text="")
Result.place(x=165, y=30)

root.mainloop()