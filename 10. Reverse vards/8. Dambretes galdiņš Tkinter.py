# Programmas nosaukums: 1. uzd MPR10
# 1. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas uzzīmē dambretes galdiņu.
# Versija 1.0

import tkinter
from tkinter import ttk


# Loga atribūti

logs = tkinter.Tk()
logs.geometry("800x800")

# Kanvas novietošana

kanva = tkinter.Canvas(logs, bg="white", height=900, width=900)
kanva.place(x=-100, y=-100)

kanva.create_rectangle (0,0,900,900, fill = "white")

for i in range (1,9):
    for j in range (1,9):
        if (i + j)%2 == 1:
            kanva.create_rectangle(i*100, j*100, i*100+100, j*100+100, fill="gray")
            
            if j < 4:
                kanva.create_oval(i*100+10, j*100+10, i*100+90, j*100+90, fill="black")
                
                kanva.create_oval(i*100+20, j*100+20, i*100+80, j*100+80, outline="white")
                kanva.create_oval(i*100+30, j*100+30, i*100+70, j*100+70, outline="white")
                

            if j > 5:
                kanva.create_oval(i*100+10, j*100+10, i*100+90, j*100+90, fill="white")
            
                kanva.create_oval(i*100+20, j*100+20, i*100+80, j*100+80, outline="black")
                kanva.create_oval(i*100+30, j*100+30, i*100+70, j*100+70, outline="black")
                


# Obligāta rindiņa, lai logs būtu redzāms visu laiku
logs.mainloop()
