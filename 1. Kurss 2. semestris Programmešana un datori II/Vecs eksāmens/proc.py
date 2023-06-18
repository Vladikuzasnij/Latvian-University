import math

def divargumentu_funkcijas_vertiba():
    print("\"Divargumentu funkciju vērtība\"\nVersija 1.6\n") # Nosaukums un vērsija
    
    x=int(input("Ievadi x vērtibu ===>")) 
    y=int(input("Ievadi y vērtibu ===>"))
    
    function_value=(math.log2(1+((x**2)**(1/3)))+math.sin(y))/((abs(x-y))+1) # Funkcijas vērtības apreķināšana ar funkcijas math.sin un math.log2
    
    print("Funkcijas vērtība, kad x="+str(x)+" un y="+str(y)+", ir vienāda ar: "+str(function_value)) # Lai savienotu str un int vērtibas pārveidosim iegūto funkcijas vērtibu par str

def operacijas_ar_skaitliem():
    print("\"Dažas operācijas ar diviem veseliem skaitļiem\"\nVersija 1.4\n") # Programmas nosaukums un vērsija parādas
    
    a=int(input("Ievadi pirmo veselo skaitļi ===>")) # Pieprasa skaitļi a un input'u => integer
    b=int(input("Ievadi otro veselo skaitļi ===>")) # Pieprasa skaitļi b un input'u => integer
    
    print(str(a) + "+" + str(b) + "=" + str(a+b) + " Summa") # Vienā rinda programma saskaita a un b un ievāda to tekstā str() veidā
    print(str(a) + "-" + str(b) + "=" + str(a-b) + " Starpība") # Pēc analoģijas izdarīts tas pats visām nepieciešāmam operācijām
    print(str(b) + "-" + str(a) + "=" + str(b-a) + " Starpība")
    print(str(a) + "*" + str(b) + "=" + str(a*b) + " Reizinājums")
    print(str(a) + "/" + str(b) + "=" + str(a/b) + " Dalījums")
    print(str(b) + "/" + str(a) + "=" + str(b/a) + " Dalījums")
    print(str(a) + "//" + str(b) + "=" + str(a//b) + " Veselais dalījums")
    print(str(b) + "//" + str(a) + "=" + str(b//a) + " Veselais dalījums")
    print(str(a) + "%" + str(b) + "=" + str(a%b) + " Dalīšanas atlikums")
    print(str(b) + "%" + str(a) + "=" + str(b%a) + " Dalīšanas atlikums")

def trijstura_perimetrs_laukums_Radiuss_radiuss():
    print("\"Trījstura paramētri\"\nVersija 2.2\n")
    
    a=float(input("Ievadi 1. mālu ===>"))
    b=float(input("Ievadi 2. mālu ===>"))
    c=float(input("Ievadi 3. mālu ===>"))
    
    # Trījstura nevienādības pārbaudīšana
    
    if   a >= b+c:
        print("Tāds trījsturis neēksiste")
    elif b >= a+c:
        print("Tāds trījsturis neēksiste")
    elif c >= a+b:
        print("Tāds trījsturis neēksiste")
    else:
        
        perimeter=(a+b+c) # Perimetra apreķināšana
        print("Trijstūra perimetrs: "+str(perimeter))
    
        p=(a+b+c)/2 # Pusperimetra apreķināšana
    
        area=math.sqrt(p*(p-a)*(p-b)*(p-c)) # Laukuma apreķināšana izmantojot Herona formulu
        print("Laukums: "+str(area))
        
        R=(a*math.sqrt(3)/3) # Apvilktas riņķa līnijas rādiuss
        print("Apvikltas riņķa līnijas rādiuss: "+str(R))
        
        r=(a*math.sqrt(3)/6) # Ievilktas riņķa līnijas rādiuss
        print("Ievilktas riņķa līnijas rādiuss: "+str(r))

def valutu_konvertacija_TUI():
    import math
    
    print("\"Valūtu konvertācija\"\nVersija 1.4\n") # Programmas nosaukums
    
    
    a=int(input("EUR=>USD vai USD=>EUR \nJa EUR=>USD tad 1, ja USD=>EUR tad 2 ====> ")) # EUR => USD vai USD => EUR izvēle ar 1 vai 2
    
    if a == 1: # Ja tika ievādits 1 (EUR => USD) tad izpildās komandas:
        EUR=input("EUR=>USD \nEUR vērtiba ==> ") # EUR vērtību ievādišana
        EUR_to_USD=float(EUR)*0.98715628 # Valūtu konvertācija
        print("Vērtiba ir " + str(EUR_to_USD) +" USD") # Ievadīšana ekrāna
        
    elif a == 2: # Ja tika ievādits 2 (USD => EUR) tad izpildās komandas:
        USD=input("USD=>EUR \nUSD vērtiba ==> ") # USD vērtību ievādišana
        USD_to_EUR=float(USD)*1.01002 # Valūtu konvertācija
        print("Vērtiba ir " + str(USD_to_EUR)+" EUR") # Ievadīšana ekrāna
        
    else:
        print("Error") # Ja tika ievadīts ne 1 vai 2, tad ir "Error"

def divargumentu_funkcijas_aprekinasana():
    print("\"Divargumentu funkcijas apreķināšana\"\nVersija 1.0\n")
    
    print("f(x,y) = (x - y, ja x > y) un (x + y, ja citādi)\n")
    
    x=float(input("Ievadi x skaitli ===>"))
    y=float(input("Ievadi y skaitli ===>"))
    
    if (x>y):
        print("Divargumentu funkcijas vērtiba ir x - y, ja x > y. \nRezultāts: " + str(x-y))
    else:
        print("Divargumentu funkcijas vērtiba ir x + y, ja x <= y. \nRezultāts: " + str(x+y))

def lielaks_skaitlis_no_diviem():
    print("\"Lielāks skaitļis\"\nVersija 1.0\n")
    
    
    x=float(input("Ievadi x skaitli ===>"))
    y=float(input("Ievadi y skaitli ===>"))
    
    if (x>y):
        print("x > y\nx ir lielāks par y")
    if (x<y):
        print("x < y\ny ir lielāks par x")
    if (x==y):
        print("x==y\nNav lielāka skaitļa")

def sakartot_cetrus_skaitlus_dilstosa_seciba():
    a = float(input("Ievadiet 1.skaitli ===> "))
    b = float(input("Ievadiet 2.skaitli ===> "))
    c = float(input("Ievadiet 3.skaitli ===> "))
    d = float(input("Ievadiet 4.skaitli ===> "))
    
    if a < b :
        x = a
        a = b
        b = x
        
    if c < d :
        x = c
        c = d
        d = x
    
    if a < c :
        x = c
        c = a
        a = x
        
    if b < d :
        x = b
        b = d
        d = x
        
    if b < c :
        x = b
        b = c
        c = x
        
    print(str(a), str(b), str(c), str(d))

def sakartot_cetrus_skaitlus_dilstosa_seciba_6_sal():
    a = float(input("Ievadiet 1.skaitli ===> "))
    b = float(input("Ievadiet 2.skaitli ===> "))
    c = float(input("Ievadiet 3.skaitli ===> "))
    d = float(input("Ievadiet 4.skaitli ===> "))
    
    if a < b :
        x = a
        a = b
        b = x
        
    if a < c :
        x = c
        c = a
        a = x
        
    if a < d :
        x = d
        d = a
        a = x
    
    if b < c :
        x = b
        b = c
        c = x
        
    if b < d :
        x = b
        b = d
        d = x
        
    if c < d :
        x = c
        c = d
        d = x
    
    print(str(a), str(b), str(c), str(d))

def sakartot_tris_skaitlus_dilstosa_seciba():
    print("\"Sakartot trīs skaitļus dilstoša secība\"\nVersija 1.0\n")
    
    
    a = float(input("Ievadiet 1.skaitli ===> "))
    b = float(input("Ievadiet 2.skaitli ===> "))
    c = float(input("Ievadiet 3.skaitli ===> "))
    
    if a < b :
        p = a
        a = b
        b = p
    
    if a < c :
        p = c
        c = a
        a = p
    
    if b < c :
        p = b
        b = c
        c = p
    
    print(str(a), str(b), str(c))

def temperaturas_konvertacija_TUI():
    print("\"Temperatūras konvertācija\"\nVersija 1.4\n") # Programmas nosaukums
    
    
    a=int(input("Izvēlies kādu mērvienību grībi konvertēt citās!\n°C, °F, K\n\nJa °C tad 1, ja °F tad 2, ja K tad 3 ====> ")) # EUR => USD vai USD => EUR izvēle ar 1 vai 2
    
    if a == 1:
        C=input("Ievādi temperatūras skaitlisko vērtibu!\n°C = ")
        
        if float(C)>=-273.15:
            
            C_to_F = 1.8*float(C) + 32
            C_to_K = float(C) + 273.15
            print(str(C) + " °C = " + str(C_to_F) +" °F") # Ievadīšana ekrāna
            print(str(C) + " °C = " + str(C_to_K) +" K") # Ievadīšana ekrāna
       
        else:
            print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")
            
    if a == 2:
        F=input("°F = ")
        
        if float(F)>=-459.67:
            
            F_to_C=((float(F)-32)/1.8) # Temperatūru konvertācija
            F_to_K=(float(F)+459.67)/1.8 # Temperatūru konvertācija
            print(str(F) + " °F = " + str(F_to_C) +" °C") # Ievadīšana ekrāna
            print(str(F) + " °F = " + str(F_to_K) +" K") # Ievadīšana ekrāna
        
        else:
            print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")    
        
    if a == 3: # Ja tika ievādits 3 tad izpildās komandas:
        K=input("K = ") # K vērtību ievādišana
        
        if float(K)>=0: # Absolūtas nulles pārbaudīšana
            
            K_to_C=float(K)-273.15 # Temperatūru konvertācija
            K_to_F=1.8*(float(K))-459.67 # Temperatūru konvertācija
            print(str(K) + " K = " + str(K_to_C) +" °C") # Ievadīšana ekrāna
            print(str(K) + " K = " + str(K_to_F) +" °F") # Ievadīšana ekrāna
        
        else:
            print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")
        
    if a!=1 and a!=2 and a!=3:
        print("Error") # Ja tika ievadīts ne 1, ne 2, ne 3, tad ir "Error"    
        
def bikvadratvienadojuma_atrisinasana():
    import math # Lai izmantotu math.sqrt()
    
    print("Bikvadrātvienādojumu atrisināšana")
    
    a = float(input("Ievadiet a koeficientu ===> "))
    b = float(input("Ievadiet b koeficientu ===> "))
    c = float(input("Ievadiet c koeficientu ===> "))
    
    if a == 0 : # Pēc def. tas nav bikvadrātvienādojums ja a == 0
        
        print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0")
        print("\nTas nav bikvadrātvienādojums")
    
    else :
        
        d = b*b - 4*a*c # Diskriminants
    
        if d < 0 : # Risinām ax^4 + bx^2+c=0. x^2 = t , at^2 + bt + c = 0, atrādam t1,t2 un tad atradam x1,x2 x = +-sqrt(t)
            
            print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
            print("\nBikvadrātvienādojumam nav reālas saknes")
    
            
        else :
            
            t1 = (-b + math.sqrt(d)) / 2 / a
            t2 = (-b - math.sqrt(d)) / 2 / a
            
            if t1 >= 0 :
                if t2 >=0:
                    x1=math.sqrt(t1)
                    x2=-1*(math.sqrt(t1))
                    x3=math.sqrt(t2)
                    x4=-1*(math.sqrt(t2))
                    print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
    
                    print("x1 = "+str(x1))
                    print("x2 = "+str(x2))
                    print("x3 = "+str(x3))
                    print("x4 = "+str(x4))                
                
                else:
                    
                    x1= math.sqrt(t1)
                    x2 = -1*(math.sqrt(t1))
                    print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
                    
                    print("x1 = "+str(x1))
                    print("x2 = "+str(x2))
                    
                
            elif t2>=0:
                x1 = math.sqrt(t2)
                x2 = -1*(math.sqrt(t2))
                print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
                print("x1 = "+str(x1))
                print("x2 = "+str(x2))
                
            else:
                print("Sakņu nav")    
                
def funkcijas_vertibu_aprekins_sistema():
    import math # Lai izmantotu mat.log funkciju
    
    x = float(input("Ievadiet argumenta x vērtību ===> ")) # Paprasīt lietotājam ievadit x vērtību
    
    if x<3 and x>-3 : # Ja x atrodas tādas robežas tad :
        a=(x+3)*(x+3)
        print("x = " + str(x) + " \nf(x) = "+ (str(a))) # Izvada ekrāna vērtības
        
    if  x<-10 or x>10: # Ja x atrodas tādas robežas tad :
        a=math.log((x*x),2)
        print("x = " + str(x) + " \nf(x) = "+ (str(a)))
    
    if  (x >= 3 and x <= 10) or (x <= -3 and x>=-10): # Ja x atrodas tādas robežas tad :
        a=81-x*x
        print("x = " + str(x) + " \nf(x) = "+ (str(a)))   
        
def kvadratvienadojumu_atrisinasana():
    import math # Lai izmantotu math.sqrt()
    
    print("Kvadrātvienādojumu atrisināšana")
    
    a = float(input("Ievadiet a koeficientu ===> ")) # Input no lietotāja
    b = float(input("Ievadiet b koeficientu ===> "))
    c = float(input("Ievadiet c koeficientu ===> "))
    
    # Nav kvadrātvienādojums pēc definīcijas
    if a == 0 :
        
        print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
        print("\nTas nav kvadraatvienādojums")
    
    else : # Citādi risinām kvadrātvienādojumu
        
        d = b*b - 4*a*c # Diskriminants
    
        if d < 0 : # Tad ir komplēksa skaitļi
            
            print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
            print("\nKvadrātvienādojumam realu saknu nav\nIr divas kompleksas saknes\n")
            
            Re = -b
            Im = abs(math.sqrt(-d) / (2 * a))
            print(f"x1 = {Re} + i*{Im} \nx2 = {Re} - i*{Im}")        
    
        elif d == 0 : # Tad divas vienādas saknes
            
            x12 = -b / 2 / a
            
            print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
            print("\nKvadrātvienādojumam ir divas vienādas saknes")
            print("x1 = x2 = " + str(x12))
    
        else : # Divas atšķirīgas saknes
            
            x1 = (-b + math.sqrt(d)) / 2 /a
            x2 = (-b - math.sqrt(d)) / 2 / a
            
            print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
            print("\nKvadrātvienādojumam ir divas atšķirīgas saknes")
            print("\nx1 = " + str(x1))
            print("x2 = " + str(x2))
        
def LVS_atrisinajums_ar_determinantiem():
    # Informācija lietotājam
    print("2. kārtas lineāras vienādojumu sistēmas atrisinājums izmantojot Krāmera formulas\n\nax + by = c\ndx + ey = f\n")
    
    # a,b,c,d,e,f vērtību input
    
    a = float(input("Ievadiet a vērtību ===> "))
    b = float(input("Ievadiet b vērtību ===> "))
    c = float(input("Ievadiet c vērtību ===> "))
    d = float(input("Ievadiet d vērtību ===> "))
    e = float(input("Ievadiet e vērtību ===> "))
    f = float(input("Ievadiet f vērtību ===> "))
    
    # Determinantu apreķināšana
    D=a*e-b*d
    Dx=c*e-b*f
    Dy=a*f-c*d
    
    # Ja Sistēmas determinants ir 0 un (Dx != 0 vai Dy != 0 tad nav atrisinājumu)
    
    if D==0 and (Dx !=0 or Dy !=0) :
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
        
        print("\nNav atrisinājumu")
    
    # Ja visi determinanti (D == 0 un Dx == 0 un Dy == 0) tad ir bezgalīgi daudz atrisinājumu
    
    if D==0 and Dx == 0 and Dy==0 :
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))    
        
        print("\nBezgalīgi daudz atrisinājumu")
    
    # Ja sistēmas determinants nav 0, tad ir viens vienīgs atrisinājums
        
    if D!=0:
    
        x=Dx/D
        y=Dy/D
        
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
        
        print("\nx = "+str(x)+"\ny = "+str(y))    
        
def LVS_atrisinajums_ar_proporcijam():
    # Informācija lietotājam
    print("2. kārtas lineāras vienādojumu sistēmas atrisinājums izmantojot proporciju salidzināšanu metodi\n\nax + by = c\ndx + ey = f\n")
    
    # a,b,c,d,e,f vērtību input
    
    a = float(input("Ievadiet a vērtību ===> "))
    b = float(input("Ievadiet b vērtību ===> "))
    c = float(input("Ievadiet c vērtību ===> "))
    d = float(input("Ievadiet d vērtību ===> "))
    e = float(input("Ievadiet e vērtību ===> "))
    f = float(input("Ievadiet f vērtību ===> "))
    
    # Determinantu apreķināšana (Lai paradītu atrisinājumu, ja tads ir)
    D=a*e-b*d
    Dx=c*e-b*f
    Dy=a*f-c*d
    
    # Gadījums, kad nav atrisinājums
    if a/d == b/e and b/e != c/f:
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
        
        print("\nNav atrisinājumu")
    
    # Gadījums, kad bezgalīgi daudz atrisinājumu  
    if a/d==b/e and b/e==c/f :
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))    
        
        print("\nBezgalīgi daudz atrisinājumu")
    
    # Ir viens atrisinājums
    if a/d != b/e:
    
        x=Dx/D
        y=Dy/D
        
        print("\n"+str(a)+"x + " + "(" + str(b) + ")"+ "y"+" = "+str(c))
        print(str(d)+"x + " + "(" + str(e) + ")"+ "y"+" = "+str(f))
        
        print("\nx = "+str(x)+"\ny = "+str(y))    
        
def piecsturis_bez_slidesanas_velas_x_ass_pozitivaja_virziena():
    import math
    
    print("Izliekts piecsturis bez slidēšanas veļas x ass pozitīvajā virzienā.\nProgramma noteic kura izliekta piecstūra mala vai virsotne uzkritis uz punktu F.\nIevadiet koordinātas tikai 1.kvadrantā un tikai tādas koordinātas, lai veidotos izliekts piecstūris!\n")
    
    x1 = float(input("Ievadiet x1 ===> ")) # A punkts
    
    x2 = float(input("Ievadiet x2 ===> ")) # B punkts
    
    x3 = float(input("Ievadiet x3 ===> ")) # C punkts
    y3 = float(input("Ievadiet y3 ===> "))
    
    x4 = float(input("Ievadiet x4 ===> ")) # D punkts
    y4 = float(input("Ievadiet y4 ===> "))
    
    y5 = float(input("Ievadiet y5 ===> ")) # E punkts
    
    x6 = float(input("Ievadiet x6 ===> ")) # F punkts
    
    # Katras malas garums
    
    #AB mala
    
    AB=x2-x1
    
    #BC mala
    
    BC=math.sqrt((x3-x2)*(x3-x2)+(y3*y3))
    
    #DC mala
    
    CD=math.sqrt((x3-x4)*(x3-x4)+(y4-y3)*(y4-y3))
    
    #DE mala
    
    DE=math.sqrt((y4-y5)*(y4-y5)+x4*x4)
    
    #EA mala
    
    EA=math.sqrt(y5*y5+x1*x1)
    
    # ------------ #
    
    #OA mala
    
    OA=x1
    
    #OF mala
    
    OF=x6
    
    # ------------ #
    
    #Perimetrs
    
    Perimeter= int(AB)+int(BC)+int(CD)+int(DE)+int(EA)
    if OF<OA :
        print("Piecsturis nekad neuzkritīs uz punktu F") # Ka OF<OA tad piecsturis neuzkritīs uz punktu F, jo piecsturis veļas x ass pozitīvajā virzienā.
        
    else:
        z=(OF-OA) # z - ceļš kuru piecsturim ir jāparverš
        u=math.floor(z/Perimeter) # u - cik reizes ceļš ietilpst piecstura perimetrā
        Atl=z-u*Perimeter # atl - atlikums
        AC=AB+BC # AC nogriežņa garums
        AD=AB+BC+CD # AD nogriežņa garums
        AE=AB+BC+CD+DE # AE nogriežņa garums
        
        if Atl==0:
            print("F atrodas uz punkta A")
        
        if Atl > 0 and Atl < AB: # Atrodas šajos robežos
            print("F atrodas uz AB nogriežņa")
            
        
        if Atl==AB:
            print("F atrodas uz punkta B")    
        
        if Atl > AB and Atl < AC :
            print("F atrodas uz BC nogriežņa")
    
            
        if Atl==AC :
            print("F atrodas uz punkta C")
            
        if Atl > AC and Atl < AD :
            print("F atrodas uz CD nogriežņa")
        
        
        if Atl==AD :
            print("F atrodas uz punkta D")
                
        if Atl > AD and Atl < AE :
            print("F atrodas uz DE nogriežņa")
            
        
        if Atl==AE :
            print("F atrodas uz punkta E")    

def atrisina_vienadojumu_sistemu_1():
    import math
    import sys
    
    print("ax^2 + by^2 + c = 0\ndx^2 + ey + f = 0\n")
    
    a = float(input("Ievadiet a ===> "))
    b = float(input("Ievadiet b ===> "))
    
    c = float(input("Ievadiet c ===> "))
    d = float(input("Ievadiet d ===> "))
    
    e = float(input("Ievadiet e ===> "))
    f = float(input("Ievadiet f ===> "))
    
    a_di = d*b
    b_di = -1*a*e
    c_di = d*c-a*f
    
    D = (b_di)*(b_di) - 4*(a_di)*(c_di)
    
    if D < 0:
        print("Nav atrisinājumu")
        sys.exit(0)
    
    elif d==0:
        print("Nav atrisinājumu")
        sys.exit(0)
    
    elif a==0:
        print("Nav atrisinājumu")
        sys.exit(0)
    
    else:
        y1 = (-1*(b_di) + math.sqrt(D))/(2*a_di)
        y2 = (-1*(b_di) - math.sqrt(D))/(2*a_di)
    
        
        k1 = (-1*c-b*y1*y1)/a
        k2 = (-1*c-b*y2*y2)/a
    
        if k2 > 0 and k1 > 0:
    
            x1 = math.sqrt(k1)
            x2 = -1*math.sqrt(k1)
    
            x3 = math.sqrt(k2)
            x4 = -1*math.sqrt(k2)
            
            print("x1 = " + str(x1) + " y1 = " + str(y1) + " x2 = " + str(x2) + " y2 = " + str(y2) )
            print("x3 = " + str(x3) + " y2 = " + str(y2) + " x4 = " + str(x4) + " y2 = " + str(y2) )
    
        else:
            print("Nav atrisinājumu")
            sys.exit(0)
    
def atrisina_vienadojumu_sistemu_2():
    import math
    
    print("ax^2 + ay^2 + b = 0\ncxy + d = 0\n")
    
    a = float(input("Ievadiet a ===> "))
    b = float(input("Ievadiet b ===> "))
    
    c = float(input("Ievadiet c ===> "))
    d = float(input("Ievadiet d ===> "))
    
    if a==0 or c==0 :
        print("Specgadījums")
    
    else:
        zemsakne1 = (-b/a) - ((2*d)/c)
        zemsakne2 = (-b/a) + ((2*d)/c)
    
        if zemsakne1 < 0 or zemsakne2 < 0 :
            print("Nav atrisinājumu realos skaitļos")
    
        else:
            p1= math.sqrt(zemsakne1)
            p2= math.sqrt(zemsakne2)
    
            x = (-p1 + p2)/2
            y = (-p1 - p2)/2
    
            if abs(x) == abs(y):
                print("x1 = " +str(x) + " y1 = " + str(y))
                print("x2 = " +str(-x) + " y2 = " + str(-y))
                
            if abs(x) != abs(y):
                print("")
                print("x1 = " + str(x) + " y1 = " + str(y))
                print("x2 = " + str(y) + " y2 = " + str(x))
                print("x3 = " + str(-x) + " y3 = " + str(-y))
                print("x4 = " + str(-y) + " y4 = " + str(-x))
                
def ieliekts_vai_izliekts_cetrsturis():
    # A
    x1 = float(input("Ievadi X1 ===> "))
    y1 = float(input("Ievadi Y1 ===> "))
    
    # B
    x2 = float(input("Ievadi X2 ===> "))
    y2 = float(input("Ievadi Y2 ===> "))
    
    # C
    x3 = float(input("Ievadi X3 ===> "))
    y3 = float(input("Ievadi Y3 ===> "))
    
    # D
    x4 = float(input("Ievadi X4 ===> "))
    y4 = float(input("Ievadi Y4 ===> "))
    
    
    #AC taisne
    z1 = (x4 - x1)*(y3 - y1) - (y4 - y1)*(x3 - x1)
    
    z2 = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
    
    #BD taisne
    z3 = (x1-x2)*(y4-y2)-(y1-y2)*(x4-x2)
    
    z4 = (x3-x2)*(y4-y2)-(y3-y2)*(x4-x2)
    
    if z1*z2 > 0 or z3*z4 > 0:
        print ("Izliekts")
        
        
    else :
        print ("Ieliekts")

def vai_punkts_atrodas_trijstura_iekspuse_1_var():
    import math
    
    x1 = float(input("Ievadi X1 ===> "))
    y1 = float(input("Ievadi Y1 ===> "))
    x2 = float(input("Ievadi X2 ===> "))
    y2 = float(input("Ievadi Y2 ===> "))
    x3 = float(input("Ievadi X3 ===> "))
    y3 = float(input("Ievadi Y3 ===> "))
    x4 = float(input("Ievadi X4 ===> "))
    y4 = float(input("Ievadi Y4 ===> "))
    
    ab = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    bc = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
    ac = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
    ad = math.sqrt((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4))
    bd = math.sqrt((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4))
    cd = math.sqrt((x3-x4)*(x3-x4)+(y3-y4)*(y3-y4))
    
    
    z1 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
    z2 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
    z3 = (x4 - x2) * (y3 - y2) - (x3 - x2) * (y4 - y2)
    z4 = (x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)
    z5 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
    z6 = (x2 - x3) * (y1 - y3) - (x1 - x3) * (y2 - y3)
    
    if (z1*z2 > 0) and (z3*z4 > 0) and (z5*z6 > 0) :
        
        print("Punkts D atrodas trijstūra iekšpusē")
    
    else :
        print("Punkts D neatrodas trijstūra iekšpusē")    
        
def vai_punkts_atrodas_trijstura_iekspuse_2_var():
    import math
    
    x1 = float(input("Ievadi X1 ===> "))
    y1 = float(input("Ievadi Y1 ===> "))
    x2 = float(input("Ievadi X2 ===> "))
    y2 = float(input("Ievadi Y2 ===> "))
    x3 = float(input("Ievadi X3 ===> "))
    y3 = float(input("Ievadi Y3 ===> "))
    x4 = float(input("Ievadi X4 ===> "))
    y4 = float(input("Ievadi Y4 ===> "))
    
    ab = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    bc = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
    ac = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
    ad = math.sqrt((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4))
    bd = math.sqrt((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4))
    cd = math.sqrt((x3-x4)*(x3-x4)+(y3-y4)*(y3-y4))
    
    
    z1 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
    z2 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
    z3 = (x4 - x2) * (y3 - y2) - (x3 - x2) * (y4 - y2)
    z4 = (x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)
    z5 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
    z6 = (x2 - x3) * (y1 - y3) - (x1 - x3) * (y2 - y3)
    
    if (z1*z2 > 0) and (z3*z4 > 0) and (z5*z6 > 0) :
        print("Punkts D atrodas trijstūra iekšpusē")
    else :
        print("Punkts D neatrodas trijstūra iekšpusē")

def vai_tris_punkti_atrodas_uz_vienas_taisnes():
    x1 = float(input("Ievadiet x1 ===> "))
    y1 = float(input("Ievadiet y1 ===> "))
    
    x2 = float(input("Ievadiet x2 ===> "))
    y2 = float(input("Ievadiet y2 ===> "))
    
    x = float(input("Ievadiet x3 ===> "))
    y = float(input("Ievadiet y3 ===> "))
    
    
    a=(x-x2)*(y1-y2)
    b=(y-y2)*(x1-x2)
    
    if a==b:
        print("\nPunkti atrodas uz vienas taisnes")
        
    if a!=b:
        print("\nPunkti nav uz vienas taisnes")    

def divu_punktu_novietojums_pret_taisni():
    print("Ax + By + C = 0\nA(x1,y1) B(x2,y2)\n")
    
    a = float(input("Ievadi A ===> "))
    b = float(input("Ievadi B ===> "))
    c = float(input("Ievadi C ===> "))
    x1 = float(input("Ievadi x1 ===> "))
    y1 = float(input("Ievadi y1 ===> "))
    x2 = float(input("Ievadi x2 ===> "))
    y2 = float(input("Ievadi y2 ===> "))
    
    z1 = a*x1 + b*y1 + c
    z2 = a*x2 + b*y2 + c
    
    if z1 == 0 and z2 == 0:
        
        print("Divi punkti ir uz vienas taisnes")
        
    elif z1 == 0 or z2 == 0:
        print("Viens punkts ir uz taisnes, otrais punkts nav uz taisnes")
        
    elif z1*z2 > 0:
        print("Atrodas vienā puse no taisnes")
        
    else:
        print("Punkti nav vienā pusē taisnei")    

def horoskopa_zime():
    print("Horoskopa zīmes noteikšana")
    
    print(("\n1 - Janvāris\n2 - Februāris\n3 - Marts\n4 - Aprīlis\n5 - Maijs\n6 - Jūnijs\n7 - Jūlijs\n8 - Augusts\n9 - Septembris\n10 - Oktobris\n11 - Novembris\n12 - Decembris\n"))
    m = int(input("Ievadiet savu dzimšanas mēnesi ===> "))
    d = int(input("Ievadi savu dzimšanas datumu ===> "))
    
    if d > 31 or d < 1:
        print("Nepareizi ievādīti dati")
    
    else:
        Hor = "Jūsu horoskopa zīme: "
    
        match m :
            case 1 :
                if d<20 :
                    print(Hor + "Mežāzis")
                else :
                    print(Hor + "Ūdensvīrs")
            
            case 2 :
                if d<19 :
                    print(Hor + "Ūdensvīrs")
                    
                elif d == 30:
                    print("\n30. februāris ir bijis trīs reizes pasaules vēsturē dažās valstīs,\nlai gan pēc Gregora kalendāra februārī ir 28 dienas parastajā gadāvai 29 dienas garajā gadā.")
                
                elif d > 29:
                    print("Nepareizi ievādīti dati")
                            
                else :
                    print(Hor + "Zivis")
            
            case 3 :
                if d<21 :
                    print(Hor + "Zivis")
                else :
                    print(Hor + "Auns")
            
            case 4 :
                if d<20 :
                    print(Hor + "Auns")
                    
                elif d<31:
                    print(Hor + "Vērsis")
                    
                else:
                    print("Nepareizi ievādīti dati")
            
            case 5 :
                if d<21 :
                    print(Hor + "Vērsis")
                else :
                    print(Hor + "Dvīņi")
        
            case 6 :
                if d<22 :
                    print(Hor + "Dvīņi")
                elif d<31:
                    print(Hor + "Vēzis")
                else:
                    print("Nepareizi ievādīti dati")                
        
            case 7 :
                if d<23 :
                    print(Hor + "Vēzis")
                else :
                    print(Hor + "Lauva")
        
            case 8 :
                if d<23 :
                    print(Hor + "Vēzis")
                else :
                    print(Hor + "Jaunava")
        
            case 9 :
                if d<23 :
                    print(Hor + "Jaunava")
                    
                elif d<31:
                    print(Hor + "Svari")
                else :
                    print("Nepareizi ievādīti dati") 
            
            case 10 :
                if d<23 :
                    print(Hor + "Svari")
            
                else :
                    print(Hor + "Skorpions")
                
            case 11 :
        
                if d<23 :
                    print(Hor + "Skorpions")
                
                elif d<31:
                    print(Hor + "Strēlnieks")
            
                else :
                    print("Nepareizi ievādīti dati") 
    
            
            case 12 :
            
                if d<22 :
                    print(Hor + "Strēlnieks")
                else :
                    print(Hor + "Mežāzis")
            
            case other:
                print("Nepareizi ievādīti dati")    

def kaulina_mesana():
    import random
    x = int(random.randint(1,6))
    
    print("Metamo kauliņu mešana programma\n")
    
    if x == 1 :
        print("Viens")
        
    elif x == 2 :
        print("Divi")
        
    elif x == 3 :
        print("Trīs")
        
    elif x == 4 :
        print("Četri")
        
    elif x == 5 :
        print("Pieci")
        
    elif x == 6 :
        print("Seši")    

def nedelas_dienas_nosaukumi_no_1_2100_gadam():
    import sys
    
    # G -gads
    # M - mēnesis
    # D - datums 
    
    G = int(input("Ievadiet gadu ===> "))
    M = int(input("Ievadiet mēnesi ===> "))
    D = int(input("Ievadiet datumu ===> "))
    
    if G < 1 or G > 2100:
        print("Kalendārs darbojas intervāla no 1.gada līdz 2100.gadam")
        sys.exit(0)
    
    if M < 1 or M > 12:
        print("Tāds datums neeksistē")
        sys.exit(0)
    
    if D < 1 or D > 31:
        print("Tāds datums neeksistē")
        sys.exit(0)
        
    
    if  M == 4 and D > 30:
        print("Tāds datums neeksistē")
        sys.exit(0)
    
    if  M == 6 and D > 30:
        print("Tāds datums neeksistē")
        sys.exit(0)
    
    if  M == 9 and D > 30:
        print("Tāds datums neeksistē")
        sys.exit(0)
    
    if  M == 11 and D > 30:
        print("Tāds datums neeksistē")
        sys.exit(0)
    
    if M == 1:
        month="janvārī"
    if M == 2:
        month="februārī"
    if M == 3:
        month="martā"
    if M == 4:
        month="aprīli"
    if M == 5:
        month="maijā"
    if M == 6:
        month="jūnijā"
    if M == 7:
        month="jūlijā"
    if M == 8:
        month="augustā"
    if M == 9:
        month="septembrī"
    if M == 10:
        month="oktobrī"
    if M == 11:
        month="novembrī"
    if M == 12:
        month="decembrī"
    
    x = (G-1)*365 + (G-1)//4 - (G-1)//100 + (G-1)//400 # pagajušo dienu skaits
    
    
    if G == 1900:
        F = 29
    
    elif (G % 400) == 0:
        F = 29
        
    elif (G % 100) == 0:
        F = 28
    
    elif (G % 4) == 0:
        F = 29
    
    else:
        F = 28
    
    if M == 2 and D > F:
        print("Tāds datums neeksistē")
        sys.exit(0)    
    
    match M:
        
        case 1 :
            
            d1 = D + x
        
        case 2 :
            d1 = D + x + 31
            
        case 3 :
            d1 = D + x + 31 + F
            
        case 4 :
            d1 = D + x + 31 + F + 31
            
        case 5 :
            d1 = D + x + 31 + F + 31 + 30
            
        case 6 :
            d1 = D + x + 31 + F + 31 + 30 + 31
            
        case 7 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30
            
        case 8 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31
            
        case 9 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31
            
        case 10 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30
            
        case 11 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            
        case 12 :
            d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30    
    
    SimboluVirkne = ""
        
    match d1 % 7 :
        case 4:
            SimboluVirkne = SimboluVirkne + "Ceturtdiena, "
        case 5 :
            SimboluVirkne = SimboluVirkne + "Piektdiena, "
        case 6 :
            SimboluVirkne = SimboluVirkne + "Sestdiena, "
        case 0 :
            SimboluVirkne = SimboluVirkne + "Svētdiena, "
        case 1 :
            SimboluVirkne = SimboluVirkne + "Pirmdiena, "
        case 2 :
            SimboluVirkne = SimboluVirkne + "Otrdiena, "
        case 3 :
            SimboluVirkne = SimboluVirkne + "Trešdiena, "
    
    Tukstosi = G // 1000
    Simti = G // 100
    Vieni = G % 10
    PirmieDiviCipari =  G // 10
    T = PirmieDiviCipari % 10
    Desmiti = G % 100
            
    
    
    match Tukstosi:
                
                case 1 :
                    SimboluVirkne = SimboluVirkne + "vieni tukstoši"
                
                case 2 :
                    SimboluVirkne = SimboluVirkne + "divi tukstoši"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""
    
    
    match Simti:
                
                case 1 | 11 | 21:
                    SimboluVirkne = SimboluVirkne + " vieni simti"
                
                case 2 | 12 | 22 :
                    SimboluVirkne = SimboluVirkne + " divi simti"
                
                case 3 | 13 | 23:
                    SimboluVirkne = SimboluVirkne + " trīs simti"
                
                case 4 | 14 | 24:
                    SimboluVirkne = SimboluVirkne + " četri simti"
                    
                case 5 | 15 | 25:
                    SimboluVirkne = SimboluVirkne + " pieci simti"     
                    
                case 6 | 16 | 26:
                    SimboluVirkne = SimboluVirkne + " seši simti"                
                
                case 7 | 17 | 27:
                    SimboluVirkne = SimboluVirkne + " septiņi simti"      
                    
                case 8 | 18 | 28:
                    SimboluVirkne = SimboluVirkne + " astoņi simti"
            
                case 9 | 19 | 29:
                    SimboluVirkne = SimboluVirkne + " deviņi simti"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""
            
    if T == 1 :
                match Desmiti:
                    case 10:
                        SimboluVirkne = SimboluVirkne + " desmit"                       
                    case 11:
                        SimboluVirkne = SimboluVirkne + " vienpadsmit"
                    case 12:
                        SimboluVirkne = SimboluVirkne + " divpadsmit"
                    case 13:
                        SimboluVirkne = SimboluVirkne + " trīspadsmit"
                    case 14:
                        SimboluVirkne = SimboluVirkne + " četrpadsmit"
                    case 15:
                        SimboluVirkne = SimboluVirkne + " piecpadsmit"
                    case 16:
                        SimboluVirkne = SimboluVirkne + " sešpadsmit"
                    case 17:
                        SimboluVirkne = SimboluVirkne + " septiņpadsmit"
                    case 18:
                        SimboluVirkne = SimboluVirkne + " astoņpadsmit"
                    case 19:
                        SimboluVirkne = SimboluVirkne + " deviņpadsmit"             
            
    else:
                
        
                match Desmiti: # Desmiti
                    
                    case 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 :
                        SimboluVirkne = SimboluVirkne + " divdesmit"
                    
                    case 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 :
                        SimboluVirkne = SimboluVirkne + " trīsdesmit"
                    
                    case 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49:
                        SimboluVirkne = SimboluVirkne + " četrdesmit"
                    
                    case 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59:
                        SimboluVirkne = SimboluVirkne + " piecdesmit"
                        
                    case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
                        SimboluVirkne = SimboluVirkne + " sešdesmit"     
                        
                    case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
                        SimboluVirkne = SimboluVirkne + " septiņdesmit"                
                    
                    case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
                        SimboluVirkne = SimboluVirkne + " astoņdesmit"      
                        
                    case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99:
                        SimboluVirkne = SimboluVirkne + " deviņdesmit"
                        
                    case _:
                        SimboluVirkne = SimboluVirkne + ""            
        
                match Vieni:
                    
                    case 1 :
                        SimboluVirkne = SimboluVirkne + " viens"
                    
                    case 2 :
                        SimboluVirkne = SimboluVirkne + " divi"
                    
                    case 3:
                        SimboluVirkne = SimboluVirkne + " trīs"
                    
                    case 4:
                        SimboluVirkne = SimboluVirkne + " četri"
                        
                    case 5:
                        SimboluVirkne = SimboluVirkne + " pieci"     
                        
                    case 6:
                        SimboluVirkne = SimboluVirkne + " seši"                
                    
                    case 7:
                        SimboluVirkne = SimboluVirkne + " septiņi"      
                        
                    case 8:
                        SimboluVirkne = SimboluVirkne + " astoņi"
                
                    case 9:
                        SimboluVirkne = SimboluVirkne + " deviņi"
                        
                    case _:
                        SimboluVirkne = SimboluVirkne + ""
                    
                    
    SimboluVirkne = SimboluVirkne + " gada " + month
    print(SimboluVirkne)    
    
def nodruka_skaitli_1_999_ar_vardiem():
    x = int(input("Ievadiet naturālo skaitli no 1 līdz 999\n===> "))
    
    if x < 1 or x > 999:
        print("Nepareizi ievadīti dati")
    
    else:
        Simti = x // 100
        Vieni = x % 10
        PirmieDiviCipari =  x // 10
        D = PirmieDiviCipari % 10
        Desmiti = x % 100
        
        SimboluVirkne = ""
    
    
        match Simti:
            
            case 1 :
                SimboluVirkne = SimboluVirkne + "vieni simti"
            
            case 2 :
                SimboluVirkne = SimboluVirkne + "divi simti"
            
            case 3:
                SimboluVirkne = SimboluVirkne + "trīs simti"
            
            case 4:
                SimboluVirkne = SimboluVirkne + "četri simti"
                
            case 5:
                SimboluVirkne = SimboluVirkne + "pieci simti"     
                
            case 6:
                SimboluVirkne = SimboluVirkne + "seši simti"                
            
            case 7:
                SimboluVirkne = SimboluVirkne + "septiņi simti"      
                
            case 8:
                SimboluVirkne = SimboluVirkne + "astoņi simti"
        
            case 9:
                SimboluVirkne = SimboluVirkne + "deviņi simti"
                
            case _:
                SimboluVirkne = SimboluVirkne + ""
        
        if D == 1 :
            match Desmiti:
                case 10:
                    SimboluVirkne = SimboluVirkne + " desmit"            
                case 11:
                    SimboluVirkne = SimboluVirkne + " vienpadsmit"
                case 12:
                    SimboluVirkne = SimboluVirkne + " divpadsmit"
                case 13:
                    SimboluVirkne = SimboluVirkne + " trīspadsmit"
                case 14:
                    SimboluVirkne = SimboluVirkne + " četrpadsmit"
                case 15:
                    SimboluVirkne = SimboluVirkne + " piecpadsmit"
                case 16:
                    SimboluVirkne = SimboluVirkne + " sešpadsmit"
                case 17:
                    SimboluVirkne = SimboluVirkne + " septiņpadsmit"
                case 18:
                    SimboluVirkne = SimboluVirkne + " astoņpadsmit"
                case 19:
                    SimboluVirkne = SimboluVirkne + " deviņpadsmit"             
        
        else:
            
    
            match Desmiti:        
                
                case 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 :
                    SimboluVirkne = SimboluVirkne + " divdesmit"
                
                case 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 :
                    SimboluVirkne = SimboluVirkne + " trīsdesmit"
                
                case 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49:
                    SimboluVirkne = SimboluVirkne + " četrdesmit"
                
                case 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59:
                    SimboluVirkne = SimboluVirkne + " piecdesmit"
                    
                case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
                    SimboluVirkne = SimboluVirkne + " sešdesmit"     
                    
                case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
                    SimboluVirkne = SimboluVirkne + " septiņdesmit"                
                
                case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
                    SimboluVirkne = SimboluVirkne + " astoņdesmit"      
                    
                case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99:
                    SimboluVirkne = SimboluVirkne + " deviņdesmit"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""            
    
            match Vieni:
                
                case 1 :
                    SimboluVirkne = SimboluVirkne + " viens"
                
                case 2 :
                    SimboluVirkne = SimboluVirkne + " divi"
                
                case 3:
                    SimboluVirkne = SimboluVirkne + " trīs"
                
                case 4:
                    SimboluVirkne = SimboluVirkne + " četri"
                    
                case 5:
                    SimboluVirkne = SimboluVirkne + " pieci"     
                    
                case 6:
                    SimboluVirkne = SimboluVirkne + " seši"                
                
                case 7:
                    SimboluVirkne = SimboluVirkne + " septiņi"      
                    
                case 8:
                    SimboluVirkne = SimboluVirkne + " astoņi"
            
                case 9:
                    SimboluVirkne = SimboluVirkne + " deviņi"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""
    
        print(SimboluVirkne)    

def romiesu_pieraksts_konverte_uz_arabu():
    import sys
    
    print("Pieejamie simboli:\nI - 1 \nV - 5 \nX - 10 \nL - 50 \nC - 100 \nD - 500 \nM - 1000\n")
    
    A = str(input("Ievadiet pirmo Romiešu ciparu skaitļa pieraksta (pirmo simbolu)\n===> "))
    B = str(input("Ievadiet otro Romiešu ciparu skaitļa pieraksta (otro simbolu)\n===> "))
    C = str(input("Ievadiet trešo Romiešu ciparu skaitļa pieraksta (trešo simbolu)\n===> "))
    
    if A+B+C == "VVV" or A+B+C == "LLL" or A+B+C == "DDD":
        print("Neder")
        sys.exit(0)
    
    match A :
        case "I" :
            A = 1
        case "V" :
            A = 5
        case "X" :
            A = 10
        case "L" :
            A = 50
        case "C" :
            A = 100
        case "D" :
            A = 500
        case "M" :
            A = 1000
        case other :
            print("Error")
            sys.exit(0)        
        
        
    match B :
        case "I" :
            B = 1
        case "V" :
            B = 5
        case "X" :
            B = 10
        case "L" :
            B = 50
        case "C" :
            B = 100
        case "D" :
            B = 500
        case "M" :
            B = 1000
        case other :
            print("Error")
            sys.exit(0)
            
    match C :
        case "I" :
            C = 1
        case "V" :
            C = 5
        case "X" :
            C = 10
        case "L" :
            C = 50
        case "C" :
            C = 100
        case "D" :
            C = 500
        case "M" :
            C = 1000
        case other :
            print("Error")
            sys.exit(0)
           
    if A >= B:
        if B >= C:
            
            if (B == 5 and C == 5) or (B == 50 and C == 50) or (B == 500 and C == 500):
                print("Neder")
                sys.exit(0)
             
            else:
                #print("A + B + C")
                print(A+B+C)
                sys.exit(0)
            
            
        elif A>=C:
            
            if B == 10 and (C == 50 or C == 100):
                print(A+C-B)
                sys.exit(0)
                
            if B == 100 and (C == 500 or C == 1000):
                print(A+C-B)
                sys.exit(0)        
                
            if A != 10 and A == C:
                print("Neder")
                sys.exit(0)
                
            if B == 5 and C == 10:
                print("Neder")
                sys.exit(0)
            
            if B != 1 or B != 5 and C >= 50:
                print("Neder")
                sys.exit(0)
                
            if B == 1 and C == 5 or C == 10:
                print(A+C-B)
                sys.exit(0)
                
            else:
                #print("A + C - B")
                print(A+C-B)
                sys.exit(0)
        
        else:
            print("Neder")
            sys.exit(0)
    
    
    elif B <= C:
        print("Neder")
        sys.exit(0)
        
        
    elif A <= C:
        print("Neder")
        sys.exit(0)
        
        
    else:
        if A > C:
            print("Neder")
            sys.exit(0)
            
            
        else:
            #print("-A + B + C")
            print(B+C-A)
            sys.exit(0)
    
def tris_punktu_novietojums_pret_taisni():
    print("Ax + By + C = 0\nA(x1,y1) B(x2,y2) C(x3,y3)\n")
    
    a = float(input("Ievadi A ===> "))
    b = float(input("Ievadi B ===> "))
    c = float(input("Ievadi C ===> "))
    
    x1 = float(input("Ievadi x1 ===> "))
    y1 = float(input("Ievadi y1 ===> "))
    
    x2 = float(input("Ievadi x2 ===> "))
    y2 = float(input("Ievadi y2 ===> "))
    
    x3 = float(input("Ievadi x3 ===> "))
    y3 = float(input("Ievadi y3 ===> "))
    
    z1 = a*x1 + b*y1 + c
    z2 = a*x2 + b*y2 + c
    z3 = a*x3 + b*y3 + c
    
    if z1 == 0 and z2 == 0 and z3 == 0:
        print("Trīs punkti ir uz vienas taisnes")
        
    elif (z1 == 0 and z2 == 0) or (z2 == 0 and z3 == 0) or (z3 == 0 and z1 == 0):
        print("Divi punkti ir uz taisnes, bet trešais nav uz taisnes")
        
    elif (z1 == 0 and z2*z3 > 0) or (z2 == 0 and z1*z3 > 0) or (z3 == 0 and z1*z2 > 0):
        print("Viens uz taisnes, divi pārejie ir vienā puse no taisnes")
        
    elif (z1 == 0 and z2*z3 < 0) or (z2 == 0 and z1*z3 < 0) or (z3 == 0 and z1*z2 < 0):
        print("Viens uz taisnes, divi pārejie ir pretējas puses no taisnes")
        
    elif (z1*z2>0) and (z1*z3>0):
        print("Visi trīs punkti ir vienā puse no taisnes")
    
    else:
        print("Divi punkti ir vienā puse no taisnes, trešais punkts ir pretēja puse no taisnes")
        
def for_i_in_range_no_1_15_katro_treso():
    print("Programma nodrukā secīgi skaitļus no 1 līdz 15 pēc kārtas un katru trešo.\n")
    for x in range(1, 16, 3):
        print(x)

def for_i_in_range_no_15_1_katro_treso():
    print("Programma nodrukā secīgi skaitļus no 15 līdz 1 pēc kārtas un katru trešo.\n")
    for x in range(15, 1, -3):
        print(x)

def ir_palindroms_vai_nav():
    x = input("Ievadi vārdu: ")
    y = len(x) # Cik ir garums
    
    atb = "Ir palindroms"
     
    for i in range (y//2):
        if x[i] != x[y-1-i]:
            atb ="Nav palindroms"
            break
        
    print(atb)

def kombinacijas_C_n_m():
    import sys
    
    n = int(input("Ievadi naturālu skaitli N (no cik) ===> "))
    m = int(input("Ievadi naturālu skaitli M (pa cik) ===> "))
    
    if m > n:
        print("M nevar būt lielākam par N")
        sys.exit(0)
        
    fn = 1
    
    for i in range(2, n+1) :
        fn = fn * i
        
    fm = 1
    
    for i in range(2, m+1) :
        fm = fm * i
        
    fnm = 1
    for i in range(2, n-m+1) :
        fnm = fnm * i
    
    c=fn/fm/fnm
    
    
    print ("\nC(" + str(m) + "," + str(n) +") = " + str(int(c)) + "\n")
    
    # ----------------------------------------
    
    nn = int(input("Ievadi no cik (N) ===> "))
    mm = int(input("Ievadi pa cik (M) ===> "))
    
    if mm > nn:
        print("M nevar būt lielākam par N")
        sys.exit(0)
    
    n = nn
    m = mm
    
    if m > n/2 :
        m=n-m
    n=n+1
    c=1
    
    for i in range(1, m+1) :
        c = c * (n-i) / i
        
    print ("\nC(" + str(mm) + "," + str(nn) +") = " + str(int(c)))

def nodruka_vardu_otradi():
    v=input("Ievadiet vārdu : ")
    
    v2=""
    
    for i in v:
    
        v2=i+v2
    
    print(v2)

def vai_pirmskaitlis():
    a = int(input("Ievadiet naturālo skaitļi, kurš ir lielāks par 1.\n==> ")) 
    
    #-------------
    if a <= 0:
        print("Skaitlis "+ str(a) + " nav naturāls skaitlis.")
        quit()
        
    if a==1:
        print("Skaitlis 1 nav lielāks par 1.")
        quit()
    #-------------
    
    b=1
    c=a
    
    for a in range (1, a-1, 1):
        b = b+1
        if c%b == 0:
    
            print("Skaitlis " + str(c) + " nav pirmskaitlis")
            quit()
    
    
    print("Skaitlis " + str(c) + " ir pirmskaitlis")

def cik_pilnu_kvadratu_satur_gredzens_2_var():
    # Importēsim math bibliotēku, lai izmantotu math.floor
    import math 
    
    # Definēsim funkciju, kura pārbauda vai punkts piedēr gredzenām vai nēpiedēr
    
    def bls(r, R, x, y):                                        # nosaukums funkcijai ir bls - no angl. belongs (piedēr)
        if (r*r <= x*x + y*y) and (x*x + y*y <= R*R): 
            return 1                                            # jā punkts ir gredzenā iekšā, tad return 1
        else: 
            return 0                                            # jā punkts nav gredzenā, tad return 0
        
        
    ammount = 0              # kvadrātu skaits gredzenā (tas ir kvadrātu skaititājs, sākuma ir 0 kvadrātu).
    
    
    R = float(input("Ievadiet gredzena arējo rādiusu ==> ")) # Lielāis rādiuss (arējais)
    r = float(input("Ievadiet riņķa iekšējo radiusu ==>  ")) # Mazais rādiuss (iekšējais)
    
    
    for x in range(0, math.floor(R) + 1): # Paitonā range(0,n) = [0,n), tāpēc paņemsim +1
        
        for y in range(0, math.floor(R) + 1): # Šeit cikls ir ciklā, lai visas iespējamās kombinācijas līdz R tiek pārbaudītas. ( x=0 y=0 ; x=0 y=1 ; x=0 y=2 utt. ------ x=1 y=0 ; x=1 y=1 ; x=1 y=2 utt. -------- līdz beigām)
            
            
            # Pirmkārt pārbaudam visas y pie x=0, pēc tām visas y pie x=1 utt. Vispār pārbaudīsim R*R kvadrātus (pilnā pārlase).
            if ((bls(r , R, x, y) == 1) and 
               (bls(r , R, x, y + 1) == 1) and 
               (bls(r , R, x + 1, y) == 1) and    # Pārbaudam, vai visi četri punkti piedēr gredzenam
               (bls(r , R, x + 1, y + 1) == 1)): 
                ammount = ammount+1               # ja piedēr, tad +1 kvadrātu skaititājam
                
                # Sākuma tiek pārbaudīts kvadrāts ar virsotnem (0 0) (0 1) (1 0) (1 1)
                # Tālak iterācijas y kļūst par 1 un tad tiek pārbaudīts kvadrāts ar virsotnem (0 1) (0 2) (1 1) (1 2) un tā tālāk uz augšu līdz R (līdz radiusa garumam).
                # Pēc tām x palielināsies par 1 arī (jo cikls ciklā) un tādēļ mes pārbaudisim visas kombinācijas.
    
    print(str(ammount*4) + " pilno kvadrātu ir gredzenā") # Pārbaudījam tikai pirmo kvadrāntu (I). Riņķis ir simetrisks pret (0;0) un tāpēc pareizināsim ar 4 kvadrātu skaitu.

def cik_pilnu_kvadratu_satur_gredzens():
    import math
    import sys
    
    def check_squares(a, b):
        n = 0
        if r1*r1 >= (a+1)*(a+1) + b*b >= r2*r2 and r1*r1 >= a*a + (b+1)*(b+1) >= r2*r2 and r1*r1 >= (a+1)*(a+1) + (b+1)*(b+1) >= r2*r2:
            n+=1
    
        if r1*r1 >= (a+1)*(a+1) + b*b >= r2*r2 and r1*r1 >= (a+1)*(a+1) + (b-1)*(b-1) >= r2*r2 and r1*r1 >= a*a + (b-1)*(b-1) >= r2*r2:
            n+=1
            
        if r1*r1 >= a*a + (b+1)*(b+1) >= r2*r2 and r1*r1 >= (a-1)*(a-1) + b*b >= r2*r2 and r1*r1 >= (a-1)*(a-1) + (b+1)*(b+1) >= r2*r2:
            n+=1
            
        if r1*r1 >= a*a + (b-1)*(b-1) >= r2*r2 and r1*r1 >= (a-1)*(a-1) + b*b >= r2*r2 and r1*r1 >= (a-1)*(a-1) + (b-1)*(b-1) >= r2*r2:
            n+=1
            
        return n
    
    r1 = float(input("Ievadiet gredzena arējo rādiusu ==> "))
    r2 = float(input("Ievadiet gredzena iekšējo rādiusu ==> "))
    
    
    if r1 < 0 or r2 < 0 :
        print("Dati nav ievadīti atbilstoši nosacījumiem")
        sys.exit(0)
    
    
    a = math.floor(r1)
    b = -math.floor(r1)
    
    number_of_squares = 0
    
    while a >= -r1:
        b = -math.floor(r1)
        while b <= r1:
            if r1*r1 >= a*a + b*b >= r2*r2:
                
                number_of_squares += check_squares(a, b)
            b+=1
        a-=1
        
    print(str(int(number_of_squares/4)) + " pilno kvadrātu ir gredzenā")

def cik_pilnu_kvadratu_satur_rinkis_R():
    import math
    
    r=float(input("Ievadiet riņķa rādiusu ==> "))
    r1=int(r)
    s=0
    
    for i in range (1, r1):
        x=round(math.sqrt(r*r-i*i))
        if x*x+i*i==r*r:
            s=s+4*x
        else:
            s=s+int(math.sqrt(r*r-i*i))*4
    
    print(str(s) + " pilno kvadrātu 1x1 satur riņķis ar rādiusu " + str(r) + " vienības")

def izdruka_vardu_ka_kvadratu():
    x = str(input("Ievādi vārdu => "))
    
    n = len(x)
    
    print(x)
    
    for i in range (1, n-1):
        sv = x[i]
        
        sv = sv + (n-2)*" "
        
        sv = sv + x[n-1-i]
        print(sv)
        
    sv = ""
    
    for i in x:
        sv = i + sv
    print(sv)

def izdruka_vardu_ka_paradits():
    x=input("Ievadi simbolu virkni => ")
    n=len(x)
    for i in range (n):
        print(x[i:n]+x[0:i])

def laimigie_loterijas_bilesu_numuri():
    # Uzdevuma formulējums: Sastādīt programmu, kas nodrukā visus laimīgos loterijas biļešu numurus.
    # Ja zināms, ka loterijas biļešu numuri ir četrciparu skaitļi no 0000 līdz 9999, bet par laimīgiem tie uzskatīti
    # tie numuri, kas apmierina šādus nosacījumus:
    # 1) visi cipari ir dažādi.
    # 2) Pirmo divu un pēdējo divu ciparu veidoto skaitļu summa ir vienāda ar visu četru ciparu reizinājumu.
    # Versija 1.0
    
    for a in range(0, 10) :
        for b in range(0, 10) :
            for c in range(0, 10) :
                for d in range(0, 10) :
    
                    if ((a!=0) and (b!=0) and
                        (c!=0) and (d!=0) and
                        (a!=b) and (a!=c) and
                        (a!=d) and (b!=c) and
                        (b!=d) and (c!=d) and
                        (10*a+b+10*c+d==a*b*c*d)) :
                        print (str(a) + str(b) +
                               str(c) + str(d))


def nodruka_visus_pirmskaitlus_no_1_lidz_N():
    import math
    import sys
    
    x = int(input("Programmā nodrukā visus pirmskaitļus no 1 līdz N. Ievadiet naturālo skaitļi N ==> "))
    
    if x < 1:
        print("Tas nav naturāls skaitlis")
        sys.exit(0)
        
    if x == 1:
        print("1 nav naturāls skaitlis")
        sys.exit(0)
    
    for a in range (1, x+1):
        if a > 1:
            for i in range (2, a):
                if (a % i) == 0:
                    break
            else:
                print(a)    

def cetru_skaitlu_LKD_un_MKD():
    # Uzdevumu skicē:
    
    # 4 skaitli:
    # a b c d
    # lcm (a, b) = f
    # f c d
    # lcm (f, c) = g
    # g d
    # lcm (g, d) = lcm (a, b, c, d)
    
    # Lai atrāstu lcm diviem skaitliem:
    # a b
    # gcd (a, b) = c
    # lcm (а b) = a * b / c
    # gcd var atrāst pēc Eiklīda algoritma
    
    #--------------------------
    
    # Uzdevumu plāns
    
    # Četri skaitli
    # a b c d
    # 1) gcd(a, b) = C
    # 2) lcm (a, b) = a*b/C = f
    # 3) gcd(f, c) = D
    # 4) lcm(f, c) = f*c/D = g
    # 5) gcd(g, d) = K
    # 6) lcm(g, d) = g*d/K
    # 7) lcm(g, d) = lcm(a, b, c, d) (tas vajag printēt)
    # 8) lcm(a,b) = f
    # 9) lcm(c,d) = n
    # 10) lcm(a,b,c,d) = lcm(f,n) (tas vajag printēt)
    
    import math
    
    x = int(input("Ievadi 1.skaitli ===> ")) # skaitlis a
    y = int(input("Ievadi 2.skaitli ===> ")) # skaitlis b
    
    if x<=0 or y<=0:
        print("Ievadiet pozitivo veselo skaitli!")
        quit()
    
    A1 = x
    B1 = y
    
    #----------
    # aprēķini 
    # gcd (a, b) = C
    # lcm (a, b) = f
    
    a = x
    b = y
    
    while b != 0 :
        c = a % b
        a = b
        b = c
    
    LKD12 = a       # gcd (a,b) = C       
    MKD12 = (x*y)/a # lcm (a, b) = a*b/C
    f = MKD12       # lcm (a, b) = f
    
    #----------
    
    # aprēķini 
    # gcd(f, c) = D
    # lcm(f, c) = g
    
    x = int(input("Ievadi 3.skaitli ===> ")) # skaitlis c
    
    if x<=0:
        print("Ievadiet pozitivo veselo skaitli!")
        quit()
        
    C1 = x
    y = f
    a = x
    b = y
    
    while b != 0 :
        c = a % b
        a = b
        b = c
    
    LKDfc = a        # gcd(f, c) = D
    MKDfc = (x*y)/a  # lcm(f, c) = f*c/D = g
    g = MKDfc        # lcm(f, c) = g
    x = g
    
    
    #----------
    
    # aprēķini 
    # gcd(g, d) = K
    # lcm(g, d) = lcm(a, b, c, d)
    
    y = int(input("Ievadi 4.skaitli ===> ")) # skaitlis d
    
    if y<=0:
        print("Ievadiet pozitivo veselo skaitli!")
        quit()
        
    D1 = y
    
    a = x
    b = y
    
    while b != 0 :
        c = a % b
        a = b
        b = c
    
    
    LKDgd = a              # gcd(g, d) = K
    MKDgd = int((x*y)/a)
    
    #----------
    
    print("\nMazākais kopīgais dalāmais MKD = " + str(MKDgd)) 
    print("lcm(" + str(A1) + ", " + str(B1) + ", " + str(C1) + ", " + str(D1) + ") = " + str(MKDgd) + "\n")
    
    #----------
    # aprēķini 
    # lcm(c,d) = n
    # lcm(c,d) = n
    
    a = C1
    b = D1
    
    while b != 0 :
        c = a % b
        a = b
        b = c
    
    
    LKD34 = a # lcm(c,d) = n
    
    a = LKD12 # lcm(a,b) = f
    b = LKD34 # lcm(c,d) = n
    
    #----------
    # aprēķini 
    # lcm(a,b,c,d) = lcm(f,n)
    
    
    while b != 0 :
        c = a % b
        a = b
        b = c
    
    LKDkop = a    # lcm(a,b,c,d) = lcm(f,n)
    
    #----------
    
    print("Lielākais kopīgais dalītājs LKD = " + str(LKDkop)) 
    print("gcd(" + str(A1) + ", " + str(B1) + ", " + str(C1) + ", " + str(D1) + ") = " + str(LKDkop) + "\n")

def dators_min_iedomato_skaitli():
    import random
    import math
    
    
    min_diapazons = 1
    
    try:
        max_diapazons = int(input("Programma minēs skaitļi intervalā [1, N] veseļos skaitļos \nIevadiet skaitļi N (maksimālo skaitļi, lai noteiktu diapazonu) \n==> "))
        print("\nIedomajiet veselo skaitļi no 1 līdz " + str(max_diapazons))
        print("\nJa mans minetāis skaitlis ir mazāks vai lielāks par jūsu iedomāto skaitļi, ievadiet attiecīgi “<” vai “>”, un, ja es uzminēju pareizi, ievadiet “=”")
    
    except ValueError:
        print("Nepareiza ievade! Ievadiet veselo skaitļi!")
        quit(0)
        
        
    rnd = math.floor(max_diapazons/2)
    sk = 1
    atbilde = ""
    
    
    while 1 > 0:
        print("\nJūsu iedomatais skaitlis ir:\n" + str(rnd) + "\nvai es minēju? Intervāls no", min_diapazons, "līdz", max_diapazons)
        
        atbilde = input("Atbilde (>, <, =): ")
        
        if atbilde == "=":
            print("Es minēju jūsu skaitļi " + str(rnd) + " no " + str(sk) + " reizes. Spēle beigusies.")
            break
        
        elif atbilde == "<":
            max_diapazons = rnd - 1
            
            try:
                rnd = random.randint(min_diapazons, max_diapazons)
                sk = sk + 1
            except:
                print("Tā nevar būt! Tu melo! Es ar tevi vairs nespēlēšos!")
                break
                
        elif atbilde == ">":
            min_diapazons = rnd + 1
            
            try:
                rnd = random.randint(min_diapazons, max_diapazons)
                sk = sk + 1
            except:
                print("Tā nevar būt! Tu melo! Es ar tevi vairs nespēlēšos!")
                break
            
        else:
            print("Nepareiza ievade! Ievadiet: '<', '>' vai '='")    

def fibonaci_skaitlis_kas_parsniedz_ievadito():
    print("Programma nosaka mazāko Fibonači skaitli (skaitli no Fibonači virknes), kas pārsniedz lietotāja ievadīto skaitli N.")
    n = float(input("Ievadiet skaitli N ==> "))
    
    b=1
    a=1
    c=0         # a,b=b,a+b (ja to izmantojam, tad nevajadzēs izmantot palīgmainīgo c)
    
    while n>=a: # kāmer n>=a, tad 
    
                    # a,b=b,a+b
                    # var arī to konstrukciju izmantot
        c = a + b
        a = b
        b = c
    
    print("Mazakais Fibonači skaitlis, kas pārsniedz skaitli " + str(n) + " ir " + str(a))

def n_ciparu_fibonaci_virkne():
    n = int(input("Ievadiet skaitli N ==> "))
    
    if n<=0:
        print("Neēksistē cipars ar tādu numuru")
        quit()
    
    a=1
    b=1
    c=0
    
    sv = str(a) + str(b)
    
    while len(sv) < n:
        c = a+b
        a=b
        b=c
        sv = sv+str(c)
        
    print("Fibonači virknē zem numura " + str(n) + " atrodas cipars:")
    print(sv[n-1])

def skaitlu_minesana():
    import random
    
    print("Spēlē:\nDators 'iedomāsies' veselo skaitli no 1 līdz N un Jums būs nepieciešāms to atminēt.")
    N = int(input("Ievādiet veselo skaitli N ==> "))
    
    
    x = random.randint(1, N)
    sk=1
    y=0
    
    y = int(input("Mini skaitļi! ==> "))
    
    while y != x:
        if y < x:
            y = int(input("Neatminēji! Ievadi lielāko ==> "))
        elif y > x:
            y = int(input("Neatminēji! Ievadi mazako ==> "))
        sk = sk+1
        
    print("Malacis! Atminēji skaitļi " + str(x) + " intervāla no 1 līdz " + str(N) + " no " + str(sk) + " reizes")    

def vai_veido_aritmetisko_progresiju():
    sv = "Dota virkne ir aritmētiska progresija"
    
    x1 = float(input("Ievadiet 1 locekli ===> "))
    
    if x1 == 0:
        print("Šajā virknē nav elementu.") # Ja uzreiz 0 ievada
        quit()
        
    x2 = float(input("Ievadiet 2 locekli ===> "))
    
    if x2 == 0: # Ja tikai vienu elementu ievada
        print("Šajā virknē ir tikai viens elements.\nAritmētiskas progresijas tiek definētas skaitļu virknem ar vismaz diviem elementiem.")
        quit()
        
    d = x2 - x1
    
    N = 3
    
    x = float(input( "Ievadiet " + str(N) + " locekli ===> "))
    
    
    while x != 0:
        d1 = x - x2
        
        if d != d1:
            sv = "Dota virkne nav aritmētiska progresija"
            
        x2 = x
        N = N+1
        x =  float(input("Ievadiet " + str(N) + " locekli ===> "))   
    else:
        print(sv)
       
       
        
    if x==0: # pedējo un prikšpēdējo atņēmt
        d1 = x - x2
        if d != d1:
            sv = "Dota virkne nav aritmētiska progresija"     
    else:
        print(sv)

def vai_veido_aritmetisko_vai_geometrisko_progresiju():
    sv = "Dota virkne ir aritmētiskā progresija"
    sv1 = "Dota virkne ir geometriskā progresija"
    
    x1 = float(input("Ievadiet 1 locekli ===> "))
    
    if x1 == 0:
        print("Šajā virknē nav elementu.") # Ja uzreiz 0 ievada
        quit()
        
    x2 = float(input("Ievadiet 2 locekli ===> "))
    
    if x2 == 0: # Ja tikai vienu elementu ievada
        print("Šajā virknē ir tikai viens elements.\nAritmētiskas un ģeometriskas progresijas tiek definētas skaitļu virknem ar vismaz diviem elementiem.")
        quit()
        
    d = x2 - x1
    q = x2/x1
    N = 3
    
    x = float(input( "Ievadiet " + str(N) + " locekli ===> "))
    
    
    while x != 0:
        d1 = x - x2
        q1 = x/x2
        
        if d != d1:
            sv = "Dota virkne nav aritmētiskā progresija"
            
        if q != q1:
            sv1 = "Dota virkne nav geometriskā progresija"        
            
        x2 = x
        N = N+1
        x =  float(input("Ievadiet " + str(N) + " locekli ===> "))   
    else:
        print(sv)
        print(sv1)
       
       
        
    if x==0: # pedējo un prikšpēdējo atņēmt
        d1 = x - x2
        q1 = x/x2
        if d != d1:
            sv = "Dota virkne nav aritmētiskā progresija"
        if q != q1:
            sv1 = "Dota virkne nav geometriskā progresija" 
    else:
        print(sv)
        print(sv1)

def cos_x_ar_noradito_precizitati():
    x = float(input("Ievadi funkcijas argumentu ===> "))
    pr = float(input("Ievadi precizitāti ===> "))
    
    z = 1
    s = 1
    n = 0
    y = 1
    
    while abs(y) > pr:
        z = -z
        n = n + 1
        y = y * x * x / 2 / n / (2 * n - 1)
        s = s + z * y
        
    print("сos(" + str(x) + ") = " + str(s) + " ar precizitāti " + str(pr))    

def fibonaci_eglite():
    d = int(input("Ievadi lielākā zara garumu ===> "))
    
    a = 1
    b = 1
    c = a + b
    garums = 1
    
    # ------ Maksimālo garumu noteikšana
    
    k=1
    while k != 0:
        
        if c>d:
            garums=b*2 # *2, jo eglītei ir divas puses. Tāpēc, lai reķinātu tukšumus mums
            k=0 # cikla apstāšanai
            
        a = b
        b = c
        c = a + b # Fibonači virkne
        
    # ------ 
    
    #--------------Pirmais zars (augšējais - pirmā rinda)    
    
    tuksumi = " " * int((garums-len("**"))//2)    # Tukšumu skaitīšana. Dalām ar 2 jo tukšumi ir no divām pusēm. Nakāmajā rindā tas ir parādīts
    egles_pirmais_zars = tuksumi + "**" + tuksumi
    print(egles_pirmais_zars)
    
    #--------------   
    
    # ----- Parējo zaru noteikšana
    
    a = 1
    b = 1
    c = 1 # mainīgie Fibonači virknei
    
    egle = ""
    
    while c <= d :
        
        zars = "**"*c                                 # No kā ir veidots zars
        tuksumi = " " * int((garums-len(zars))//2)      # Tukšumu skaitīšana. Dalām ar 2 jo tukšumi ir no divām pusēm. Nakāmajā rindā tas ir parādīts
        egle = egle + tuksumi + zars + tuksumi + "\n" # ______****______
        
        a = b
        b = c
        c = a + b
    
    print(egle)

def laukums_kuru_ierobezo_divas_parabolas():
    import math
    
    print("Programma noteic laukumu kuru ierobežo divas parabolas:\ny = ax^2 + bx + c \ny = dx^2 + ex + f\n")
    
    a1 = float(input("Ievadi a ===> "))
    b1 = float(input("Ievadi b ===> "))
    c1 = float(input("Ievadi c ===> "))
    
    a2 = float(input("Ievadi d ===> "))
    b2 = float(input("Ievadi e ===> "))
    c2 = float(input("Ievadi f ===> "))
    
    pr =  float(input("Ievadi precizitāti ===> "))
    
    a = a1 - a2
    b = b1 - b2
    c = c1 - c2
    
    if a == 0 :
        print("Laukums ir 0")
        quit()
    else :
        d = b * b - 4 * a * c # Diskriminants
        if d < 0:
            print("Laukums ir 0") # Kvadratvienādojumam realu saknu nav jo divam parabolam nav krustpunktu, tāpēc laukums neveidojas.
            quit()
        elif d == 0 :
            x12 = -b / 2 / a
            print("Laukums ir 0") # jo divas parabolas krustpunkts ir tikai viens, tāpēc laukums neveidojas.
            quit()
        else :
            x1 = (-b + math.sqrt(d)) / (2 * a) # Parabolu krustpunkti
            x2 = (-b - math.sqrt(d)) / 2 / a
            
    # ---------  laukums zem pirmās funkcijas  
    
    a = x1 
    b = x2
    
    
    s1 = 0
    n = 2
    x = (b - a) / n
    s2 = 0
    
    for i in range (n) :
        y = a+i*x
        s2 = s2 + (a1*y*y + b1*y + c1)*x
    n = n * 2
    
    while abs(s1 - s2) > pr :
        s1 = s2
        x = (b - a) / n
        s2 = 0
        for i in range (n) :
            y = a+i*x
            s2 = s2 + (a1*y*y + b1*y + c1)*x
        n = n * 2
    
    S1 = s2
    
    # --------- laukums zem otras funkcijas
    
    a = x1 
    b = x2
    
    
    s1 = 0
    n = 2
    x = (b - a) / n
    s2 = 0
    
    for i in range (n) :
        y = a+i*x
        s2 = s2 + (a2*y*y + b2*y + c2)*x
    n = n * 2
    
    while abs(s1 - s2) > pr :
        s1 = s2
        x = (b - a) / n
        s2 = 0
        for i in range (n) :
            y = a+i*x
            s2 = s2 + (a2*y*y + b2*y + c2)*x
        n = n * 2
        
        
    S2 = s2
    
    S_kop = abs(S1 - S2)
    
    print("\nLaukums, kuru ierobežo divas parabolas, ir vienāds ar:\n" + str(S_kop))
    print("Rezultāts ir iegūts ar precizitāti:\n" + str(pr))

def laukums_zem_funkcijas_grafika():
    print("Programma noteic laukumu zem funkcijas y = ax^3 + bx^2 + cx + d intervāla [u,w].\nJa laukums ir zem X ass, tad laukums ir negatīvs.\n")
    
    q = float(input("Ievadi a ===> "))
    w = float(input("Ievadi b ===> "))
    e = float(input("Ievadi c ===> "))
    r = float(input("Ievadi d ===> "))
    
    a = float(input("Ievadi sākumpunktu u ===> "))
    b = float(input("Ievadi galapunktu w ===> "))
    
    pr = float(input("Ievadi precizitāti ===> "))
    
    
    #------------------- ar taisnsturiem
    
    s2 = 0
    n=2
    paz = True
    while paz :
        s1 = s2
        x = (b - a) / n
        s2 = 0
        for i in range (n) :
            y=a+i*x
            s2 = s2 + (y*y*y*q+y*y*w+y*e+r) * x
        n = n * 2
        if abs(s1 - s2) < pr :
            paz = False
    
    print("\nS ar taisnturiem = " + str(s2))
    print("Iterāciju skaits: " + str(n) + "\n")
    
    
    #------------------- ar trapecem
    
    n = 2
    s2 = 0
    
    paz = True
    while paz :
        s1 = s2
        x = (b - a) / n
        s2 = 0
        c = a*a*a*q+a*a*w+a*e+r
        for i in range (1,n+1) :
            y=a+x*i
            d = y*y*y*q+y*y*w+y*e+r
            s2 = s2 + x * (c + d) / 2
            c = d
        n = n * 2
        if abs(s1 - s2) < pr :
            paz = False
            
    print("S ar trapecem = " + str(s2))
    print("Iterāciju skaits: " + str(n))

def skaitla_N_pirmreizinataji():
    n = int(input("Ievadi naturālu skaitli ===> "))
    a = n
    j = 2
    
    sv1 = str(n) + " | "
    
    while a > 1 :
        k = 0
        
        while (a % j) == 0 :
            sv1 = str(a) + " | " + str(j)
            a = a // j
            k = k + 1
            print(sv1)
            
        j = j + 1
        
    print("1 | 1")    

def katru_vardu_apgriez_otradi():
    x = input("Ievadi simbolu virkni ===> ")
    
    x = x.strip()
    n = len(x)
    
    v = ""
    sv = ""
    
    for i in range(n): # for s in x
        if x[i] != " " :  # s ! = ""
            v = x[i] + v # v = s + v
            
        else:
            sv = sv + v + " "
            v = ""
    sv = sv + v
    
    print(sv)

def vai_ir_naturals_skaitlis():
    import math
    
    A = input("Ievadi skaitli A ===> ")
    B = input("Ievadi skaitli B ===> ")
    
    try:
        d = float(A)
        e = float(B)
        
    except:
        print("A vai B nav skaitlis")
        quit()
        
    else:   
        A=A.strip()
        B=B.strip()
    
        if len(A)<1 or len(B)<1 or A =="." or A=="+" or A=="-" or B =="." or B=="+" or B=="-":
            print("A vai B nav skaitlis")
            quit()
            
    a=1
    while a<=3:
            x = input("\nIevadi simbolu virkni ===> ")
            x=x.strip()
        
        
            if len(x)<1 or x=="." or x=="+" or x=="-":
                print("\nIevadīta simbolu virkne nav naturāls skaitlis")
        
            else:
                if (x[0]=="-") or (x[0]=="+"):
                    y=1
                else:
                    y=0
            p=0
            r=0
            for i in range(y,len(x)):
                s=x[i]
                if s==".":
                    p = p+1
                elif (s<"0" or s>"9"):
                    r = r+1
            if (p == 0) and r==0:
                #print("Ievadīta simbolu virkne ir vesels skaitlis")
                if float(x) <= 0:
                    print("Ievadīta simbolu virkne nav naturāls skaitlis (patstāvīgi analizējot simbolu virkni)")
                else:
                    #print("Ievadīta simbolu virkne ir naturāls skaitlis")
        
                    A = float(A)
                    B = float(B)
        
                    if A > B:
                        K = B
                        B = A
                        A = K        
        
                    if float(x) >= float(A) and float(x) <= float(B):
                        print("Ievadīta simbolu virkne ir naturāls skaitlis intervāla no " + str(A) + " līdz " + str(B) + " (patstāvīgi analizējot simbolu virkni)")
        
                    else:
                        print("Ievadīta simbolu virkne ir naturāls skaitlis, bet skaitlis nav intervāla no " + str(A) + " līdz " + str(B) + " (patstāvīgi analizējot simbolu virkni)")        
        
            else:
                print("Ievadīta simbolu virkne nav naturāls skaitlis (patstāvīgi analizējot simbolu virkni)")
    
            try :
                t = float(x)
                b = int(x)
                k = math.sqrt(t)
                u = 0/(float(x))
                    
            except:
                print("Ievadīta simbolu virkne nav naturāls skaitlis (izmantojot try/except)")
                a=a+1
        
            else:
                if x == 0:
                    print("Ievadīta simbolu virkne nav naturāls skaitlis (izmantojot try/except)")
                    
                if float(x) >= float(A) and float(x) <= float(B):
                    print("Ievadīta simbolu virkne ir naturāls skaitlis intervāla no " + str(A) + " līdz " + str(B) + " (izmantojot try/except)")
                    quit()
                else:
                    print("Ievadīta simbolu virkne ir naturāls skaitlis, bet skaitlis nav intervāla no " + str(A) + " līdz " + str(B) + " (izmantojot try/except)")
                    a=a+1
                    
    print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")

def vai_ir_reals_skaitlis_ar_komatiem():
    # Programma arī pārbauda skaitļus ar komatiem!
    
    a=1
    while a<=3:
        x = input("\nIevadi simbolu virkni ===> ")
        x=x.strip()
    
        if len(x)<1 or x=="." or x=="+" or x=="-" or x=="," or x[0] == "," or x[0:2] == "-," or x[0:2] == "+,":
            print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
    
        else:
            if (x[0]=="-") or (x[0]=="+"):
                y=1
    
            else:
                y=0
    
            p=0
            r=0
    
            for i in range(y,len(x)):
                s=x[i]
    
                if s=="." or s==",":
                    p = p+1
    
                elif (s<"0" or s>"9"):
                    r = r+1
    
            if (p==1 or p == 0) and r==0:
                print("Ievadīta simbolu virkne ir reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
    
            else:
                print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
    
    
    
        # Ar try, except. Arī 5,2 arī tiek uzskaitīts par skaitli. Tiek izmantots if lai piemēram ,2 -,2 +,2 "skaitļus" neuzskaitītu par skaitliem
    
        try :
            if x[0] == "," or x[0:2] == "-," or x[0:2] == "+,":
                quit()
            x = float(x.replace(',', '.')) 
            b = float(x)
    
        except :
            print("Ievadīta simbolu virkne nav reāls skaitlis (izmantojot try/except)")
            a=a+1
        else:
            print("Ievadīta simbolu virkne ir reāls skaitlis (izmantojot try/except)")
            quit()
            
    print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")

def vai_ir_reals_skaitlis():
    # Programma neparbauda skaitļus ar komatiem.
    
    a=1
    while a<=3:
        x = input("\nIevadi simbolu virkni ===> ")
        x=x.strip()
        
        if len(x)<1 or x=="." or x=="+" or x=="-":
            print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
            
        else:
            if (x[0]=="-") or (x[0]=="+"):
                y=1
            else:
                y=0
            p=0
            r=0
            for i in range(y,len(x)):
                s=x[i]
                if s==".":
                    p = p+1
                elif (s<"0" or s>"9"):
                    r = r+1
            if (p==1 or p == 0) and r==0:
                print("Ievadīta simbolu virkne ir reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
                
            else:
                print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")
                
    
    
        # Šeit nav uzskaitīts 2,2 skaitlis par skaitli
        try :
            b = float(x)
    
        except :
            print("Ievadīta simbolu virkne nav reāls skaitlis (izmantojot try/except)")
            a=a+1
    
        else:
            print("Ievadīta simbolu virkne ir reāls skaitlis (izmantojot try/except)")
            quit()
        
    print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")

def vai_ir_vesels_skaitlis():
    # Programma neparbauda skaitļus ar komatiem.
    
    a=1
    while a<=3:
        x = input("\nIevadi simbolu virkni ===> ")
        x=x.strip()
        
        if len(x)<1 or x=="." or x=="+" or x=="-":
            print("Ievadīta simbolu virkne nav vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
            
        else:
            if (x[0]=="-") or (x[0]=="+"):
                y=1
            else:
                y=0
            p=0
            r=0
            for i in range(y,len(x)):
                s=x[i]
                if s==".":
                    p = p+1
                elif (s<"0" or s>"9"):
                    r = r+1
            if (p == 0) and r==0:
                print("Ievadīta simbolu virkne ir vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
                
            else:
                print("Ievadīta simbolu virkne nav vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
        
        # Šeit nav uzskaitīts 2,2 skaitlis par skaitli
        try :
            
            b = int(x)
    
        except :
            print("Ievadīta simbolu virkne nav vesels skaitlis (izmantojot try/except)")
            a=a+1
    
        else:
            print("Ievadīta simbolu virkne ir vesels skaitlis (izmantojot try/except)")
            quit()
        
    print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")

def draudzigie_pirmskaitli_no_1_lidz_N():
    import math
    
    def vaipirmskaitlis (n):
        M = round(math.sqrt(n))+1
        for i in range(2, M):
            if n % i == 0:
                return False
        return True
    
    def draugi(x,y):
        if abs(x-y)==2:
            return True
        else:
            return False
    
    
    print("Programma nodrukā visus “draudzīgos” pirmskaitļu pārus no 1 līdz N.\nPar draudzīgu pirmskaitļu pāri tādus divus pirmskaitļus, kuru starpība ir 2.\n")
    
    
    M=0
    while M<=3:
        
        if M==0:
            x=input("Ievadiet naturālo skaitli N => ")
        elif M==1 or M==2:
            x=input("Tas nav naturāls skaitlis. Ievadiet naturālo skaitli N => ")
        elif M==3:
            x=input("Jūs 3 reizes kļūdījāties. Beidzam sadarbību!")
            quit()
            
        try:
            x = int(x)
            a = 1/x
            b=math.sqrt(x)
    
        except:
            M=M+1
    
        else:
            if x<5:
                print("Pāru nav")
                break
            else:
    
                sv=""
                b = 3
                for i in range (5, x+1, 2):
                    if vaipirmskaitlis(i):
                        a = b
                        b = i
                        if draugi (a,b):
                            sv = sv + (str(a) + " " + str(b)) + "\n"
    
                print(sv)
                break    

def izliekts_vai_ieliekts_piecsturis_un_laukums():
    import math
    
    def line_and_check(x1,y1,x3,y3,x2,y2,x4,y4):
        a = y3-y1
        b = x1-x3
        c = x3*y1-x1*y3
    
        z1=a*x2+b*y2+c
        z3=a*x4+b*y4+c
        
        if (z1*z3>0) :
            return False
            #print("Punkti ir vienā pusē taisnei.")    
        else :
            return True
            #print("Punkti nav vienā pusē taisnei.")
    
    # x*(y3-y1)+y*(x1-x3)+x3*y1-x1*y3=0
    
    print("Programma nosaka, vai dotais piecstūris ir vai nav izliekts.\nJa piecstūris ir izliekts, tā aprēķina tā laukumu.\nPiecstūra virsotņu koordinātas secīgi pulksteņa rādītajā virzienā ievada lietotājs.\n")
    x1 = input("Ievadi x1 ===> ")
    y1 = input("Ievadi y1 ===> ")
    
    x2 = input("Ievadi x2 ===> ")
    y2 = input("Ievadi y2 ===> ")
    
    x3 = input("Ievadi x3 ===> ")
    y3 = input("Ievadi y3 ===> ")
    
    x4 = input("Ievadi x4 ===> ")
    y4 = input("Ievadi y4 ===> ")
    
    x5 = input("Ievadi x5 ===> ")
    y5 = input("Ievadi y5 ===> ")
    
    M=1
    while M<3:
        try:
            x1 = float(x1)
            y1 = float(y1)
            
            x2 = float(x2)
            y2 = float(y2)
            
            x3 = float(x3)
            y3 = float(y3)
            
            x4 = float(x4)
            y4 = float(y4)
            
            x5 = float(x5)
            y5 = float(y5)
            
        except:
            M=M+1
            print("\nKaut viena koordināta tika nekorekti ievadīta. Ievadiet realus skaitļus!\n")
            x1 = input("Ievadi x1 ===> ")
            y1 = input("Ievadi y1 ===> ")
    
            x2 = input("Ievadi x2 ===> ")
            y2 = input("Ievadi y2 ===> ")
    
            x3 = input("Ievadi x3 ===> ")
            y3 = input("Ievadi y3 ===> ")
    
            x4 = input("Ievadi x4 ===> ")
            y4 = input("Ievadi y4 ===> ")
    
            x5 = input("Ievadi x5 ===> ")
            y5 = input("Ievadi y5 ===> ")
    
        else:
    
            if ((line_and_check(x1,y1,x3,y3,x2,y2,x4,y4)) and line_and_check(x1,y1,x3,y3,x2,y2,x5,y5) and
                 line_and_check(x1,y1,x4,y4,x2,y2,x5,y5) and line_and_check(x1,y1,x4,y4,x3,y3,x5,y5) and
                 line_and_check(x2,y2,x4,y4,x3,y3,x1,y1) and line_and_check(x2,y2,x4,y4,x3,y3,x5,y5) and
                 line_and_check(x2,y2,x5,y5,x1,y1,x3,y3) and line_and_check(x2,y2,x5,y5,x1,y1,x4,y4) and
                 line_and_check(x3,y3,x5,y5,x4,y4,x2,y2) and line_and_check(x3,y3,x5,y5,x4,y4,x1,y1) and 
                 line_and_check(x3,y3,x1,y1,x2,y2,x5,y5) and line_and_check(x3,y3,x1,y1,x2,y2,x4,y4) and
                 line_and_check(x4,y4,x2,y2,x1,y1,x3,y3) and line_and_check(x4,y4,x2,y2,x5,y5,x3,y3) and
                 line_and_check(x5,y5,x2,y2,x1,y1,x3,y3) and line_and_check(x5,y5,x2,y2,x1,y1,x4,y4)):
                
                print("\nPiecstūris ir izliekts")
                S1 = 0.5*((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
                S2 = 0.5*((x3-x1)*(y5-y1)-(x5-x1)*(y3-y1))
                S3 = 0.5*((x3-x5)*(y4-y5)-(x4-x5)*(y3-y5))
                S = S1 + S2 + S3
                print("S = " + str(abs(S)))
                quit()
    
            else:
                print("\nPiecstūris ir ieliekts. Programma nevar aprēķināt ieliekta piecstūra laukumu.")
                quit()
                
    print("\nJūs 3 reizes kļūdījāties. Beidzam sadarbību!")

def piecu_skaitlu_LKD_un_MKD():
    import math
    
    # Divu skaitļu gcd atrāšana
    def my_gcd(a,b):
        
        while b != 0 :
            c = a % b
            a = b
            b = c
    
        return a
    
    # Divu skaitļu lcm atrāšana
    # lcm (a, b) = a*b/(gcd (a,b))
    def my_lcm(a,b):
    
        return a*b/my_gcd(a,b)
    
    print("Programma atrod 5 naturālo skaitļu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo.\nIevadiet naturālus skaitļus!\n")
    x = input("Ievadi 1.skaitli ===> ") # skaitlis a
    y = input("Ievadi 2.skaitli ===> ") # skaitlis b
    z = input("Ievadi 3.skaitli ===> ")
    w = input("Ievadi 4.skaitli ===> ")
    q = input("Ievadi 5.skaitli ===> ")
    
    #skaitļu parbaude vai viņi ir veseli pozitivie skaitļi (dalam ar 0 un sqrt()) tests.
    M=0
    while M<=3:
        
        if M==1 or M==2:
            #print("Viens no ievadītajiem skaitliem nav naturāls skaitlis!")
            x = input("Ievadi 1.skaitli ===> ") # skaitlis a
            y = input("Ievadi 2.skaitli ===> ") # skaitlis b
            z = input("Ievadi 3.skaitli ===> ")
            w = input("Ievadi 4.skaitli ===> ")
            q = input("Ievadi 5.skaitli ===> ")
        elif M==3:
            print("Jūs 3 reizes kļūdījāties. Beidzam sadarbību!")
            quit()    
            
        try:
            x = int(x)
            a = 1/x
            b=math.sqrt(x)
    
            y = int(y)
            c = 1/y
            d = math.sqrt(y)
    
            z = int(z)
            e = 1/z
            f = math.sqrt(z)
    
            w = int(w)
            g = 1/w
            h = math.sqrt(w)
    
            q = int(q)
            k = 1/q
            v = math.sqrt(q)
    
        except:
            M=M+1
            print("\nViens no ievadītajiem skaitļiem nav naturāls skaitlis!\n")
            
    
        else:
            #noteiksim gcd no 5 skaitliem
            t=my_gcd(x,y)
            u=my_gcd(t,z)
            l=my_gcd(u,w)
            v=my_gcd(l,q)
            #print(v)
            #print("gcd(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))
            print("LKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))
    
            #noteiksim lcm no 5 skaitliem
            a=my_lcm(x,y)
            s=my_lcm(a,z)
            d=my_lcm(s,w)
            g=my_lcm(d,q)
            #print(g)
            # print("lcm(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
            print("MKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
            break

def cik_dienu_lidz_ziemassvetkiem():
    # Programmas nosaukums: 2. uzd MPR15
    # 2. uzdevums MPR15
    # Uzdevuma formulējums: Sastādīt programmu, kas pēc ievadīta datuma nosaka, cik dienu ir palicis līdz Ziemassvētku vakaram (24. decembrim). Datuma ievades pieļaujamais formāts ir DD.MM.GGGG. un tas tiek ievadīts kā simbolu virkne. Datuma apstrādes iebūvētās funkcijas izmantot nedrīkst.
    # Versija 1.0
    
    
    def date_check(DD_MM_GGGG_):
    
        DD_ = DD_MM_GGGG_[0:3]
        
        MM_ = DD_MM_GGGG_[3:6]
        
        GGGG_ = DD_MM_GGGG_[6:11]
        
        DD = DD_MM_GGGG_[0:2]
        
        MM = DD_MM_GGGG_[3:5]
        
        GGGG = DD_MM_GGGG_[6:10]
        
        # --------------- simbolu virknes garums ir precīzi 11 simboli. DD.MM.GGGG.
        if len(DD_MM_GGGG_) != 11:
            return False  
        
        if DD_[2:3] != "." or MM_[2:3] != "." or GGGG_[4:5] != ".":
            return False
        
        if DD_MM_GGGG_.count('.') !=3:
            return False
        
        try:
            
            DD = int(DD)
            b = 1/DD # 00.MM.GGGG.
            
            MM = int(MM)
            c = 1/MM # DD.00.GGGG.
            
            GGGG = int(GGGG)
            d = 1/GGGG # DD.MM.0000.
            
        except:
            return False
            #print("Tāds datums neeksistē")
            #quit()
            
        else:
            pass
            
        DD = int(DD) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 31 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē 
        if  DD > 31 or DD <= 0 :
            return False
            #print("Tāds datums neeksistē")
            #quit()
            
        MM = int(MM) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 12 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē 
        
        if  MM > 12 or MM <= 0:
            return False
            #print("Tāds datums neeksistē")
            #quit()
            
        GGGG = int(GGGG)  # Parveidojam int, lai uzzinātu vai tas ir mazāks vai vienāds ar 0, tad tāds datums neeksistē 
        
        if  GGGG <= 0:
            return False
            #print("Tāds datums neeksistē")
            #quit()
        
        if  MM == 4 and DD > 30: # Aprilī maksimāli ir tikai 30 dienas.
            return False
            #print("Tāds datums neeksistē")
            #quit()
        
        if  MM == 6 and DD > 30: # Jūnija maksimāli ir tikai 30 dienas.
            return False
            #print("Tāds datums neeksistē")
            #quit()
        
        if  MM == 9 and DD > 30: # Septembrī maksimāli ir tikai 30 dienas.
            return False
            #print("Tāds datums neeksistē")
            #quit()
        
        if  MM == 11 and DD > 30: # Novembrī maksimāli ir tikai 30 dienas.
            return False
            #print("Tāds datums neeksistē")
            #quit()
        
    
        
        F = 28 #default # Dienu skaits Februāri
        
        if (GGGG % 400) == 0: # Ja garais gad tad februarī dienu skaits ir 29
            F = 29
            
        elif (GGGG % 100) == 0: # Ja isais gads tad februarī dienu skaits ir 28
            F = 28
        
        elif (GGGG % 4) == 0: # Ja garais gad tad februarī dienu skaits ir 29
            F = 29
        
        else:
            F = 28 # Ja isais gads tad februarī dienu skaits ir 28
        
        if MM == 2 and DD > F: # Lai noteiktu vai ir pareizi ievadīti dati
            return False
    
    def leap_year(GGGG): # Noteicam vai gads (int) ir garais gads vai nav)
        # F = 28 # default
        GGGG = int(GGGG)
        if (GGGG % 400) == 0:
            return True # F = 29
            
        elif (GGGG % 100) == 0:
            return False # F = 28
        
        elif (GGGG % 4) == 0:
            return True # F = 29
        
        else:
            return False # F = 28 
    
    
    def day_count(Year, MM, DD): # Skaitam cik ir pagajušas dienas no 1. gada līdz ievadītam datumam
        F = 28
        days = 0
        days_year = 0
        
        days_year = (Year-1)*365 + (Year-1)//4 - (Year-1)//100 + (Year-1)//400 # pagajušo dienu skaits
        
        if leap_year(GGGG) == False:
            F = 28
        else:
            F = 29
            
        if MM == "01" :
            days = days_year + DD # only january
            return days
        if MM == "02" : # MM == 2
            
            days = days_year + DD + 31 # + all of january
            return days
        if MM == "03" : # MM == 3
                
            days = days_year + DD + 31 + F  # + all of january and february      
            return days
        if MM == "04" :
                    
            days = days_year + DD + 31 + F + 31
            return days
        if MM == "05" :
                        
            days = days_year + DD + 31 + F + 31 + 30
            return days
        if MM == "06" :
                            
            days = days_year + DD + 31 + F + 31 + 30 + 31  
            return days
        if MM == "07" :
                                
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30
            return days
        if MM == "08" :
                                    
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31
            return days
        if MM == "09" :
                                        
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31
            return days
        if MM == "10" :
                                            
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30
            return days
        if MM == "11" :
                                                
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            return days
        if MM == "12" :
                                                    
            days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
            return days 
        #return days
    
    
    
    
    
    # -------------------------------------------------- galvenā programma 
    DD_MM_GGGG_ = input("Ievadiet DD.MM.GGGG. ==> ")
    
    if date_check(DD_MM_GGGG_) == False: # Ja kaut vienu pārbaudi neizturēja, tad tāds datums neeksistē
        print("Tāds datums neeksistē")
        quit()
        
    DD = DD_MM_GGGG_[0:2]    
    MM = DD_MM_GGGG_[3:5]
    GGGG = DD_MM_GGGG_[6:10]
    
    if int(DD) == 24 and MM == "12": # Ja ievada 24.decembrī uzreiz
        print("Šajā dienā ir Ziemassvētku vakars! (24.decembrīs)") 
        
    elif (day_count(int(GGGG), str(MM), int(DD))) < (day_count(int(GGGG), str("12"), int(24))):
        
        remaining_days_until_christmas = (day_count(int(GGGG), str("12"), int(24))) - (day_count(int(GGGG), str(MM), int(DD))) # Ja pirms Ziemāssvetkiem, tad atņemsim cik
        # print(remaining_days_until_christmas)                                                                                # ir pagājis no 1.gada 1.janvāri līdz šai ievadītam datumam un līdz šīs gāda Ziemāssvētkiem. Tad iegūsim nepieciešamo dienu skaitu
        print("Līdz Ziemassvētkiem ir palikušas " + str(remaining_days_until_christmas) + " dienas.")
    
    else: # Ja (day_count(int(GGGG), str(MM), int(DD))) > (day_count(int(GGGG), str("12"), int(24))):
        remaining_days_until_christmas = (day_count(int(GGGG)+1, str("12"), int(24))) - (day_count(int(GGGG), str(MM), int(DD))) # Ja pirms Ziemāssvetkiem, tad atņemsim cik ir pagājis no 1.gada 1.janvāri līdz šai ievadītam datumam un līdz šīs gāda+1 (līdz nākama gāda) Ziemāssvētkiem. 
        print("Līdz Ziemassvētkiem ir palikušas " + str(remaining_days_until_christmas) + " dienas.")                            # Tad iegūsim nepieciešamo dienu skaitu    

def e_pasta_parbaudisana():
    def is_valid_email(email):
        # pārbauda, vai e-pasts ir īsāks par 256 rakstzīmēm
        if len(email) > 256:
            return False
        
        symbol_at_count = 0 # @ simbolu skaits, (sākuma ir 0) ja != 1 tad False
        dot_count = 0       # punktu . skaits. (Sākuma ir 0)
        
        if email[0] == "_": # Jo ir jāsakas ar burtu vai ciparu (pārbaude uz visiem legāliem burtiem ir tālak)
            return False
        
        for i in range(0,len(email)):
            if email[i] == "@"  :
                symbol_at_count += 1
                # pārbauda, vai ir vismaz 1 rakstzīme pirms simbola @
                if i == 0:
                    return False
                # pārbauda, vai ir vismaz 1 rakstzīme pēc simbola @
                if i == len(email) - 1:
                    return False
                if email[i+1] == ".": # pārbauda, pēc @ nav ., ja ir tad False
                    return False                   
                
            elif email[i] == ".":
                dot_count += 1
                # pārbauda, vai ir vismaz 1 rakstzīme pirms punkta
                if i == 0:
                    return False
                # pārbauda, vai ir vismaz 1 rakstzīme pēc punkta
                if i == len(email) - 1:
                    return False
                
                if email[i+1] == ".": # pārbauda, pēc punkta nav otrā punkta, ja ir tad False
                    return False
                
                if email[i+1] == "@": # pārbauda, pēc punkta nav @, ja ir tad False
                    return False
                
            elif not ( email[i] == "q" or email[i] == "w" or email[i] == "e" or email[i] == "r" or
                       email[i] == "t" or email[i] == "y" or email[i] == "u" or email[i] == "i" or
                       email[i] == "o" or email[i] == "p" or email[i] == "a" or email[i] == "s" or
                       email[i] == "d" or email[i] == "f" or email[i] == "g" or email[i] == "h" or
                       email[i] == "j" or email[i] == "k" or email[i] == "l" or email[i] == "z" or
                       email[i] == "x" or email[i] == "c" or email[i] == "v" or email[i] == "b" or
                       email[i] == "n" or email[i] == "m" or
                      
                       email[i] == "Q" or email[i] == "W" or email[i] == "E" or email[i] == "R" or
                       email[i] == "T" or email[i] == "Y" or email[i] == "U" or email[i] == "I" or
                       email[i] == "O" or email[i] == "P" or email[i] == "A" or email[i] == "S" or
                       email[i] == "D" or email[i] == "F" or email[i] == "G" or email[i] == "H" or
                       email[i] == "J" or email[i] == "K" or email[i] == "L" or email[i] == "Z" or
                       email[i] == "X" or email[i] == "C" or email[i] == "V" or email[i] == "B" or
                       email[i] == "N" or email[i] == "M" or
                       
                       email[i] == "1" or email[i] == "2" or email[i] == "3" or email[i] == "4" or
                       email[i] == "5" or email[i] == "6" or email[i] == "7" or email[i] == "8" or
                       email[i] == "9" or email[i] == "0" or
                       
                       email[i] == "_" or email[i] == "."):
                
                # atsevišķie vārdi var saturēt tikai latīņu burtus, ciparus un pasvītrojuma rakstzīmi _
                
                return False
    
                
        if symbol_at_count != 1: # Jābut tieši vienam @ simbolam
            return False
        if dot_count == 0: # jābut vismaz vienam punktam. @inbox.lv @lu.lv
            return False
      
        return True
    
    # ----------------- galvenā programma
    
    email = input("Ievadiet derīgo e-pastu => ")
    
    is_valid_email(email)
    while True:
        if is_valid_email(email) == False:
            email = input("\nTas nav korekts e-pasts!\nIevadiet derīgo e-pastu => ")
            is_valid_email(email)
        else:
            print("Tas ir korekts e-pasts!")
            break    

def punkta_XX_YY_koordinatas_skat_pdf():
    import math
    
    def is_real_number(x):
        while True:
            try:
                x = float(x)
            except:
                x = input("Mēģini vēlreiz ===> ")
            else:
                return float(x)
            
    def is_real_positive_number(x):
        while True:
            try:
                x = float(x)
            except:
                x = input("Mēģini vēlreiz ===> ")
            else:
                if x <= 0:
                    x = input("Mēģini vēlreiz ===> ")
                else:
                    return float(x)
                
    def lidzibas_koeficients(x,y,r):
        hipotenuzes_garums = math.sqrt(x*x + y*y) 
        k = r/hipotenuzes_garums # k - līdzības koeficients, r - rādiuss
        return k
    
    def koordinatas_aprekinasana(a,k): # koordinātas aprēķināšana pēc līdzības koeficienta un vienas malas
        return a*k
    
    # ----------------------------------------------
    
    print("Programma nosaka punkta (XX, YY) koordinātas, ja zināms punkta (X, Y) koordinātas un rādiuss R, ko lietotājs ievada no tastatūras.\n")
    
    x = input("Ievadiet X koordinātu ===> ")
    x = is_real_number(x)
    
    y = input("Ievadiet Y koordinātu ===> ")
    y = is_real_number(y)
    
    if x == 0 and y == 0:
        print("Nav iespējami noteikt")
        quit()
    
    r = input("Ievadiet rādiusu R ===> ")
    r = is_real_positive_number(r)
    
    k = lidzibas_koeficients(x,y,r)
    
    x_koordinatas = koordinatas_aprekinasana(x,k)
    y_koordinatas = koordinatas_aprekinasana(y,k)
    
    print("\n(XX, YY) = (" + str(x_koordinatas) + ", " + str(y_koordinatas) + ")")    