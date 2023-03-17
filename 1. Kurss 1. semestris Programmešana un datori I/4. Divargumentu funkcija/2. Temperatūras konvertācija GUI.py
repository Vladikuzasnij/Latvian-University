# Programmas nosaukums: Temperatūras konvertācija ar GUI
# PU 7. uzdevums (MPR4)
# Uzdevuma formulējums: Sastādīt programmu, kas pieprasa ievadīt temperatūras skaitlisko vērtību un mērvienību, un veic konvertāciju uz citām mērvienībām ar GUI.
# Programmas autors: Vladislavs Babaņins
# Versija 6.0



from tkinter import * # Importējam tkinter moduli

root = Tk() # Tkinter (lai izmantotu to komandas)

root.geometry("430x165") # Loga izmēra definēšana
root.title("Temperatūru konvertācija") # Windows "loga" nosaukums



# Labels
Temperaturu_konvertacija_label = Label(root, text="Temperatūru konvertācija") # Teksta "Temperatūru konvertācija" definēšana
Temperaturu_konvertacija_label.place(x=147, y=0) # Rāda tekstu uz attiecīgam koordinātam

C_label = Label(root, text="°С") # Teksta "°С" definēšana
C_label.place(x=60, y=25) # Rāda tekstu uz attiecīgam koordinātam (atrodas virs pogam)

F_label = Label(root, text="°F") # Teksta "°F" definēšana
F_label.place(x=200, y=25) # Rāda tekstu uz attiecīgam koordinātam (atrodas virs pogam)

K_label = Label(root, text="K") # Teksta "K" definēšana
K_label.place(x=355, y=25) # Rāda tekstu uz attiecīgam koordinātam (atrodas virs pogam)



Input_C=Entry(root) # Input definēšana (USD input)
Input_C.insert(0, "°C vērtība") # 0, "USD vērtība" - tas kas ir pēc noklusējuma uzreiz ir uzrakstīts ailītē
Input_C.get() # Lai "saņemtu" kas bija ierakstīts ailītē
Input_C.place(x=10,y=50)  # Rāda input (ailīte) EUR 2. rinda, 3. kolonnā

Input_F=Entry(root) # Input definēšana (Fārenheita)
Input_F.insert(0, "°F vērtība") # 0, "°F vērtība" - tas kas ir pēc noklusējuma uzreiz ir uzrakstīts ailītē
Input_F.get() # Lai "saņemtu" kas bija ierakstīts ailītē
Input_F.place(x=155, y=50) # Rāda input Fārenheita(ailīte)

Input_K=Entry(root) # Input definēšana (Kelvin input)
Input_K.insert(0, "K vērtība") # 0, "K vērtība" - tas kas ir pēc noklusējuma uzreiz ir uzrakstīts ailītē
Input_K.get() # Lai "saņemtu" kas bija ierakstīts ailītē
Input_K.place(x=300,y=50) # Rāda input Kelvinos (ailīte)



# Tukšie "Label", lai varētu ievadīt un mainīt to saturošo informāciju
l1 = Label(root, text="")
l1.place(x=10, y=110)

l2 = Label(root, text="")
l2.place(x=10, y=130)

l3 = Label(root, text="")
l3.place(x=165, y=110)

l4 = Label(root, text="")
l4.place(x=165, y=130)

l5 = Label(root, text="")
l5.place(x=300, y=110)

l6 = Label(root, text="")
l6.place(x=300, y=130)

l7 = Label(root, text="")
l7.place(x=100, y=125)


def Click_on_C(): # Definējam komandu Click_on_C
    
    l1.config(text = "") # Iepriekšējo rezultātu notīrīšana
    l2.config(text = "")
    l7.config(text = "")    
    
    if float(Input_C.get())>=-273.15: # Ja vērtība ir lielāka vai vienāda ar absolūto nulli, tad konvertēsim to
    
        a_float = float(Input_C.get())*1.8+32 
        a_round = "{:.2f}".format(a_float) # Lai rezultāts būtu 2 cipāru pēc komata
    
        a = str(Input_C.get()) + "°C = " + str(float(a_round)) + " °F"
    
        l1.config(text=str(a)) # Rezultātu parādīšana


        b_float = float(Input_C.get())+273.15
        b_round = "{:.2f}".format(b_float) # Lai rezultāts būtu 2 cipāru pēc komata
    
        b = str(Input_C.get()) + "°C = " + str(float(b_float)) + " K"
        l2.config(text=str(b)) # Izmainīt tekstu ""
    
        Input_C.delete(0, "end") # Nodzēst ierakstīto
    
    else: # Ja vērtība ir lielāka vai vienāda ar absolūto nulli, tad konvertēsim to
        l7.config(text = "") # Visu iepriekšējo rezultātu notīrīšana
        
        l1.config(text = "")
        l2.config(text = "")        
        l3.config(text = "")
        l4.config(text = "")
        l5.config(text = "")
        l6.config(text = "")
        
        l7.config(text="Error. Vērtība ir mazākā nekā absolūtā nulle")
        Input_C.delete(0, "end")   # Nodzēst ierakstīto




def Click_on_F(): # Definējam komandu Click_on_F
    
    l3.config(text = "")
    l4.config(text = "")
    l7.config(text = "")  
    
    if float(Input_F.get())>=-459.67:
    
        c_float = ((float(Input_F.get())-32)/1.8) 
        c_round = "{:.2f}".format(c_float) # Lai rezultāts būtu 2 cipāru pēc komata   
    
        c = str(Input_F.get()) + "°F = " + str(float(c_round)) + " °C"
        l3.config(text=str(c)) # Teksta "" izmainīšana

        d_float = ((float(Input_F.get())+459.67)/1.8)
        d_round = "{:.2f}".format(d_float) # Lai rezultāts būtu 2 cipāru pēc komata

        d = str(Input_F.get()) + "°F = " + str(float(d_round)) + " K"
        l4.config(text=str(d)) # Teksta "" izmainīšana

        Input_F.delete(0, "end") # Nodzēst ierakstīto
        
    else:
        l7.config(text = "") # Visu iepriekšējo rezultātu notīrīšana
        
        l1.config(text = "")
        l2.config(text = "")        
        l3.config(text = "")
        l4.config(text = "")
        l5.config(text = "")
        l6.config(text = "")  
        
        l7.config(text="Error. Vērtība ir mazākā nekā absolūtā nulle")
        Input_F.delete(0, "end") # Nodzēst ierakstīto
    
    
    
    
def Click_on_K(): # Definējam komandu Click_on_K

    l5.config(text = "")
    l6.config(text = "")
    l7.config(text = "")
    
    if float(Input_K.get())>=0:
    
        e_float = float(Input_K.get())-273.15
        e_round = "{:.2f}".format(e_float) # Lai rezultāts būtu 2 cipāru pēc komata 
    
        e = str(Input_K.get()) + "K = " + str(float(e_round)) + " °C"
        l5.config(text=str(e)) # Teksta "" izmainīšana
    
    
        f_float = float(Input_K.get())
        f_float2 = (((f_float)*1.8)-459.67)
        f_round = "{:.2f}".format(f_float2) # Lai rezultāts būtu 2 cipāru pēc komata   
    
        f = str(Input_K.get()) + "K = " + str(float(f_round)) + " °F"
        l6.config(text=str(f)) # Teksta "" izmainīšana
        Input_K.delete(0, "end") # Nodzēst ierakstīto
        
    else: # Ja vērtība ir mazāka tad ERROR.
        l7.config(text = "") # Visu iepriekšējo rezultātu notīrīšana
        
        l1.config(text = "")
        l2.config(text = "")
        l3.config(text = "")
        l4.config(text = "")
        l5.config(text = "")
        l6.config(text = "")
        
        l7.config(text="Error. Vērtība ir mazākā nekā absolūtā nulle")
        Input_K.delete(0, "end") # Nodzēst ierakstīto




# Pogu definēšana
C_button = Button(root, text="Konvertēt °C", command=Click_on_C) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta (Click_on_C)
C_button.place(x=20, y=75, width=100) # Parādam, kur poga tiks attēlota

F_button = Button(root, text="Konvertēt °F", command=Click_on_F) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta (Click_on_F)
F_button.place(x=165, y=75, width=100) # Parādam, kur poga tiks attēlota

K_button = Button(root, text="Konvertēt K", command=Click_on_K) # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta (Click_on_K)
K_button.place(x=307, y=75, width=100) # Parādam, kur poga tiks attēlota





root.mainloop() # Obligāta rindiņa, lai logs butu redzāms visu laiku