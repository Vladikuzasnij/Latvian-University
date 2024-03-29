# Programmas nosaukums: Viendimensijas masīva izveidi.
# 4. uzdevums (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas organizē viendimensijas masīva izveidi, datu ievadi un izvadi, lielākās un mazākās vērtības atrašanu. Masīva izmēru N ievada lietotājs.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def izveidot_masivu_ar_garumu(n):
    a = numpy.arange(n)
    for i in range(n):
        a[i] = int(input("Ievadi " + str(i) + ".elementu ===> ")

	return a

def izvade(x):
	n=len(x)
	s=str(x[0])
	for i in range(1, n):
		s=s + ", " + str(x[i])
	print(s)

def insert_sort(a):
	n=len(a)
	for i in range(1, n):
		if a[i - 1] > a[i]:
			x=a[i]
			j=i
			while a[j - 1] > x:
				a[j]=a[j - 1]
				j=j - 1
				if j == 0:
					break
			a[j]=x

while is_natural(n) == False:
    n=input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n=int(n)
m=izveidot_masivu_ar_garumu(n)

print("Masīva elementi ievadīšanas secībā:")
izvade(m)


print("Masīva minimālais elements: " + str(min(a)))
print("Masīva maksimālais elements: " + str(max(a)))
