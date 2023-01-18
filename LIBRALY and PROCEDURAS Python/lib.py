#my libraly

import math
import random

# ---------------------------------------------------------
"""
for a in range(0, 31) :
    for b in range(0, 12) :
        for c in range(0, 9999) :
            a = str(a)
            b = str(b)
            c = str(c)
            d = a + b + c
            d = int(d)
            if vai_palindroms(d):
                print(d)
"""
def calc_e(x,n):
    #n = int(input("Noradiet precizitāti ==> "))
    #x = float(input("Noradiet x pakāpi ==> "))
    
    s = 0
    for i in range(1, n, 1) :
        
        s += (x**i)/(math.factorial(i))
    
    s = s+1
    return s
    #print(s)    

def calc_pi(num_digits):
    # Calculate the value of pi to the specified number of digits
    return round(math.pi, num_digits)

def calc_e_2_var(x,n):
    s = 0
    for i in range(1,n,1):
        
        s += (x**i)/(math.factorial(i))
    
    return s+1

def calc_sin(x,n):
    #n = int(input("Noradiet precizitāti ==> "))
    #x = float(input("Noradiet x ==> "))
    
    s = 0
    for i in range(1,n,1):
        
        s += ((-1)**(i-1))*((x**(2*i-1))/(math.factorial(2*i-1)))
    
    return s
    #print(s)    

def calc_cos(x,n):
    #n = int(input("Noradiet precizitāti ==> "))
    #x = float(input("Noradiet x ==> "))
    
    s = 0
    for i in range(1,n,1):
        
        s += (((-1)**(i+1))*(x**(2*i)))/(math.factorial(2*i))
    
    return 1-s

def calc_ln_1_plus_x(x,n):
    s = 0
    for i in range(1,n,1):
        
        s += (((-1)**(i+1))*(x**i))/i
    
    return s
   
def arctgx(x,n):
    s = 0
    if abs(x) <= 1:
        for i in range(1,n,1):
        
            s += (((-1)**(i-1))*((x)**(2*i-1)))/(2*i-1)
    
        return s
    else:
        return False

def shx(x,n):
    s = 0
    for i in range(1,n,1):
        
        s += ((x**(2*i-1))/(math.factorial((2*i-1))))
    
    return s    

def chx(x,n):
    s = 0
    for i in range(1,n,1):
        
        s += ((x**(2*i))/(math.factorial((2*i))))
    
    return s

# -----------------

def sorting_augosa():
    name = input('>>>')
    order = name.split(',')
    for i in range(len(order)):
        order[i] = int(order[i])
    order = sorted(order, reverse=False)
    print(order)
    
def sorting_dilstosa():
    name = input('>>>')
    order = name.split(',')
    for i in range(len(order)):
        order[i] = int(order[i])
    order = sorted(order, reverse=True)
    print(order)
    
def sorting_augosa_3():
    n = 0
    a = []
    c = ""
    while len(a) != 3:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    #print(a)
    print(' '.join(map(str, a)))

def sorting_augosa_4():
    n = 0
    a = []
    c = ""
    while len(a) != 4:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    #print(a)
    print(' '.join(map(str, a)))
    
def sorting_augosa_5():
    n = 0
    a = []
    c = ""
    while len(a) != 5:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    #print(a)
    print(' '.join(map(str, a)))

def sorting_dilstosa_3():
    n = 0
    a = []
    c = ""
    while len(a) != 3:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    a = a[::-1]
    #print(a)
    print(' '.join(map(str, a)))
    
def sorting_dilstosa_4():
    n = 0
    a = []
    c = ""
    while len(a) != 4:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    a = a[::-1]
    #print(a)
    print(' '.join(map(str, a)))

def sorting_dilstosa_5():
    n = 0
    a = []
    c = ""
    while len(a) != 5:
        n = n + 1
        c = input("Ievadi skaitli ==> ")
    
        a.append(c)
        

    a = sorted(a)
    a = a[::-1]
    #print(a)
    print(' '.join(map(str, a)))

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
    
# ---------------------------------------------------------
    
def cbrt(x):
    return x**(1/3)

# ---------------------------------------------------------

def if_number_3_attempts():
    # vai skaitlis?
    k = 0
    while k<3:
        x=input("Ievadi skaitli => ")
        try:
            x=float(x)
        except:
            k=k+1
            print("Nepareiza ievade")
        else:
            return x
    else:
        print("Jūs pārak daudz reizes kļūdījāties! Beidzam sadarbību!")
    

#x = if_number_3_attempts("x")
#y = if_number_3_attempts("y")
# katram tiek dots trīs pārbaudījumi
# ---------------------------------------------------------
def solve_quadratic(a,b,c): # ax^2 + bx + c = 0 (in real numbers)
    if a == 0 :
        print("Tas nav kvadratvienadojums")
    else :
        d = b * b - 4 * a * c # Diskriminants
        if d < 0 :
            return False

        else :
            x1 = (-b + math.sqrt(d)) / 2 / a
            x2 = (-b - math.sqrt(d)) / 2 / a
            return x1,x2
#print(lib.solve_quadratic(1,1,2))   

# ---------------------------------------------------------

def solve_quadratic_complex(a,b,c): # ax^2 + bx + c = 0 (in complex numbers)
    
    # Nav kvadrātvienādojums pēc definīcijas
    if a == 0 :
        return False # Tas nav kvadraatvienādojums

    
    else : # Citādi risinām kvadrātvienādojumu
        
        d = b*b - 4*a*c # Diskriminants
    
        if d < 0 : # Tad ir komplēksa skaitļi
            
            #print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
            #print("\nKvadrātvienādojumam realu saknu nav\nIr divas kompleksas saknes\n")
            
            Re = -b
            Im = abs(math.sqrt(-d) / (2 * a))
            return (f"{Re} + i*{Im} \n{Re} - i*{Im}")        
    
        else : # Divas atšķirīgas saknes
            
            x1 = (-b + math.sqrt(d)) / 2 /a
            x2 = (-b - math.sqrt(d)) / 2 / a
            
            #print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
            #print("\nKvadrātvienādojumam ir divas atšķirīgas vai vienādas saknes")
            return x1,x2
            
#print(lib.solve_quadratic_complex(1,1,2))     
# ---------------------------------------------------------

def solve_bikvadrat_vienadojums(a,b,c): # ax^4 + bx^2 + c = 0
    if a == 0 : # Pēc def. tas nav bikvadrātvienādojums ja a == 0
        
        return False
        #print("\nTas nav bikvadrātvienādojums")
    
    else :
        
        d = b*b - 4*a*c # Diskriminants
    
        if d < 0 : # Risinām ax^4 + bx^2+c=0. x^2 = t , at^2 + bt + c = 0, atrādam t1,t2 un tad atradam x1,x2 x = +-sqrt(t)
            
            return False
            #print("\nBikvadrātvienādojumam nav reālas saknes")

        else :
            
            t1 = (-b + math.sqrt(d)) / 2 / a
            t2 = (-b - math.sqrt(d)) / 2 / a
            
            if t1 >= 0 :
                if t2 >=0:
                    x1=math.sqrt(t1)
                    x2=-1*(math.sqrt(t1))
                    x3=math.sqrt(t2)
                    x4=-1*(math.sqrt(t2))
                    #print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
        
                    return x1, x2, x3, x4               
                
                else:
                    
                    x1= math.sqrt(t1)
                    x2 = -1*(math.sqrt(t1))
                    #print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")
                    
                    return x1,x2
                
            elif t2>=0:
                x1 = math.sqrt(t2)
                x2 = -1*(math.sqrt(t2))
                print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")

                return x1,x2
                
            else:
                return False

# ---------------------------------------------------------

def triangle_area_in_coordinates(x1,y1, x2,y2, x3,y3):
    Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    if Area == 0:
        return False
    else:
        return Area
#print(lib.triangle_area_in_coordinates(1,1, 2,3, 4,6))

# ---------------------------------------------------------

def vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2):
    SD = A1*B2 - A2*B1
    
    if SD == 0:
        return False
    else:
        return True
    
#print(lib.vai_taisnem_ir_kopigs_punkts(1, 1, 2, 2))
# ---------------------------------------------------------

def two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dx = -C1*B2 + B1*C2
    x = Dx/D
    return x

#print(lib.two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2)) # x koordinata
# ---------------------------------------------------------

def two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dy = -C2*A1 + A2*C1
    y = Dy/D
    return y

#print(lib.two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2)) # y koordinata
# ---------------------------------------------------------

def triangle_perimeter(x1,y1, x2,y2, x3,y3):
    a = math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))
    b = math.sqrt((x2-x3) * (x2-x3) + (y2-y3) * (y2-y3))
    c = math.sqrt((x3-x1) * (x3-x1) + (y3-y1) * (y3-y1))
    p = a + b + c
    return p

#print(lib.triangle_perimeter(1,1, 2,3, 4,6))
# ---------------------------------------------------------   

"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
"""

def is_prime(n):
    try:
        n = int(n)
    except:
        return False
    else:
        if n <= 1:
            return False
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True

#print(lib.is_prime(11))

# ---------------------------------------------------------

""" не работает для отрицательных
def check_str_whole_number(x):
    if (x[0]=="-") or (x[0]=="+") :
        y=x[1:]
    else:
        y=x
        if y.isdigit() :
            return True
        else:
            return False
#print(lib.check_str_whole_number("11"))
"""

# ---------------------------------------------------------

def check_str_natural(x):
    x=x.strip()
    if x.isdigit() :
        if int(x)>0 :
            return True
        else:
            return False
    else:
        return False
    
#print(lib.check_str_natural(x))
#sv means simbolu virkne (string)

# ---------------------------------------------------------

# здесь всякие -.2 и .6 это числа, число с запятой не число
def check_str_real_number(x):
    x=x.strip()
    if (x[0]=="-") or (x[0]=="+") :
        y=x[1:]
    else:
        y=x
    z=y.find(".")
    if z == -1 :
        vd=y # veselā daļa
        dd="0" # daļveida daļa
    elif z == 0 :
        vd="0"
        dd=y[1:]
    elif z == len(y)-1 :
        vd=y[0:len(y)-1:]
        dd="0"
    else:
        vd=y[0:z:]
        dd=y[z+1:]
    if vd.isdigit() and dd.isdigit() :
        return True
    else:
        return False
    
# print(lib.check_str_real_number(x))  

# ---------------------------------------------------------

def is_zero(n):
    try:
        n = 1/n
    except:
        return True
    else:
        return False
    
#print(lib.is_zero(0))

# ---------------------------------------------------------

def is_real_positive(n):
    try:
        n = float(n)
        b = math.sqrt(n)
        c = 1/n
    except:
        return False
    else:
        return True
    
#print(lib.is_zero(0))

# ---------------------------------------------------------

# можно вводить как str "" так и числа
def is_real(n):
    try:
        n = float(n)
    except:
        return False
    else:
        return True
    
#print(lib.is_real("ad"))
# ---------------------------------------------------------

def is_real_number_velreiz(): # By Kristaps. Bezgalīgi daudz reizes ievāda
    x = input("Ievadi reālo skaitli ===> ")
    while True:
        try:
            x = float(x)
        except:
            x = input("Mēģini vēlreiz ===> ")
        else:
            return float(x)
        
#print(lib.is_real_number("10"))
# ---------------------------------------------------------

def is_real_positive_number(): # By Kristaps. Bezgalīgi daudz reizes ievāda
    x = input("Ievadi reālo pozitīvo skaitli ===> ")
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
            
#print(lib.is_real_positive_number("asd"))

# ---------------------------------------------------------

def is_real_not_negative(n):
    try:
        n = float(n)
        b = math.sqrt(n)
    except:
        return False
    else:
        return True
    
#print(lib.is_real("ad"))

# ---------------------------------------------------------

def my_gcd(x,y):
    a = x
    b = y
    while b != 0 :
        c = a % b
        a = b
        b = c
    return a

# Lielākais kopīgais dalītājs
# LKD

# ---------------------------------------------------------

def my_lcm(x,y):
    return abs(x*y)/my_gcd(x,y)

def my_gcd_3(a,b,c):
    def my_gcd(x,y):
        a = x
        b = y
        while b != 0 :
            c = a % b
            a = b
            b = c
        return a
    return my_gcd(a,my_gcd(b,c))

def my_lcm_3(a,b,c):
    return my_lcm(a,my_lcm(b,c))

# Mazākais kopīgais dalāmais
# MKD
# print(lib.my_lcm(10,120))  

# ---------------------------------------------------------

def combinations(m,n): # n is bottom n>=k Pick two from four
    if m > n:
        return False
 
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
    
    return c
#print(lib.combinations(2,5)) # pick two from 5

# ---------------------------------------------------------

def prime_factor(n): #pirmreizinātaji
    a = n
    j = 2
    sv = str(n) + "="
    while a > 1 :
        k = 0
        while (a % j) == 0 :
            a = a // j
            k = k + 1
        if k > 0 :
            sv = sv + str(j) + "^" + str(k) + "*"
        j = j + 1
        
    sv = sv + "1"
    
    return sv
#print(lib.prime_factor(10))
# ---------------------------------------------------------

def sakartot_4(a,b,c,d):
    if a > b :
        x = a
        a = b
        b = x
    if c > d :
        x = c
        c = d
        d = x
    if a > c :
        x = c
        c = a
        a = x
    if b > d :
        x = b
        b = d
        d = x
    if b > c :
        x = b
        b = c
        c = x
    
    return str(a), str(b), str(c), str(d)

#print(lib.sakartot_4(4,-2,1,10))
# ---------------------------------------------------------

def sakartot_3(a,b,c):
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
    
    return str(a), str(b), str(c)

# ---------------------------------------------------------

def can_make_triangle(a,b,c): # malu garumi a b c nevis koordinatas
    if (a + b > c) and (b + c > a) and (a + c > b) :
        return True
    else:
        return False

#print(lib.can_make_triangle(3,4,5))
# ---------------------------------------------------------

def are_two_points_on_the_one_side(a,b,c, x1,y1, x2,y2): #pēc ax+by+c=0 taisne x1,y1 - 1.punkts. x2,y2 - 2.punkts
    
    z1=a*x1+b*y1+c
    z2=a*x2+b*y2+c
    
    if z1*z2>0 :
        return True # ir vienā puse
    else :
        return False # dažādas puses no taisnem

#print(lib.are_two_points_on_the_one_side(1,1,1,  3,4, 5,6))
# ---------------------------------------------------------

def roll_dice():
    a = random.randint(1,6)
    return a

#print(lib.roll_dice())
# ---------------------------------------------------------

def horoskopi_pec_gadiem(g):
    g = g % 12
    match g :
        case 11 :
            a = "Kaza"
        case 10 :
            a = "Zirgs"
        case 9 :
            a = "Čūska"
        case 8 :
            a = "Pūķis"
        case 7 :
            a = "Kaķis"
        case 6 :
            a = "Tīģeris"
        case 5 :
            a = "Vērsis"
        case 4 :
            a = "Žurka"
        case 3 :
            a = "Cūka"
        case 2 :
            a = "Suns"
        case 1 :
            a = "Gailis"
        case 0 :
            a = "Mērkaķis"
    return a

#print(lib.horoskopi_pec_gadiem(3)) # kaza
# ---------------------------------------------------------

def horoskopi_pec_menesiem(menesis, datums):
    m = menesis
    d = datums
    match m :
        case 1 :
            if d<20 :
                a = "Mežāzis"
            else :
                a = "Ūdensvīrs"
        case 2 :
            if d<19 :
                a = "Ūdensvīrs"
            else :
                a = "Zivis"
        case 3 :
            if d<21 :
                a = "Zivis"
            else :
                a = "Auns"
        case 4 :
            if d<20 :
                a = "Auns"
            else :
                a = "Vērsis"
        case 5 :
            if d<21 :
                a = "Vērsis"
            else :
                a = "Dvīņi"
        case 6 :
            if d<22 :
                a = "Dvīņi"
            else :
                a = "Vēzis"
        case 7 :
            if d<23 :
                a = "Vēzis"
            else :
                a = "Lauva"
        case 8 :
            if d<23 :
                a = "Vēzis"
            else :
                a = "Jaunava"
        case 9 :
            if d<23 :
                a = "Jaunava"
            else :
                a = "Svari"
        case 10 :
            if d<23 :
                a = "Svari"
            else :
                a = "Skorpions"
        case 11 :
            if d<23 :
                a = "Skorpions"
            else :
                a = "Strēlnieks"
        case 12 :
            if d<22 :
                a = "Strēlnieks"
            else :
                a = "Mežāzis"
        
    return a

#print(lib.horoskopi_pec_menesiem(2, 5)) # kaza
# ---------------------------------------------------------

def cubic_equation_in_whole_numbers(a,b,c,d): #ax^3 + bx^2 + cx + d = 0

    s = ""
    w = abs(d)
    n = round(math.sqrt(w)) + 1
    for i in range (1, n) :
        if (w % i) == 0 :
            x = i * i * i
            y = i * i
            z = w // i
            u = z * z * z
            v = z * z
            if a * x + b * y + c * i + d == 0 :
                s = s + str(i) + " "
            if -a * x + b * y - c * i + d == 0 :
                s = s + str(-i) + " "
            if a * u + b * v + c * z + d == 0 :
                s = s + str(z) + " "
            if -a * u + b * v - c * z + d == 0 :
                s = s + str(-z) + " "
            if s == "" :
                return "Veselu sakņu nav"
            else :
                return s

#print(lib.cubic_equation_in_whole_numbers(a,b,c,d))
# ---------------------------------------------------------

def number_of_point_in_circle(r):
    r1 = math.floor(r)
    sk = 1
    for i in range(0, r1+1) :
        sk = sk + 4 * math.floor(math.sqrt(r*r-i*i))
        
    return sk

#print(lib.number_of_point_in_circle(5))
# ---------------------------------------------------------

# какое число находится на n позиции
def what_is_on_n_position(n, virkne):
    virkne=str(virkne)
    k = 0
    skaitlis = 0
    while k<n :
        skaitlis = skaitlis + 1
        garums = len(virkne)
        k = k + garums
    cipars = virkne[garums - k + n - 1]
    return cipars

#print(lib.what_is_on_n_position(1, 1000000)) => 1
#print(lib.what_is_on_n_position(2, 1000000)) => 0
#print(lib.what_is_on_n_position(5, 1000000)) => 0

# ---------------------------------------------------------

def fibonacci_number_on_place(n): 
    return round(1.618033988749895**n / 5**0.5)

#print(lib.fibonacci_number_on_place(1)) => 1
#print(lib.fibonacci_number_on_place(2)) => 1
#print(lib.fibonacci_number_on_place(3)) => 2
#print(lib.fibonacci_number_on_place(4)) => 3
#print(lib.fibonacci_number_on_place(5)) => 5
#print(lib.fibonacci_number_on_place(6)) => 8
# ---------------------------------------------------------
def cetrsturis_laukums(x1,y1, x2,y2, x3,y3, x4,y4): # koordinātas
    
    def puses(x1, y1, x2, y2, x3, y3, x4, y4):
        z1=(x1 - x4) * (y3 - y4) - (y1 - y4) * (x3 - x4)
        z2=(x2 - x4) * (y3 - y4) - (y2 - y4) * (x3 - x4)
        return z1 * z2 > 0
    
    def mala(xs, ys, xb, yb):
        return math.sqrt((xs-xb)*(xs-xb)+(ys-yb)*(ys-yb))
    
    def laukums(x1, y1, x2, y2, x3, y3):
        a = mala(x1, y1, x2, y2)
        b = mala(x2, y2, x3, y3)
        c = mala(x1, y1, x3, y3)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    if (puses(x1, y1, x2, y2, x3, y3, x4, y4) and
        puses(x4, y4, x1, y1, x2, y2, x3, y3) and
        puses(x3, y3, x4, y4, x1, y1, x2, y2) and
        puses(x2, y2, x3, y3, x4, y4, x1, y1)) :
        s = laukums(x1, y1, x2, y2, x3, y3) + laukums(x1, y1, x4, y4, x3, y3)
        return s
    else :
        return False # ieliekts
    
# ---------------------------------------------------------    

def vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2):
    SD = A1*B2 - A2*B1
    if SD == 0:
        return False
    else:
        return True
    
# ---------------------------------------------------------   

def two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dx = -C1*B2 + B1*C2
    x = Dx/D
    return x

# ---------------------------------------------------------

def two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2): # (x;y)
    D = A1*B2 - A2*B1
    Dy = -C2*A1 + A2*C1
    y = Dy/D
    return y

# ---------------------------------------------------------

# правильно ли дата указана? (допустимый формат DD.MM.GGGG.)
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
    
    return True

#  print(lib.date_check("12.13.2002."))
# ---------------------------------------------------------

def day_count(DD_MM_GGGG_): # Skaitam cik ir pagajušas dienas no 1. gada līdz ievadītam datumam
    
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
        
    DD_ = DD_MM_GGGG_[0:3]
    
    MM_ = DD_MM_GGGG_[3:6]
    
    GGGG_ = DD_MM_GGGG_[6:11]
    
    DD = DD_MM_GGGG_[0:2]
    
    MM = DD_MM_GGGG_[3:5]
    
    GGGG = DD_MM_GGGG_[6:10]    
    
    F = 28
    days = 0
    days_year = 0
    Year = int(GGGG)
    days_year = (Year-1)*365 + (Year-1)//4 - (Year-1)//100 + (Year-1)//400 # pagajušo dienu skaits
    days_year = int(days_year)
    DD = int(DD)
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

"""

date = input("date ==> ")

if lib.date_check(date) == True:
    print(lib.day_count(date))
else:
    print("Nav pareizs")
    
"""

# ---------------------------------------------------------

def reverse_string(txt):
    return txt[::-1]
# import lib
# print(lib.reverse_string("Labi")) "ibaL"

def reverse_string_2(s):
    str = ""
    for i in s:
        str = i + str
    return str

# import lib
# print(lib.reverse_string2("Labi")) "ibaL"

# ---------------------------------------------------------

def reverse_string_3(v):
    
    v2=""
    
    for i in v:
    
        v2=i+v2
        
    return v2

# ---------------------------------------------------------

def faktorials(n): # N = N*(N-1)*...4*3*2*1
    
    if str(n).isdigit() and float(n) == int(n):
        faktorials = 1
        for i in range(1, n+1):
            faktorials = faktorials * i
        
        return faktorials         
    else:
        return False

# ---------------------------------------------------------

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
# --------------------------------------------------------- 

def faktorials2(n): # ar rekursiju rekursija N! = N*(N-1)!
    
    def recur_factorial(n):
        if n == 1:
            return n
        else:
            return n*recur_factorial(n-1)    
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        if n == 0:
            return 1
        else:
            return recur_factorial(n)
    else:
        return False    
    
# ---------------------------------------------------------
    
def circle_area(r):
    return math.pi*r*r

#----------------------------------------------------------  

def circle_circumference(r): # perimetrs
    return 2*math.pi*r

#----------------------------------------------------------  

def max_of_three_numbers(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
#----------------------------------------------------------  

def is_even(x): # чётное или нет
    if x % 2 == 0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def is_alphabet(ch): # является ли символ частью латинского алфавита?
    if (ch >= "a" and ch<="z") or (ch >= "A" and ch <= "Z"):
        return True
    else:
        return False
    
#----------------------------------------------------------    

def is_positive_or_zero(n):
    if n>=0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def is_positive(n):
    if n>0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def is_whole(n):
    try:
        n = int(n)
    except:
        return False
    else:
        return True
    
#----------------------------------------------------------    

def is_natural(n):
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def is_natural_or_zero(n):
    if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
        return True
    else:
        return False
    
#----------------------------------------------------------  

def multiplication_table(n1,n2):
    for i in range (1,21):
        print(format(n1, "<2"),"* ", format(i,"<2"), "=",n1*i, end="\t")
        print(format(n2, "<2"),"* ", format(i,"<2"), "=",n2*i)
        
#----------------------------------------------------------       

def trijstura_laukums(a,b,c):
    
    if a >= b+c:
        return False
    elif b >= a+c:
        return False
    elif c >= a+b:
        return False
    
    else:
        p=(a+b+c)/2 # Pusperimetra apreķināšana
    
        area=math.sqrt(p*(p-a)*(p-b)*(p-c)) # Laukuma apreķināšana izmantojot Herona formulu
        return area
    
#----------------------------------------------------------  

def divu_linear_vienadojumu_atrisinasana(a,b,c,d,e,f):
    
    D=a*e-b*d
    Dx=c*e-b*f
    Dy=a*f-c*d
    
    # Ja Sistēmas determinants ir 0 un (Dx != 0 vai Dy != 0 tad nav atrisinājumu)
    
    if D==0 and (Dx !=0 or Dy !=0) :
        return False
    
    # Ja visi determinanti (D == 0 un Dx == 0 un Dy == 0) tad ir bezgalīgi daudz atrisinājumu
    
    if D==0 and Dx == 0 and Dy==0 :
        return "Bezgalīgi daudz atrisinājumu"
    
    # Ja sistēmas determinants nav 0, tad ir viens vienīgs atrisinājums
        
    if D!=0:
    
        x=Dx/D
        y=Dy/D
        
        return x, y
    
#----------------------------------------------------------     

def divu_linear_vienadojumu_atrisinasana_ar_proporciju(a,b,c,d,e,f):
    
    # Determinantu apreķināšana (Lai paradītu atrisinājumu, ja tads ir)
    D=a*e-b*d
    Dx=c*e-b*f
    Dy=a*f-c*d
    
    # Gadījums, kad nav atrisinājums
    if a/d == b/e and b/e != c/f:
        return False
    
    # Gadījums, kad bezgalīgi daudz atrisinājumu  
    if a/d == b/e and b/e == c/f :
        return "Bezgalīgi daudz atrisinājumu"
    
    # Ir viens atrisinājums
    if a/d != b/e:
    
        x = Dx/D
        y = Dy/D
        
        return x, y
    
#----------------------------------------------------------

def vai_izliekts_cetrsturis(x1,y1, x2,y2, x3,y3, x4,y4):  # Ieliekts (вогнутый, нестандартный). Izliekts - выпуклый - хороший # pēc koordinātam
    
    #AC taisne
    z1 = (x4 - x1)*(y3 - y1) - (y4 - y1)*(x3 - x1)
    
    z2 = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
    
    #BD taisne
    z3 = (x1-x2)*(y4-y2)-(y1-y2)*(x4-x2)
    
    z4 = (x3-x2)*(y4-y2)-(y3-y2)*(x4-x2)
    
    if z1*z2 > 0 or z3*z4 > 0:
        return True 
        # print ("Izliekts") (хороший, можно посчитать площадь)
        
        
    else :
        return False
        # print ("Ieliekts") # вогнутый (плохой, нельзя посчитать площадь)  
        
#----------------------------------------------------------  

# pēc lietotāja ievadītajām trijstūra virsotņu A(x1, y1), B(x2, y2) un C(x3, y3), un punkta D(x4, y4) koordinātām, noskaidro un paziņo, vai punkts D atrodas trijstūra ABC iekšpusē.
def vai_punkts_trijstūri_iekspuse(x1,y1, x2,y2, x3,y3, x4,y4): # D - x4,y4 находится ли он внутри треугольника с такими координатами?
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
        return True
        #print("Punkts D atrodas trijstūra iekšpusē")
    
    else :
        return False
        #print("Punkts D neatrodas trijstūra iekšpusē")
        
# --------------------------------------------------------------------  

# pēc lietotāja ievadītajām trīs punktu A(x1, y1), B(x2, y2) un C(x3, y3) koordinātām, noskaidro un paziņo, vai šie trīs punkti atrodas uz vienas taisnes.
def vai_3_punkti_atrodas_uz_vienas_taisnes(x1,y1,  x2,y2,  x,y): # x,y tas ir x3,y3
    
    a=(x-x2)*(y1-y2)
    b=(y-y2)*(x1-x2)
    
    if a==b:
        return True
        # print("\nPunkti atrodas uz vienas taisnes")
        
    if a!=b:
        return False
        # print("\nPunkti nav uz vienas taisnes")
 
# ---------------------------------------------------------
     
# divu punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) ievada lietotājs kā arī A, B un C koeficientus.        
# Ax + By + C = 0   A(x1,y1) B(x2,y2)
def divu_punktu_novietojums_attieciba_pret_taisnei(a,b,c,  x1,y1,  x2,y2):
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
        
# ---------------------------------------------------------
        
# paziņo par trīs punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) C(x3, y3) ievada lietotājs kā arī A, B un C koeficientus.
# Ax + By + C = 0   A(x1,y1) B(x2,y2) C(x3,y3))
def tris_punktu_novietojums_attieciba_pret_taisnei(a,b,c,  x1,y1,  x2,y2,  x3,y3):
    
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
        
# ---------------------------------------------------------
    
# lietotāja ievadīto naturālo skaitli no 1 līdz 999 nodrukā uz ekrāna ar vārdiem.
def skaitlis_ar_vardiem(x): # x - int no 1 līdz 999
    try:
        x = int(x)
    except:
        return False
    else:
        if x < 1 or x > 999:
            return False
        
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
        
            return SimboluVirkne
        
# ---------------------------------------------------------

# Sastādīt programmu, kas noskaidro, vai lietotāja ievadītais skaitlis ir pirmskaitlis.
# "Ievadiet naturālo skaitļi, kurš ir lielāks par 1.\n==> "
def vai_pirmskaitlis(a):

    if a <= 0:
        return False
        
    if a==1:
        return False

    
    b=1
    c=a
    
    for a in range (1, a-1, 1):
        b = b+1
        if c%b == 0:

            return False

    
    return True

# ---------------------------------------------------------

def vai_palindroms(x):


    y = len(x) # Cik ir garums
    
    atb = "Ir palindroms"
     
    for i in range (y//2):
        if x[i] != x[y-1-i]:
            atb ="Nav palindroms"
            break

    if atb == "Ir palindroms":
        return True
    else:
        return False
    
# ---------------------------------------------------------
    
def simbolu_virknes_parvietosana_pa_vienu(x):
    n=len(x)
    for i in range (n):
        print(x[i:n]+x[0:i])
    
    return ""

# ---------------------------------------------------------

# lietotāja ievadīto vārdu izkārto ka parādīts piemērā. (квадратиком)
def simbolu_virkne_ka_kvadrats(x):

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
    
    return ""

# ---------------------------------------------------------

# mazāko Fibonači skaitli, kas pārsniedz lietotāja ievadīto skaitli N.
def mazakais_fibonaci_skaitlis_kas_parsniedz_ievadito_skaitli(n):
    
    b=1
    a=1
    c=0         # a,b=b,a+b (ja to izmantojam, tad nevajadzēs izmantot palīgmainīgo c)
    
    while n>=a: # kāmer n>=a, tad 
    
                    # a,b=b,a+b
                    # var arī to konstrukciju izmantot
        c = a + b
        a = b
        b = c
    
    return a
    #print("Mazakais Fibonači skaitlis, kas pārsniedz skaitli " + str(n) + " ir " + str(a))

# ---------------------------------------------------------

# atrod N ciparu pēc kārtas bez atstarpēm uzrakstītajā Fibonači skaitļu virknē. Skaitli N ievada lietotājs.    
def atrast_n_ciparu_pec_kartas_fibonaci_virkne(n):
    
    if n<=0:
        return False
    
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
    return (sv[n-1])    
    
# ---------------------------------------------------------

def vai_aritmetiska_progresija(): # функцию вызываем
    sv = "Dota virkne ir aritmētiska progresija"
    
    x1 = float(input("Ievadiet 1 locekli ===> "))
    
    if x1 == 0:
        print("Šajā virknē nav elementu.") # Ja uzreiz 0 ievada
        
    x2 = float(input("Ievadiet 2 locekli ===> "))
    
    if x2 == 0: # Ja tikai vienu elementu ievada
        print("Šajā virknē ir tikai viens elements.\nAritmētiskas progresijas tiek definētas skaitļu virknem ar vismaz diviem elementiem.")
        
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

# ----------------------------------------

def vai_aritmetiska_vai_geometriska():
    sv = "Dota virkne ir aritmētiskā progresija"
    sv1 = "Dota virkne ir geometriskā progresija"
    
    x1 = float(input("Ievadiet 1 locekli ===> "))
    
    if x1 == 0:
        print("Šajā virknē nav elementu.") # Ja uzreiz 0 ievada

        
    x2 = float(input("Ievadiet 2 locekli ===> "))
    
    if x2 == 0: # Ja tikai vienu elementu ievada
        print("Šajā virknē ir tikai viens elements.\nAritmētiskas un ģeometriskas progresijas tiek definētas skaitļu virknem ar vismaz diviem elementiem.")

        
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
        
# ---------------------------------------------------------

def katru_vardu_apgriez_otradi(x):
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
    
    return sv

# ---------------------------------------------------------

def piecu_skaitlu_LKD_un_MKD(x,y,z,w,q): # gcd,lcm / LKD,MKD / НОД,НОК
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
    
    #noteiksim gcd no 5 skaitliem
    t=my_gcd(x,y)
    u=my_gcd(t,z)
    l=my_gcd(u,w)
    v=my_gcd(l,q)
    #print(v)
    #print("gcd(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))
    #print("LKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))

    #noteiksim lcm no 5 skaitliem
    a=my_lcm(x,y)
    s=my_lcm(a,z)
    d=my_lcm(s,w)
    g=my_lcm(d,q)
    #print(g)
    # print("lcm(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
    return v,g
    #print("MKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
    
# ---------------------------------------------------------

def piecstura_laukums(x1,y1,  x2,y2,  x3,y3,  x4,y4,  x5,y5):
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

    if ((line_and_check(x1,y1,x3,y3,x2,y2,x4,y4)) and line_and_check(x1,y1,x3,y3,x2,y2,x5,y5) and
         line_and_check(x1,y1,x4,y4,x2,y2,x5,y5) and line_and_check(x1,y1,x4,y4,x3,y3,x5,y5) and
         line_and_check(x2,y2,x4,y4,x3,y3,x1,y1) and line_and_check(x2,y2,x4,y4,x3,y3,x5,y5) and
         line_and_check(x2,y2,x5,y5,x1,y1,x3,y3) and line_and_check(x2,y2,x5,y5,x1,y1,x4,y4) and
         line_and_check(x3,y3,x5,y5,x4,y4,x2,y2) and line_and_check(x3,y3,x5,y5,x4,y4,x1,y1) and 
         line_and_check(x3,y3,x1,y1,x2,y2,x5,y5) and line_and_check(x3,y3,x1,y1,x2,y2,x4,y4) and
         line_and_check(x4,y4,x2,y2,x1,y1,x3,y3) and line_and_check(x4,y4,x2,y2,x5,y5,x3,y3) and
         line_and_check(x5,y5,x2,y2,x1,y1,x3,y3) and line_and_check(x5,y5,x2,y2,x1,y1,x4,y4)):
        
        # print("\nPiecstūris ir izliekts")
        S1 = 0.5*((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))
        S2 = 0.5*((x3-x1)*(y5-y1)-(x5-x1)*(y3-y1))
        S3 = 0.5*((x3-x5)*(y4-y5)-(x4-x5)*(y3-y5))
        S = S1 + S2 + S3
        return abs(S)
        # print("S = " + str(abs(S)))
        
    else:
        return False # print("\nPiecstūris ir ieliekts. Programma nevar aprēķināt ieliekta piecstūra laukumu.")
    
# ---------------------------------------------------------

def vai_punkti_nav_viena_puse_no_taines(x1,y1,x3,y3,x2,y2,x4,y4):
    a = y3-y1
    b = x1-x3
    c = x3*y1-x1*y3

    z1=a*x2+b*y2+c
    z3=a*x4+b*y4+c
    
    if (z1*z3>0) :
        return False
        #print("Punkti ir vienā pusē taisnei.")   нельзя вычислять площадь 
    else :
        return True # точки находятся по разным сторонам от прямой
    
# ---------------------------------------------------------   

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