import numpy


def is_real_check(n):
    # Pārbauda vai simbolu virkne ir reāls skaitlis vai nav.
    # Atgriež True, ja tas ir reāls skaitlis (float).
    # Atgriež False, ja tas nav reāls skaitlis (float).
    # n - pārbaudāma simbolu virkne.

    try:
        float(n)
    except:
        return False
    else:
        return True


def ievade_matrica_float(n, m):
    # Lietotājs var ievādīt nXm matricas elementus un funkcija atgriež divdimensijas masīvu ar n rindam un m kolonnam ar ievadītām vērtībam.
    # Ievādītas vērtības ir reālas vērtības (matricas elementi varētu būt float)
    # Glīti izvada atkarīgi no tas, cik ir nepieciešams starpes likt.
    # n - naturāls skaitlis, kurš nosaka matricas rindas skaitu
    # m - naturāls skaitlis, kurš nosaka matricas kolonnas skaitu

    a = numpy.empty((n, m), dtype=float)

    for i in range(n):
        for j in range(m):
            temp = input("Ievadiet matricas elememtu A(" + str(i) + "," + str(j) + ") ===> ")
            while is_real_check(temp) == False:
                temp = input("Kļūda! Ievadītais elements nav skaitlis!\nIevadiet matricas elememtu A(" + str(i) + "," + str(j) + ") ===> ")

            a[i, j] = float(temp)

    return a


def matricas_izvade_4_cipari(m):
    # Izvada divdimensijas masīvu tabulas veidā tā, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Tiek nodrošināta matricas elementu izvade_matrica_int tabulas veidā, pieņemot, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Atgriež matricas elementu izvade_matrica_int tabulas veidā
    # m - divdimensijas masīvs
    nm = (numpy.shape(m))
    sv = ""
    for x in range(nm[0]):
        for y in range(nm[1]):
            for i in range(5 - len(str(m[x, y]))):
                sv = sv + " "
            sv = sv + str(m[x, y])
        sv = sv + "\n"
    nn = len(sv)
    return sv[:nn - 1]


def transponet(a):
    n = a.shape[0]
    m = a.shape[1]
    b = numpy.empty((m, n), "O")

    for i in range(m):
        for j in range(n):
            b[i, j] = a[j, i]
    return b


n = int(input("Ievadiet N ==> "))
m = int(input("Ievadiet M ==> "))
a = ievade_matrica_float(n, m)
print("Ievadītā matrica:")
print(matricas_izvade_4_cipari(a))
print("\n")
print("Transponētā matrica:")

t = transponet(a)
print(matricas_izvade_4_cipari(t))

'''
def ievade_matrica(n, m):
	# Lietotājs var ievādīt nXm matricas elementus un funkcija atgriež divdimensijas masīvu ar n rindam un m kolonnam ar ievadītām vērtībam
	# n - naturāls skaitlis, kurš nosaka matricas rindas skaitu
	# m - naturāls skaitlis, kurš nosaka matricas kolonnas skaitu
	a = numpy.empty((n, m), dtype=int)
	for i in range(n):
		for j in range(m):
			temp = input("Ievadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
			while is_whole(temp) == False:
				temp = input("Kļūda! Ievadītais elements nav vesels skaitlis!\nIevadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
			a[i, j] = int(temp)
	return a

def is_whole(n):
	# Pārbauda vai simbolu virkne ir vesels skaitlis vai nav
	# Ja ir vesels skaitlis, tad True. Ja nav tad False.
	# n - simbolu virkne, kuru pārbauda.
	try:
		n = int(n)
	except:
		return False
	else:
		return True
'''

'''
import numpy
def ievade(n, m):
	#funkcija realizē divdimensiju masīva ievadi
	a = numpy.empty((n, m),"O")
	for i in range(n):
		for j in range(m):
			a[i,j] = input("ievadi matricas "
			               + "elememtu a("
			        + str(i+1) + ","
			        + str(j+1) + ") ===>") 

	return a

def transponeta(a):
	n = a.shape[0] 
	m = a.shape[1] 
	b = numpy.empty((m,n),"O")

	for i in range(m):
		for j in range(n):
			b[i,j]=a[j,i]
	return b



def izvade(a):
	#funckija izvada matricu
	n = a.shape[0] # x axis
	m = a.shape[1] # y axis
	s = ""
	for i in range(n):
		for j in range(m):
			s = s + "{:20s}".format(a[i,j])        
		s = s + "\n"
	return s

n=int(input("n>"))
m=int(input("m>"))
a=ievade(n,m)
print("Ievadītā matrica:")
print(izvade(a))
print("\n")
print("Transponētā matrica:")

t=transponeta(a)
print(izvade(t))
'''
