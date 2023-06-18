#my libraly

import math
import random
import numpy as np

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


def factorials_cikls(n):
	if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
		n = int(n)
		a = 1
		while n >= 1:
			a = a * n
			n = n - 1
		return a
	else:
		return False


def factorial_rekursija(n):
	if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
		n = int(n)
		if n >= 0:
			if n == 0:
				return 1
			return factorial_rekursija(n - 1) * n
		else:
			return False
	else:
		return False

def count_dilstosa_rekursija(n):
	print(n)
	if n == 0:
		return
	else:
		count_dilstosa_rekursija(n - 1)


def count_augosa_cikls(n):
	n = n + 1
	for i in range(n, 1, -1):
		print(n - i + 1)


def calc_arcsin(x, PR):
	# Atgriež arcisn(x) vērtību
	# x - arcins(x) - funkcijas arguments
	# PR - precizitāte (nosaka pedējais saskaitamais)
	n = 0
	s = x
	y = x
	while abs(y / (n + 1)) > PR:
		n = n + 2
		y = y * x * x * (n - 1) / n
		s += y / (n + 1)
	return s


def is_real_and_abs_mazaks_neka_viens(n):
	# Pārbauda vai simbolu virkne n ir reāls skaitls un abs(n) < 1
	# Atgriež True, ja izpildas abi nosacījumi.
	# Atgriež "Nav reals skaitlis", ja simbolu virkne n nav reāls skaitlis
	# Atgriež "Ir reals skaitlis, bet abs(n) >= 1", ja ja simbolu virkne ir reāls skaitlis, bet abs(n) >= 1
	# n - simbolu virkne
	try:
		n = float(n)
	except:
		return "Nav reals skaitlis"
	else:
		n = float(n)
		if abs(n) >= 1:
			return "Ir reals skaitlis, bet abs(n) >= 1"
		else:
			return True


def make_string_from_list(mylist):
	p = ""
	for i in range(0, len(mylist), 1):
		p += mylist[i] + " "
	return p
	#print(p)
	#print(mylist[i])


def fool(k):
	t = k.split()
	return t


def delete_repeteated(mylist):
	return list(dict.fromkeys(mylist))


def sadalit_pirmreizinatajos(n):
	a = n
	j = 2
	t = ""
	sv1 = str(n) + " | "

	while a > 1:
		k = 0

		while (a % j) == 0:
			sv1 = str(j)
			a = a // j
			k = k + 1
			t += str(sv1) + " "

		j = j + 1

	return t


def sadalisana_uz_pirmskaitliem_kuri_neatkartojas(x):
	# Sadala skaitli x uz pirmskaitliem, kuri neatkartojas
	# Ja ir naturāls skaitlis, tad True. Ja nav tad False.
	# x - naturāls skaitlis
	n = 2
	r = ""
	while x > 1:
		if x % n == 0:
			r = r + str(n) + " "
			x = x // n
			while x % n == 0:
				x = x // n
		n += 1

	if r == "":
		return 1
	return r


def sum_until_0_ievadam():
	s = 0
	x = float(input("Ievadi skaitli ==> "))
	while x != 0:
		s = s + x
		x = float(input("Ievadi skaitli ==> "))
	print(str(s))


def swap_two_numbers(x, y):
	x, y = y, x
	return x, y


'''
def factorial_vezis(n):
        if n <= 1:
                return 1
        else:
                return n*factorial_vezis(n-1)
'''


def factorial_rekursija(n):
	if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
		n = int(n)
		if n >= 0:
			if n == 0:
				return 1
			return factorial_rekursija(n - 1) * n
		else:
			return False
	else:
		return False

# import lib
# print(lib.factorial_rekursija(5))

def factorial_cikls(n):
	# Aprēķina n faktoriāla vērtību izmantojot ciklu.
	# ja ir naturāls skaitlis vai nulle, tad return n!
	# ja nav naturāls skaitlis vai nulle, tad return False.
	# n - simbolu virkne (str).
	if is_natural_or_zero(n):
		n = int(n)
		a = 1
		while n >= 1:
			a = a * n
			n = n - 1
		return a
	else:
		return False


def burti_rekursija(n):
	print("A")
	if n > 1:
		burti_rekursija(n - 1)
	print("B")

	return ""


def GCD_rekursija(a, b): # Eiklīda algoritms LKD
	if a == 0:
		return b
	elif a < b:
		return GCD_rekursija(b, a)
	else:
		return GCD_rekursija(a - b, b)


def pakape_rekursija2(a, b):
	if b == 0:
		return 1
	elif b > 0:
		return a * pakape_rekursija2(a, b - 1)
	else:
		return 1 / pakape_rekursija2(a, abs(b))


def count_uz_leju_rekursija(x):
	if x > 0:
		print(x)
		return count_uz_leju_rekursija(x - 1)
	return


#count(5)


def count_dividers_rekursija(num_A, num_B, count): # количество делителей (само число их сколько их?)
	if num_A >= num_B:
		if num_A % num_B == 0:
			return count_dividers_rekursija(num_A, num_B + 1, count + 1)
		return count_dividers_rekursija(num_A, num_B + 1, count)
	else:
		return count


#n = 12
#print(count_dividers_rekursija(n, 1, 0))


# Является ли число точной степенью двойки?
# -1 значит false нет. 1 значит true - da
def power_of_two_rekursija(n, power, i): #
	if power < n:
		return power_of_two_rekursija(n, power * 2, i + 1)
	elif power == n:
		return i
	else:
		return -1
#n = 2
#print(power_of_two_rekursija(n, 1, 0))


def fibonaci_rekursija_list(n, index, lst):
	if (index + 1) <= n:
		lst.append(lst[index - 1] + lst[index - 2])
		return fibonaci_rekursija_list(n, index + 1, lst)
	return lst
#n = 10
#print(fibonaci_rekursija_list(n, 2, [0, 1]))


def range():
	A = range(1, 10**1000, 2) # арифметическая прогрессия пробежать от 1 до 10**1000 с шагом 2
	return (A[5])
	# A = range(1, 10**1000, 2) # range(start, stop, step)
	# print((A[5])) # Выводит 6 элемент

# x станет равным своей последней цифре


def x_becomes_its_last_number(x):
	x %= 10
	return x


def x_becomes_its_first_number(x):
	x //= 10
	return x


def factorial_rekursija_no_check(n):
	if n == 0:
		return 1
	return factorial_rekursija(n - 1) * n
# import lib
# print(lib.factorial_rekursija_no_check(5))


def fibonaci_rekursija_no_check(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fibonaci_rekursija(n - 1) + fibonaci_rekursija(n - 2)


def fibonacci_without_recursion(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		fib_prev = 0
		fib_current = 1
		for i in range(2, n + 1):
			fib_next = fib_prev + fib_current
			fib_prev = fib_current
			fib_current = fib_next
		return fib_current


def fibonaci_rekursija(n):
	if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
		if n == 1:
			return 0
		if n == 2:
			return 1
		return fibonaci_rekursija(n - 1) + fibonaci_rekursija(n - 2)
	else:
		return False


def palindroms_rekursija(s):
	s = str(s)
	if len(s) == 1 or len(s) == 0:
		return True
	elif s[0] == s[-1]:
		return palindroms_rekursija(s[1:-1])
	else:
		return False

# import lib
# print(lib.palindroms_rekursija("manam"))


def sakne_rekursija(a, b, pr): # монотонно возрастающая или монотонно убывающая и функция с разными знаками на концах
	if abs(a - b) < pr:
		return (a + b) / 2
	else:
		vp = (a + b) / 2
		x = f(a)
		y = f(vp)
		z = f(b)
		if y == 0:
			return vp
		elif x * y < 0:
			return sakne_rekursija(a, vp, pr)
		else:
			return sakne_rekursija(vp, b, pr)


def pakape_rekursija(x, n):
	if n == 0:
		return 1
	if n < 0:
		return 1 / pakape_rekursija(x, -n)
	if n % 2 == 0:
		return pakape_rekursija(x, n // 2) * pakape_rekursija(x, n // 2)
	else:
		return pakape_rekursija(x, n - 1) * x


def sum_rekursija(x): # 0 + 1 + 2 + 3 + 4 + ... + n
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return x + sum_rekursija(x - 1)


def calc_e(x, n):
	#n = int(input("Noradiet precizitāti ==> "))
	#x = float(input("Noradiet x pakāpi ==> "))

	s = 0
	for i in range(1, n, 1):

		s += (x**i) / (math.factorial(i))

		s = s + 1
		return s
	#print(s)


def cal_pi_2(precision):
	# Initialize denominator
	k = 1

	# Initialize sum
	s = 0

	for i in range(precision):

		# even index elements are positive
		if i % 2 == 0:
			s += 4 / k
		else:

			# odd index elements are negative
			s -= 4 / k

		# denominator is odd
		k += 2

	return s


def calc_pi(num_digits):
	# Calculate the value of pi to the specified number of digits
	return round(math.pi, num_digits)


def calc_e_2_var(x, n):
	s = 0
	for i in range(1, n, 1):
		s += (x**i) / (math.factorial(i))

	return s + 1


def calc_sin(x, n):
	#n = int(input("Noradiet precizitāti ==> "))
	#x = float(input("Noradiet x ==> "))

	s = 0
	for i in range(1, n, 1):
		s += ((-1)**(i - 1)) * ((x**(2 * i - 1)) / (math.factorial(2 * i - 1)))

	return s
	#print(s)


def calc_cos(x, n):
	#n = int(input("Noradiet precizitāti ==> "))
	#x = float(input("Noradiet x ==> "))

	s = 0
	for i in range(1, n, 1):

		s += (((-1)**(i + 1)) * (x**(2 * i))) / (math.factorial(2 * i))

	return 1 - s


def calc_ln_1_plus_x(x, n):
	s = 0
	for i in range(1, n, 1):
		s += (((-1)**(i + 1)) * (x**i)) / i

	return s


def arctgx(x, n):
	s = 0
	if abs(x) <= 1:
		for i in range(1, n, 1):
			s += (((-1)**(i - 1)) * ((x)**(2 * i - 1))) / (2 * i - 1)

		return s
	else:
		return False


def shx(x, n):
	s = 0
	for i in range(1, n, 1):
		s += ((x**(2 * i - 1)) / (math.factorial((2 * i - 1))))

	return s


def chx(x, n):
	s = 0
	for i in range(1, n, 1):
		s += ((x**(2 * i)) / (math.factorial((2 * i))))

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
	return x**(1 / 3)

# ---------------------------------------------------------


def if_number_3_attempts():
	# vai skaitlis?
	k = 0
	while k < 3:
		x = input("Ievadi skaitli => ")
		try:
			x = float(x)
		except:
			k = k + 1
			print("Nepareiza ievade")
		else:
			return x
	else:
		print("Jūs pārak daudz reizes kļūdījāties! Beidzam sadarbību!")


#x = if_number_3_attempts("x")
#y = if_number_3_attempts("y")
# katram tiek dots trīs pārbaudījumi
# ---------------------------------------------------------
def solve_quadratic(a, b, c): # ax^2 + bx + c = 0 (in real numbers)
	if a == 0:
		print("Tas nav kvadratvienadojums")
	else:
		d = b * b - 4 * a * c # Diskriminants
		if d < 0:
			return False

		else:
			x1 = (-b + math.sqrt(d)) / 2 / a
			x2 = (-b - math.sqrt(d)) / 2 / a
			return x1, x2
#print(lib.solve_quadratic(1,1,2))

# ---------------------------------------------------------


def solve_quadratic_complex(a, b, c): # ax^2 + bx + c = 0 (in complex numbers)

	# Nav kvadrātvienādojums pēc definīcijas
	if a == 0:
		return False # Tas nav kvadraatvienādojums

	else: # Citādi risinām kvadrātvienādojumu

		d = b * b - 4 * a * c # Diskriminants

		if d < 0: # Tad ir komplēksa skaitļi

			#print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
			#print("\nKvadrātvienādojumam realu saknu nav\nIr divas kompleksas saknes\n")

			Re = -b
			Im = abs(math.sqrt(-d) / (2 * a))
			return (f"{Re} + i*{Im} \n{Re} - i*{Im}")

		else: # Divas atšķirīgas saknes

			x1 = (-b + math.sqrt(d)) / 2 / a
			x2 = (-b - math.sqrt(d)) / 2 / a

			#print("\n("+str(a)+")*x^2 + " + "(" + str(b) + ")"+ "*x"+" + ("+str(c)+") = 0")
			#print("\nKvadrātvienādojumam ir divas atšķirīgas vai vienādas saknes")
			return x1, x2

#print(lib.solve_quadratic_complex(1,1,2))
# ---------------------------------------------------------


def solve_bikvadrat_vienadojums(a, b, c): # ax^4 + bx^2 + c = 0
	if a == 0: # Pēc def. tas nav bikvadrātvienādojums ja a == 0

		return False
		#print("\nTas nav bikvadrātvienādojums")

	else:

		d = b * b - 4 * a * c # Diskriminants

		if d < 0: # Risinām ax^4 + bx^2+c=0. x^2 = t , at^2 + bt + c = 0, atrādam t1,t2 un tad atradam x1,x2 x = +-sqrt(t)

			return False
			#print("\nBikvadrātvienādojumam nav reālas saknes")

		else:

			t1 = (-b + math.sqrt(d)) / 2 / a
			t2 = (-b - math.sqrt(d)) / 2 / a

			if t1 >= 0:
				if t2 >= 0:
					x1 = math.sqrt(t1)
					x2 = -1 * (math.sqrt(t1))
					x3 = math.sqrt(t2)
					x4 = -1 * (math.sqrt(t2))
					#print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")

					return x1, x2, x3, x4

				else:

					x1 = math.sqrt(t1)
					x2 = -1 * (math.sqrt(t1))
					#print("\n("+str(a)+")*x^4 + " + "(" + str(b) + ")"+ "*x^2"+" + ("+str(c)+") = 0\n")

					return x1, x2

			elif t2 >= 0:
				x1 = math.sqrt(t2)
				x2 = -1 * (math.sqrt(t2))
				print("\n(" + str(a) + ")*x^4 + " + "(" + str(b) + ")" + "*x^2" + " + (" + str(c) + ") = 0\n")

				return x1, x2

			else:
				return False

# ---------------------------------------------------------


def cbrt(x):
	if x < 0:
		x = abs(x)
		cube_root = x**(1 / 3) * (-1)
	else:
		cube_root = x**(1 / 3)
	return cube_root


def triangle_area_in_coordinates(x1, y1, x2, y2, x3, y3):
	Area = abs((0.5) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
	if Area == 0:
		return False
	else:
		return Area
#print(lib.triangle_area_in_coordinates(1,1, 2,3, 4,6))

# ---------------------------------------------------------


def vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2):
	SD = A1 * B2 - A2 * B1

	if SD == 0:
		return False
	else:
		return True

#print(lib.vai_taisnem_ir_kopigs_punkts(1, 1, 2, 2))
# ---------------------------------------------------------


def two_line_interseption_point_coordinate_x(A1, B1, C1, A2, B2, C2): # (x;y)
	D = A1 * B2 - A2 * B1
	Dx = -C1 * B2 + B1 * C2
	x = Dx / D
	return x

#print(lib.two_line_interseption_point_coordinate_x(A1,B1,C1, A2,B2,C2)) # x koordinata
# ---------------------------------------------------------


def two_line_interseption_point_coordinate_y(A1, B1, C1, A2, B2, C2): # (x;y)
	D = A1 * B2 - A2 * B1
	Dy = -C2 * A1 + A2 * C1
	y = Dy / D
	return y

#print(lib.two_line_interseption_point_coordinate_y(A1,B1,C1, A2,B2,C2)) # y koordinata
# ---------------------------------------------------------


def triangle_perimeter(x1, y1, x2, y2, x3, y3):
	a = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
	b = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
	c = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
	p = a + b + c
	return p

#print(lib.triangle_perimeter(1,1, 2,3, 4,6))
# ---------------------------------------------------------



def is_prime_old(n):
	if n <= 1:
		return False

	for i in range(2,n):
		if (n%i) == 0:
			return False

	return True



def is_prime(n):
	try:
		n = int(n)
	except:
		return False
	else:
		if n <= 1:
			return False
		for i in range(2, n):
			if (n % i) == 0:
				return False
		return True

#print(lib.is_prime(11))


def is_pirmskaitlis(n):
	m = math.floor(math.sqrt(n)) + 1
	for i in range(2, m):
		if (n % i) == 0:
			return False
	return True


def divi_pakape(i):
	sk = 1
	for j in range(i):
		sk = sk * 2
	return sk

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
	x = x.strip()
	if x.isdigit():
		if int(x) > 0:
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
	x = x.strip()
	if (x[0] == "-") or (x[0] == "+"):
		y = x[1:]
	else:
		y = x
	z = y.find(".")
	if z == -1:
		vd = y # veselā daļa
		dd = "0" # daļveida daļa
	elif z == 0:
		vd = "0"
		dd = y[1:]
	elif z == len(y) - 1:
		vd = y[0:len(y) - 1:]
		dd = "0"
	else:
		vd = y[0:z:]
		dd = y[z + 1:]
	if vd.isdigit() and dd.isdigit():
		return True
	else:
		return False

# print(lib.check_str_real_number(x))

# ---------------------------------------------------------


def is_zero(n):
	try:
		n = 1 / n
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
		c = 1 / n
	except:
		return False
	else:
		return True

#print(lib.is_zero(0))

# ---------------------------------------------------------

# можно вводить как str "" так и числа


def izteiksmes_vertiba(n):
	# Funkcija atrgriež uzdevumā norādītas izteiksmes vērtību.
	# n - naturāls skaitlis
	s = n + 1
	for i in range(n, 0, -1):
		s = i + 1 / s
	return s

#print(lib.is_real("ad"))
# ---------------------------------------------------------


def solve_equation_ax3_plus_by2_plus_cz_plus_d_equals_0(a, b, c, d):
	# Funkcija atrod visus veselos atrisinājumus vienādojumam ax^3 + by^2 + cz + d = 0
	# Funkcija izmanto pilno pārlasi. Tālak funkcija nodot "kortežus" (x, y, z) veidā kā vienu lielo simbolu virkni
	# a - funkcijas parametrs a (ax^3 + ...)
	# b - funkcijas parametrs b (... + by^2 + ...)
	# c - funkcijas parametrs c (... + cz + ...)
	# d - funkcijas parametrs d (... + d = 0)
	sv = ""
	for x in range(-10, 11):
		for y in range(-10, 11):
			for z in range(-10, 11):
				if a * x * x * x + b * y * y + c * z + d == 0:
					sv += "(" + str(x) + ", " + str(y) + ", " + str(z) + ")\n"
	return sv


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

def is_real(x): # By Kristaps. Bezgalīgi daudz reizes ievāda
	x = input("Ievadi reālo pozitīvo skaitli ===> ")
	while True:
		try:
			x = float(x)
		except:
			x = input("Mēģini vēlreiz ===> ")
		else:
			return float(x)

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

def is_real_positive_or_zero(): # By Kristaps. Bezgalīgi daudz reizes ievāda
	x = input("Ievadi reālo pozitīvo skaitli ===> ")
	while True:
		try:
			x = float(x)
		except:
			x = input("Mēģini vēlreiz ===> ")
		else:
			if x < 0:
				x = input("Mēģini vēlreiz ===> ")
			else:
				return float(x)


def input_number_that_is_real_positive_or_zero():
	x = input("Ievadi reālo pozitīvo skaitli ===> ")
	while True:
		try:
			x = float(x)
		except:
			x = input("Mēģini vēlreiz ===> ")
		else:
			if x < 0:
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


def my_gcd(x, y):
	a = x
	b = y
	while b != 0:
		c = a % b
		a = b
		b = c
	return a

# Lielākais kopīgais dalītājs
# LKD

# ---------------------------------------------------------


def my_lcm(x, y):
	return abs(x * y) / my_gcd(x, y)


def my_gcd_3(a, b, c):
	def my_gcd(x, y):
		a = x
		b = y
		while b != 0:
			c = a % b
			a = b
			b = c
		return a
	return my_gcd(a, my_gcd(b, c))


def my_lcm_3(a, b, c):
	return my_lcm(a, my_lcm(b, c))

# Mazākais kopīgais dalāmais
# MKD
# print(lib.my_lcm(10,120))

# ---------------------------------------------------------


def combinations(m, n): # n is bottom n>=k Pick two from four
	if m > n:
		return False

	fn = 1
	for i in range(2, n + 1):
		fn = fn * i

	fm = 1
	for i in range(2, m + 1):
		fm = fm * i

	fnm = 1
	for i in range(2, n - m + 1):
		fnm = fnm * i
		c = fn / fm / fnm

	return c
#print(lib.combinations(2,5)) # pick two from 5

# ---------------------------------------------------------


def prime_factor(n): #pirmreizinātaji
	a = n
	j = 2
	sv = str(n) + "="
	while a > 1:
		k = 0
		while (a % j) == 0:
			a = a // j
			k = k + 1
		if k > 0:
			sv = sv + str(j) + "^" + str(k) + "*"
		j = j + 1

	sv = sv + "1"

	return sv
#print(lib.prime_factor(10))
# ---------------------------------------------------------


def sakartot_4(a, b, c, d):
	if a > b:
		x = a
		a = b
		b = x
	if c > d:
		x = c
		c = d
		d = x
	if a > c:
		x = c
		c = a
		a = x
	if b > d:
		x = b
		b = d
		d = x
	if b > c:
		x = b
		b = c
		c = x

	return str(a), str(b), str(c), str(d)

#print(lib.sakartot_4(4,-2,1,10))
# ---------------------------------------------------------


def sakartot_3(a, b, c):
	if a < b:
		p = a
		a = b
		b = p

	if a < c:
		p = c
		c = a
		a = p

	if b < c:
		p = b
		b = c
		c = p

	return str(a), str(b), str(c)

# ---------------------------------------------------------


def can_make_triangle_old(a, b, c): # malu garumi a b c nevis koordinatas
	if (a + b > c) and (b + c > a) and (a + c > b):
		return True
	else:
		return False

def can_make_triangle(a, b, c): # malu garumi a b c nevis koordinatas
	if (a + b <= c) or (a + c <= b) or (b + c <= a):
		return False
	else:
		return True
#print(lib.can_make_triangle(3,4,5))
# ---------------------------------------------------------


def are_two_points_on_the_one_side(a, b, c, x1, y1, x2, y2): #pēc ax+by+c=0 taisne x1,y1 - 1.punkts. x2,y2 - 2.punkts

	z1 = a * x1 + b * y1 + c
	z2 = a * x2 + b * y2 + c

	if z1 * z2 > 0:
		return True # ir vienā puse
	else:
		return False # dažādas puses no taisnem

#print(lib.are_two_points_on_the_one_side(1,1,1,  3,4, 5,6))
# ---------------------------------------------------------


def roll_dice():
	a = random.randint(1, 6)
	return a

#print(lib.roll_dice())
# ---------------------------------------------------------



def horoskopi_pec_gadiem(g):
	g = g % 12
	match g:
		case 11:
			a = "Kaza"
		case 10:
			a = "Zirgs"
		case 9:
			a = "Čūska"
		case 8:
			a = "Pūķis"
		case 7:
			a = "Kaķis"
		case 6:
			a = "Tīģeris"
		case 5:
			a = "Vērsis"
		case 4:
			a = "Žurka"
		case 3:
			a = "Cūka"
		case 2:
			a = "Suns"
		case 1:
			a = "Gailis"
		case 0:
			a = "Mērkaķis"

	return a

#print(lib.horoskopi_pec_gadiem(3)) # kaza
# ---------------------------------------------------------


def horoskopi_pec_menesiem(menesis, datums):
	m = menesis
	d = datums
	match m:
		case 1:
			if d < 20:
				a = "Mežāzis"
			else:
				a = "Ūdensvīrs"
		case 2:
			if d < 19:
				a = "Ūdensvīrs"
			else:
				a = "Zivis"
		case 3:
			if d < 21:
				a = "Zivis"
			else:
				a = "Auns"
		case 4:
			if d < 20:
				a = "Auns"
			else:
				a = "Vērsis"
		case 5:
			if d < 21:
				a = "Vērsis"
			else:
				a = "Dvīņi"
		case 6:
			if d < 22:
				a = "Dvīņi"
			else:
				a = "Vēzis"
		case 7:
			if d < 23:
				a = "Vēzis"
			else:
				a = "Lauva"
		case 8:
			if d < 23:
				a = "Vēzis"
			else:
				a = "Jaunava"
		case 9:
			if d < 23:
				a = "Jaunava"
			else:
				a = "Svari"
		case 10:
			if d < 23:
				a = "Svari"
			else:
				a = "Skorpions"
		case 11:
			if d < 23:
				a = "Skorpions"
			else:
				a = "Strēlnieks"
		case 12:
			if d < 22:
				a = "Strēlnieks"
			else:
				a = "Mežāzis"

	return a

#print(lib.horoskopi_pec_menesiem(2, 5)) # kaza
# ---------------------------------------------------------


def cubic_equation_in_whole_numbers(a, b, c, d): #ax^3 + bx^2 + cx + d = 0

	s = ""
	w = abs(d)
	n = round(math.sqrt(w)) + 1
	for i in range(1, n):
		if (w % i) == 0:
			x = i * i * i
			y = i * i
			z = w // i
			u = z * z * z
			v = z * z
			if a * x + b * y + c * i + d == 0:
				s = s + str(i) + " "
			if -a * x + b * y - c * i + d == 0:
				s = s + str(-i) + " "
			if a * u + b * v + c * z + d == 0:
				s = s + str(z) + " "
			if -a * u + b * v - c * z + d == 0:
				s = s + str(-z) + " "
			if s == "":
				return "Veselu sakņu nav"
			else:
				return s

#print(lib.cubic_equation_in_whole_numbers(a,b,c,d))
# ---------------------------------------------------------


def number_of_point_in_circle(r):
	r1 = math.floor(r)
	sk = 1
	for i in range(0, r1 + 1):
		sk = sk + 4 * math.floor(math.sqrt(r * r - i * i))

	return sk

#print(lib.number_of_point_in_circle(5))
# ---------------------------------------------------------

# какое число находится на n позиции


def what_is_on_n_position(n, virkne):
	virkne = str(virkne)
	k = 0
	skaitlis = 0
	while k < n:
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


def cetrsturis_laukums(x1, y1, x2, y2, x3, y3, x4, y4): # koordinātas

	def puses(x1, y1, x2, y2, x3, y3, x4, y4):
		z1 = (x1 - x4) * (y3 - y4) - (y1 - y4) * (x3 - x4)
		z2 = (x2 - x4) * (y3 - y4) - (y2 - y4) * (x3 - x4)
		return z1 * z2 > 0

	def mala(xs, ys, xb, yb):
		return math.sqrt((xs - xb) * (xs - xb) + (ys - yb) * (ys - yb))

	def laukums(x1, y1, x2, y2, x3, y3):
		a = mala(x1, y1, x2, y2)
		b = mala(x2, y2, x3, y3)
		c = mala(x1, y1, x3, y3)
		p = (a + b + c) / 2
		return math.sqrt(p * (p - a) * (p - b) * (p - c))

	if (puses(x1, y1, x2, y2, x3, y3, x4, y4)
        and puses(x4, y4, x1, y1, x2, y2, x3, y3)
        and puses(x3, y3, x4, y4, x1, y1, x2, y2) and
        puses(x2, y2, x3, y3, x4, y4, x1, y1)) :
		s = laukums(x1, y1, x2, y2, x3, y3) + laukums(x1, y1, x4, y4, x3, y3)
		return s
	else:
		return False # ieliekts

# ---------------------------------------------------------


def vai_taisnem_ir_kopigs_punkts(A1, B1, A2, B2):
	SD = A1 * B2 - A2 * B1
	if SD == 0:
		return False
	else:
		return True

# ---------------------------------------------------------


def two_line_interseption_point_coordinate_x(A1, B1, C1, A2, B2, C2): # (x;y)
	D = A1 * B2 - A2 * B1
	Dx = -C1 * B2 + B1 * C2
	x = Dx / D
	return x

# ---------------------------------------------------------


def two_line_interseption_point_coordinate_y(A1, B1, C1, A2, B2, C2): # (x;y)
	D = A1 * B2 - A2 * B1
	Dy = -C2 * A1 + A2 * C1
	y = Dy / D
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

	if DD_MM_GGGG_.count('.') != 3:
		return False

	try:

		DD = int(DD)
		b = 1 / DD # 00.MM.GGGG.

		MM = int(MM)
		c = 1 / MM # DD.00.GGGG.

		GGGG = int(GGGG)
		d = 1 / GGGG # DD.MM.0000.

	except:
		return False
		#print("Tāds datums neeksistē")
		#quit()

	else:
		pass

	DD = int(DD) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 31 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē
	if DD > 31 or DD <= 0:
		return False
		#print("Tāds datums neeksistē")
		#quit()

	MM = int(MM) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 12 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē

	if MM > 12 or MM <= 0:
		return False
		#print("Tāds datums neeksistē")
		#quit()

	GGGG = int(GGGG)  # Parveidojam int, lai uzzinātu vai tas ir mazāks vai vienāds ar 0, tad tāds datums neeksistē

	if GGGG <= 0:
		return False
		#print("Tāds datums neeksistē")
		#quit()

	if MM == 4 and DD > 30: # Aprilī maksimāli ir tikai 30 dienas.
		return False
		#print("Tāds datums neeksistē")
		#quit()

	if MM == 6 and DD > 30: # Jūnija maksimāli ir tikai 30 dienas.
		return False
		#print("Tāds datums neeksistē")
		#quit()

	if MM == 9 and DD > 30: # Septembrī maksimāli ir tikai 30 dienas.
		return False
		#print("Tāds datums neeksistē")
		#quit()

	if MM == 11 and DD > 30: # Novembrī maksimāli ir tikai 30 dienas.
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
	days_year = (Year - 1) * 365 + (Year - 1) // 4 - (Year - 1) // 100 + (Year - 1) // 400 # pagajušo dienu skaits
	days_year = int(days_year)
	DD = int(DD)
	if leap_year(GGGG) == False:
		F = 28
	else:
		F = 29

	if MM == "01":
		days = days_year + DD # only january
		return days
	if MM == "02": # MM == 2

		days = days_year + DD + 31 # + all of january
		return days
	if MM == "03": # MM == 3

		days = days_year + DD + 31 + F  # + all of january and february
		return days
	if MM == "04":

		days = days_year + DD + 31 + F + 31
		return days
	if MM == "05":

		days = days_year + DD + 31 + F + 31 + 30
		return days
	if MM == "06":

		days = days_year + DD + 31 + F + 31 + 30 + 31
		return days
	if MM == "07":

		days = days_year + DD + 31 + F + 31 + 30 + 31 + 30
		return days
	if MM == "08":

		days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31
		return days
	if MM == "09":

		days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31
		return days
	if MM == "10":

		days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30
		return days
	if MM == "11":

		days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
		return days
	if MM == "12":

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

	v2 = ""

	for i in v:

		v2 = i + v2

	return v2

# ---------------------------------------------------------


def faktorials(n): # N = N*(N-1)*...4*3*2*1
	if str(n).isdigit() and float(n) == int(n):
		n = int(n)
		faktorials = 1
		for i in range(1, n + 1):
			faktorials = faktorials * i

		return faktorials
	else:
		return False

# ---------------------------------------------------------


def recur_factorial(n):
	if n == 1:
		return n
	else:
		return n * recur_factorial(n - 1)

# ---------------------------------------------------------


def faktorials2(n): # ar rekursiju rekursija N! = N*(N-1)!

	def recur_factorial(n):
		if n == 1:
			return n
		else:
			return n * recur_factorial(n - 1)
	if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
		if n == 0:
			return 1
		else:
			return recur_factorial(n)
	else:
		return False

# ---------------------------------------------------------


def circle_area(r):
	return math.pi * r * r

#----------------------------------------------------------


def circle_circumference(r): # perimetrs
	return 2 * math.pi * r

#----------------------------------------------------------


def max_of_three_numbers(a, b, c):
	if a >= b and a >= c:
		return a
	elif b >= a and b >= c:
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
	if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
		return True
	else:
		return False

#----------------------------------------------------------


def is_positive_or_zero(n):
	if n >= 0:
		return True
	else:
		return False

#----------------------------------------------------------


def is_positive(n):
	if n > 0:
		return True
	else:
		return False

#----------------------------------------------------------


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

#----------------------------------------------------------


def is_natural(n):
	# Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
	# Ja ir naturāls skaitlis, tad True. Ja nav tad False.
	# n - simbolu virkne, kuru pārbauda.
	if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
		return True
	else:
		return False


def izteiksmes_vertiba_1uzd_cepnaja_drob(n):
	# Funkcija atrgriež uzdevumā norādītas izteiksmes vērtību.
	# n - naturāls skaitlis
	s = n + 1
	for i in range(n, 0, -1):
		s = i + 1 / s
	return s

#----------------------------------------------------------


def is_natural_or_zero(n):
	# Pārbauda vai simbolu virkne ir naturāls skaitlis vai nulle, vai nav
	# Ja ir naturāls skaitlis vai nulle, tad True. Ja nav tad False.
	# n - simbolu virkne, kuru pārbauda.	
	if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
		return True
	else:
		return False

#----------------------------------------------------------


def multiplication_table(n1, n2):
	for i in range(1, 21):
		print(format(n1, "<2"), "* ", format(i, "<2"), "=", n1 * i, end="\t")
		print(format(n2, "<2"), "* ", format(i, "<2"), "=", n2 * i)

#----------------------------------------------------------


def trijstura_laukums(a, b, c):

	if a >= b + c:
		return False
	elif b >= a + c:
		return False
	elif c >= a + b:
		return False

	else:
		p = (a + b + c) / 2 # Pusperimetra apreķināšana

		area = math.sqrt(p * (p - a) * (p - b) * (p - c)) # Laukuma apreķināšana izmantojot Herona formulu
		return area

#----------------------------------------------------------


def divu_linear_vienadojumu_atrisinasana(a, b, c, d, e, f):

	D = a * e - b * d
	Dx = c * e - b * f
	Dy = a * f - c * d

	# Ja Sistēmas determinants ir 0 un (Dx != 0 vai Dy != 0 tad nav atrisinājumu)

	if D == 0 and (Dx != 0 or Dy != 0):
		return False

	# Ja visi determinanti (D == 0 un Dx == 0 un Dy == 0) tad ir bezgalīgi daudz atrisinājumu

	if D == 0 and Dx == 0 and Dy == 0:
		return "Bezgalīgi daudz atrisinājumu"

	# Ja sistēmas determinants nav 0, tad ir viens vienīgs atrisinājums

	if D != 0:

		x = Dx / D
		y = Dy / D

		return x, y

#----------------------------------------------------------


def divu_linear_vienadojumu_atrisinasana_ar_proporciju(a, b, c, d, e, f):

	# Determinantu apreķināšana (Lai paradītu atrisinājumu, ja tads ir)
	D = a * e - b * d
	Dx = c * e - b * f
	Dy = a * f - c * d

	# Gadījums, kad nav atrisinājums
	if a / d == b / e and b / e != c / f:
		return False

	# Gadījums, kad bezgalīgi daudz atrisinājumu
	if a / d == b / e and b / e == c / f:
		return "Bezgalīgi daudz atrisinājumu"

	# Ir viens atrisinājums
	if a / d != b / e:

		x = Dx / D
		y = Dy / D

		return x, y

#----------------------------------------------------------


def vai_izliekts_cetrsturis(x1, y1, x2, y2, x3, y3, x4, y4):  # Ieliekts (вогнутый, нестандартный). Izliekts - выпуклый - хороший # pēc koordinātam

	#AC taisne
	z1 = (x4 - x1) * (y3 - y1) - (y4 - y1) * (x3 - x1)

	z2 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

	#BD taisne
	z3 = (x1 - x2) * (y4 - y2) - (y1 - y2) * (x4 - x2)

	z4 = (x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2)

	if z1 * z2 > 0 or z3 * z4 > 0:
		return True
		# print ("Izliekts") (хороший, можно посчитать площадь)

	else:
		return False
		# print ("Ieliekts") # вогнутый (плохой, нельзя посчитать площадь)

#----------------------------------------------------------

# pēc lietotāja ievadītajām trijstūra virsotņu A(x1, y1), B(x2, y2) un C(x3, y3), un punkta D(x4, y4) koordinātām, noskaidro un paziņo, vai punkts D atrodas trijstūra ABC iekšpusē.


def vai_punkts_trijstūri_iekspuse(x1, y1, x2, y2, x3, y3, x4, y4): # D - x4,y4 находится ли он внутри треугольника с такими координатами?
	ab = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
	bc = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
	ac = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
	ad = math.sqrt((x1 - x4) * (x1 - x4) + (y1 - y4) * (y1 - y4))
	bd = math.sqrt((x2 - x4) * (x2 - x4) + (y2 - y4) * (y2 - y4))
	cd = math.sqrt((x3 - x4) * (x3 - x4) + (y3 - y4) * (y3 - y4))

	z1 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
	z2 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
	z3 = (x4 - x2) * (y3 - y2) - (x3 - x2) * (y4 - y2)
	z4 = (x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)
	z5 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
	z6 = (x2 - x3) * (y1 - y3) - (x1 - x3) * (y2 - y3)

	if (z1 * z2 > 0) and (z3 * z4 > 0) and (z5 * z6 > 0):
		return True
		#print("Punkts D atrodas trijstūra iekšpusē")

	else:
		return False
		#print("Punkts D neatrodas trijstūra iekšpusē")

# --------------------------------------------------------------------

# pēc lietotāja ievadītajām trīs punktu A(x1, y1), B(x2, y2) un C(x3, y3) koordinātām, noskaidro un paziņo, vai šie trīs punkti atrodas uz vienas taisnes.


def vai_3_punkti_atrodas_uz_vienas_taisnes(x1, y1, x2, y2, x, y): # x,y tas ir x3,y3

	a = (x - x2) * (y1 - y2)
	b = (y - y2) * (x1 - x2)

	if a == b:
		return True
		# print("\nPunkti atrodas uz vienas taisnes")

	if a != b:
		return False
		# print("\nPunkti nav uz vienas taisnes")

# ---------------------------------------------------------

# divu punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) ievada lietotājs kā arī A, B un C koeficientus.
# Ax + By + C = 0   A(x1,y1) B(x2,y2)


def divu_punktu_novietojums_attieciba_pret_taisnei(a, b, c, x1, y1, x2, y2):
	z1 = a * x1 + b * y1 + c
	z2 = a * x2 + b * y2 + c

	if z1 == 0 and z2 == 0:
		print("Divi punkti ir uz vienas taisnes")

	elif z1 == 0 or z2 == 0:
		print("Viens punkts ir uz taisnes, otrais punkts nav uz taisnes")

	elif z1 * z2 > 0:
		print("Atrodas vienā puse no taisnes")

	else:
		print("Punkti nav vienā pusē taisnei")

# ---------------------------------------------------------

# paziņo par trīs punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) C(x3, y3) ievada lietotājs kā arī A, B un C koeficientus.
# Ax + By + C = 0   A(x1,y1) B(x2,y2) C(x3,y3))


def tris_punktu_novietojums_attieciba_pret_taisnei(a, b, c, x1, y1, x2, y2, x3, y3):

	z1 = a * x1 + b * y1 + c
	z2 = a * x2 + b * y2 + c
	z3 = a * x3 + b * y3 + c

	if z1 == 0 and z2 == 0 and z3 == 0:
		print("Trīs punkti ir uz vienas taisnes")

	elif (z1 == 0 and z2 == 0) or (z2 == 0 and z3 == 0) or (z3 == 0 and z1 == 0):
		print("Divi punkti ir uz taisnes, bet trešais nav uz taisnes")

	elif (z1 == 0 and z2 * z3 > 0) or (z2 == 0 and z1 * z3 > 0) or (z3 == 0 and z1 * z2 > 0):
		print("Viens uz taisnes, divi pārejie ir vienā puse no taisnes")

	elif (z1 == 0 and z2 * z3 < 0) or (z2 == 0 and z1 * z3 < 0) or (z3 == 0 and z1 * z2 < 0):
		print("Viens uz taisnes, divi pārejie ir pretējas puses no taisnes")

	elif (z1 * z2 > 0) and (z1 * z3 > 0):
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
			PirmieDiviCipari = x // 10
			D = PirmieDiviCipari % 10
			Desmiti = x % 100

			SimboluVirkne = ""

			match Simti:

				case 1:
					SimboluVirkne = SimboluVirkne + "vieni simti"

				case 2:
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

			if D == 1:
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

					case 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29:
						SimboluVirkne = SimboluVirkne + " divdesmit"

					case 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39:
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

					case 1:
						SimboluVirkne = SimboluVirkne + " viens"

					case 2:
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

	if a == 1:
		return False

	b = 1
	c = a

	for a in range(1, a - 1, 1):
		b = b + 1
		if c % b == 0:

			return False

	return True

# ---------------------------------------------------------


def vai_palindroms(x):

	y = len(x) # Cik ir garums

	atb = "Ir palindroms"

	for i in range(y // 2):
		if x[i] != x[y - 1 - i]:
			atb = "Nav palindroms"
			break

	if atb == "Ir palindroms":
		return True
	else:
		return False

# ---------------------------------------------------------


def simbolu_virknes_parvietosana_pa_vienu(x):
	n = len(x)
	for i in range(n):
		print(x[i:n] + x[0:i])

	return ""

# ---------------------------------------------------------

# lietotāja ievadīto vārdu izkārto ka parādīts piemērā. (квадратиком)


def simbolu_virkne_ka_kvadrats(x):

	n = len(x)

	print(x)

	for i in range(1, n - 1):
		sv = x[i]

		sv = sv + (n - 2) * " "

		sv = sv + x[n - 1 - i]
		print(sv)

	sv = ""

	for i in x:
		sv = i + sv
	print(sv)

	return ""

# ---------------------------------------------------------

# mazāko Fibonači skaitli, kas pārsniedz lietotāja ievadīto skaitli N.


def mazakais_fibonaci_skaitlis_kas_parsniedz_ievadito_skaitli(n):

	b = 1
	a = 1
	c = 0         # a,b=b,a+b (ja to izmantojam, tad nevajadzēs izmantot palīgmainīgo c)

	while n >= a: # kāmer n>=a, tad

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

	if n <= 0:
		return False

	a = 1
	b = 1
	c = 0

	sv = str(a) + str(b)

	while len(sv) < n:
		c = a + b
		a = b
		b = c
		sv = sv + str(c)

	print("Fibonači virknē zem numura " + str(n) + " atrodas cipars:")
	return (sv[n - 1])

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

	x = float(input("Ievadiet " + str(N) + " locekli ===> "))

	while x != 0:
		d1 = x - x2

		if d != d1:
			sv = "Dota virkne nav aritmētiska progresija"

		x2 = x
		N = N + 1
		x = float(input("Ievadiet " + str(N) + " locekli ===> "))
	else:
		print(sv)

	if x == 0: # pedējo un prikšpēdējo atņēmt
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
	q = x2 / x1
	N = 3

	x = float(input("Ievadiet " + str(N) + " locekli ===> "))

	while x != 0:
		d1 = x - x2
		q1 = x / x2

		if d != d1:
			sv = "Dota virkne nav aritmētiskā progresija"

		if q != q1:
			sv1 = "Dota virkne nav geometriskā progresija"

		x2 = x
		N = N + 1
		x = float(input("Ievadiet " + str(N) + " locekli ===> "))
	else:
		print(sv)
		print(sv1)

	if x == 0: # pedējo un prikšpēdējo atņēmt
		d1 = x - x2
		q1 = x / x2
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
		if x[i] != " ":  # s ! = ""
			v = x[i] + v # v = s + v

		else:
			sv = sv + v + " "
			v = ""
	sv = sv + v

	return sv

# ---------------------------------------------------------


def piecu_skaitlu_LKD_un_MKD(x, y, z, w, q): # gcd,lcm / LKD,MKD / НОД,НОК
	def my_gcd(a, b):

		while b != 0:
			c = a % b
			a = b
			b = c

		return a

	# Divu skaitļu lcm atrāšana
	# lcm (a, b) = a*b/(gcd (a,b))
	def my_lcm(a, b):

		return a * b / my_gcd(a, b)

	#noteiksim gcd no 5 skaitliem
	t = my_gcd(x, y)
	u = my_gcd(t, z)
	l = my_gcd(u, w)
	v = my_gcd(l, q)
	#print(v)
	#print("gcd(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))
	#print("LKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))

	#noteiksim lcm no 5 skaitliem
	a = my_lcm(x, y)
	s = my_lcm(a, z)
	d = my_lcm(s, w)
	g = my_lcm(d, q)
	#print(g)
	# print("lcm(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
	return v, g
	#print("MKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))

# ---------------------------------------------------------


def piecstura_laukums(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
	def line_and_check(x1, y1, x3, y3, x2, y2, x4, y4):
		a = y3 - y1
		b = x1 - x3
		c = x3 * y1 - x1 * y3

		z1 = a * x2 + b * y2 + c
		z3 = a * x4 + b * y4 + c

		if (z1 * z3 > 0):
			return False
			#print("Punkti ir vienā pusē taisnei.")
		else:
			return True
			#print("Punkti nav vienā pusē taisnei.")

		# x*(y3-y1)+y*(x1-x3)+x3*y1-x1*y3=0

	if ((line_and_check(x1, y1, x3, y3, x2, y2, x4, y4)) and line_and_check(x1, y1, x3, y3, x2, y2, x5, y5) and
        line_and_check(x1, y1, x4, y4, x2, y2, x5, y5) and line_and_check(x1, y1, x4, y4, x3, y3, x5, y5)
        and line_and_check(x2, y2, x4, y4, x3, y3, x1, y1) and line_and_check(x2, y2, x4, y4, x3, y3, x5, y5)
        and line_and_check(x2, y2, x5, y5, x1, y1, x3, y3) and line_and_check(x2, y2, x5, y5, x1, y1, x4, y4)
        and line_and_check(x3, y3, x5, y5, x4, y4, x2, y2) and line_and_check(x3, y3, x5, y5, x4, y4, x1, y1)
        and line_and_check(x3, y3, x1, y1, x2, y2, x5, y5) and line_and_check(x3, y3, x1, y1, x2, y2, x4, y4)
        and line_and_check(x4, y4, x2, y2, x1, y1, x3, y3) and line_and_check(x4, y4, x2, y2, x5, y5, x3, y3)
        and line_and_check(x5, y5, x2, y2, x1, y1, x3, y3) and line_and_check(x5, y5, x2, y2, x1, y1, x4, y4)):

		# print("\nPiecstūris ir izliekts")
		S1 = 0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
		S2 = 0.5 * ((x3 - x1) * (y5 - y1) - (x5 - x1) * (y3 - y1))
		S3 = 0.5 * ((x3 - x5) * (y4 - y5) - (x4 - x5) * (y3 - y5))
		S = S1 + S2 + S3
		return abs(S)
		# print("S = " + str(abs(S)))

	else:
		return False # print("\nPiecstūris ir ieliekts. Programma nevar aprēķināt ieliekta piecstūra laukumu.")

# ---------------------------------------------------------


def vai_punkti_nav_viena_puse_no_taines(x1, y1, x3, y3, x2, y2, x4, y4):
	a = y3 - y1
	b = x1 - x3
	c = x3 * y1 - x1 * y3

	z1 = a * x2 + b * y2 + c
	z3 = a * x4 + b * y4 + c

	if (z1 * z3 > 0):
		return False
		#print("Punkti ir vienā pusē taisnei.")   нельзя вычислять площадь
	else:
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

	for i in range(0, len(email)):
		if email[i] == "@":
			symbol_at_count += 1
			# pārbauda, vai ir vismaz 1 rakstzīme pirms simbola @
			if i == 0:
				return False
			# pārbauda, vai ir vismaz 1 rakstzīme pēc simbola @
			if i == len(email) - 1:
				return False
			if email[i + 1] == ".": # pārbauda, pēc @ nav ., ja ir tad False
				return False

		elif email[i] == ".":
			dot_count += 1
			# pārbauda, vai ir vismaz 1 rakstzīme pirms punkta
			if i == 0:
				return False
			# pārbauda, vai ir vismaz 1 rakstzīme pēc punkta
			if i == len(email) - 1:
				return False

			if email[i + 1] == ".": # pārbauda, pēc punkta nav otrā punkta, ja ir tad False
				return False

			if email[i + 1] == "@": # pārbauda, pēc punkta nav @, ja ir tad False
				return False

		elif not (email[i] == "q" or email[i] == "w" or email[i] == "e" or email[i] == "r" or
                  email[i] == "t" or email[i] == "y" or email[i] == "u" or email[i] == "i"
                  or email[i] == "o" or email[i] == "p" or email[i] == "a" or email[i] == "s"
                  or email[i] == "d" or email[i] == "f" or email[i] == "g" or email[i] == "h"
                   or email[i] == "j" or email[i] == "k" or email[i] == "l" or email[i] == "z"
                   or email[i] == "x" or email[i] == "c" or email[i] == "v" or email[i] == "b"
                   or email[i] == "n" or email[i] == "m"

                   or email[i] == "Q" or email[i] == "W" or email[i] == "E" or email[i] == "R"
                   or email[i] == "T" or email[i] == "Y" or email[i] == "U" or email[i] == "I"
                   or email[i] == "O" or email[i] == "P" or email[i] == "A" or email[i] == "S"
                   or email[i] == "D" or email[i] == "F" or email[i] == "G" or email[i] == "H"
                   or email[i] == "J" or email[i] == "K" or email[i] == "L" or email[i] == "Z"
                   or email[i] == "X" or email[i] == "C" or email[i] == "V" or email[i] == "B"
                   or email[i] == "N" or email[i] == "M"

                   or email[i] == "1" or email[i] == "2" or email[i] == "3" or email[i] == "4"
                   or email[i] == "5" or email[i] == "6" or email[i] == "7" or email[i] == "8"
                   or email[i] == "9" or email[i] == "0"

                   or email[i] == "_" or email[i] == "."):

			# atsevišķie vārdi var saturēt tikai latīņu burtus, ciparus un pasvītrojuma rakstzīmi _

			return False

	if symbol_at_count != 1: # Jābut tieši vienam @ simbolam
		return False
	if dot_count == 0: # jābut vismaz vienam punktam. @inbox.lv @lu.lv
		return False

	return True

# -----------------------------------------------
# -----------------------------------------------


def enable_button_linija(): # Aktīve pogu "Parādīt funkciju"
	# Aktive pogu "Linija", kura parāda kardioīdu
	poga3['state'] = ACTIVE


def disable_button_linija(): # Dizaktīve pogu "Parādīt funkciju"
	# Padara pogu "Linija" par neaktīvu, kura parāda kardioīdu
	poga3['state'] = DISABLED


def enable_button_plakne(): # Dizaktīve pogu "Parādīt funkciju"
	# Padara pogu "Plakne" par aktīvu, kura parāda plakni
	poga1['state'] = ACTIVE


def disable_button_plakne(): # Dizaktīve pogu "Parādīt funkciju"
	# # Padara pogu "Plakne" par neaktīvu, kura parāda kardioīdu
	poga1['state'] = DISABLED


def notirit():
	# Kanvas satura dzēšanai un dizaktivē pogu "Līnija"
	kanva.delete("all")
	disable_button_linija()


def is_real_number_in_entry(event):
	# Parbauda vai e1 entry logā ir ierakstīts reāls skaitlis
	# Padara tā, ka poga "Plakne" ir aktīva tikai tad, ja entry logā ir ierakstīts reāls skaitlis
	# Padara tā, ka poga "Līnija" ir aktīva tikai tad, ja tika nospiests uz pogu "Plakne"
	# Tas ir izdārīts, lai nevarētu uzzīmēt līnju, bez uzzimētas plaknes
	# event - simbolu ierakstīšana entry logā
	disable_button_plakne()
	disable_button_linija()
	kanva.delete("all")
	try:
		float(e1.get()) # Pārbaude no e1 ņemsim simbolu virkni un pārbaudīsim vai to var pārveidot float
	except:
		disable_button_plakne()
		disable_button_linija()
		kanva.delete("all")

	else:
		if float(e1.get()) > 0:
			enable_button_plakne()
		else:
			disable_button_plakne()
			disable_button_linija()
			kanva.delete("all")


def paradit():
	# Koordinātu plaknes uzzīmēšana, kura pielāgojas atkarība no a (Lai tāda veidā parādīt kardioīda izmēru).
	enable_button_linija()
	a = float(e1.get())
	kanva.create_line(150, 350, 850, 350, fill="gray")
	kanva.create_line(845, 345, 850, 350, fill="gray")
	kanva.create_line(845, 355, 850, 350, fill="gray")
	kanva.create_text(845, 330, text="X", anchor="nw", font=("Helvetica", 10), fill="gray")
	kanva.create_line(500, 0, 500, 700, fill="gray")
	kanva.create_line(505, 5, 500, 0, fill="gray")
	kanva.create_line(495, 5, 500, 0, fill="gray")
	kanva.create_text(505, 0, text="Y", anchor="nw", font=("Helvetica", 10), fill="gray")

	for i in range(175, 826, 25):
		kanva.create_line(i, 347, i, 353, fill="gray")
	#kanva.create_text(175, 330, text = str(-3*a), anchor = "nw", font = ("Helvetica",10), fill = "gray")
	#kanva.create_text(591, 330, text = str(a), anchor = "nw", font=("Helvetica", 10), fill = "gray")

	for i in range(25, 676, 25):
		kanva.create_line(497, i, 503, i)
	#kanva.create_text(505, 603, text = str(-2.5*a), anchor = "nw", font = ("Helvetica", 10), fill = "gray")
	#kanva.create_text(505, 80, text = str(2.5*a), anchor = "nw", font = ("Helvetica", 10), fill = "gray")

	for i in range(-13, 0): # minusiem uz X
		kanva.create_text(490 + i * 25, 330, text=str(i * a / (4)), anchor="nw", fill="gray")

	for i in range(1, 14): # plusiem uz X
		kanva.create_text(496 + i * 25, 330, text=str(i * a / (4)), anchor="nw", fill="gray")

	for i in range(-13, 0): # minusiem uz Y
		kanva.create_text(505, 341 - i * 25, text=str(i * a / (4)), anchor="nw", fill="gray")

	for i in range(1, 14): # minusiem uz X
		kanva.create_text(505, 341 - i * 25, text=str(i * a / (4)), anchor="nw", fill="gray")


def polari():
	# Līnijas uzzīmēšana

	x0 = 500
	y0 = 350
	a = float(e1.get())

	lenght = a
	b = 4
	a = b

	b = 2 * x0 + a / 25
	x1 = x0 + a / 25
	y1 = y0

	# Līnija
	for i in range(1, 3600, 1):

		f = i / 1800 * math.pi
		x = a * (2 * math.cos(f) - math.cos(2 * f))

		y = a * (2 * math.sin(f) - math.sin(2 * f))
		y2 = -y * 25 + y0
		x2 = x * 25 + x0

		kanva.create_line(x1, y1, x2, y2)
		x1 = x2
		y1 = y2

# -----------------------------------------------
# -----------------------------------------------


def bubblesort(elements):
	swapped = False
	for n in range(len(elements) - 1, 0, -1):
		for i in range(n):
			if elements[i] > elements[i + 1]:
				swapped = True
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
		if not swapped:
			return
# a = list(map(int, input('введите 4 числа ').split()))
# bubblesort(a)
# print(*a)

# -----------------------------


def solve_cubic(a, b, c, d): # ax^3 + bx^2 + cx + d = 0 # using NumPy
	return np.roots([a, b, c, d])


def solve_quartic(a, b, c, d, e): # ax^4 + bx^3 + cx^2 + dx + e = 0 # using NumPy
	return np.roots([a, b, c, d, e])


def solve_quintic(a, b, c, d, e, f): # ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0 # using NumPy
	return np.roots([a, b, c, d, e, f])


def solve_sextic(a, b, c, d, e, f, g): # ax^6 + bx^5 + cx^4 + dx^3 + ex^2 + fx + g = 0 # using NumPy
	return np.roots([a, b, c, d, e, f, g])


def solve_any_polynomial(polynomial): # [4,2,3,5,6] 4x^4 + 2x^3 + 3x^2 + 5x + 6 = 0
	return np.roots(polynomial)   # [1,2,3]     1x^2 + 2x + 3 = 0


def perebor_chisel(a, b): # [a,b] в каком интервале перебираем
	for i in range(a, b + 1, 1):
		for j in range(a, b + 1, 1): # шаг в 1 (можно изменить
			for k in range(a, b + 1, 1):
				if i * i == j * j + k * k: # то выражение какое перебираем # a^2 + b^2 = c^2
					print(str(j) + " " + str(k) + " " + str(i))


''' программа перебора квадратных a^2 + b^2 = c^2
for i in range(1,101,1):
    for j in range(1,101,1):
        for k in range(1,101,1):
            if i*i == j*j + k*k:
                print(str(j) + " " + str(k) + " " + str(i))
'''


def a_reizinājums_ar_b(a, b):
	return a * b


def a_dalīts_ar_b(a, b):
	return a / b


def horoskopi_gadi(g):
	g1 = g % 10

	match g1:
		case 0 | 1:
			zime = "baltais metāla "
		case 2 | 3:
			zime = "zilais ūdens "
		case 4 | 5:
			zime = "zaļais koka "
		case 6 | 7:
			zime = "sarkanais uguns "
		case 8 | 9:
			zime = "dzeltenais zemes "

	g2 = g % 12

	match g2:
		case 0:
			zime += "pērtiķa "
		case 1:
			zime += "gaiļa "
		case 2:
			zime += "suņa "
		case 3:
			zime += "cūkas "
		case 4:
			zime += "žurkas "
		case 5:
			zime += "vērša "
		case 6:
			zime += "tīģera "
		case 7:
			zime += "truša "
		case 8:
			zime += "pūķa "
		case 9:
			zime += "cūskas "
		case 10:
			zime += "zirga "
		case 11:
			zime += "kazas "
	return str(g) + ". gads ir " + zime + "gads"


def until_0_ievade():
	s = 0
	x = 1
	while x != 0:
		x = float(input("ievadi skaitli ===> "))
		s = s + x
	print(str(s)) # return str(s)


def spele_ar_datoru():
	pass


'''
def rekursija_fibonaci_serija(n):
        if n <= 1:
                return n
        else:
                return(rekursija_fibonaci_serija(n - 1) + rekursija_fibonaci_serija(n - 2))


n_terms = int(input("n ==> "))

for i in range(n_terms):
        print(rekursija_fibonaci_serija(i))
'''


def akkerman_rekusija_funkcija(m, n):
	if m == 0:
		return n + 1

	elif m > 0 and n == 0:
		return akkerman(m - 1, 1)

	elif m > 0 and n > 0:
		return akkerman(m - 1, akkerman(m, n - 1))


def otradi_teksta_apgriesana(sv):
	if len(sv) == 0:
		return sv
	else:
		return otradi_teksta_apgriesana(sv[1:]) + sv[0]


"""
def print_numbers_rekursija(n):
        if n == 1:
                print(1)
        else:
                print_numbers_rekursija(n - 1)
                print(n)


n = int(input("Ievadiet naturālo skaitli ==> "))
print_numbers_rekursija(n)
"""


'''
def print_numbers_augosa_seciba(a, b):
        if a == b:
                print(a)
        elif a < b:
                print(a)
                print_numbers_augosa_seciba(a + 1, b)
        else:
                print(a)
                print_numbers_augosa_seciba(a - 1, b)


a = int(input("Ievadiet skaitli A: "))
b = int(input("Ievadiet skaitli B: "))

print_numbers(a, b)
'''

'''
#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two_rekursija(n):
        if n == 1:
                return True
        elif n % 2 != 0 or n == 0:
                return False
        else:
                return is_power_of_two_rekursija(n // 2)


n = int(input("Введите натуральное число: "))

if is_power_of_two(n):
        print("YES")
else:
        print("NO")
'''


'''
# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
# используйте рекурсию
def digit_sum_rekursija(n):
        if n < 10:
                return n
        else:
                return n % 10 + digit_sum_rekursija(n // 10)


n = int(input("Введите натуральное число: "))
print("Сумма цифр числа", n, "равна", digit_sum_rekursija(n))
'''

"""
def reverse_digit_rekursija(n):
        if n < 10:
                print(n)
        else:
                print(n % 10, end=" ")
                reverse_digit_rekursija(n // 10)


n = int(input("Введите натуральное число: "))
reverse_digit_rekursija(n)
"""

'''
def skaitla_cipari_no_kreisas_puses_uz_labo(n):
        if n < 10:
                print(n)
        else:
                skaitla_cipari_no_kreisas_puses_uz_labo(n // 10)
                print(n % 10)

n = int(input("Введите натуральное число: "))
skaitla_cipari_no_kreisas_puses_uz_labo(n)
'''

"""
def prime_factors_razlozit(n, d=2):
        if n < 2:
                return
        if d > math.isqrt(n):
                print(n)
                return
        if n % d == 0:
                print(d, end=" ")
                prime_factors_razlozit(n // d, d)
        else:
                prime_factors_razlozit(n, d+1)

n = int(input("Введите натуральное число: "))
prime_factors_razlozit(n)
"""


def is_palindrome_rekursija(word):
	if len(word) <= 1:
		return True
	elif word[0] != word[-1]:
		return False
	else:
		return is_palindrome_rekursija(word[1:-1])


#is_palindrome_rekursija("ok")


def my_gcd_rekursija(a, b):
	if b == 0:
		return a
	return my_gcd_rekursija(b, a % b)


def pakape_rekursija_fast(a, n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return pakape_rekursija_fast(a * a, n / 2)
	else:
		return a * pakape_rekursija_fast(a, n - 1)


#print(pakape_rekursija_fast(5, 3))

def Hanoi(n, A, C, B):
	if (n != 0):
		Hanoi(n - 1, A, B, C)
		print('Move the plate from', A, 'to', C)
		Hanoi(n - 1, B, C, A)


def otradi_ar_izsaukuma_zimi():
	sv = input("Ievadi vārdu, ja beigt - ! ==>")
	if sv != "!":
		otradi_ar_izsaukuma_zimi()
	print(sv)


def binari2(a):
	if a == 1:
		return "1"
	else:
		return binari2(a // 2) + str(a % 2)


def list_of_primes(a, b):
	nums = range(a, b)

	return list(filter(is_prime, nums))


def kvadratsakne_ar_precizitati(x, pr):
	x1 = x
	x2 = x / 2
	while abs(x1 - x2) > pr:
		x1 = x2
		x2 = (x1 + x / x1) / 2
	return x2


'''
# mas - masivs
import numpy

mas = numpy.arange(30)
mas[0] = 1
for i in range(1, 30):
        mas[i] = mas[i-1] + mas[i//2]
print(mas)
'''


'''
mas = [1 ,]
for i in range(1,30):
        mas.append(mas[i-1] + mas[i//2])
print(mas)
'''

'''
def balts(n):
        if n <= 2:
                return 1
        else:
                return balts(n - 1) + melns(n - 1)
def melns(n):
        if n <= 1:
                return 0
        else:
                return balts(n - 1)
x = int(input("Ievadi ===>"))
print("Baltie -", balts(x), "Melnie - ", melns(x))
'''

'''
# mkd 28.02.2023 3 kontroldarbs
def mkd28_02_2023(n):
        if n == 0:
                return 1
        else:
                return mkd28_02_2023(n - 1) + mkd28_02_2023(n // 2)


simbolu_virkne = "1"
for i in range(0, 30):
        simbolu_virkne += " " + str(mkd28_02_2023(i))
        #print(str(mkd28_02_2023(i)))
print(simbolu_virkne)
'''

def izveidot_masivu_ar_garumu(n):
	# Izveido masīvu ar noradīto garumu n
	# n - naturāls skaitlis
	a = numpy.arange(n)
	for i in range(n):
		a[i] = int(input("Ievadiet " + str(i) + ".elementu ===> "))
	return a

def izvade(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam
	# x - masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return s


def videjais_aritmetiskais(x):
	# Aprēķina masīva vidējo aritmētisko
	# x - masīvs
	n = len(x)
	t = 0
	for i in range(0, n):
		t = t + x[i]

	return t / n


def videjais_kvadratiskais(x):
	# Aprēķina masīva videjo kvadrātisko
	# x - masīvs
	n = len(x)
	t = 0
	for i in range(0, n):
		t = t + x[i] * x[i]

	return math.sqrt(t / n)


def videjais_harmoniskais(x):
	# Aprēķina masīva videjo harmonisko
	# x - masīvs
	n = len(x)
	t = 0

	for i in range(0, n):
		t = t + 1 / x[i]

	return n / t

def videjais_harmoniskais_parbaude(x):
	# Aprēķina masīva videjo harmonisko
	# x - masīvs
	n = len(x)
	t = 0

	for i in range(0, n):
		if x[i] == 0:
			return "Kļūda! Dalīšana ar 0"
		else:
			t = t + 1 / x[i]

	return n / t


def videjais_geometriskais(x):
	# Aprēķina masīva videjo ģeomētrisko
	# x - masīvs
	n = len(x)
	s = 1

	for i in x:
		s = s * i

	return math.pow(s, (1 / n))

def videjais_geometriskais_ar_parbaudi(x):
	# Aprēķina masīva videjo ģeomētrisko
	# x - masīvs
	n = len(x)
	s = 1

	for i in x:
		s = s * i

	if n % 2 == 0:  # Pārbauda vai n-sakne ir pāra skaitlis
		if s >= 0:  # Ja n-sakne pāra skaitlis, tad pārbaudam vai nav negatīvs, ja ir tad nevaram aprēķināt
			k = math.pow(s, (1 / n))  # ja ir pozitīvs vai 0, tad viss ir labi, varam aprēķināt pāra-sakni no pozitīvas vērtības
		else:
			k = "nevar aprēķināt reālos skaitļos"  # ja ir negatīvs un n-sakne ir pāra skaitlis, tad nevaram to aprēķināt reālos skaitlos
	else:
		k = numpy.sign(s) * (numpy.abs(s)) ** (1 / n)  # ja n-sakne ir nepāra skaitlis, tad aprēķināt to šādi (parasta pow(a,b) funkcija nedarbojas ar tādiem skaitliem)

	return k

def videjas_linearas_novirzes_vertiba(x):
	# Aprēķina masīva vidējās absolūtās jeb vidējās lineārās novirzes vērtību
	# x - masīvs
	n = len(x)
	t = 0
	k = 0
	for i in range(0, n):
		t = t + x[i]

	c = t / n

	for i in range(0, n):
		k = k + abs(x[i] - c)

	return k / n


def standartnovirze(x):
	# Aprēķina masīva standartnovirzi
	# x - masīvs
	n = len(x)
	t = 0
	k = 0
	for i in range(0, n):
		t = t + x[i]

	c = t / n

	for i in range(0, n):
		k = k + (x[i] - c) * (x[i] - c)

	return math.sqrt(k / n)

def videja_sversta_vertiba(x, y):
	# Aprēķina masīvu vidējo svērsto vērtību
	# x - pirmais masīvs
	# y - otrais masīvs
	n = len(x)
	t = 0
	z = 0

	for i in range(0, n):
		t = t + x[i] * y[i]

	for i in range(0, n):
		z = z + y[i]

	return t / z

def naivais_dilstosa(a):
	# Naivā kārtošanas metode
	# Sakarto masīva elementus dilstoša (neaugoša) secība un
	# izvada paveikto salīdzīnašanas skaits, lai sakārtot masīvu. (izmanto naivo kārtošanas metode)
	# a - masīvs
	skaititajs = 0
	n = len(a)
	for j in range(n - 1):
		min1 = a[j]
		imin = j
		for i in range(j + 1, n):
			if min1 < a[i]:
				#skaititajs = skaititajs + 1  # skaititājs
				min1 = a[i]
				imin = i
		a[imin] = a[j]
		a[j] = min1

	#print(skaititajs)  # Izvada paveikto salīdzīnašanas skaits, lai sakārtot masīvu

def burbulis(a):
	n = len(a)
	for i in range(n - 1, 0, -1):
		for j in range(0, i):
			if a[j] > a[j + 1]:
				x = a[j]
				a[j] = a[j + 1]
				a[j + 1] = x


def burbulis_uzlabotais(a):
	# Burbulis (uzlabotais) kartošanas metode
	# Sakarto masīva elementus dilstoša (neaugoša) secība un
	# izvada paveikto salīdzīnašanas skaits, lai sakārtot masīvu. Izmanto burbuļa metodi (uzlaboto)
	# a - masīvs
	skaititajs = 0
	n = len(a)
	i = n - 1
	paz = True
	while paz:
		paz = False
		for j in range(0, i):
			if a[j] < a[j + 1]:
				#skaititajs = skaititajs + 1
				paz = True
				x = a[j]
				a[j] = a[j + 1]
				a[j + 1] = x
		i = i - 1
	#print(skaititajs)


def izveidot_masivu_ar_garumu_un_parbaude(n):
	# Izveido masīvu ar noradīto garumu n
	# Pārbauda vai tiek ievadīti reāli skaitli elementiem
	# n - naturāls skaitlis
	a = numpy.arange(n)
	for i in range(n):
		b = input("Ievadiet " + str(i) + ".elementu ===> ")
		try:
			b = float(x)
		except:
			b = input("Kļūda! Mēģini vēlreiz! Ievadiet " + str(i) + ".elementu ===> ")
		else:
			b = int(b)

		a[i] = b
	return a

def pirmskaitli(n):
	p = [2, 3]
	k = 5
	while k <= n:
		i = 0
		s = round(math.sqrt(k))
		while (k % p[i]) != 0:
			i = i + 1
			if p[i] > s:
				p.append(k)
				break
		k = k + 2
	return p
'''
print("Pirmskaitļi ir", pirmskaitli(500))
a = numpy.array(pirmskaitli(500))
print("Pirmskaitļi ir", a
'''

def determinant_2x2(a):
	# a - divdimensiju masīvs (2x2 matrica)
	return a[0][0] * a[1][1] - a[0][1] * a[1][0]

def determinant_3x3(a):
	# a - trīsdimensiju masīvs (3x3 matrica)
	return a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] - a[0][2] * a[1][1] * a[2][0] - a[0][0] * a[1][2] * a[2][1] - a[0][1] * a[1][0] * a[2][2]


def is_natural_number_from_0_to_9_velreiz(i):
	# Pārbauda vai tiek ievadīts naturāls skaitlis no 0 līdz 9. Ja nav, tad paprasa ievadīt to velreiz. Bezgalīgi daudz ievades.
	# i - tiek izmantots kosmetiski, lai pielāgotu programmas ziņojumu katrai ievadei. str(i) + ".ciparu => "
	x = input("Ievadiet " + str(i) + ".ciparu => ")
	while True:
		try:
			x = int(x)
		except:
			x = input("Kļūda! Cipars ir no 0 līdz 9\nIevadiet " + str(i) + ".ciparu => ")
		else:
			x = int(x)
			if x > 9 or x < 0:
				x = input("Kļūda! Cipars ir no 0 līdz 9\nIevadiet " + str(i) + ".ciparu => ")
			else:
				return int(x)


def ievade(n):
	# Izsauc is_natural_number_from_0_to_9_velreiz(i) un atgriež lietotāja ievadīto masīvu
	# n - naturāls skaitlis, kurš atbild par masīva garumu
	a = numpy.arange(n)
	for i in range(n):
		a[i] = is_natural_number_from_0_to_9_velreiz(i)  # int(input("Ievadiet " + str(i) + ".ciparu => "))

	return a

def long_sqrt(num):
	num_str = str(num)
	len_num = len(num_str)
	if len_num % 2 == 1:
		num_str = '0' + num_str
		len_num += 1
	result = ''
	remainder = 0
	dividend = int(num_str[:2])
	root = int(dividend**0.5)
	result += str(root)
	remainder = dividend - root**2
	for i in range(2, len_num, 2):
		dividend = remainder * 100 + int(num_str[i:i + 2])
		digit = 0
		temp = root * 20
		while (temp + digit) * digit <= dividend:
			digit += 1
		digit -= 1
		result += str(digit)
		remainder = dividend - (temp + digit) * digit
		root = root * 10 + digit
	return int(result)


def long_sqrt(num):
	# Funkciju, kas kā ievadi izmanto nenegatīvu veselu skaitli un atgriež tā veselā skaitļa kvadrātsakni
	# num - int, skaitlis, no kura vajag atrāst kvadrātsakni
	# Atgriež sqrt(num) kā int

	# Konvertējat ievadīto veselo nenegatīvo skaitli par simbolu virkni un saglabājam to mainīgajā
	num_str = str(num)
	# Saglabājam ievadītā veselā skaitļa simbolu virknes garumu
	len_num = len(num_str)

	# Ja ievadītā veselā skaitļa simbolu virknes garums ir nepāra skaitlis, tad pievienojam sākuma nulli, lai padarītu to par pāru simbolu virkni (garums ir pāra skaitlis)
	if len_num % 2 == 1:
		num_str = '0' + num_str  # Ievadītā veselā skaitļa simbolu virknei sākumam pievienojam '0'
		len_num += 1  # Palielinām ievadītā veselā skaitļa simbolu virknes garumu par 1

	result = ''  # Tukša simbolu virkne, lai saglabātu kvadrātsaknes aprēķina rezultātu
	remainder = 0

	# Sadalam ievadītā veselā skaitļa virknes pirmus divus ciparus [:2]
	dividend = int(num_str[:2])

	j = 1                     # Atrodam pirmo "tuvinājumu"
	while j * j <= dividend:  # Tas ir lai atrāstu pirmu ciparu kvadrātsaknei
		j = j + 1             # Var arī atrāst tā:
	root = j - 1              # root = int(dividend**0.5) (lai nebūtu cikls)

	result = result + str(root)
	remainder = dividend - root * root  # Atlikums
	# Cikls pār katru otro "ciparu pāri"
	for i in range(2, len_num, 2):
		# Reizinām atlikumu ar 100 un pievienojiet nākamos divus veselā skaitļa ciparus, lai iegūtu dividendi
		dividend = remainder * 100 + int(num_str[i:i + 2])
		digit = 0
		temp = root * 20
		while (temp + digit) * digit <= dividend:
			digit += 1
		digit -= 1
		result += str(digit)  # Rezultātam pievienojam iegūto ciparu
		remainder = dividend - (temp + digit) * digit
		root = root * 10 + digit

	return int(result)


def izvade(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam
	# x - viendimensijas masīvs

	try:
		n = len(x)
		s = str(x[0])
		for i in range(1, n):
			s = s + ", " + str(x[i])
		print(s)
	except IndexError:
		print("Nav pirmskaitļu šajā intervālā.")  # Ja parādās index error, tad tas nozīme, ka šajā intervālā nav pirmskaitļu.
	except:
		print("Kļūda!")  # Citām kļūdam


def pirmskaitlu_masivs(n, drosibas_koeficients):
	# Atgriež tuple ar pirmskaitļu masīvu līdz skaitlim n bez liekām 0 un ar nodzēsto nulles skaitu. (Ja ir lieki elementi, tad funkcija to nodzes)
	# n - naturāls skaitlis (int), līdz kurām meklēsīm pirmskaitļus
	# drosibas_koeficients - drošības koeficients. Tiek reizināts ar n/log(n) un tiek izmantots masīva izmēra definēšanai.
	# Parasti, jo lielāks, jo vairāk liekas nulles būs. Pēc noklusējuma labāk, lai tās būtu aptuvēni 1.2

	if n <= 1:  # Funkcija nedarbotos jā ievadīs 0, 1 vai 2, tāpēc tas tiek atsevišķi definēts.
		return numpy.array([])
	if n == 2:
		return numpy.array([2])

	# drosibas_koeficients = 1.2  # izmantots, lai palidzētu nodefinētu masīva izmēru (size). Masīva izmēra definēšanai tiek izmantota formula n/log(n) https://en.wikipedia.org/wiki/Prime_number_theorem un https://en.wikipedia.org/wiki/Prime-counting_function
	size = math.ceil((n / math.log(n)) * drosibas_koeficients)  # aprēķina masīva garumu, izmantojot formulu n/log(n) un reizinot ar drošības koeficientu (bez viņa nevienmēr pietiks vietas)
	p = numpy.zeros(size, dtype=numpy.int32)  # izveido masīvu ar 0 vērtībām tādu garumu, kuru aprēķinaja ar formulu (n/log(n))*drosibas_koeficientu
	p[0] = 2  # pirmais pirmskaitlis
	p[1] = 3  # otrais pirmskaitlis
	j = 2
	k = 5
	try:
		while k <= n:
			i = 0
			s = round(math.sqrt(k))
			while (k % p[i]) != 0:
				i = i + 1
				if p[i] > s:
					p[j] = k
					j = j + 1
					break
			k = k + 2
		deleted_zeros_count = len(p) - len(p[:j])
		return (p[:j], deleted_zeros_count)  # [:j], lai izvadītu bez nullem
	except:
		print("Palieliniet drošības koeficientu! Nepietika vietas masīva aizpildīšanai.")


def izvade_bez_komatiem_kopigi(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam kopīgi bez komatiem (izmanto lai izvadītu masīvu kā vienu str skaitli)
	# x - viendimensijas masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + "" + str(x[i])
	print(s[::-1])

def transponeta(a):
	n = a.shape[0] 
	m = a.shape[1] 
	b = numpy.empty((m,n),"O")

	for i in range(m):
		for j in range(n):
			b[i,j]=a[j,i]
	return b


def parveide_sv_to_mas(sv, m):
	# Transformē simbolu virkni par masīvu ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	# sv - simbolu virkne, kura sastāv no cipariem
	# m - garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	n = len(sv)
	a = numpy.arange(m)
	for i in range(n):
		a[i] = int(sv[-i - 1])
	for i in range(n, m):
		a[i] = 0
	return a


def parveide_mas_to_sv(a):
	# Transformē masīvu par simbolu virkni. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
	# a - viendimensijas masīvs
	n = len(a)
	sv = ""
	for i in range(n):
		sv = str(a[i]) + sv

	try:  # try/except gadījumam ja 0 + 0
		while sv[0] == "0":
			sv = sv[1:]
		return sv

	except IndexError:  # Tas ir nepieciešams gadījumam ja lietotājs ievadīs 0 + 0 = 0.
		return "0"  # bez šim rindām būtu kļūda, kad 0 + 0


def saskaitisana(a, b):
	# Saskaita masīvu a un b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) saskaitīšanu
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	a = a[::-1]
	b = b[::-1]
	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2
	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(n + 1, dtype=numpy.int_)

	s = 0
	for i in range(n):
		s = s + m1[i] + m2[i]
		m3[i] = s % 10
		s = s // 10
	m3[n] = s

	return parveide_mas_to_sv(m3)

def parveide_mas_to_sv_reverse(a):
	# Transformē masīvu simbolu virknē un apgriež to
	# a - viendimensijas masīvs
	n = len(a)
	sv = ""
	for i in range(n):
		sv = str(a[i]) + sv
	return sv[::-1]


def remove_front_zeros(s):
	# Atgriež simbolu virkni bez nullem priekšā
	# s - simbolu virkne, kura sastav no cipariem, potenciāli ar nullēm priekšā
	i = 0
	while i < len(s) - 1 and s[i] == '0':
		i += 1
	s = s[i:]
	return s


def atnemsana(a, b):
	# Atņem masīvu a no b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) atņemšanai. Atgriež simbolu virkni bez nullem priekšā
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	if str(a) == str(b):
		return "0"

	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2
	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(n, dtype=numpy.int_)

	for i in range(-1, -n1, -1):
		if m1[i] < m2[i]:
			m1[i - 1] = m1[i - 1] - 1
			m1[i] = m1[i] + 10

	for i in range(n):
		m3[i] = m1[i] - m2[i]

	a = parveide_mas_to_sv(m3)
	a = a[::-1]
	a = remove_front_zeros(a)
	return a


def is_natural_or_zero_long(s):
	# Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
	# Atgriež True, ja virkne reprezentē naturālo skaitli.
	# Atgriež False, ja nereprezentē naturālo skaitli.
	# s - pārbaudāma simbolu virkne

	# Noņema no virknes visas sākuma vai beigu atstarpes
	s = s.strip()

	# Pārbauda, vai virkne ir tukša
	if len(s) == 0:
		return False

	# Iet cikliski cauri katrām simbolam simbolu virknē (string'ā)
	for c in s:
		# Ja kāda rakstzīme nav cipars, virkne neatspoguļo naturālu skaitli. return False
		if not c.isdigit():
			return False

	# Virkne atspoguļo naturālu skaitli, ja ietu cauri ciklas netika pamanīts not .isdigit()
	return True


def is_a_bigger_b(a, b):
	# Vai masīvs a ir lielāks vai vienāds nekā masīvs b, ja jā, tad return True. Ja nē, tad return False
	# a - pirmais viendimensijas masīvs
	# b - otrais viendimensijas masīvs
	a = parveide_mas_to_sv_reverse(a)
	b = parveide_mas_to_sv_reverse(b)
	if int(a) < int(b):
		return False
	else:
		return True

def reizinasana(a, b):
	# Sareizina masīvu a ar b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) reizināšanai
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs

	a = a[::-1]
	b = b[::-1]
	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2

	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(2 * n, dtype=numpy.int_)
	s = 0
	for j in range(2 * n - 1):
		for i in range(n):
			if (0 <= j - i) and (j - i <= n - 1):
				s = s + m1[i] * m2[j - i]
		m3[j] = s % 10
		s = s // 10
	m3[n * 2 - 1] = s

	return parveide_mas_to_sv(m3)

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


def izvade_matrica_int(a):
	# Atgriež divdimensiju masīvu (matricu), tabulas veidā, str formāta, kur katra rinda ir atdalīta ar jauno rindkopu
	# a - divdimensijas masīvs (matrica)
	n = a.shape[0]  # "x axis" masīva izmēri
	m = a.shape[1]  # "y axis" masīva izmēri

	s = ""
	for i in range(n):
		for j in range(m):
			s = s + "{:8.2f}".format(int(a[i, j]))
		s = s + "\n"
	return s


def matricas_izvade_4_cipari(m):
	# Izvada divdimensijas masīvu tabulas veidā tā, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
	# Tiek nodrošināta matricas elementu izvade tabulas veidā, pieņemot, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
	# Atgriež matricas elementu izvade tabulas veidā
	# m - divdimensijas masīvs
	nm = numpy.shape(m)
	sv = ""
	for x in range(nm[0]):
		for y in range(nm[1]):
			for i in range(5 - len(str(m[x, y]))):
				sv = sv + " "
			sv = sv + str(m[x, y])
		sv = sv + "\n"
	nn = len(sv)
	return sv[:nn - 1]


def max_value_in_2_dimensional_array_and_its_coords(a):
	# Atgriež tuple (max_value, coords) ar divdimensijas masīva (matricas) maksimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
	# Atgriež maksimālo vērtību un kur tā vērtība atrodas pēc koordinātam
	# a - divdimensijas masīvs
	max_value = a[0][0]
	coords = [0, 0]

	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] > max_value:
				max_value = a[i][j]
				coords = [i, j]

	return (max_value, coords)


def min_value_in_2_dimensional_array_and_its_coords(a):
	# Atgriež kortežu (tuple) (min_value, coords) ar divdimensijas masīva (matricas) minimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
	# Atgriež minimālo vērtību un kur tā vērtība atrodas pēc koordinātam
	# a - divdimensijas masīvs
	min_value = a[0][0]
	coords = [0, 0]
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] < min_value:
				min_value = a[i][j]
				coords = [i, j]

	return (min_value, coords)


def izvade_matrica_int(a):
	# Atgriež divdimensiju masīvu (matricu), tabulas veidā, str formāta, kur katra rinda ir atdalīta ar jauno rindkopu
	# a - divdimensijas masīvs (matrica)
	n = a.shape[0]  # "x axis" masīva izmēri
	m = a.shape[1]  # "y axis" masīva izmēri

	s = ""
	for i in range(n):
		for j in range(m):
			s = s + "{:8.2f}".format(int(a[i, j]))
			# s = s + "   " + str(int(a[i,j])) #"{:8.2f}".format(a[i,j], dtype=int)
		s = s + "\n"
	return s


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


def check_fake_matrix_multiplication(n1, m1, n2, m2):
	# Pārbauda vai divas matricas (divdimensiju masīvi) ir ar vienādu izmēru. Pārbauda vai sakrīt 1.matricas rindas skaits ar 2.matricas rindas skaitu.
	# un pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas kolonnu skaitu. Ja abas prasības izpildās, tad return True. Ja kaut viena neizpildās, tad return False.
	# Tiek izmantota, lai pārbaudītu vai var sareizināt matricas atbilstošus elementus vai nē.
	# n1 - 1.matricas rindu skaits
	# m1 - 1.matricas kolonnu skaits
	# n2 - 2.matricas rindu skaits
	# m2 - 2.matricas kolonnu skaits
	if n1 == n2 and m1 == m2:
		return True
	else:
		return False


def check_matrix_multiplication(n1, m1, n2, m2):
	# Pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas rindu skaitu. Ja sakrīt, tad return True. Ja nē, tad return False.
	# Tiek izmantots, lai pārbaudītu vai ir iespējams sareizināt divas matricas.
	# n1 - 1.matricas rindu skaits (tā ne uz ko neietekme)
	# m1 - 1.matricas kolonnu skaits
	# n2 - 2.matricas rindu skaits
	# m2 - 2.matricas kolonnu skaits (tā ne uz ko neietekme)
	if m1 == n2:
		return True
	else:
		return False


def matrix_multiplication_integer(a, b):
	# Sareizina divu divdimensijas masīvus (divas matricas) a ar b.
	# Atgriež divdimensiju masīvu, vai ja nevar sareizināt atgriež "Kļūda"
	# a - divdimensijas masīvs
	# b - divdimensijas masīvs
	n1 = a.shape[0]
	m1 = a.shape[1]
	n2 = b.shape[0]
	m2 = b.shape[1]
	if m1 == n2:
		c = numpy.zeros((n1, m2), numpy.int_)
		for i in range(n1):
			for j in range(m2):
				for k in range(m1):
					c[i, j] = c[i, j] + a[i, k] * b[k, j]
		return c
	else:
		return "Kļūda"


def fake_matrix_multiplication(a, b):
	# Sareizina divas matricas atbilstošus elementus un atgriež atbilstošu divdimensiju masīvu
	# a - divdimensiju masīvs
	# b - divdimensiju masīvs
	c = numpy.empty((n1, m1), dtype=int)

	for i in range(n1):
		for j in range(m2):
			c[i, j] = a[i][j] * b[i][j]

	return c

def dalit_lielus_skaitlus(s, n):
	# Funkcija atgriež tuple (dalījums, atlikums) no s / n. Dalījums ir int un atlikums ir int.
	# Jāizmanto lielo skaitļu dalīšanai.
	# Dalā pēc "cipariem".
	# s - str, dalāmais
	# n - str, dalītājs
	n = int(n)
	galva = 0
	atlikums = 0
	dalijums_sv = ""

	for i in range(len(s)):

		cipars = int(s[i])
		tmp = cipars + atlikums * galva
		dalijums_sv = dalijums_sv + str(tmp // n)

		if tmp % n == 0:
			galva = 0
			atlikums = 0
		else:
			atlikums = tmp % n
			galva = 10

	dalijums = nodzest_liekas_nulles(dalijums_sv)
	dalijums = int(dalijums)

	return (dalijums, atlikums)


def nodzest_liekas_nulles(s):
	# Nodzes liekas nulles sākumā
	# s - simbolu virkne
	for i in range(len(s)):
		if s[i] != '0':
			return s[i:]
	return '0'

def long_sqrt(skaitlis):
	# Funkciju, kas kā ievadi izmanto nenegatīvu veselu skaitli un atgriež tā veselā skaitļa kvadrātsakni
	# skaitlis - int, skaitlis, no kura vajag atrast kvadrātsakni
	# Atgriež sqrt(skaitlis) kā int

	# Konvertējat ievadīto veselo nenegatīvo skaitli par simbolu virkni un saglabājam to mainīgajā
	sk_sv = str(skaitlis)  # sk_sv - skaitlis_simbolu virkne
	# Saglabājam ievadītā veselā skaitļa simbolu virknes garumu
	len_sk = len(sk_sv)  # slen_skaitlis

	# Ja ievadītā veselā skaitļa simbolu virknes garums ir nepāra skaitlis, tad pievienojam sākuma nulli, lai padarītu to par pāru simbolu virkni (garums ir pāra skaitlis)
	if len_sk % 2 == 1:
		sk_sv = '0' + sk_sv  # Ievadītā veselā skaitļa simbolu virknei sākumam pievienojam '0'
		len_sk = len_sk + 1  # Palielinām ievadītā veselā skaitļa simbolu virknes garumu par 1

	result = ''  # Tukša simbolu virkne, lai saglabātu kvadrātsaknes aprēķina rezultātu
	atlikums = 0

	# Sadalām ievadītā veselā skaitļa virknes pirmos divus ciparus [:2]
	a = int(sk_sv[:2])

	j = 1              # Atrodam pirmo "tuvinājumu"
	while j * j <= a:  # Tas ir lai atrastu pirmo ciparu kvadrātsaknei
		j = j + 1      # Var arī atrast tā:
	sakne = j - 1      # sakne = int(a**0.5) (lai nebūtu cikls)

	result = result + str(sakne)
	atlikums = a - sakne * sakne  # Atlikums
	# Cikls pār katru otro "ciparu pāri"
	for i in range(2, len_sk, 2):  # Stabiņveidā atrodam nākamo un nākamo un ... un pēdējo ciparu
		# Reizinām atlikumu ar 100 un pievienojiet nākamos divus veselā skaitļa ciparus, lai iegūtu dividendi
		a = atlikums * 100 + int(sk_sv[i:i + 2])
		cipars = 0
		temp = sakne * 20
		while (temp + cipars) * cipars <= a:
			cipars += 1
		cipars -= 1
		result += str(cipars)  # Rezultātam pievienojam iegūto ciparu
		atlikums = a - (temp + cipars) * cipars
		sakne = sakne * 10 + cipars

	return int(result)

def apvieno(a, b):
	# Apvieno divus sakartotus masīvus a un b, un sakārto tos
	# Lineāra laiks o(n)
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	ga = len(a)
	gb = len(b)
	gc = ga + gb
	c = numpy.arange(gc)
	ia = 0
	ib = 0
	ic = 0
	while (ia < ga) and (ib < gb):
		if a[ia] < b[ib]:
			c[ic] = a[ia]
			ia = ia + 1
		else:
			c[ic] = b[ib]
			ib = ib + 1
		ic = ic + 1
	if ia < ga:
		for i in range(ia, ga):
			c[ic] = a[i]
			ic = ic + 1
	else:
		for i in range(ib, gb):
			c[ic] = b[i]
			ic = ic + 1
	return c

def reverse(masivs):
	# Pārkarto masīvā visus elementus pretēji
	# masivs - viendimensijas masīvs
	start_index = 0
	end_index = len(masivs) - 1
	while end_index > start_index:
		temp = masivs[start_index]
		masivs[start_index] = masivs[end_index]
		masivs[end_index] = temp
		start_index = start_index + 1
		end_index = end_index - 1

def to_vards(n):
	# Pārveido reālo skaitli no 0 līdz 9999 tā, ka tas ir izrūnāms latviešu valodā
	# n - reāls skaitlis no 0 līdz 9999
	lst_word = numpy.array(["desmit tūkstoši ", "deviņi tūkstoši ", "astoņi tūkstoši ", "septiņi tūkstoši ", "seši tūkstoši ", "pieci tūkstoši ", "četri tūkstoši ", "trīs tūkstoši ", "divi tūkstoši ", "tūkstošs ",
                            "deviņi simti ", "astoņi simti ", "septiņi simti ", "seši simti ", "pieci simti ", "četri simti ", "trīs simti ", "divi simti ", "simts ",
                            "deviņdesmit ", "astoņdesmit ", "septiņdesmit ", "sešdesmit ", "piecdesmit ", "četrdesmit ", "trīsdesmit ", "divdesmit ",
                            "deviņpadsmit ", "astoņpadsmit ", "septiņpadsmit ", "sešpadsmit ", "piecpadsmit ", "četrpadsmit ", "trīspadsmit ", "divpadsmit ", "vienpadsmit ", "desmit ",
                            "deviņi ", "astoņi ", "septiņi ", "seši ", "pieci ", "četri ", "trīs ", "divi ", "viens "])

	lst_numbers = numpy.array([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000,
                               900, 800, 700, 600, 500, 400, 300, 200, 100,
                               90, 80, 70, 60, 50, 40, 30, 20,
                               19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
                               9, 8, 7, 6, 5, 4, 3, 2, 1])

	sv = ""
	for i in range(46):
		while lst_numbers[i] <= n:
			sv = sv + lst_word[i]
			n = n - lst_numbers[i]

	if sv == "":
		return "nulle "
	else:
		return sv

def is_ascending(n):  # vai nedilstoša?
	# Pārbauda vai masīvs ir augošs (nedilstošs)
	# Ja masīvs ir nedilstošs (nav augošs), tad return True
	# Ja masīvs nav nedilstošs (nav augošs), tad return False
	# n - viendimensijas masīvs
	if len(n) == 1:
		return True

	for i in range(0, len(n)):
		if i < len(n) - 1 and n[i] > n[i + 1]:
			return False  # Nē, nav augoša, nav nedilstoša, nav konstanta (varētu būt augoša, vai nekāda)

	return True  # Jā, ir augoša (vai nedilstoša)


def is_descending(n):  # vai neaugoša?
	# Pārbauda vai masīvs ir dilstošs (neaugošs)
	# Ja masīvs ir neaugošs (nav dilstošs), tad return True
	# Ja masīvs nav neaugošs (nav dilstošs), tad return False
	# n - viendimensijas masīvs
	if len(n) == 1:
		return True

	for i in range(0, len(n)):
		if i < len(n) - 1 and n[i] < n[i + 1]:
			return False  # Nē, nav dilstoša, nav neaugoša, nav konstanta (varētu būt augoša, vai nekāda)

	return True  # Jā, ir dilstoša (vai neaugoša)

def atrais(a, sv, bv):  # sv = 0, bv = len(a)
	# Sakārto masīvu augoša secība
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] > a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			j = j + solis
		atrais(a, sv, i - 1)
		atrais(a, i + 1, bv)


def vards():
	# Ģenerē vārdus ar garumu no 3 līdz 8 (garums - uz labu laimi) un ģenerē to vārdu ar lieliem latiņu alfabēta burtiem
	# Atgriež vienu izveidotu vārdu
	r = random.randint(3, 8)
	v = ""
	for i in range(r):
		v += chr(random.randint(65, 90))  # ASCII 65;90
	return v


def masivs(length):
	# Aizpildā masīvu ar vārdiem atsaucoties uz "vards()". Atgriež aizpildīto masīvu.
	# length - viendimensijas masīva garums
	mas = numpy.empty(length, dtype=object)
	for j in range(length):
		mas[j] = vards()
	# print(mas)
	return mas


def meklet(a, b):
	# Sameklē a masīva b skaitļi (vai vārdu). Atgriež to vērtību, kur viņa atrodas pēc index. Ja nav tādas vērtības masīva, tad atgriež -1.
	# a - viendimensijas masīvs
	# b - to ko mēs meklējam (skaitlis vai vārds (str))
	l = 0
	r = len(a) - 1
	while (l <= r):
		i = (l + r) // 2
		if a[i] == b:
			break
		elif a[i] < b:
			l = i + 1
		else:
			r = i - 1
	if a[i] == b:
		return i
	else:
		return -1


def to_roman(n):
	# Pārveido veselo skaitli no 1 līdz 3899 no arābu pieraksta uz romiešu pierakstu
	# n - naturāls skaitlis no 1 līdz 3899
	romas = numpy.array(["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", 'I'])
	vertibas = numpy.array([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1])
	sv = ""
	for i in range(13):
		while vertibas[i] <= n:
			sv = sv + romas[i]
			n = n - vertibas[i]
	return sv

def to_vards(n):
	# Pārveido reālo skaitli no 0 līdz 9999 tā, ka tas ir izrūnāms latviešu valodā
	# n - reāls skaitlis no 0 līdz 9999
	lst_word = numpy.array(["desmit tūkstoši ", "deviņi tūkstoši ", "astoņi tūkstoši ", "septiņi tūkstoši ", "seši tūkstoši ", "pieci tūkstoši ", "četri tūkstoši ", "trīs tūkstoši ", "divi tūkstoši ", "tūkstošs ",
	                        "deviņi simti ", "astoņi simti ", "septiņi simti ", "seši simti ", "pieci simti ", "četri simti ", "trīs simti ", "divi simti ", "simts ",
	                        "deviņdesmit ", "astoņdesmit ", "septiņdesmit ", "sešdesmit ", "piecdesmit ", "četrdesmit ", "trīsdesmit ", "divdesmit ",
	                        "deviņpadsmit ", "astoņpadsmit ", "septiņpadsmit ", "sešpadsmit ", "piecpadsmit ", "četrpadsmit ", "trīspadsmit ", "divpadsmit ", "vienpadsmit ", "desmit ",
	                        "deviņi ", "astoņi ", "septiņi ", "seši ", "pieci ", "četri ", "trīs ", "divi ", "viens "])

	lst_numbers = numpy.array([10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000,
	                           900, 800, 700, 600, 500, 400, 300, 200, 100,
	                           90, 80, 70, 60, 50, 40, 30, 20,
	                           19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
	                           9, 8, 7, 6, 5, 4, 3, 2, 1])

	sv = ""
	for i in range(46):
		while lst_numbers[i] <= n:
			sv = sv + lst_word[i]
			n = n - lst_numbers[i]

	if sv == "":
		return "nulle "
	else:
		return sv


def check():
	# Bezgalīgi daudz ievades. Pārbauda vai skaitlis ir reāls pozitīvs un atrodas intervālā [0, 9999]
	x = input("Ievadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
	while True:
		try:
			x = float(x)
		except:
			x = input("Kļūda!\nIevadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
		else:
			if x < 0 or x > 9999:
				x = input("Kļūda! Skaitlis nepieder intervālam [0, 9999]\nIevadiet reālo pozitīvo skaitli no 0 līdz 9999 ===> ")
			else:
				return float(x)

def is_natural_and_interval(n):
	# Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
	# Ja ir naturāls skaitlis, tad True. Ja nav tad False.
	# n - simbolu virkne, kuru pārbauda.
	if (str(n).isdigit() and float(n) == int(n) and int(n) > 0):
		if (int(n) < 1 or int(n) > 3899):
			return False
		else:
			return True
	else:
		return False


def skaldi_un_valdi_dilstosa(a, sv, bv):
	# Sakarto masīvu dilstoša secība izmantojot "Skaldi un valdi" algoritmu un atgriež salīdzināšanas skaitu
	# ātrums - o(nlog(n))
	# a - viendimensijas masīvs
	# sv - sākumvērtība (parasti 0)
	# bv - beigu vērtība (parasti len(a))
	p = 0
	b = numpy.arange(len(a))
	if sv < bv:
		vv = (sv + bv) // 2
		p1 = skaldi_un_valdi_dilstosa(a, sv, vv)
		p2 = skaldi_un_valdi_dilstosa(a, vv + 1, bv)
		for i in range(sv, bv + 1):
			b[i] = a[i]
		i = sv
		j = vv + 1
		k = sv
		while (i <= vv) and (j <= bv):
			p += 1
			if b[i] > b[j]:
				a[k] = b[i]
				i = i + 1
			else:
				a[k] = b[j]
				j = j + 1
			k = k + 1
		if j > bv:
			while i <= vv:
				a[k] = b[i]
				i = i + 1
				k = k + 1
		p = p + p1 + p2
	return p

def sort_atspole_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota atspoles metode
	# a - viendimensijas masīvs
	n = len(a)
	count = 0
	for i in range(1, n):
		if a[i - 1] < a[i]:
			count += 1
			for j in range(i, 0, -1):
				if a[j - 1] < a[j]:
					count += 1
					x = a[j]
					a[j] = a[j - 1]
					a[j - 1] = x
				else:
					count += 1
					break
		else:
			count += 1

	return count


def sort_ievietosana_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
	# a - viendimensijas masīvs
	n = len(a)
	sk = 0
	for i in range(1, n):
		sk = sk + 1
		if a[i - 1] < a[i]:
			x = a[i]
			j = i
			sk = sk + 1
			while a[j - 1] < x:
				a[j] = a[j - 1]
				j = j - 1
				if j == 0:
					break
				sk = sk + 1
			a[j] = x

	return sk

def sort_ievietosana_augosa(a):
	# Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
	# a - viendimensijas masīvs	
	n = len(a)
	for i in range(1, n):
		if a[i - 1] > a[i]:
			x = a[i]
			j = i
			while a[j - 1] > x:
				a[j] = a[j - 1]
				j = j - 1
				if j == 0:
					break
			a[j] = x
	return a

def sort_sella_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Šellas metode (Shell sort)
	# a - viendimensijas masīvs
	sk = 0
	n = len(a)
	solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
	while solis >= 1:
		for k in range(0, solis):
			for i in range(solis + k, n, solis):
				sk = sk + 1
				if a[i - solis] < a[i]:
					x = a[i]
					j = i
					sk = sk + 1
					while a[j - solis] < x:
						a[j] = a[j - solis]
						j = j - solis
						if j == k:
							break
						sk = sk + 1
					a[j] = x
		solis = (solis - 1) // 3

	return sk


def sort_atrais_dilstosa(a, sv, bv):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	p = 0
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] < a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			p += 1
			j = j + solis
		p1 = sort_atrais_dilstosa(a, sv, i - 1)
		p2 = sort_atrais_dilstosa(a, i + 1, bv)
		p = p + p1 + p2
	return p


def izvadit_masivu_un_salidzinasanas_skaitu(x, sal):
	# Izvada salīdzināšanas skaitu un izvada masīva elementus ar komatiem
	# x - viendimensijas masīvs
	# sal - int skaitlis
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return str(sal) + " salīdzināšanas - " + s


def samaisit(masivs):
	# Samaisa masīva elementus (funkcija tiek izmantota, lai no sakārtota masīva numpy.arange(n + 1) izveidot nesakārtotu (unsort)
	# masivs - viendimensijas masīvs
	i = 0
	while i < len(masivs) // 2:
		x = random.randint(1, len(masivs) - 1)
		y = random.randint(1, len(masivs) - 1)
		temp = masivs[x]
		masivs[x] = masivs[y]
		masivs[y] = temp
		i = i + 1
	return masivs

def meklet(a, b):
	l = 0
	r = len(a) - 1
	while (l <= r):
		i = (l + r) // 2
		print(f"Checking {a[i]} at index {i}")  # print current value and index
		if a[i] == b:
			print(f"Found {b} at index {i}")
			return i
		elif a[i] < b:
			l = i + 1
			print("Moving right endpoint")
		else:
			r = i - 1
			print("Moving left endpoint")
	print(f"{b} not found")
	return -1


def inversaMatrica(matrica):
	n = matrica.shape[0]
	m = matrica.shape[1]
	if n != m:
		return "Nekorekti izmēri"
	# Palīgmatricas izveide
	a = numpy.zeros((n, 2*n))
	for i in range(n):
		for j in range(n):
			a[i, j] = matrica[i, j]
			if i == j:
				a[i, j + n] = 1
			else:
				a[i, j + n] = 0
	# =========================
	for u in range(n):
		# "nulles" rindiņas maiņa
		if a[u, u] == 0:
			k = u
			while a[k, u] == 0:
				k = k + 1
				if k >= n:
					return "Inversā matrica neeksistē"
			# =======================
			for i in range(2*n):
				x = a[u, i]
				a[u, i] = a[k, i]
				a[k, i] = x
		# ======================
		for j in range(2*n-1, u-1, -1):
			a[u, j] = a[u, j] / a[u, u]
		for i in range(n):
			if i == u:
				continue
			for j in range(2*n-1, u-1, -1):
				a[i, j] = a[i, j] - a[i, u] * a[u,j]
	# inversa matrica
	b = numpy.zeros((n,n))
	for i in range(n):
		for j in range(n):
			b[i, j] = a[i, j + n]
	return b


def determinants(matrica):
	n = matrica.shape[0]
	m = matrica.shape[1]
	if n != m:
		return "Tas nav determinants"
	det = 1
	for u in range(n):
		# "nulles" rindiņas maiņa
		if matrica[u, u] == 0:
			k = u
			while matrica[k, u] == 0:
				k = k + 1
				if k >= n:
					return 0
			# =======================
			det = -det
			for i in range(n):
				x = matrica[u, i]
				matrica[u, i] = matrica[k, i]
				matrica[k, i] = x
		# ======================
		det = det * matrica[u, u]
		for j in range(n-1, u-1, -1):
			matrica[u, j] = matrica[u, j] / matrica[u, u]
		for i in range(u + 1, n):
			for j in range(n-1, u-1, -1):
				matrica[i, j] = matrica[i, j] - matrica[i, u] * matrica[u,j]
	return det

def add_numeration_to_matrix(a):
	# Pievieno rindas un kolonnu numerāciju matricai un atgriež simbolu virkni ar matricas elementiem un ir rindas un kolonnas numerācija
	# a - divdimensijas masīvs
	s = ""
	len1 = a.shape[1]
	for j in range(len1 + 1):
		s = s + "{:3d}".format(j)  # izmantot formāta norādītāju, lai nodrošinātu nepieciešāmu atstarpi
	s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

	n = a.shape[0]
	for i in range(n):
		s = s + "{:3d}".format(i + 1)  # rindas numurs
		for j in range(len1):
			s = s + "{:3.0f}".format(a[i, j])
		s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

	return s


def matrix_to_string(matrix):
	# Returns a string representation of a matrix, where each row is separated by a newline character.
	# If a value is a whole number, it is represented without a decimal point. Otherwise, it is represented with a decimal point.
	# The function also finds the maximum length of the values in the matrix, and indents each number so that they align properly.

	rows = len(matrix)
	cols = len(matrix[0])
	max_len = len("{:.2f}".format(matrix.max()))
	output = ""

	for i in range(rows):
		for j in range(cols):
			value = matrix[i][j]

			if value == int(value):
				value = int(value)
			else:
				value = "{:.2f}".format(value)

			padding = " " * (max_len - len(str(value)))
			output = output + padding + str(value)

			if j < cols - 1:
				output += " "

		output = output + "\n"

	return output

def matrix_to_string_float(matrix):
	# Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n.
	# Ja vērtība ir vesels skaitlis, tā tiek attēlota bez komata. Pretējā gadījumā tas tiek attēlots ar komatu.
	# Funkcija atrod arī maksimālo vērtību garumu matricā un papildina nepieciešamus skaitļus ar tujšumiem " ", lai tie būtu pareizi izlīdzināti.
	# matrix - matrica (divdimensijas numpy masīvs ar izmēriem n x m)
	rows = len(matrix)
	cols = len(matrix[0])
	max_len = 0

	for i in range(rows):
		for j in range(cols):
			value = matrix[i][j]
			if value == int(value):
				value_len = len(str(int(value)))
			else:
				value_len = len(str(float(value)))
			if value_len > max_len:
				max_len = value_len

	output = ""

	for i in range(rows):
		for j in range(cols):
			value = matrix[i][j]
			if value == int(value):
				value = int(value)
			else:
				value = str(float(value))
			padding = " " * (max_len - len(str(value)))
			output += padding + str(value)
			if j < cols - 1:
				output = output + " "
		output = output + "\n"

	return output

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

def ievadiet_5_skaitlus_seta(a):
	# Procedura kura ļauj ievādit 5 skaitļus un ieliekt tos kopā.
	# a - tukša kopa (set). a = set().

	for i in range(1, 6):
		while True:
			b = input("Ievadiet " + str(i) + ". skaitli ==> ")
			try:
				b = int(b)
				if b < 1 or b > 35:
					print("Skaitlim jābūt veselam skaitlim no 1 līdz 35!")
				elif b in a:
					print("Šis skaitlis jau eksistē, lūdzu ievadiet citu skaitli!")
				else:
					a.add(b)
					break
			except ValueError:
				print("Ievadei jābūt skaitlim!")
				continue

	return a

def izloze(cik, nocik):
	v = set()
	for i in range(1, nocik + 1):
		v.add(i)
	k = set()
	for i in range(cik):
		b = random.choice(list(v))
	v.remove(b)
		k.add(b)

	return k


def sort_set(set_to_sort):

	sorted_list = []
	while set_to_sort:
		min_element = None
		for element in set_to_sort:
			if min_element is None or element < min_element:
				min_element = element
		sorted_list.append(min_element)
		set_to_sort.remove(min_element)

		return set(sorted_list)

def keno():
	numbers = set()
	while len(numbers) < 20:
		number = random.randint(1, 62)
		numbers.add(number)
	numbers = sort_set(numbers)
	return numbers

def kombinacijas_cikls(n, m):
	# Aprēķina kombinācijas skaitu C(n,m) izmantojot ciklu. n >= m
	# n - naturāls skaitlis vai nulle (no cik) n ir "apakšā"
	# m - naturāls skaitlis vai nulle (pa cik) m ir "augšā"

	if m > n:
		return False

	elif m == 0 or m == n:
		return 1

	fn = 1
	for i in range(2, n + 1):
		fn = fn * i

	fm = 1
	for i in range(2, m + 1):
		fm = fm * i

	fnm = 1
	for i in range(2, n - m + 1):
		fnm = fnm * i

	return fn / fm / fnm


def kombinacijas_rekursija(n, m):
	# Aprēķina kombinācijas skaitu C(n,m) izmantojot rekursiju. n >= m
	# n - naturāls skaitlis vai nulle (no cik) n ir "apakšā"
	# m - naturāls skaitlis vai nulle (pa cik) m ir "augšā"
	if m > n:
		return False

	if m == 0 or m == n:
		return 1
	return kombinacijas_rekursija(n - 1, m - 1) + kombinacijas_rekursija(n - 1, m)

def circles_four_directions(x, r, y):
	# Uzzīme riņķa līnijas četros virzienos
	# x - x koordināta riņķa līnijas centram
	# r - r riņķa līnijas rādiuss
	# y - y koordināta riņķa līnijas centram
	if r <= 3:
		return
	canva.create_oval(x - r, y - r, x + r, y + r, width=2)
	circles_four_directions(x + r, r // 2, y)
	circles_four_directions(x - r, r // 2, y)
	circles_four_directions(x, r // 2, y - r)
	circles_four_directions(x, r // 2, y + r)


def circles_six_directions(x, r, y):
	# Uzzīme riņķa līnijas sešos virzienos
	# x - x koordināta riņķa līnijas centram
	# r - r riņķa līnijas rādiuss
	# y - y koordināta riņķa līnijas centram
	if r <= 2:
		return
	canva.create_oval(x - r, y - r, x + r, y + r, width=3)

	circles_six_directions(x + 2 * r, r / 3, y)
	circles_six_directions(x - 2 * r, r / 3, y)

	circles_six_directions(x + r, r / 3, y - r * math.sqrt(3))
	circles_six_directions(x - r, r / 3, y - r * math.sqrt(3))

	circles_six_directions(x + r, r / 3, y + r * math.sqrt(3))
	circles_six_directions(x - r, r / 3, y + r * math.sqrt(3))

def zimet_pitagora_koku(x, y, garums, lenkis, rekursijas_skaits):
	# Uzzīme Pitagora koku noteiktā vietā, izmēra un tas tiek zimēts rekursīvi "rekursijas_skaits" reizes.
	# x - x koordināta pirmā nogriežņa sākumam
	# y - y koordināta pirmā nogriežņa beigām
	# garums - garums pirmām nogriežņim. Tāda veidā tiek regulēts Pitagora koka izmērs
	# lenkis - leņķis grādos pirmām nogriežņim ar "zēmi"
	# rekursijas_skaits - rekursijas skaits. Maksimālais skaits pēc kurā zimēšana beigsies
	if rekursijas_skaits > 0:
		# print(lenkis)
		x1 = x + garums * math.cos(math.radians(lenkis))
		y1 = y - garums * math.sin(math.radians(lenkis))
		canvas.create_line(x, y, x1, y1)

		zimet_pitagora_koku(x1, y1, garums * math.sqrt(2) / 2, lenkis - 45, rekursijas_skaits - 1)
		zimet_pitagora_koku(x1, y1, garums * math.sqrt(2) / 2, lenkis + 45, rekursijas_skaits - 1)


def draw_line(x0, y0, x1, y1):
	# Uzzīme nogriežņi pēc diviem dotiem punktiem ar biezumu (width) 2
	# x0 - x koordināta sākumpunktam
	# y0 - y koordināta sākumpunktam
	# x1 - x koordināta galapunktam
	# y1 - y koordināta galapunktam
	canvas.create_line(x0, y0, x1, y1, width=2)


def draw_crosses(x0, y0, x1, y1, rekursijas_skaits):
	# Rekursīvi uzzīme krustiņus. Koeficienti tika iegūti aptuveni.
	# x0 - x koordināta sākumpunktam (nogriežņim)
	# y0 - y koordināta sākumpunktam (nogriežņim)
	# x1 - x koordināta galapunktam (nogriežņim)
	# y1 - y koordināta galapunktam (nogriežņim)
	length = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

	if rekursijas_skaits == 0:
		return

	angle = math.atan2(y1 - y0, x1 - x0) # math.atan2() atgriež y/x arktangensu radiānos. Kur x un y ir punkta (x,y) koordinātas.

	draw_line(x0, y0, x1, y1)

	dx = math.cos(angle + math.pi / 4) * length / 2.3 # izmaiņa pēc x
	dy = math.sin(angle + math.pi / 4) * length / 2.3 # izmaiņa pēc y
	draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

	dx = math.cos(angle - math.pi / 4) * length / 2.3
	dy = math.sin(angle - math.pi / 4) * length / 2.3
	draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

	dx = math.cos(angle + math.pi * 3 / 4) * length / 2.3
	dy = math.sin(angle + math.pi * 3 / 4) * length / 2.3
	draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)

	dx = math.cos(angle - math.pi * 3 / 4) * length / 2.3
	dy = math.sin(angle - math.pi * 3 / 4) * length / 2.3
	draw_crosses(x1, y1, x1 + dx, y1 + dy, rekursijas_skaits - 1)



def get_new_pos(x, y, lenkis, attalums):
	# Saņem x un y koordinātas, leņķi un attālumu un atgriež jauno pozīciju pēc dotā attāluma pārvietošanas dotajā leņķī
	# x - jaunais x
	# y - jaunais y
	# lenkis - leņķis grādos
	# attalums - attālums
	return x + attalums * math.cos(math.radians(lenkis)), y + attalums * math.sin(math.radians(lenkis))


def draw_circle(center_x, center_y, r):
	# Pēc dota centras koordinātas (center_x, center_y) un rādiusa (r) uzzīmē riņķa līniju.
	# center_x - riņķa līnijas centrs pēc x koordinātas
	# center_y - riņķa līnijas centrs pēc y koordinātas
	# r - riņķa līnijas rādiuss
	x1 = center_x - r
	x2 = center_x + r
	y1 = center_y - r
	y2 = center_y + r
	#print(x1, x2, y1, y2)
	canva.create_oval(x1, y1, x2, y2)


# ZIMEŠANA
def recursion(center_x, center_y, r, rekursijas_skaits):
	# Tas saņem pašreizējās iterācijas centra koordinātas, rādiusu un dziļuma līmeni (rekursijas skaits).
	# Katrā dziļuma līmenī (rekursijas skaitam) tiek uzzīmēta riņķa līnijas pie dotajām centra koordinātām
	# un pēc tam funkcija tiek rekursīvi izsaukta ar sešām jaunām centra koordinātām,
	# kuras aprēķina, izmantojot funkciju get_new_pos.
	# center_x - riņķa līnijas centrs pēc x koordinātas
	# center_y - riņķa līnijas centrs pēc y koordinātas
	# r - riņķa līnijas rādiuss
	# rekursijas_skaits - rekursījas dziļums (cik reizes rekursija tiek īstenota)

	draw_circle(center_x, center_y, r)

	if rekursijas_skaits == 0:
		return
	attalums = r * 2 / 3
	jauns_radiuss = r / 3 # apzīmē mazāko apļu rādiusu, kas rekursīvi apvilkti ap lielākiem apļiem.
	lenkis = 30 # 30 grādi

	for t in range(6): # t netiek izmantota
		new_x, new_y = get_new_pos(center_x, center_y, lenkis, attalums)
		recursion(new_x, new_y, jauns_radiuss, rekursijas_skaits - 1)
		lenkis = lenkis + 60 # Katras jaunās centra koordinātas leņķis tiek nobīdīts par 60 grādiem no iepriekšējās, jo ap pašreizējo apli ir sešas riņķa līnijas

	recursion(center_x, center_y, jauns_radiuss, rekursijas_skaits - 1)

def draw_serpinskis(x1, y1, x2, y2, x3, y3):
	# Uzzīmē Serpinskā trijstūri izmantojot rekursiju
	# x1 - x koordināta kreisai apakšējai trijstūra virsotnei
	# y1 - y koordināta kreisai apakšējai trijstūra virsotnei
	# x2 - x koordināta labai apakšējai trijstūra virsotnei
	# y2 - y koordināta labai apakšējai trijstūra virsotnei
	# x3 - x koordināta augšējai centrālai trijstūra virsotnei
	# y3 - y koordināta augšējai centrālai trijstūra virsotnei

	area = abs((0.5) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) # Trijstūra laukums

	if area < 10: # regulē rekursijas skaitu. Ja trijstūra laukums ir mazāks neka 10, tad stop
		kanva.create_polygon(x1, y1, x2, y2, x3, y3, fill='white', outline='black')
	else:
		x1x2 = (x1 + x2) / 2
		y1y2 = (y1 + y2) / 2
		x1x3 = (x1 + x3) / 2
		y1y3 = (y1 + y3) / 2
		x2x3 = (x2 + x3) / 2
		y2y3 = (y2 + y3) / 2

		draw_serpinskis(x1, y1, x1x2, y1y2, x1x3, y1y3)
		draw_serpinskis(x2, y2, x1x2, y1y2, x2x3, y2y3)
		draw_serpinskis(x3, y3, x1x3, y1y3, x2x3, y2y3)

def zimet_serpinska_paklaju(x, y, izmers):
	# Uzzīmē Serpinska paklāju
	# x - kreisa augšēja koordināta x Serpinska paklājam
	# y - kreisa augšēja koordināta y Serpinska paklājam
	if izmers < 5:
		kanva.create_rectangle(x, y, x + izmers, y + izmers, fill="black", outline="")
	else:
		maz_izmers = izmers / 3
		zimet_serpinska_paklaju(x, y, maz_izmers)
		zimet_serpinska_paklaju(x + maz_izmers, y, maz_izmers)
		zimet_serpinska_paklaju(x + 2 * maz_izmers, y, maz_izmers)
		zimet_serpinska_paklaju(x, y + maz_izmers, maz_izmers)
		zimet_serpinska_paklaju(x + 2 * maz_izmers, y + maz_izmers, maz_izmers)
		zimet_serpinska_paklaju(x, y + 2 * maz_izmers, maz_izmers)
		zimet_serpinska_paklaju(x + maz_izmers, y + 2 * maz_izmers, maz_izmers)
		zimet_serpinska_paklaju(x + 2 * maz_izmers, y + 2 * maz_izmers, maz_izmers)

def zimet_koha_zvaigzni(x1, y1, x5, y5):
	# Rekursīvi uzzīme daļu no Koha zvaigznes
	# x1 - nogriežņa sākumpunkta x koordināta
	# y1 - nogriežņa sākumpunkta y koordināta
	# x5 - nogriežņa galapunkta x koordināta
	# y5 - nogriežņa galapunkta y koordināta
	if math.sqrt((x1 - x5)**2 + (y1 - y5)**2) < 4: # kad nogriežņa garums paliek mazāks par 4, tad pārtraucam rekursiju
		kanva.create_line(x1, y1, x5, y5)
	else:
		dx = x5 - x1
		dy = y5 - y1
		x2 = x1 + dx // 3
		y2 = y1 + dy // 3
		x3 = (x1 + x5) // 2 + math.sqrt(3) * (y1 - y5) // 6
		y3 = (y1 + y5) // 2 + math.sqrt(3) * (x5 - x1) // 6
		x4 = x1 + 2 * dx // 3
		y4 = y1 + 2 * dy // 3
		zimet_koha_zvaigzni(x1, y1, x2, y2)
		zimet_koha_zvaigzni(x2, y2, x3, y3)
		zimet_koha_zvaigzni(x3, y3, x4, y4)
		zimet_koha_zvaigzni(x4, y4, x5, y5)

def rinka_linija(x, y, r):
	# Izveido riņķa līniju kurai centrs ir (x;y) un rādiuss ir r
	# x - x koordināta riņķa līnijas centram
	# y - y koordināta riņķa līnijas centram
	# r - riņķa līnijas rādiuss
	kanva.create_oval(x - r, y - r, x + r, y + r)


def kvadrats(x, y, r):
	# Izveido kvadrātu pēc dota centra koordinātam (x;y) un pēc r (puse no kvadrātas malas)
	# x - x koordināta kvadrātas centram
	# y - y koordināta kvadrātas centram
	# r - puse no kvadrātas malas (lai uzzimētu kvadrātu)
	kanva.create_rectangle(x - r, y - r, x + r, y + r)


def rekursija_1(x, y, r):
	# Uzzime kvadrātu un četras riņķa līnijas blakus pa visam pusem
	# x - x koordināta centram
	# y - y koordināta centram
	# r - rādiuss riņķa līnijai vai puse no kvadrātas malas
	kvadrats(x, y, r)
	if r > 5:
		rekursija_2(x + 3 * r, y, r / 3)
		rekursija_2(x - 3 * r, y, r / 3)
		rekursija_2(x, y + 3 * r, r / 3)
		rekursija_2(x, y - 3 * r, r / 3)


def rekursija_2(x, y, r):
	# Uzzime riņķa līniju un četrus kvadrātus blakus pa visam pusem
	# x - x koordināta centram
	# y - y koordināta centram
	# r - rādiuss riņķa līnijai vai puse no kvadrātas malas
	rinka_linija(x, y, r)
	if r > 5:
		rekursija_1(x + 3 * r, y, r / 3)
		rekursija_1(x - 3 * r, y, r / 3)
		rekursija_1(x, y + 3 * r, r / 3)
		rekursija_1(x, y - 3 * r, r / 3)

#----------------
def zila(N, krasa):
	# Skaita cik ir zīlas krāsas pērlītes N rindā
	# N - N rindā
	# krasa - "z" - zīla, "s" - sarkana, "o" - oranža
	if N == 1:
		if krasa == "z":
			return 1
		else:
			return 0
	else:
		return 2 * sarkana((N - 1), krasa) + zila((N - 1), krasa) + 3 * oranzs((N - 1), krasa)


def sarkana(N, krasa):
	# Skaita cik ir sarkanas krāsas pērlītes N rindā
	# N - N rindā
	# krasa - "z" - zīla, "s" - sarkana, "o" - oranža
	if N == 1:
		if krasa == "s":
			return 1
		else:
			return 0
	else:
		return 3 * sarkana((N - 1), krasa) + 2 * zila((N - 1), krasa) + 2 * oranzs((N - 1), krasa)


def oranzs(N, krasa):
	# Skaita cik ir oranžas krāsas pērlītes N rindā
	# N - N rindā
	# krasa - "z" - zīla, "s" - sarkana, "o" - oranža
	if N == 1:
		if krasa == "o":
			return 1
		else:
			return 0

	else:
		return sarkana((N - 1), krasa) + 3 * zila((N - 1), krasa) + oranzs((N - 1), krasa)
#-----------


import tkinter
from tkinter import ttk


def create_circle(x, y, r):
	# Uzzīme riņķa līniju
	# r - riņķa līnijas rādiuss
	# x - x koordināta riņķa līnijas centram
	# y - y koordināta riņķa līnijas centram
	kanva.create_oval(x - r, y - r, x + r, y + r, outline="black", width=3)


def draw_circles(x, y, r): # r - rādiuss
	# Uzzīme riņķa līnijas rekursīvi uz labo pusi
	# r - riņķa līnijas rādiuss
	# x - x koordināta riņķa līnijas centram
	# y - y koordināta riņķa līnijas centram
	if r >= 2:
		create_circle(x, y, r)
		draw_circles(x + r, y, r // 2)
#--------------

def zimet_piecsturi_ar_diagonalem(x0, y0, R):
	# uzzīme regulāro piecsturi (nav rotēts)
	# x0 - regulāra piecstūra centra x koordināta
	# y0 - regulāra piecstūra centra y koordināta
	# R - regulāra piecstūra rādiuss

	# t - regulāra piecstūra vienas malas garums (nepieciešams, lai izrēķinātu koordinātas)
	# h - regulāra piecstūra augstuma garums (nepieciešams, lai izrēķinātu koordinātas)

	t = R * math.sqrt((5 - math.sqrt(5)) / 2) # R * 1.17557
	h = (math.tan(math.radians(72)) / 2) * t # 1.539 * t
	k = t * math.sin(math.radians(54)) # k = t*sin(54 degree) (palīgnogriežnis)
	p = t * math.cos(math.radians(54)) # p = t*cos(54 degree) (palīgnogriežnis)

	# piecstura koordinātas
	x1 = x0 - t / 2
	y1 = y0 - R + h

	x2 = x0 - k
	y2 = y0 - R + p

	x3 = x0
	y3 = y0 - R

	x4 = x0 + k
	y4 = y0 - R + p

	x5 = x0 + t / 2
	y5 = y0 - R + h

	# pati piecstūra uzzimēšana
	kanva.create_line(x1, y1, x2, y2)
	kanva.create_line(x2, y2, x3, y3)
	kanva.create_line(x3, y3, x4, y4)
	kanva.create_line(x4, y4, x5, y5)
	kanva.create_line(x5, y5, x1, y1)

	# diagonāles uzzimēšana
	kanva.create_line(x1, y1, x3, y3)
	kanva.create_line(x1, y1, x4, y4)

	kanva.create_line(x2, y2, x4, y4)
	kanva.create_line(x2, y2, x5, y5)

	kanva.create_line(x3, y3, x5, y5)


def zimet_piecsturi_ar_diagonalem_rotets(x0, y0, R):
	# uzzīme regulāro piecsturi (ir rotēts)
	# x0 - regulāra piecstūra centra x koordināta
	# y0 - regulāra piecstūra centra y koordināta
	# R - regulāra piecstūra rādiuss

	# t - regulāra piecstūra vienas malas garums (nepieciešams, lai izrēķinātu koordinātas)
	# h - regulāra piecstūra augstuma garums (nepieciešams, lai izrēķinātu koordinātas)

	t = R * math.sqrt((5 - math.sqrt(5)) / 2) # t aptuvēni = R * 1.17557
	h = (math.tan(math.radians(72)) / 2) * t # h aptuvēni = 1.539 * t
	k = t * math.sin(math.radians(54)) # k = t*sin(54 degree) (palīgnogriežnis)
	p = t * math.cos(math.radians(54)) # p = t*cos(54 degree) (palīgnogriežnis)

	# piecstura koordinātas
	x1 = x0
	y1 = y0 + R

	x2 = x0 - k
	y2 = y0 + R - p

	x3 = x0 - t / 2
	y3 = y0 + R - h

	x4 = x0 + t / 2
	y4 = y0 + R - h

	x5 = x0 + k
	y5 = y0 + R - p

	# pati piecstūra uzzimēšana
	kanva.create_line(x1, y1, x2, y2)
	kanva.create_line(x2, y2, x3, y3)
	kanva.create_line(x3, y3, x4, y4)
	kanva.create_line(x4, y4, x5, y5)
	kanva.create_line(x5, y5, x1, y1)

	# diagonāles uzzimēšana
	kanva.create_line(x1, y1, x3, y3)
	kanva.create_line(x1, y1, x4, y4)

	kanva.create_line(x2, y2, x4, y4)
	kanva.create_line(x2, y2, x5, y5)

	kanva.create_line(x3, y3, x5, y5)


def zimet_piecsturi_rekursivi(x0, y0, R):
	# zime rekursīvi piecstūrus ar diagonālem izsaucot divas citas funkcijas
	# rekursija beigās kad R <= 10
	if R > 10:

		zimet_piecsturi_ar_diagonalem(x0, y0, R)
		zimet_piecsturi_ar_diagonalem_rotets(x0, y0, R * math.pi / 8.25)
		r = R * math.pi / 8.25
		zimet_piecsturi_rekursivi(x0, y0, r * math.pi / 8.25)


def draw_serpinskis(x1, y1, x2, y2, x3, y3, rekursijas_skaits):
	# uzzimē vienu Serpinska trijsturi izmantojot rekursiju
	# x1 - vislielāka trijstūra koordināta x vienai virsotnei
	# y1 - vislielāka trijstūra koordināta y vienai virsotnei
	# x2 - vislielāka trijstūra koordināta x otrai virsotnei
	# y2 - vislielāka trijstūra koordināta y otrai virsotnei
	# x3 - vislielāka trijstūra koordināta x trešai virsotnei
	# y3 - vislielāka trijstūra koordināta y trešai virsotnei
	# rekursijas_skaits - rekursijas skaits (cik līmeņus ir jāuzzīme Serpinska trijstūri)

	if rekursijas_skaits == 0:
		kanva.create_polygon(x1, y1, x2, y2, x3, y3, fill='white', outline='black')
	else:
		x1x2 = (x1 + x2) / 2
		y1y2 = (y1 + y2) / 2
		x1x3 = (x1 + x3) / 2
		y1y3 = (y1 + y3) / 2
		x2x3 = (x2 + x3) / 2
		y2y3 = (y2 + y3) / 2

		draw_serpinskis(x1, y1, x1x2, y1y2, x1x3, y1y3, rekursijas_skaits - 1)
		draw_serpinskis(x2, y2, x1x2, y1y2, x2x3, y2y3, rekursijas_skaits - 1)
		draw_serpinskis(x3, y3, x1x3, y1y3, x2x3, y2y3, rekursijas_skaits - 1)

def zimet(x, y, garums):
	# uzzīmē rekursīvi "koku"
	# x - pirmā nogriežņa x koordināta
	# y - pirmā nogriežņa y koordināta
	# garums - pirmā nogriežņa garums (pēc tā tiek izrēķinātas koordinātas nepieciešamas, lai uzzīmēt nogriezni)
	lx = x + garums * math.cos(math.pi * 7 / 4) # -1*math.pi / 4 (-45 gradi)
	ly = y + garums * math.sin(math.pi * 7 / 4) # -1*math.pi / 4 (-45 gradi)

	lenkis = -1 * math.pi / 2 + math.pi * 7 / 4
	rx = x + garums * math.cos(lenkis)
	ry = y + garums * math.sin(lenkis)

	kanva.create_line(x, y, lx, ly)
	kanva.create_line(x, y, rx, ry)

	if garums > 1: # Stop kad garums nogrieznim ir mazāks nekā 1
		zimet(lx, ly, garums / 2)
		zimet(rx, ry, garums / 2)

def zimet_rekursivi(x0, y0, x2, y2, x1, y1, x3, y3):
	# Uzzīmē rekursīvi kvadrātus noteiktā secība
	# x0 - kreisā apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
	# y0 - kreisā apakšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

	# x2 - laba augšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
	# y2 - laba augšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

	# x1 - kreisā augšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
	# y1 - kreisā augšēja stūra koordināta pēc y (runājot par 1. iterācijas kvadrātu)

	# x3 - laba apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)
	# y3 - laba apakšēja stūra koordināta pēc x (runājot par 1. iterācijas kvadrātu)

	# attālums no punkta (x0;y0) līdz (x1;y1)
	if math.sqrt((x0 - x1)**2 + (y0 - y1)**2) > 5: # ja attālums starp šiem punktiem paliek mazāks nekā 5 (kvadrāta mala paliek mazāka nekā 5), tad rekursija pārtraucās
		kanva.create_line(x0, y0, x2, y2)
		kanva.create_line(x2, y2, x1, y1)
		kanva.create_line(x1, y1, x3, y3)
		kanva.create_line(x3, y3, x0, y0)

		zimet_rekursivi((x0 + x2) / 2, (y0 + y2) / 2, (x2 + x1) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2, (x3 + x0) / 2, (y0 + y3) / 2)

def izveidot_masivu_ar_garumu(n):
	# Izveido masīvu ar noradīto garumu n
	a = numpy.arange(n)
	for i in range(n):
		a[i] = int(input("Ievadi " + str(i) + ".elementu ===> "))
	return a

def izveidot_masivu_ar_garumu(n):
	# Izveido masīvu ar noradīto garumu n
	# n - naturāls skaitlis
	a = numpy.arange(n)
	for i in range(n):
		b = input("Ievadiet " + str(i) + ".elementu ===> ")
		b = is_whole(b, i)
		a[i] = b
	return a

def izvade(x):
	# Izvada masīva elementus ar komatiem pēc kārtas ievadīšanas secība
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	print(s)


def min_element_in_matrix(b):
	# Atrod mazako elementu masīva
	min1 = b[0]
	for i in range(1, n_elements):
		if min1 > b[i]:
			min1 = b[i]
	return min1


def max_element_in_matrix(b):
	# Atrod lielāku elementu masīva
	max1 = b[0]
	for i in range(1, n_elements):
		if max1 < b[i]:
			max1 = b[i]
	return max1


def print_matrix(b):
	for row in b:
		print(row)


# Function to encrypt a message into Morse code and play it


def encrypt_and_play(message):
	encrypted_message = encrypt_to_morse_code(message, morse_code_dictionary)
	for symbol in encrypted_message:
		if symbol == ".":
			play_beep(DOT_DURATION)
		elif symbol == "-":
			play_beep(DASH_DURATION)
		elif symbol == " ":
			play_beep(SYMBOL_SPACE_DURATION)
		elif symbol == "/":
			play_beep(WORD_SPACE_DURATION)


def krustpunkts(punkts, radius):
	# Atrod nepieciešāmo krustpunktu un return kā kortežu (xx, yy)
	# punkts - (x1,y1) kortežs
	# radius - rādiusa vērtība [0; + bezg)
	(x, y) = punkts
	if (x, y) == (0, 0) and radius == 0:
		return False # Dalīšana ar 0
	d = math.sqrt(x * x + y * y)
	xx = x * radius / d
	yy = y * radius / d
	return (xx, yy)



def det(a, b, c, d):
	# Atgriež determinanta vērtību
	# a - skaitlis float
	# b - skaitlis float
	# c - skaitlis float
	# d - skaitlis float
	return a * d - b * c


def mala(kp1, kp2): # kp1 = (a,b)   kp2 = (c,d)
	# Malas garums pēc diviem punktiem
	# Atgriež malas garumu
	# kp1 - 1. punkts
	# kp2 - 2. punkts
	return math.sqrt((kp1[0] - kp2[0]) * (kp1[0] - kp2[0]) + (kp1[1] - kp2[1]) * (kp1[1] - kp2[1]))


def laukums(kp1, kp2, kp3): # kp1 =(a,b)   kp2 = (c,d)   kp3 = (f,g)
	# Noskaidro trījstūra laukumu ar Herona formulu pēc trīs krustpunktiem
	# kp1 - 1. krustpunkts
	# kp2 - 2. krustpunkts
	# kp3 - 3. krustpunkts
	m1 = mala(kp1, kp2)
	m2 = mala(kp1, kp3)
	m3 = mala(kp2, kp3)

	p = (m1 + m2 + m3) / 2

	return math.sqrt(p * (p - m1) * (p - m2) * (p - m3))


def vai_pa_pariem_krustojas(t1, t2, t3):
	# Funkcija noskaidro vai pa pariem krustojas trīs taisnes
	# return True, ja krustojas
	# return False, ja nekrustojas
	# t1 - pirmā taisne
	# t2 - otrā taisne
	# t3 - treša taisne
	if (det(t1[0], t1[1], t2[0], t2[1]) * det(t1[0], t1[1], t3[0], t3[1]) * det(t2[0], t2[1], t3[0], t3[1])) == 0:
		return False
	else:
		return True

def gcd(a, b):
	while b != 0:
		c = a % b
		a = b
		b = c
	return a


def krustpunkts(t1, t2):
	# t1 - pirmā taisne
	# t2 - otrā taisne
	# return krustpunktu divām taisnēm (x,y)
	d = det(t1[0], t1[1], t2[0], t2[1])
	dx = det(t1[1], t1[2], t2[1], t2[2])
	dy = det(t1[2], t1[0], t2[2], t2[0])

	x = dx / d
	y = dy / d
	return (x, y)

def izveidot_masivu_ar_garumu(n):
	a = numpy.arange(n)
	for i in range(n):
		a[i] = int(input("Ievadi " + str(i) + ".elementu ===> ")

		return a

def izvade(x):
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	print(s)

def insert_sort(a):
	n = len(a)
	for i in range(1, n):
		if a[i - 1] > a[i]:
			x = a[i]
			j = i
			while a[j - 1] > x:
				a[j] = a[j - 1]
				j = j - 1
				if j == 0:
					break
			a[j] = x


def videjais_aritmetiskais(x):
	# Aprēķina masīva vidējo aritmētisko
	# x - masīvs
	n = len(x)
	t = 0
	for i in range(0, n):
		t = t + x[i]

	return t / n


def videjais_kvadratiskais(x):
	# Aprēķina masīva videjo kvadrātisko
	# x - masīvs
	n = len(x)
	t = 0
	for i in range(0, n):
		t = t + x[i] * x[i]

	return math.sqrt(t / n)


def videjais_harmoniskais(x):
	# Aprēķina masīva videjo harmonisko
	# x - masīvs
	n = len(x)
	t = 0

	for i in range(0, n):

		if x[i] == 0:
			return "Kļūda! Dalīšana ar 0"
		elif is_natural(x[i]):
			t = t + 1 / x[i]
		else:
			return "Kļūda! Visiem skaitļiem jābut pozitīviem!"

	return n / t


def videjais_geometriskais(x):
	# Aprēķina masīva videjo ģeomētrisko
	# x - masīvs
	n = len(x)
	s = 1

	for i in x:
		s = s * i

	if n % 2 == 0:  # Pārbauda vai n-sakne ir pāra skaitlis
		if s >= 0:  # Ja n-sakne pāra skaitlis, tad pārbaudam vai nav negatīvs, ja ir tad nevaram aprēķināt
			k = math.pow(s, (1 / n))  # ja ir pozitīvs vai 0, tad viss ir labi, varam aprēķināt pāra-sakni no pozitīvas vērtības
		else:
			k = "Nevar aprēķināt reālos skaitļos"  # ja ir negatīvs un n-sakne ir pāra skaitlis, tad nevaram to aprēķināt reālos skaitlos
	else:
		k = numpy.sign(s) * (numpy.abs(s)) ** (1 / n)  # ja n-sakne ir nepāra skaitlis, tad aprēķināt to šādi (parasta pow(a,b) funkcija nedarbojas ar tādiem skaitliem)

	return k


def videjas_linearas_novirzes_vertiba(x):
	# Aprēķina masīva vidējās absolūtās jeb vidējās lineārās novirzes vērtību
	# x - masīvs
	n = len(x)
	t = 0
	k = 0
	for i in range(0, n):
		t = t + x[i]

	c = t / n

	for i in range(0, n):
		k = k + abs(x[i] - c)

	return k / n


def standartnovirze(x):
	# Aprēķina masīva standartnovirzi
	# x - masīvs
	n = len(x)
	t = 0
	k = 0
	for i in range(0, n):
		t = t + x[i]

	c = t / n

	for i in range(0, n):
		k = k + (x[i] - c) * (x[i] - c)

	return math.sqrt(k / n)


def videja_sverta_vertiba(x, y):
	# Aprēķina masīvu vidējo svērsto vērtību
	# x - pirmais masīvs
	# y - otrais masīvs
	n = len(x)
	t = 0
	z = 0

	for i in range(0, n):
		t = t + x[i] * y[i]

	for i in range(0, n):
		z = z + y[i]

	return t / z


def videjais_aritmetiskais(x):
	# Aprēķina masīva vidējo aritmētisko
	# x - masīvs
	n = len(x)
	t = 0
	for i in range(0, n):
		t = t + x[i]

	return t / n


def linearas_korelacijas_koeficients(x, y):
	# Aprēķina masīvu linearas korelacijas koeficientu
	# x - pirmais masīvs
	# y - otrais masīvs
	n = len(x)
	vidx = videjais_aritmetiskais(x)
	vidy = videjais_aritmetiskais(y)

	s = 0
	tx = 0
	ty = 0

	for i in range(n):
		s = s + (x[i] - vidx) * (y[i] - vidy)
		tx = tx + (x[i] - vidx) * (x[i] - vidx)
		ty = ty + (y[i] - vidy) * (y[i] - vidy)

	p = math.sqrt(tx * ty)

	if p != 0:
		return s / p
	else:
		return "Kļūda! Dalīšana ar 0"

def sort_atrais_augosa(a, sv, bv):
	# Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakartotu masīvu
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] > a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			j = j + solis
		sort_atrais_augosa(a, sv, i - 1)
		sort_atrais_augosa(a, i + 1, bv)


def is_even_masivs(x):
	# Pārbauda vai masīva garums ir pāra skaitlis
	# Ja masīva garums ir pāra skaitlis, tad atgriež True
	# Ja masīva garums nav pāra skaitlis, tad atgriež False
	# x - viendimensijas masīvs
	masiva_garums = len(x)
	if masiva_garums % 2 == 0:
		return True
	else:
		return False


def mediana(x):
	# Atgriež masīva x mediānu
	# x - viendimensijas masīvs
	if is_even_masivs(x):
		return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
	else:
		return x[len(x) // 2]

def sort_atspole_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota atspoles metode
	# a - viendimensijas masīvs
	n = len(a)
	count = 0
	for i in range(1, n):
		if a[i - 1] < a[i]:
			count += 1
			for j in range(i, 0, -1):
				if a[j - 1] < a[j]:
					count += 1
					x = a[j]
					a[j] = a[j - 1]
					a[j - 1] = x
				else:
					count += 1
					break
		else:
			count += 1

	return count


def sort_ievietosana_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
	# a - viendimensijas masīvs
	n = len(a)
	sk = 0
	for i in range(1, n):
		sk = sk + 1
		if a[i - 1] < a[i]:
			x = a[i]
			j = i
			sk = sk + 1
			while a[j - 1] < x:
				a[j] = a[j - 1]
				j = j - 1
				if j == 0:
					break
				sk = sk + 1
			a[j] = x

	return sk


def sort_sella_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Šellas metode (Shell sort)
	# a - viendimensijas masīvs
	sk = 0
	n = len(a)
	solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
	while solis >= 1:
		for k in range(0, solis):
			for i in range(solis + k, n, solis):
				sk = sk + 1
				if a[i - solis] < a[i]:
					x = a[i]
					j = i
					sk = sk + 1
					while a[j - solis] < x:
						a[j] = a[j - solis]
						j = j - solis
						if j == k:
							break
						sk = sk + 1
					a[j] = x
		solis = (solis - 1) // 3

	return sk


def sort_atrais_dilstosa(a, sv, bv):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	p = 0
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] < a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			p += 1
			j = j + solis
		p1 = sort_atrais_dilstosa(a, sv, i - 1)
		p2 = sort_atrais_dilstosa(a, i + 1, bv)
		p = p + p1 + p2
	return p


def izvadit_masivu_un_salidzinasanas_skaitu(x, sal):
	# Izvada salīdzināšanas skaitu un izvada masīva elementus ar komatiem
	# x - viendimensijas masīvs
	# sal - int skaitlis
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return str(sal) + " salīdzināšanas - " + s


def izvadit_masivu(x):
	# Izvada masīva elementus ar komatiem
	# x - viendimensijas masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return s


def samaisit(masivs):
	# Samaisa masīva elementus (funkcija tiek izmantota, lai no sakārtota masīva numpy.arange(n + 1) izveidot nesakārtotu (unsort)
	# masivs - viendimensijas masīvs
	i = 0
	while i < len(masivs) // 2:
		x = random.randint(1, len(masivs) - 1)
		y = random.randint(1, len(masivs) - 1)
		temp = masivs[x]
		masivs[x] = masivs[y]
		masivs[y] = temp
		i = i + 1
	return masivs

def mode(masivs):
	# Atrod masīva modu un atgriež masīvu ar modam (vai modu)
	# Ja masīva visi elementi ir vienādi, tad atgriež False (moda netika atrasta)
	# masivs - viendimensijas masīvs (kurš vel netika kārtots augoša secība)
	'''
	Paskaidrojums, kā šī funkcija darbojas:

	Funkcija vispirms paņem, ka moda ir pirmais sakārtotā masīva elements.
	Pēc tam, funkcija iziet cauri katram masīva elementam un atjaunina sarakstu ar modam un to biežumu katru reizi, kad tiek atrasta jauna mode ar augstāku biežumu (elements, kuru ir vairāk).
	Ja tas saskaras ar modu ar tādu pašu biežumu (biežums - skaits, cik reizes paradās šis elements) kā pašreizēja moda, tad tas pievieno jauno modu, modu sarakstam.

	Funkcija iterē katru elementu sakārtotajā masīvā un pārbauda, vai tas ir vienāds ar iepriekšējo elementu.
	Ja tā ir, mainīgais "sk" tiek palielināts. Ja tā nav, funkcija pārbauda, vai pašreizējais skaits ir lielāks par līdz šim saglabāto maksimālo skaitu.
	Ja ir lielāks, tad maksimālais skaits tiek atjaunināts un pašreizējais skaitlis (elements) tiek pievienots modas sarakstam.
	Ja pašreizējais skaits ir vienāds ar maksimālo līdz šim saglabāto skaitu, modas sarakstam tiek pievienots arī šis skaitlis (elements) (vairākas modes).
	Pēc tam kad tika "iziterēts" viss masīvs, tad pārbaudām, vai pēdējā elementa biežums ir lielāks par līdz šim redzēto maksimālo biežumu. 
	Ja tā ir, tad maksimālais skaits tiek atjaunināts un modas saraksts ir tas pēdējais elements. 
	Ja pēdējā elementa skaits ir vienāds ar maksimālo līdz šim redzēto (saglabāto) skaitu, modas sarakstam tiek pievienots arī pēdējais elements (vairākas modes).

	Ja maksimālais biežums ir vienāds ar 1 (t.i., visi masīva elementi ir unikāli), funkcija atgriež vērtību False. 
	Pretējā gadījumā tas atgriež atrasto modas sarakstu.
	'''

	sort_atrais_augosa(masivs, 0, len(masivs) - 1)  # Ievadītais masīvs tiek izkārtots augošā secībā, izmantojot sort_atrais_augosa
	sk = 1  # seko pašreizējā apstrādājamā skaitļa (elementa) biežumam
	max_sk = 1  # saglabā jebkura masīva skaitļa (elementa) maksimālo biežumu
	modas_list = [masivs[0]]  # līdz šim atrasto modu saraksts

	if len(masivs) == 1:  # Ja masīva garums ir 1, tad moda arī ir tas skaitlis (vienīgais elements)
		modas_list = [masivs[0]]
		return modas_list

	for i in range(1, len(masivs)):
		if masivs[i] == masivs[i - 1]:  # Ja elements i ir vienāds ir i - 1, tad palielinām skaitītāju
			sk = sk + 1
		else:
			if sk > max_sk:  # ja skaititajs kļūst lielāks nekā maksimālais skaitītājs
				max_sk = sk  # tad maksimālais skaititajs atjaunojas
				modas_list = [masivs[i - 1]]  # modas saraksts atjaunojas un paliek tas masīva elements, kurš vislielāko reizi paradījās pēc skaitītajā

			elif sk == max_sk:  # Ja skaititajs ir vienāds ar pašreizējo maksimālo skaitītāju (max biežumu)
				modas_list.append(masivs[i - 1])  # tad pievienojam sarakstam jauno modu (papildus modu)

			sk = 1  # pēc iterācijām sk atkal kļūst par 1

	if sk > max_sk:  # Tas ir veidots pēdējam elementam. Ja lielāks skaititajs nekā pašreizējais maksimālais.
		max_sk = sk  # tad atjaunojam maksimālo skaitītāju
		modas_list = [masivs[-1]]  # atjaunojam modas sarakstu

	elif sk == max_sk:  # Ja modas biežumi ir vienādi, tad pievienojam modas sarakstam
		modas_list.append(masivs[-1])

	if max_sk == 1:  # Ja maksimālais biežums ir vienāds ar 1 (visi masīva elementi ir unikāli), atgriež vērtību False
		return False
	else:
		return modas_list  # Atgriež atrasto modas sarakstu


def apvieno(a, b):
	# Apvieno divus sakartotus masīvus a un b, un sakārto tos
	# Lineāra laiks o(n)
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	ga = len(a)
	gb = len(b)
	gc = ga + gb
	c = numpy.arange(gc)
	ia = 0
	ib = 0
	ic = 0
	while (ia < ga) and (ib < gb):
		if a[ia] < b[ib]:
			c[ic] = a[ia]
			ia = ia + 1
		else:
			c[ic] = b[ib]
			ib = ib + 1
		ic = ic + 1
	if ia < ga:
		for i in range(ia, ga):
			c[ic] = a[i]
			ic = ic + 1
	else:
		for i in range(ib, gb):
			c[ic] = b[i]
			ic = ic + 1
	return c


def apvieno(a, b):
	# Apvieno divus sakartotus masīvus a un b, un sakarto tos
	# Lineāra laiks o(n)
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	ga = len(a)
	gb = len(b)
	gc = ga + gb
	c = numpy.arange(gc)
	ia = 0
	ib = 0
	ic = 0
	while (ia < ga) and (ib < gb):
		if a[ia] < b[ib]:
			c[ic] = a[ia]
			ia = ia + 1
		else:
			c[ic] = b[ib]
			ib = ib + 1
		ic = ic + 1
	if ia < ga:
		for i in range(ia, ga):
			c[ic] = a[i]
			ic = ic + 1
	else:
		for i in range(ib, gb):
			c[ic] = b[i]
			ic = ic + 1
	return c


def reverse(masivs):
	# Pārkarto masīvā visus elementus pretēji
	# masivs - viendimensijas masīvs
	start_index = 0
	end_index = len(masivs) - 1
	while end_index > start_index:
		temp = masivs[start_index]
		masivs[start_index] = masivs[end_index]
		masivs[end_index] = temp
		start_index = start_index + 1
		end_index = end_index - 1

def izvadit_masivu(x):
	# Izvada masīva elementus ar komatiem
	# x - viendimensijas masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return s


def sort_atspole_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota atspoles metode
	# a - viendimensijas masīvs
	n = len(a)
	count = 0
	for i in range(1, n):
		if a[i - 1] < a[i]:
			count += 1
			for j in range(i, 0, -1):
				if a[j - 1] < a[j]:
					count += 1
					x = a[j]
					a[j] = a[j - 1]
					a[j - 1] = x
				else:
					count += 1
					break
		else:
			count += 1

	return count


def sort_ievietosana_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
	# a - viendimensijas masīvs
	n = len(a)
	sk = 0
	for i in range(1, n):
		sk = sk + 1
		if a[i - 1] < a[i]:
			x = a[i]
			j = i
			sk = sk + 1
			while a[j - 1] < x:
				a[j] = a[j - 1]
				j = j - 1
				if j == 0:
					break
				sk = sk + 1
			a[j] = x

	return sk


def sort_sella_dilstosa(a):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Šellas metode (Shell sort)
	# a - viendimensijas masīvs
	sk = 0
	n = len(a)
	solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
	while solis >= 1:
		for k in range(0, solis):
			for i in range(solis + k, n, solis):
				sk = sk + 1
				if a[i - solis] < a[i]:
					x = a[i]
					j = i
					sk = sk + 1
					while a[j - solis] < x:
						a[j] = a[j - solis]
						j = j - solis
						if j == k:
							break
						sk = sk + 1
					a[j] = x
		solis = (solis - 1) // 3

	return sk


def sort_atrais_dilstosa(a, sv, bv):
	# Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	p = 0
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] < a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			p += 1
			j = j + solis
		p1 = sort_atrais_dilstosa(a, sv, i - 1)
		p2 = sort_atrais_dilstosa(a, i + 1, bv)
		p = p + p1 + p2
	return p


def izvadit_masivu_un_salidzinasanas_skaitu(x, sal):
	# Izvada salīdzināšanas skaitu un izvada masīva elementus ar komatiem
	# x - viendimensijas masīvs
	# sal - int skaitlis
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + ", " + str(x[i])
	return str(sal) + " salīdzināšanas - " + s


def samaisit(masivs):
	# Samaisa masīva elementus (funkcija tiek izmantota, lai no sakārtota masīva numpy.arange(n + 1) izveidot nesakārtotu (unsort)
	# masivs - viendimensijas masīvs
	i = 0
	while i < len(masivs) // 2:
		x = random.randint(1, len(masivs) - 1)
		y = random.randint(1, len(masivs) - 1)
		temp = masivs[x]
		masivs[x] = masivs[y]
		masivs[y] = temp
		i = i + 1
	return masivs

def skaldi_un_valdi_dilstosa(a, sv, bv):
	# Sakarto masīvu dilstoša secība izmantojot "Skaldi un valdi" algoritmu un atgriež salīdzināšanas skaitu
	# ātrums - o(nlog(n))
	# a - viendimensijas masīvs
	# sv - sākumvērtība (parasti 0)
	# bv - beigu vērtība (parasti len(a))
	p = 0
	b = numpy.arange(len(a))
	if sv < bv:
		vv = (sv + bv) // 2
		p1 = skaldi_un_valdi_dilstosa(a, sv, vv)
		p2 = skaldi_un_valdi_dilstosa(a, vv + 1, bv)
		for i in range(sv, bv + 1):
			b[i] = a[i]
		i = sv
		j = vv + 1
		k = sv
		while (i <= vv) and (j <= bv):
			p += 1
			if b[i] > b[j]:
				a[k] = b[i]
				i = i + 1
			else:
				a[k] = b[j]
				j = j + 1
			k = k + 1
		if j > bv:
			while i <= vv:
				a[k] = b[i]
				i = i + 1
				k = k + 1
		p = p + p1 + p2
	return p


def atrais(a, sv, bv):  # sv = 0, bv = len(a)
	# Sakārto masīvu augoša secība
	# Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
	# a - viendimensijas masīvs
	# sv - sākuma vērtība
	# bv - beigu vērtība
	if sv < bv:
		i = sv
		j = bv
		solis = -1
		lv = True
		while i != j:
			if lv == (a[i] > a[j]):
				x = a[i]
				a[i] = a[j]
				a[j] = x
				x = i
				i = j
				j = x
				lv = not lv
				solis = -solis
			j = j + solis
		atrais(a, sv, i - 1)
		atrais(a, i + 1, bv)


def vards():
	# Ģenerē vārdus ar garumu no 3 līdz 8 (garums - uz labu laimi) un ģenerē to vārdu ar lieliem latiņu alfabēta burtiem
	# Atgriež vienu izveidotu vārdu
	r = random.randint(3, 8)
	v = ""
	for i in range(r):
		v += chr(random.randint(65, 90))  # ASCII 65;90
	return v


def masivs(length):
	# Aizpildā masīvu ar vārdiem atsaucoties uz "vards()". Atgriež aizpildīto masīvu.
	# length - viendimensijas masīva garums
	mas = numpy.empty(length, dtype=object)
	for j in range(length):
		mas[j] = vards()
	# print(mas)
	return mas


def meklet(a, b):
	# Sameklē a masīva b skaitļi (vai vārdu). Atgriež to vērtību, kur viņa atrodas pēc index. Ja nav tādas vērtības masīva, tad atgriež -1.
	# a - viendimensijas masīvs
	# b - to ko mēs meklējam (skaitlis vai vārds (str))
	l = 0
	r = len(a) - 1
	while (l <= r):
		i = (l + r) // 2
		if a[i] == b:
			break
		elif a[i] < b:
			l = i + 1
		else:
			r = i - 1
	if a[i] == b:
		return i
	else:
		return -1


def is_ascending(n):  # vai nedilstoša?
	# Pārbauda vai masīvs ir augošs (nedilstošs)
	# Ja masīvs ir nedilstošs (nav augošs), tad return True
	# Ja masīvs nav nedilstošs (nav augošs), tad return False
	# n - viendimensijas masīvs
	if len(n) == 1:
		return True

	for i in range(0, len(n)):
		if i < len(n) - 1 and n[i] > n[i + 1]:
			return False  # Nē, nav augoša, nav nedilstoša, nav konstanta (varētu būt augoša, vai nekāda)

	return True  # Jā, ir augoša (vai nedilstoša)


def is_descending(n):  # vai neaugoša?
	# Pārbauda vai masīvs ir dilstošs (neaugošs)
	# Ja masīvs ir neaugošs (nav dilstošs), tad return True
	# Ja masīvs nav neaugošs (nav dilstošs), tad return False
	# n - viendimensijas masīvs
	if len(n) == 1:
		return True

	for i in range(0, len(n)):
		if i < len(n) - 1 and n[i] < n[i + 1]:
			return False  # Nē, nav dilstoša, nav neaugoša, nav konstanta (varētu būt augoša, vai nekāda)

	return True  # Jā, ir dilstoša (vai neaugoša)

def izvade(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam
	# x - viendimensijas masīvs

	try:
		n = len(x)
		s = str(x[0])
		for i in range(1, n):
			s = s + ", " + str(x[i])
		print(s)
	except IndexError:
		print("Nav pirmskaitļu šajā intervālā.")  # Ja parādās index error, tad tas nozīme, ka šajā intervālā nav pirmskaitļu.
	except:
		print("Kļūda!")  # Citām kļūdam


def pirmskaitlu_masivs(n, drosibas_koeficients):
	# Atgriež tuple ar pirmskaitļu masīvu līdz skaitlim n bez liekām 0 un ar nodzēsto nulles skaitu. (Ja ir lieki elementi, tad funkcija to nodzes)
	# n - naturāls skaitlis (int), līdz kurām meklēsīm pirmskaitļus
	# drosibas_koeficients - drošības koeficients. Tiek reizināts ar n/log(n) un tiek izmantots masīva izmēra definēšanai.
	# Parasti, jo lielāks, jo vairāk liekas nulles būs. Pēc noklusējuma labāk, lai tās būtu aptuvēni 1.2

	if n <= 1:  # Funkcija nedarbotos jā ievadīs 0, 1 vai 2, tāpēc tas tiek atsevišķi definēts.
		return numpy.array([])
	if n == 2:
		return numpy.array([2])

	# drosibas_koeficients = 1.2  # izmantots, lai palidzētu nodefinētu masīva izmēru (size). Masīva izmēra definēšanai tiek izmantota formula n/log(n) https://en.wikipedia.org/wiki/Prime_number_theorem un https://en.wikipedia.org/wiki/Prime-counting_function
	size = math.ceil((n / math.log(n)) * drosibas_koeficients)  # aprēķina masīva garumu, izmantojot formulu n/log(n) un reizinot ar drošības koeficientu (bez viņa nevienmēr pietiks vietas)
	p = numpy.zeros(size, dtype=numpy.int32)  # izveido masīvu ar 0 vērtībām tādu garumu, kuru aprēķinaja ar formulu (n/log(n))*drosibas_koeficientu
	p[0] = 2  # pirmais pirmskaitlis
	p[1] = 3  # otrais pirmskaitlis
	j = 2
	k = 5
	try:
		while k <= n:
			i = 0
			s = round(math.sqrt(k))
			while (k % p[i]) != 0:
				i = i + 1
				if p[i] > s:
					p[j] = k
					j = j + 1
					break
			k = k + 2
		deleted_zeros_count = len(p) - len(p[:j])
		return (p[:j], deleted_zeros_count)  # [:j], lai izvadītu bez nullem
	except:
		print("Palieliniet drošības koeficientu! Nepietika vietas masīva aizpildīšanai.")

def izvade_bez_komatiem_kopigi(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam kopīgi bez komatiem (izmanto lai izvadītu masīvu kā vienu str skaitli)
	# x - viendimensijas masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + "" + str(x[i])
	print(s[::-1])


def parveide_sv_to_mas(sv, m):
	# Transformē simbolu virkni par masīvu ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	# sv - simbolu virkne, kura sastāv no cipariem
	# m - garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	n = len(sv)
	a = numpy.arange(m)
	for i in range(n):
		a[i] = int(sv[-i - 1])
	for i in range(n, m):
		a[i] = 0
	return a


def parveide_mas_to_sv(a):
	# Transformē masīvu par simbolu virkni. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
	# a - viendimensijas masīvs
	n = len(a)
	sv = ""
	for i in range(n):
		sv = str(a[i]) + sv

	try:  # try/except gadījumam ja 0 + 0
		while sv[0] == "0":
			sv = sv[1:]
		return sv

	except IndexError:  # Tas ir nepieciešams gadījumam ja lietotājs ievadīs 0 + 0 = 0.
		return "0"  # bez šim rindām būtu kļūda, kad 0 + 0


def saskaitisana(a, b):
	# Saskaita masīvu a un b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) saskaitīšanu
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	a = a[::-1]
	b = b[::-1]
	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2
	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(n + 1, dtype=numpy.int_)

	s = 0
	for i in range(n):
		s = s + m1[i] + m2[i]
		m3[i] = s % 10
		s = s // 10
	m3[n] = s

	return parveide_mas_to_sv(m3)

def izvade_bez_komatiem_kopigi(x):
	# Izvada masīva elementus pēc kārtas līdz pedējam kopīgi bez komatiem (izmanto lai izvadītu masīvu kā vienu str skaitli)
	# x - viendimensijas masīvs
	n = len(x)
	s = str(x[0])
	for i in range(1, n):
		s = s + "" + str(x[i])
	print(s)


def parveide_sv_to_mas(sv, m):
	# Transformē simbolu virkni masīvā ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	# sv - simbolu virkne, kura sastāv no cipariem
	# m - garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
	n = len(sv)
	a = numpy.arange(m)
	for i in range(n):
		a[i] = int(sv[-i - 1])
	for i in range(n, m):
		a[i] = 0
	return a[::-1]


def parveide_mas_to_sv(a):
	# Transformē masīvu simbolu virknē. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
	# a - viendimensijas masīvs
	n = len(a)
	sv = ""
	for i in range(n):
		sv = str(a[i]) + sv
	return sv


def parveide_mas_to_sv_reverse(a):
	# Transformē masīvu simbolu virknē un apgriež to
	# a - viendimensijas masīvs
	n = len(a)
	sv = ""
	for i in range(n):
		sv = str(a[i]) + sv
	return sv[::-1]


def remove_front_zeros(s):
	# Atgriež simbolu virkni bez nullem priekšā
	# s - simbolu virkne, kura sastav no cipariem, potenciāli ar nullēm priekšā
	i = 0
	while i < len(s) - 1 and s[i] == '0':
		i += 1
	s = s[i:]
	return s


def atnemsana(a, b):
	# Atņem masīvu a no b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) atņemšanai. Atgriež simbolu virkni bez nullem priekšā
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs
	if str(a) == str(b):
		return "0"

	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2
	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(n, dtype=numpy.int_)

	for i in range(-1, -n1, -1):
		if m1[i] < m2[i]:
			m1[i - 1] = m1[i - 1] - 1
			m1[i] = m1[i] + 10

	for i in range(n):
		m3[i] = m1[i] - m2[i]

	a = parveide_mas_to_sv(m3)
	a = a[::-1]
	a = remove_front_zeros(a)
	return a

def is_a_bigger_b(a, b):
	# Vai masīvs a ir lielāks vai vienāds nekā masīvs b, ja jā, tad return True. Ja nē, tad return False
	# a - pirmais viendimensijas masīvs
	# b - otrais viendimensijas masīvs
	a = parveide_mas_to_sv_reverse(a)
	b = parveide_mas_to_sv_reverse(b)
	if int(a) < int(b):
		return False
	else:
		return True

def reizinasana(a, b):
	# Sareizina masīvu a ar b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) reizināšanai
	# a - viendimensijas masīvs
	# b - viendimensijas masīvs

	a = a[::-1]
	b = b[::-1]
	n1 = len(a)
	n2 = len(b)
	if n1 > n2:
		n = n1
	else:
		n = n2

	m1 = parveide_sv_to_mas(a, n)
	m2 = parveide_sv_to_mas(b, n)
	m3 = numpy.zeros(2 * n, dtype=numpy.int_)
	s = 0
	for j in range(2 * n - 1):
		for i in range(n):
			if (0 <= j - i) and (j - i <= n - 1):
				s = s + m1[i] * m2[j - i]
		m3[j] = s % 10
		s = s // 10
	m3[n * 2 - 1] = s

	return parveide_mas_to_sv(m3)

def max_value_in_2_dimensional_array_and_its_coords(a):
	# Atgriež tuple (max_value, coords) ar divdimensijas masīva (matricas) maksimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
	# Atgriež maksimālo vērtību un kur tā vērtība atrodas pēc koordinātam
	# a - divdimensijas masīvs
	max_value = a[0][0]
	coords = [0, 0]

	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] > max_value:
				max_value = a[i][j]
				coords = [i, j]

	return (max_value, coords)


def min_value_in_2_dimensional_array_and_its_coords(a):
	# Atgriež kortežu (tuple) (min_value, coords) ar divdimensijas masīva (matricas) minimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
	# Atgriež minimālo vērtību un kur tā vērtība atrodas pēc koordinātam
	# a - divdimensijas masīvs
	min_value = a[0][0]
	coords = [0, 0]
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] < min_value:
				min_value = a[i][j]
				coords = [i, j]

	return (min_value, coords)

def check_fake_matrix_multiplication(n1, m1, n2, m2):
	# Pārbauda vai divas matricas (divdimensiju masīvi) ir ar vienādu izmēru. Pārbauda vai sakrīt 1.matricas rindas skaits ar 2.matricas rindas skaitu.
	# un pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas kolonnu skaitu. Ja abas prasības izpildās, tad return True. Ja kaut viena neizpildās, tad return False.
	# Tiek izmantota, lai pārbaudītu vai var sareizināt matricas atbilstošus elementus vai nē.
	# n1 - 1.matricas rindu skaits
	# m1 - 1.matricas kolonnu skaits
	# n2 - 2.matricas rindu skaits
	# m2 - 2.matricas kolonnu skaits
	if n1 == n2 and m1 == m2:
		return True
	else:
		return False


def check_matrix_multiplication(n1, m1, n2, m2):
	# Pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas rindu skaitu. Ja sakrīt, tad return True. Ja nē, tad return False.
	# Tiek izmantots, lai pārbaudītu vai ir iespējams sareizināt divas matricas.
	# n1 - 1.matricas rindu skaits (tā ne uz ko neietekme)
	# m1 - 1.matricas kolonnu skaits
	# n2 - 2.matricas rindu skaits
	# m2 - 2.matricas kolonnu skaits (tā ne uz ko neietekme)
	if m1 == n2:
		return True
	else:
		return False


def matrix_multiplication_integer(a, b):
	# Sareizina divu divdimensijas masīvus (divas matricas) a ar b.
	# Atgriež divdimensiju masīvu, vai ja nevar sareizināt atgriež "Kļūda"
	# a - divdimensijas masīvs
	# b - divdimensijas masīvs
	n1 = a.shape[0]
	m1 = a.shape[1]
	n2 = b.shape[0]
	m2 = b.shape[1]
	if m1 == n2:
		c = numpy.zeros((n1, m2), numpy.int_)
		for i in range(n1):
			for j in range(m2):
				for k in range(m1):
					c[i, j] = c[i, j] + a[i, k] * b[k, j]
		return c
	else:
		return "Kļūda"


def fake_matrix_multiplication(a, b):
	# Sareizina divas matricas atbilstošus elementus un atgriež atbilstošu divdimensiju masīvu
	# a - divdimensiju masīvs
	# b - divdimensiju masīvs
	c = numpy.empty((n1, m1), dtype=int)

	for i in range(n1):
		for j in range(m2):
			c[i, j] = a[i][j] * b[i][j]

	return c

def dalit_lielus_skaitlus(s, n):
	# Funkcija atgriež tuple (dalījums, atlikums) no s / n. Dalījums ir int un atlikums ir int.
	# Jāizmanto lielo skaitļu dalīšanai.
	# Dalā pēc "cipariem".
	# s - str, dalāmais
	# n - str, dalītājs
	n = int(n)
	galva = 0
	atlikums = 0
	dalijums_sv = ""

	for i in range(len(s)):

		cipars = int(s[i])
		tmp = cipars + atlikums * galva
		dalijums_sv = dalijums_sv + str(tmp // n)

		if tmp % n == 0:
			galva = 0
			atlikums = 0
		else:
			atlikums = tmp % n
			galva = 10

	dalijums = nodzest_liekas_nulles(dalijums_sv)
	dalijums = int(dalijums)

	return (dalijums, atlikums)


def nodzest_liekas_nulles(s):
	# Nodzes liekas nulles sākumā
	# s - simbolu virkne
	for i in range(len(s)):
		if s[i] != '0':
			return s[i:]
	return '0'


def long_sqrt(skaitlis):
	# Funkciju, kas kā ievadi izmanto nenegatīvu veselu skaitli un atgriež tā veselā skaitļa kvadrātsakni
	# skaitlis - int, skaitlis, no kura vajag atrast kvadrātsakni
	# Atgriež sqrt(skaitlis) kā int

	# Konvertējat ievadīto veselo nenegatīvo skaitli par simbolu virkni un saglabājam to mainīgajā
	sk_sv = str(skaitlis)  # sk_sv - skaitlis_simbolu virkne
	# Saglabājam ievadītā veselā skaitļa simbolu virknes garumu
	len_sk = len(sk_sv)  # slen_skaitlis

	# Ja ievadītā veselā skaitļa simbolu virknes garums ir nepāra skaitlis, tad pievienojam sākuma nulli, lai padarītu to par pāru simbolu virkni (garums ir pāra skaitlis)
	if len_sk % 2 == 1:
		sk_sv = '0' + sk_sv  # Ievadītā veselā skaitļa simbolu virknei sākumam pievienojam '0'
		len_sk = len_sk + 1  # Palielinām ievadītā veselā skaitļa simbolu virknes garumu par 1

	result = ''  # Tukša simbolu virkne, lai saglabātu kvadrātsaknes aprēķina rezultātu
	atlikums = 0

	# Sadalām ievadītā veselā skaitļa virknes pirmos divus ciparus [:2]
	a = int(sk_sv[:2])

	j = 1              # Atrodam pirmo "tuvinājumu"
	while j * j <= a:  # Tas ir lai atrastu pirmo ciparu kvadrātsaknei
		j = j + 1      # Var arī atrast tā:
	sakne = j - 1      # sakne = int(a**0.5) (lai nebūtu cikls)

	result = result + str(sakne)
	atlikums = a - sakne * sakne  # Atlikums
	# Cikls pār katru otro "ciparu pāri"
	for i in range(2, len_sk, 2):  # Stabiņveidā atrodam nākamo un nākamo un ... un pēdējo ciparu
		# Reizinām atlikumu ar 100 un pievienojiet nākamos divus veselā skaitļa ciparus, lai iegūtu dividendi
		a = atlikums * 100 + int(sk_sv[i:i + 2])
		cipars = 0
		temp = sakne * 20
		while (temp + cipars) * cipars <= a:
			cipars += 1
		cipars -= 1
		result += str(cipars)  # Rezultātam pievienojam iegūto ciparu
		atlikums = a - (temp + cipars) * cipars
		sakne = sakne * 10 + cipars

	return int(result)


def dalit_lielus_skaitlus(s, n):
	# Funkcija atgriež tuple (dalījums, atlikums) no s / n. Dalījums ir int un atlikums ir int.
	# Jāizmanto lielo skaitļu dalīšanai.
	# Dalā pēc "cipariem".
	# s - str, dalāmais
	# n - str, dalītājs

	s = str(s)
	n = str(n)

	galva = "0"
	atlikums = "0"
	dalijums_sv = ""

	for i in range(len(s)):

		cipars = s[i]
		cipars = parveide_sv_to_mas(cipars, len(cipars))

		b = reizinasana(atlikums, galva)
		b = parveide_sv_to_mas(b, len(b))

		tmp = saskaitisana(cipars, b)

		dalijums_sv = dalijums_sv + floor_division(tmp, n)

		if int(long_modulus(tmp, n)) == 0:
			galva = "0"
			atlikums = "0"
		else:
			atlikums = long_modulus(tmp, n)
			galva = "10"

	dalijums = nodzest_liekas_nulles(dalijums_sv)

	return (dalijums, atlikums)

def floor_division(num_str, div_str):
	# Jāizmanto lielo skaitļu dalīšanai
	# Atgriež num_str // div_str
	# num_str - simbolu virkne
	# div_str - simbolu virkne
	num_str = str(num_str)
	div_str = str(div_str)
	num = numpy.zeros(len(num_str), dtype=int)
	div = numpy.zeros(len(div_str), dtype=int)
	for i in range(len(num_str)):
		num[i] = int(num_str[i])
	for i in range(len(div_str)):
		div[i] = int(div_str[i])

	# // dalīšana
	quotient = []
	remainder = 0
	for i in range(len(num)):
		dividend = remainder * 10 + num[i]
		quotient_digit = 0
		while len(str(dividend)) >= len(div_str):
			div_str = ""
			for d in div:
				div_str += str(d)
			if dividend >= int(div_str):
				dividend -= int(div_str)
				quotient_digit += 1
			else:
				break
		quotient.append(quotient_digit)
		remainder = dividend

	quotient_str = ""
	for digit in quotient:
		quotient_str += str(digit)
	quotient_str = quotient_str.lstrip("0")
	if not quotient_str:
		quotient_str = "0"

	return quotient_str


def long_modulus(a, div_str):
	# nums_str - simbolu virkne
	# div_str - simbolu virkne
	# Atgriež a % div_str.
	# Jāizmanto lielo skaitļu dalīšanai
	a = str(a)
	div_str = str(div_str)
	num = numpy.zeros(len(a), dtype=int)
	div = numpy.zeros(len(div_str), dtype=int)
	for i in range(len(a)):
		num[i] = int(a[i])
	for i in range(len(div_str)):
		div[i] = int(div_str[i])

	remainder = 0
	for i in range(len(num)):
		dividend = remainder * 10 + num[i]
		quotient_digit = 0
		while len(div) <= len(str(dividend)):
			div_str = ""
			for d in div:
				div_str += str(d)
			if dividend >= int(div_str):
				dividend -= int(div_str)
				quotient_digit += 1
			else:
				break
		remainder = dividend

	return remainder

def long_sqrt(skaitlis):
	# Funkciju, kas kā ievadi izmanto nenegatīvu veselu skaitli un atgriež tā veselā skaitļa kvadrātsakni
	# skaitlis - int, skaitlis, no kura vajag atrast kvadrātsakni
	# Atgriež sqrt(skaitlis) kā int

	# Konvertējat ievadīto veselo nenegatīvo skaitli par simbolu virkni un saglabājam to mainīgajā
	sk_sv = str(skaitlis)  # sk_sv - skaitlis_simbolu virkne
	# Saglabājam ievadītā veselā skaitļa simbolu virknes garumu
	len_sk = len(sk_sv)  # slen_skaitlis

	# Ja ievadītā veselā skaitļa simbolu virknes garums ir nepāra skaitlis, tad pievienojam sākuma nulli, lai padarītu to par pāru simbolu virkni (garums ir pāra skaitlis)
	if len_sk % 2 == 1:
		sk_sv = '0' + sk_sv  # Ievadītā veselā skaitļa simbolu virknei sākumam pievienojam '0'
		len_sk = len_sk + 1  # Palielinām ievadītā veselā skaitļa simbolu virknes garumu par 1

	result = ''  # Tukša simbolu virkne, lai saglabātu kvadrātsaknes aprēķina rezultātu
	atlikums = 0

	# Sadalām ievadītā veselā skaitļa virknes pirmos divus ciparus [:2]
	a = int(sk_sv[:2])

	j = 1              # Atrodam pirmo "tuvinājumu"
	while int(reizinasana(j, j)) <= a:  # Tas ir lai atrastu pirmo ciparu kvadrātsaknei
		j = j + 1      # Var arī atrast tā:
	sakne = j - 1      # sakne = int(a**0.5) (lai nebūtu cikls)

	result = result + str(sakne)
	atlikums = a - int(reizinasana(sakne, sakne))  # sakne * sakne  # Atlikums
	# Cikls pār katru otro "ciparu pāri"
	for i in range(2, len_sk, 2):  # Stabiņveidā atrodam nākamo un nākamo un ... un pēdējo ciparu
		# Reizinām atlikumu ar 100 un pievienojiet nākamos divus veselā skaitļa ciparus, lai iegūtu dividendi
		a = int(str(atlikums) + "00") + int(sk_sv[i:i + 2])
		cipars = 0
		temp = int(str(sakne * 2) + "0")
		while (temp + cipars) * cipars <= a:
			cipars = cipars + 1
		cipars = cipars - 1
		result = result + str(cipars)  # Rezultātam pievienojam iegūto ciparu
		atlikums = a - (temp + cipars) * cipars
		sakne = int(str(sakne) + "0") + cipars

	return str(result)


def izvade_matricu_ar_diagonalu_summam(a):
	# Atgriež simbolu virkni, kura repzenetē "glītu diagonāļu summu". Labi atspoguļo tikai skaitļus līdz 999.
	# Piemēram:
	# 3  -1  -2  |
	# 2   3   4  |  -2
	# 5   6   7  |  3
	# ━━━━━━━━━━━━━━━
	#      5   8 | 13
	# a - divdimensijas masīvs (kvadrātiska matrica), kurai sameklējam diagonaļu summu izmantojot funkciju "diagonalu_summa"

	# a.ndim # dimensiju skaits
	# a.shape # kortežs ar masīva izmēriem

	n = a.shape[0]  # x axis
	m = a.shape[1]  # y axis
	s = ""
	c = diagonalu_summa(a)
	for i in range(n):
		for j in range(m):
			s = s + "{:4d}".format(int(a[i, j]))
		if i == 0:
			s = s + "  |  \n"
			len1 = len(s) - 3
			continue
		s = s + "  |  " + str(int((c[-1 * i]))) + "\n"

	s = s + "  " + "━" * (len1) + "\n"

	k = 0
	for i in range(n):
		if i == 0:
			s = s + "    "
			continue
		s = s + "   " + str(int((c[i])))
		k += 1

	s = s + " | " + str(int((c[k + 1])))

	return s


def diagonalu_summa(a):
	# Atgriež divdimensijas masīvu, kur labājā un apaksējā stūri elementi atspoguļo kvadrātiskas matricas diagonaļu summu
	# Ja nav iespējams aprēķināt, tad atgriež "Kļūda"
	# a - divdimensijas masīvs (kvadrātiska matrica)
	n = a.shape[0]
	m = a.shape[1]
	if m == n:
		c = numpy.zeros(2 * n)
		for k in range(1, 2 * n):
			s = 0
			if k <= n:
				# Apakšsumma
				for j in range(k):
					s = s + a[n - k + j, j]
			else:
				# augšsumma
				for j in range(k - n, n):
					s = s + a[n + j - k, j]
			c[k] = s
		return c
	else:
		return "Kļūda"


def create_random_2array(n, m):
	# Atgriež divdimensiju masīvu, kur visi elementi ir vai nu 0, vai 1 un aptuvēni 50% no visu elementu skaita ir 1.
	# n - divdimensiju masīva rindu skaits
	# m - divdimensiju masīva kolonnu skaits (sēdvietu skaits)
	a = numpy.ones((n, m))
	num_ones = int(n * m * 0.5)
	ones_count = 0
	for i in range(n):
		for j in range(m):
			if ones_count < num_ones and random.random() < 0.5:
				a[i][j] = 0
				ones_count += 1
	return a


def add_numeration_to_matrix(a):
	# Pievieno rindas un kolonnu numerāciju matricai un atgriež simbolu virkni ar matricas elementiem un ir rindas un kolonnas numerācija
	# a - divdimensijas masīvs
	s = ""
	len1 = a.shape[1]
	for j in range(len1 + 1):
		s = s + "{:3d}".format(j)  # izmantot formāta norādītāju, lai nodrošinātu nepieciešāmu atstarpi
	s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

	n = a.shape[0]
	for i in range(n):
		s = s + "{:3d}".format(i + 1)  # rindas numurs
		for j in range(len1):
			s = s + "  " + a[i, j]
			#s = s + "{:3.0f}".format(a[i, j])
		s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

	return s


def choose_what_change_to_one(a, sk):
	# Biļetes pirkšanai. Ja viss ir izpārdots (ja visi ir 1), tad print("Izpārdots!\n")
	# Var izvelēties, kuru ciparu izmainīt uz 1.
	# 1 -> 1 (vieta aizņemta)
	# 0 -> 1 (print("\nBiļete nopirkta!\n"))
	# a - divdimensijas masīvs (matrica)
	# sk - vieninieku skaits. Ja ir lielāks nekā n x m, tad izpārdots.

	n, m = a.shape

	if sk >= n * m:
		print("\nŠodien viss ir izpārdots!\n")
		return

	while True:
		r = input("Ievadiet vēlamo rindas numuru biļetes nopirkšanai ==> ")
		while not is_natural_or_zero(r):
			r = input("Kļūda! Ievadiet vēlamo naturālo rindas numuru biļetes nopirkšanai ==> ")
		r = int(r)

		s = input("Ievadiet vēlamo sēdvietu numuru ==> ")
		while not is_natural_or_zero(s):
			s = input("Kļūda! Ievadiet vēlamo naturālo sēdvietu numuru biļetes nopirkšanai ==> ")
		s = int(s)

		try:
			if r == 0 and s == 0:
				return print("Paldies, ka izmantojāt mūsu pakalpojumus!")

			elif r == 0 or s == 0:
				print("\nNekorekta ievade!\n")
				print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))

			elif a[r - 1, s - 1] == 1:
				print("\nJusu izvēlēta vieta " + str(r) + ".rindā " + str(s) + ".sēdvietā ir aizņemta!\n")
				print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))

			elif a[r - 1, s - 1] == 0:
				a[r - 1, s - 1] = 1
				print("\nBiļete nopirkta! Jūsu vieta ir " + str(r) + ".rindā " + str(s) + ".sēdvietā.\n")
				print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))
				sk += 1

			if sk >= n * m:
				print("Šodien viss ir izpārdots!\n")
				print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))
				return
		except IndexError:
			print("\nIr jāievāda reālu sēdvietu!\nUz redzēšanos!")
			quit()


def count_ones(a):
	# Saskaita vieninieku skaitu noteiktā masīvā a un atgriež to int skaitļi
	# a - divdimensijas masīvs (matrica)
	count = 0
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			if a[i, j] == 1:
				count += 1
	return count


def replace_ones_to_a_zeros_to_b(arr):
	# Izmaina visus divdimensija masīva vieniniekus to A, bet nulles to B
	# 1 -> A
	# 0 -> B
	# arr - divdimensijas masīvs (matrica)
	new_arr = numpy.empty(arr.shape, dtype='str')
	new_arr[arr == 1] = 'A'
	new_arr[arr == 0] = 'B'
	return new_arr

def is_labirint_path(i, j, lab, tr):
	# Atgriež masīvu found_path (atrasts ceļš), kurš sastāv no frāzem "Pa labi", "Uz leju".
	# Rekursīvi atrod ceļu, lai izietu no labirinta (var iet tikai no mazākas vērtības uz lielāku (vai vienādu)).
	# i - 0 (parasti)
	# j - 0 (parasti)
	# lab - divdimensijas masīvs ar labirinta segmēnta vērtībam.
	# tr - trase
	# trase = numpy.empty(path_length, "O")
	# path_length = n + m - 2

	n = lab.shape[0] - 1
	m = lab.shape[1] - 1

	if (i == n) and (j == m):
		return True
	else:
		found_path = False
		if (i < n) and (lab[i + 1, j] >= lab[i, j]):
			tr[i + j] = "Uz leju"
			found_path = is_labirint_path(i + 1, j, lab, tr)
		if not found_path and (j < m) and (lab[i, j + 1] >= lab[i, j]):
			tr[i + j] = "Pa labi"
			found_path = is_labirint_path(i, j + 1, lab, tr)
		return found_path


def izvade(a):
	# Atgriež simbolu virkni, kura reprezentē noteikto matricu, kā simbolu virkni stābiņveidā.
	# -1 pārkonvertē kā X.
	# X - nejauši šķēršļi (-1)
	# a - divdimensijas masīvs (matrica)

	# a.ndim # dimensiju skaits
	# a.shape # kortežs ar masīva izmēriem

	n = a.shape[0]  # x axis
	m = a.shape[1]  # y axis
	s = "\n"
	for i in range(n):
		for j in range(m):
			if a[i, j] == -1:
				s = s + "   X"
			else:
				s = s + "{:4d}".format(int((a[i, j])))
		s = s + "\n"
	return s


def get_column(a):
	# a - viendimensijas masīvs
	# [1, 2, 3] konvertēsies
	# 1
	# 2
	# 3
	# Atgriež str masīva elementus, kā kolonnu

	col_str = ""
	for elem in a:
		col_str = col_str + str(elem) + "\n"
	return col_str


def random_negative_fill(a, chance):
	# chance = 0.05 (5%) no kopēja skaita būs šķēršļi (-1)
	# chance - skaitlis (float). Jo lielāka šī vērtība, jo lielāka iespēja, ka būs vairāk "segmēntu" ar -1.
	# a - divdimensijas masīvs (labirints)
	# Atgriež divdimensijas masīvu (matricu) kurš ir aizpildīts ar -1.
	# -1 skaits ir chance * masīva_kopējais_elementu_skaits (chance == 0.05 (5%))

	a_shape = a.shape

	# Aprēķinat ievietojamo negatīvo vērtību skaitu
	num_negatives = int(a_shape[0] * a_shape[1] * chance)

	# Izvēlieties nejaušus rindu un kolonnu "segmēntus", lai ievietotu negatīvas vērtības
	indices = numpy.zeros((num_negatives, 2), dtype=int)  # indices ir nulles masīvs, kura izmērs ir (num_negatives, 2), un tajā tiek glabāti izvēlēto "segmētu" rindu un kolonnu koordinātas.
	# Pēc nejauši izvēlēto koordinātu noteikšanas row_idx un col_idx, tiek pārbaudīts, vai tās nav jau aizpildītas ar -1, un
	# vai tās nav sākumpunkts (0, 0) vai beigu punkts (a_shape[0] - 1, a_shape[1] - 1), kas atbilst labirinta sākumam un beigām.
	# Ja nosacījumi tiek izpildīti, koordinātas tiek ievietotas masīvā indices un while cikls tiek pārtraukts.
	for i in range(num_negatives):
		while True:  # Tiek izmantots while cikls, lai izvēlētos "segmētu" koordinātas, kas nav jau iepriekš aizpildītas ar -1.
			row_idx = numpy.random.randint(a_shape[0])
			col_idx = numpy.random.randint(a_shape[1])
			if a[row_idx, col_idx] != -1 and not (row_idx == 0 and col_idx == 0) and not (row_idx == a_shape[0] - 1 and col_idx == a_shape[1] - 1):
				indices[i] = (row_idx, col_idx)
				break

	# Aizpildit nejauši izvēlētus "segmēntus" ar -1

	row_indices = indices[:, 0]
	col_indices = indices[:, 1]

	for i in range(len(row_indices)):
		row_idx = row_indices[i]
		col_idx = col_indices[i]
		a[row_idx, col_idx] = -1

	return a

def determinants(x):
	# Rekursīvi atrod matricas x determinanta vērtību.
	# Atgriež determinanta vērtību kā skaitļi int no matricas x.
	# x - kvadrātiska n x n divdimensijas numpy masīvs (matrica ar izmēriem n x n)

	n = len(x)
	if n == 1:
		return x[0, 0]
	det = 0
	zime = 1
	for i in range(n):
		xx = numpy.empty((n - 1, n - 1))
		for j in range(1, n):
			z = 0
			for k in range(n):
				if k != i:
					xx[j - 1, z] = x[j, k]
					z = z + 1
		y = determinants(xx)
		det = det + zime * x[0, i] * y
		zime = -zime  # + - + - + ...
	return det

def matrix_to_string_float(matrix):
	# Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n.
	# Ja vērtība ir vesels skaitlis, tā tiek attēlota bez komata. Pretējā gadījumā tas tiek attēlots ar komatu.
	# Funkcija atrod arī maksimālo vērtību garumu matricā un papildina nepieciešamus skaitļus ar tujšumiem " ", lai tie būtu pareizi izlīdzināti.
	# matrix - matrica (divdimensijas numpy masīvs ar izmēriem n x m).

	rindas = len(matrix)
	kolonnas = len(matrix[0])
	max_len = 0

	for i in range(rindas):  # atrod max_len, lai uzzinātu cik atkāpes ir nepieciešāmas
		for j in range(kolonnas):
			value = matrix[i][j]
			if value == int(value):
				value_len = len(str(int(value)))
			else:
				value_len = len(str(float(value)))
			if value_len > max_len:
				max_len = value_len

	sv = ""
	# izveido matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n un izlidzina to pēc skaitļa ar maksimālu garumu
	for i in range(rindas):
		for j in range(kolonnas):
			value = matrix[i][j]
			if value == int(value):
				value = int(value)
			else:
				value = str(float(value))
			atkape = " " * (max_len - len(str(value)))
			sv += atkape + str(value)
			if j < kolonnas - 1:
				sv = sv + " "
		sv = sv + "\n"

	return sv

def transponenta(a):
	# Atgriež transponētu matricu a b[i, j] = a[j, i]
	# a - divdimensijas masīvs (matrica)

	n = a.shape[0]  # x axis
	m = a.shape[1]  # y axis
	b = numpy.empty((m, n))
	for i in range(m):
		for j in range(n):
			b[i, j] = a[j, i]
	return b


def adjugate_matrix(a):
	# Atgriež dotās kvadrātmatricas a adjunktu matricu a*.
	# a - nXn divdimensijas masīvs (kvadrātmatrica)

	n = a.shape[0]

	if n == 1:
		# Ja matrica is 1x1, tas adjunktu matrica ir tas paša matrica
		return a

	adj = numpy.zeros((n, n))  # Izveidojam tukšo mainīgu ar nullem, kura būs adjunktu matrica a* matricai a
	for i in range(n):
		for j in range(n):
			# Izveidojam paligmatricu, noņemot rinda i un kolonnu j no sākotnējās matricas a
			paligmatrica = []
			for k in range(n):
				if k != i:
					rinda = []
					for l in range(n):
						if l != j:
							rinda.append(a[k, l])
					paligmatrica.append(rinda)

			# Konvertējam paligmatricu par NumPy masīvu
			paligmatrica = numpy.array(paligmatrica)
			# Aprēķinam paligmatricas determinantu
			det = determinants(paligmatrica)
			# Reizinām determinantu ar (-1)^(i+j)
			zime = (-1) ** (i + j)
			# Adjunktas matricas elements (i,j) tas ir determinants no palīgmatricas ar zimes reizinājumu (-1 vai +1)
			adj[i, j] = det * zime

	return adj


def inverse_matrix_by_def(a):
	# Atgriež inverso matrīcu (divdimensijas masīvu) izmantojot transponenta, determinants un adjugate_matrix funckijas
	# a - divdimensijas masīvs (kvadrātiska matrica)

	adj = adjugate_matrix(a)
	transponent_adj_matrix = transponenta(adj)
	det = determinants(a)
	if det == 0:
		return "Neēksiste"
	else:
		inverse_det = 1 / determinants(a)
		inverse_a = inverse_det * transponent_adj_matrix
		return inverse_a

def random_set_numbers_1_to_35():
	# Atgriež kopu ar nejaušiem skaitļiem kuri neatkartojas no 1 līdz 35. [1, 35].
	# a - set (kopa) - tukša kopa.

	a = set()
	while len(a) < 5:
		b = random.randint(1, 35)
		if b not in a:
			a.add(b)

	return a


def ievadiet_n_skaitlus_seta(n, max_num):
	# Procedura kura ļauj ievādit n skaitļus un ieliekt tos kop (set'ā)
	# n - cik skaitļus ievādīt lietotājam (int)
	# max_num - maksimālais skaitlis līdz kuram tiek veikta loterija (int)

	a = set()  # a - tukša kopa (set)
	for i in range(1, n + 1):
		while True:
			b = input("Ievadiet " + str(i) + ". skaitli ==> ")
			try:
				b = int(b)
				if b < 1 or b > max_num:
					print("Skaitlim jābūt veselam skaitlim no 1 līdz " + str(max_num) + ".")
				elif b in a:
					print("Šis skaitlis jau eksistē, lūdzu ievadiet citu skaitli!")
				else:
					a.add(b)
					break
			except ValueError:
				print("Ievadei jābūt skaitlim!")
				continue

	return a


def laimests_5_35_izloze(a, b):
	# a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
	# b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

	x = a.intersection(b)
	len1 = len(x)

	if len1 == 5:
		return "Lielais laimests"
	elif len1 == 4:
		return "Vidējais laimests"
	elif len1 == 3:
		return "Mazais laimests"
	else:
		return "Nav laimesta"


def cik_atminejat(a, b):
	# Atgriež cik skaitļus Jūs laimējat (atrod kopas šķēlumu)
	# a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
	# b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

	x = a.intersection(b)
	len1 = len(x)

	return len1


def print_set(a):
	# Izvada (print) uz ekrāna kopu. Bet tas to neatgriež.
	# Jāizsauc vienkarši print_set(a)
	# a - kopa (set)

	elements = sort_ievietosana_augosa(list(a))
	# Iterējam cauri elementu indeksiem un izdrukājiem tos, atdalot tos ar komatiem
	for i in range(len(elements)):
		if i == len(elements) - 1:
			# Ja elements ir pēdējais, izdrukām to bez komata
			print(elements[i])
		else:
			# Ja elements nav pēdējais, izdrukājam to ar komatu. end="", lai nebūtu pārejas uz jauno rindu kā \n
			print(str(elements[i]) + ", ", end="")

def karsu_izdale_n_speletajiem_pa_m_kartim(n, m):
	# Atgriež simbolu virknī šāda veidā ar spēlētaju kārtu un viņa kārtem:
	# 1.spēlētājs: ♦6 ♦5 ♠J ♠5 ♠8 ♣A
	# 2.spēlētājs: ♦8 ♠9 ♥6 ♠4 ♣9 ♥Q
	# 3.spēlētājs: ♠7 ♣7 ♠6 ♦10 ♠K ♥4
	# ...
	# n.spēlētajs: ...
	# To vajag print'ēt atsevišķi print(karsu_izdale_n_speletajiem_pa_m_kartim(4, 6))

	# n - int - spēlētaju skaits (naturāls skaitlis)
	# m - int - karšu skaits (naturāls skaitlis)

	a = set(("♣", "♦", "♥", "♠"))
	b = set(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))

	c = set()

	for i in a:
		for j in b:
			c.add(i + j)

	res = ""
	for i in range(1, n + 1):
		sv = str(i) + ".spēlētājs:"
		for j in range(m):
			sv = sv + " " + c.pop()
		res = res + sv + "\n"
	return res

def print_set(a):
	# Izvada (print) uz ekrāna kopu. Bet tas to neatgriež.
	# Jāizsauc vienkarši print_set(a)
	# a - kopa (set)

	elements = sort_ievietosana_augosa(list(a))
	# Iterējam cauri elementu indeksiem un izdrukājiem tos, atdalot tos ar komatiem
	for i in range(len(elements)):
		if i == len(elements) - 1:
			# Ja elements ir pēdējais, izdrukām to bez komata
			print(elements[i])
		else:
			# Ja elements nav pēdējais, izdrukājam to ar komatu. end="", lai nebūtu pārejas uz jauno rindu kā \n
			print(str(elements[i]) + ", ", end="")


def choose_pair(students_prepare):
	# Atgriež pirmu masīva students_prepare lementu un nodzes to no saraksta students_prepare.
	# students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
	# students_prepare ir saraksts ar kortēžiem iekšā. [(studenta numurs, biļete), (studenta numurs, biļete), ... (studenta numurs, biļete)],

	first_pair = students_prepare[0]  # Paņem pirmo kortēžu ar studentu un biļeti.
	students_prepare.remove(first_pair)  # Nodzēs studentu no saraksta kuri gatavojas (jo viņš jau atbild),
	return first_pair


def choose_random_pair(students_prepare, students, exam_tickets):
	# Atgriež nejaušu (student, exam_ticket) kortēžu, no saraksta students (studenti, kas vel nav nokārtojusi eksāmenu un vēl nav eksāmena telpā).
	# Nejauši izvēlas studentu no tiem, kas vēl nav nokārtojusi eksāmenu un nesež telpā. Atgriež kortežu ar studentu un eksāmena biļeti. (student, exam_ticket),
	# students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
	# students - kopa ar visiem studenti kuri nav eksāmena telpā un pagaidam nav nokārtojusi eksāmenu.
	# exam_tickets - kopa ar visam biļetem no A līdz Z.

	if len(students) == 0:
		return None
	student = students.pop()
	exam_ticket = exam_tickets.pop()
	return (student, exam_ticket)


def print_pairs(pairs):
	# Glīti izvāda sarakstu pairs, kas reprēzentē studentus ar biļētem kuri sēž telpā un gatavojas eksāmenam.
	# Piemērs:
	# Ievade tāds saraksts: [(36, S), (50, T), (37, D), (42, R), (19, W), (22, U), (41, M), (44, Q), (52, P), (38, H)].
	# Funkcija atgriež tādu simbolu virkni: 36-S, 50-T, 37-D, 42-R, 19-W, 22-U, 41-M, 44-Q, 52-P, 38-H
	# pairs - saraksts ar kortežiem ar divam vērtībam [(students, biļete), (students, biļete), ... , (students, biļete)].

	for i in range(len(pairs)):
		if i == len(pairs) - 1:
			print(str(pairs[i][0]) + "-" + str(pairs[i][1]))
		else:
			print(str(pairs[i][0]) + "-" + str(pairs[i][1]) + ", ", end="")


def convert_int_to_str_in_set_in_range(n, m, kopa):
	# Metode (neko neatgriež), kura izmaina visas int vērtības kopā uz str.
	# Piemēram:
	# {5, 33, 14, 13, 11} -> {'5', '33', '14', '13', '11'}.
	# convert_int_to_str_in_set_in_range(1, 55, students).
	# kopa - set, kopa, kurai gribāt visas int vērtības izmainīt uz str. Piemēram: 1 -> "1"
	# n - int, no cik (parasti no 1).
	# m - int, līdz cik līdz m-1 (šeit līdz 55, bet funkcijai izmainīs int uz str līdz 54).

	for i in range(n, m):
		kopa.add(str(i))


def exam_tickets_words_in_range(n, m, exam_tickets):
	# Metode (neko neatgriež), kura piepildina tukšo kopu exam_tickets ar simboliem no ASCII koda no n līdz m str veidā.
	# exam_tickets - tukša kopa, kurai jābut kopai ar eksāmena biļētiem no A līdz Z.
	# n - int, no cik (ASCII kods simbols).
	# m - int, līdz cik (ASCII kods).
	# (65, 91) - lielajiem latiņu burtiem.
	# Piemērs: exam_tickets_words_in_range(65, 91, exam_tickets).

	for i in range(n, m):
		exam_tickets.add(chr(i))


def start_students_number(n, students, exam_tickets):
	# Atgriež students_prepare sarakstu, kura sastav no kortēžiem [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
	# un šeit ir n šādu kortežu (student, exam_ticket).
	# n - int, cik "start" studentus paņemt? (10 šajā gadījumā). Tas ir cik studentus "izlozēsim" kartot eksāmenu pirmājiem.
	# students - set, kopa ar visiem studentiem, kuri nav ienākuši eksāmenas telpā un vēl nav nokārtojusi eksāmenu. No viņiem paņemsim pirmus 10 studentu.
	# exam_tickets - set, kopa ar visiem eksāmena biļētem, kuri nav pie studentiem.

	for i in range(n):
		student = students.pop()
		exam_ticket = exam_tickets.pop()
		students_prepare.append((student, exam_ticket))
	return students_prepare


def exam_simulation(students_prepare):
	# Simulē eksāmena norisināšanas.
	# students_prepare - saraksts veidā [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
	# Kad 1. students atbildējis, viņa biļete tiek atlikta atpakaļ eksāmena biļešu "kaudzē" un nāk nākamais students un izvēlās uz labu laimi vienu eksāmena biļeti no eksāmena biļešu "kaudzes".
	# Tā process tiek atkārtots, kamēr visi studenti ir noeksaminēti.
	# Paziņo uz ekrāna, kādā secība studenti tika eksaminēti un kādu eksāmena biļeti katrs students saņēma.

	exam = True  # Karogs ir True, kamēr students_prepare != 0 (kāmer eksamenācijas telpā ir palikuši cilvēki, tad eksāmens turpinās).
	while exam:  # Kamēr eksāmens ir True
		if len(students_prepare) == 0:  # Ja nav nevienu cilvēku eksamenācijas telpā, tad eksāmens beidzās.
			print("Eksāmens beidzās!")
			exam = False  # eksāmens beidzās.
		else:
			pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
			print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam informāciju, kurš students atbild (kreisāis) un ar kādu biļeti viņš ir.
			exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
			print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.

			if len(students) == 0:  # Ja visi studenti jau ir ienākuši eksāmenā telpā, tad jau mēs vairs nevienu neaicināsim atkāl uz eksāmenu. (jo tie ir pēdējie studenti, kuri karto eksāmenu).
				print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.
				pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
				print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atbild un ar kādu biļeti.
				exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
				print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.
				print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.

			else:
				atnac = choose_random_pair(students_prepare, students, exam_tickets)  # Ja nav visi studenti ir ienākuši eksāmenā telpā, tad vajag aicināt nākamos (atnac) studentus uz eksāmenu (jo tie ir palikuši un vēl nenokārtoja eksāmenu). Nejauši izvelāmies studentu un viņam biļēti, no tiem, kuri vēl nav nokārtojuši.
				print("Atnāc " + str(atnac[0]) + ". students un izvilka biļeti " + str(atnac[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atnāca un kādu biļeti paņēma.
				students_prepare.append(atnac)  # Pievienojam sarakstam ar kortēžiem students_prepare [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)] jauno kortēžu, ar studentu kurš atnāca un izvēlējas biļeti.
				print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.

class Taisnsturis:
	# Klase taisnstūra laukuma un perimetra aprēķināšanos.
	def __init__(self, garums, platums):
		self.garums = garums
		self.platums = platums

	def laukums(self):
		# Aprēķina taisnstūra laukumu, reizinot tā garumu ar tā platumu.
		return self.garums * self.platums

	def perimetrs(self):
		# Aprēķina taisnstūra perimetru, saskaitot garumu un platumu un reizinot ar 2.
		return (self.garums + self.platums) * 2




class Trijsturis:
	# Trijstūra klase.
	def __init__(self, a, b, c):
		# Iniciālizē a, b, c.
		# a - trijstūra pirmās malas garums.
		# b - trijstūra otrais malas garums.
		# c - trijstūra trešais malas garums.
		# self - trijstūris.
		self.a = a
		self.b = b
		self.c = c

	def pusperimetrs(self):
		# Aprēķina trijstūra pusperimetru.
		p = (self.a + self.b + self.c) / 2
		return p

	def laukums(self):
		# Aprēķina trijstūra laukumu ar Herona formulu.
		p = Trijsturis.pusperimetrs(self)
		return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # self.garums * self.platums

	def perimetrs(self):
		# Aprēķina trijstūra perimetru.
		return self.a + self.b + self.c

	def ievilkta_rinka_radiuss(self):
		# Aprēķina trijstūra ievilkta riņķa līnijas rādiusu r.
		return Trijsturis.laukums(self) / Trijsturis.pusperimetrs(self)  # regulāram r = (a*sqrt(3))/6

	def apvilkta_rinka_radiuss(self):
		# Aprēķina trijstūra apvilkta riņķa līnijas rādiusu R.
		return self.a * self.b * self.c / (4 * Trijsturis.laukums(self))  # regulāram R = (a*sqrt(3))/6


class Kalkulators:
	# Kalkulatora klase

	@staticmethod
	def saskaitit(a, b):
		# Saskaita a un b
		# a - float skaitlis
		# b - float skaitlis
		return a + b

	@staticmethod
	def atnemt(a, b):
		# Atņem a un b
		# a - float skaitlis
		# b - float skaitlis
		return a - b

	@staticmethod
	def reizinat(a, b):
		# Sareizina a un b
		# a - float skaitlis
		# b - float skaitlis
		return a * b

	@staticmethod
	def dalit(a, b):
		# Izdala a ar b
		# a - float skaitlis
		# b - float skaitlis
		if a == 0 and b == 0:
			return "Nav definēts"
		if a != 0 and b == 0:
			return "Nedrīkst dalīt ar 0"
		return a / b


class Check:
	# Klase ar visam funkcijam, kuri ir noderīgi ievaddates pārbaudei.

	@staticmethod
	def is_real(value):
		# Pārbauda vai simbolu virkne (value) ir reāls skaitlis no (-inf, +inf).
		# value - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			float(value)
			return True
		except:
			return False

	@staticmethod
	def is_real_positive(value):
		# Pārbauda vai simbolu virkne (value) ir reāls pozitīvs skaitlis no (0, +inf).
		# value - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			value = float(value)
			if value > 0:
				return True
			else:
				return False
			return True
		except:
			return False

	@staticmethod
	def is_real_positive_or_zero(value):
		# Pārbauda vai simbolu virkne (value) ir reāls pozitīvs skaitlis vai nulle [0, +inf).
		# value - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			value = float(value)
			if value >= 0:
				return True
			else:
				return False
			return True
		except:
			return False

	@staticmethod
	def is_natural(value):
		# Pārbauda vai simbolu virkne (value) ir naturāls skaitlis 1, 2, 3, 4, 5, ...
		# value - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			value = int(value)
			if value > 0:
				return True
			else:
				return False
		except:
			return False

	@staticmethod
	def is_whole(value):
		# Pārbauda vai simbolu virkne (value) ir vesels skaitlis ... -3, -2, -1, 0, 1, 2, 3 ...
		# value - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			value = int(value)
			if value >= 0:
				return True
			else:
				return False
		except:
			return False

	@staticmethod
	def is_even(x):
		# Pārbauda vai simbolu virkne (value) ir pāra skaitlis 2n.
		# x - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			x = int(x)
			if x % 2 == 0:
				return True
			else:
				return False
		except:
			return False

	@staticmethod
	def is_odd(x):
		# Pārbauda vai simbolu virkne (value) ir nepāra skaitlis 2n + 1.
		# x - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			x = int(x)
			if x % 2 != 0:
				return True
			else:
				return False
		except:
			return False

	@staticmethod
	def is_prime(n):
		# Pārbauda vai simbolu virkne (value) ir pirmskaitlis.
		# n - str, simbolu virkne, kurā reprezente skaitļi.
		try:
			n = int(n)
		except:
			return False
		else:
			if n <= 1:
				return False
			for i in range(2, n):
				if (n % i) == 0:
					return False
			return True

	@staticmethod
	def can_make_triangle(a, b, c):
		# Pārbauda vai no šiem skaitļiem var izveidot trijstūri.
		# a - float skaitlis intervāla (0, +inf)
		# b - float skaitlis intervāla (0, +inf)
		# c - float skaitlis intervāla (0, +inf)
		if (a + b <= c) or (a + c <= b) or (b + c <= a):
			return False
		else:
			return True

	def ievade(description, error_desciption):
		# Metode skaitļa ievādei. Jāizmanto tāda veidā: n = Check.ievade("Ievadiet --- ", "Kļūda! ---") (nevajag rakstīt ==>).
		# description - str, simbolu virkne, kurā tiek parādīta, kad tiek paprasīts ievādit skaitļi.
		# error_desciption - str, simbolu virkne, kurā tiek parādīta, kad tiek paziņota kļūda.
		n = input(description + "==> ")
		while True:
			if Check.is_real(n):  # is_real(n):  # Check.(funkcija, kas pārbauda nepieciešamo)
				return float(n)
			print(error_desciption)
			n = input(description + "==> ")

class Kopa:
	# Klase kopa.
	def __init__(self):
		# Inicializēsim tukšo kopu.
		# self - kopa (objekts Kopa()).

		self.__kopa = []

	def saturs(self):
		# Atgriež kopas saturu.
		# self - kopa (objekts Kopa()).

		return self.__kopa

	def izdrukat(self):
		# Izdrukā glīta veidā kopas saturu.
		# Tukša kopa tiek attēlota ar Ø simbolu.
		# Piemēram, izdrūka { 1 2 3 }.
		# self - kopa (objekts Kopa()).

		sk = len(self.__kopa)
		if sk == 0:
			sv = "Ø"  # Tukša kopa ∅
		else:
			sv = "{ "
			for i in self.__kopa:
				sv = sv + str(i) + " "
			sv = sv + "}"
		print(sv)

	def pievienot(self, elements):
		# Ļauj pievienot vai nu vienu elementu kopai, vai nu elementus kā list (sarakstu), vai tuple (kortežu).
		# Piemēram, a.pievienot([1, 3, 4]), vai b.pievienot((1, 2, 3)), vai c.pievienot(2).
		# self - kopa (objekts Kopa()).
		# elements - elements vai elementi, kurus gribam pievienot kopai.

		if type(elements) == list:
			for el in elements:
				if el not in self.__kopa:
					self.__kopa.append(el)

		elif type(elements) == tuple:
			for el in elements:
				if el not in self.__kopa:
					self.__kopa.append(el)
		else:
			paz = True
			for i in self.__kopa:
				if i == elements:
					paz = False
			if paz:
				self.__kopa.append(elements)

	def izmest(self, elements):
		# Nodzēs norādītu vienu elementu (elements) no kopas.
		# Ja tāda elementa nav, tad neko nenodzēs.
		# Līdzīgs set discard.
		# self - kopa (objekts Kopa()).
		# elements - elements vai elementi, kurus gribam pievienot kopai.

		for i in self.__kopa:
			if i == elements:
				self.__kopa.remove(elements)

	def nonemt(self, elements):
		# Nodzēs norādītu vienu elementu (elements) no kopas.
		# Ja tāda elementa nav, tad raise ValueError, ka tāds elements nav kopā.
		# Līdzīgs set remove.
		# self - kopa (objekts Kopa()).
		# elements - elements vai elementi, kurus gribam pievienot kopai.

		if elements not in self.__kopa:
			raise ValueError(f"{elements} nav kopā. Nevar noņemt elementu, kuru nav. Izmantojiet 'izmest'.")  # is not in the kopa

		for i in self.__kopa:
			if i == elements:
				self.__kopa.remove(elements)

	def vai_pieder(self, elements):
		# Pārbauda vai kopai piedēr norādītais elements.
		# Atgriež True, ja norādītais elements piedēr kopai.
		# Atgriež False, ja norādītais elements nepiedēr kopai.
		# self - kopa (objekts Kopa()).
		# elements - elements vai elementi, kurus gribam pievienot kopai.

		for i in self.__kopa:
			if i == elements:
				return True
		return False

	def izdzest(self):
		# Pārverš kopu par tukšo kopu un atgriež to.
		# self - kopa (objekts Kopa()).

		self.__kopa = []
		return self.__kopa

	def atjaunot(self, elements):
		# Vai pārmainīt visas vērtības kopai.
		# Piemēram, a.update([4, 5, 6, 7]).
		# Atjauno kopu līdzīgi, ka set update.
		# self - kopa (objekts Kopa()).
		# elements - elements vai elementi, kurus gribam pievienot kopai.

		self.__kopa = []

		if type(elements) == list:
			for el in elements:
				if el not in self.__kopa:
					self.__kopa.append(el)

		elif type(elements) == tuple:
			for el in elements:
				if el not in self.__kopa:
					self.__kopa.append(el)
		else:
			paz = True
			for i in self.__kopa:
				if i == elements:
					paz = False
			if paz:
				self.__kopa.append(elements)

	def pop(self):
		# Atgriež vienu nejaušu elementu no kopas.
		# Paņem nejaušu kopas elementu līdzīgi, ka set pop.
		# Ja mēģināsim izņemt nejaušu elementu no tukšas kopas, tad print("Kļūda! Nevar izņemt elementu no tukšas kopas.").
		# self - kopa (objekts Kopa()).

		try:
			a = random.choice(self.__kopa)
		except:
			print("Kļūda! Nevar izņemt elementu no tukšas kopas.")  # Raise Exception
		else:
			self.__kopa.remove(a)
			return a

	@staticmethod
	def apvienot(a, b):
		# Apvieno divas kopas a un b.
		# A U B
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = copy.deepcopy(a)
		x = a.saturs()
		y = b.saturs()
		for i in y:
			if i not in x:
				c.pievienot(i)
		return c

	# Var izmantot arī šo metodi, "apvienot1" nevis "apvienot".
	# Metode "apvienot1" neizmanto deepcopy.
	'''
    def apvienot1(a, b): # tas pats, bet bez deepcopy
        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        for z in x:
            c.pievienot(z)
        for z in y:
            if z not in x:
                c.pievienot(z)

        return c
    '''

	@staticmethod
	def vai_parklajas(a, b):
		# Pārbauda vai divas kopas a un b pārklājas.
		# Atgriež True, ja kopas pārklājas (ir vismaz viens kopīgs elements).
		# Atgriež False, ja kopas nepārklājas (nav nevienā kopīga elementa).
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = Kopa()
		x = a.saturs()
		y = b.saturs()
		tuksa_kopa = Kopa()

		d = c.skelums(a, b)
		if Kopa.vai_vienadas(d, tuksa_kopa):
			return False
		return True

	@staticmethod
	def vai_neparklajas(a, b):
		# Pārbauda vai divas kopas a un b nepārklājas (tas pats kā vai_parklajas, bet tikai negācija).
		# Atgriež False, ja kopas pārklājas (ir vismaz viens kopīgs elements).
		# Atgriež True, ja kopas nepārklājas (nav nevienā kopīga elementa).
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = Kopa()
		x = a.saturs()
		y = b.saturs()
		tuksa_kopa = Kopa()

		d = c.skelums(a, b)
		if Kopa.vai_vienadas(d, tuksa_kopa):
			return True
		return False

	@staticmethod
	def skelums(a, b):
		# Atgriež kopas a un b šķēlumu (A ∩ B).
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = Kopa()
		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i in y:
				c.pievienot(i)
		return c

	@staticmethod
	def simetriska_starpiba(a, b):
		# Atgriež kopas a un b simetrisku starpību (A △ B).
		# Pēc formulas: A △ B = (A \ B) U (B \ A).
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = Kopa()
		d = Kopa.starpiba(a, b)
		f = Kopa.starpiba(b, a)
		c = Kopa.apvienot(d, f)
		return c

	@staticmethod
	def starpiba(a, b):
		# Atgriež kopas a un b starpību (A \ B).
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		c = Kopa()
		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i not in y:
				c.pievienot(i)
		return c

	@staticmethod
	def vai_vienadas(a, b):
		# Pārbauda vai divas kopas a un b ir vienādas (A == B).
		# Atgriež True, ja divas kopas ir vienādas.
		# Atgriež False, ja divas kopas nav vienādas.
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i not in y:
				return False

		for i in y:
			if i not in x:
				return False

		return True

	@staticmethod
	def vai_nav_vienadas(a, b):
		# Pārbauda vai divas kopas a un b nav vienādas (A != B).
		# Atgriež True, ja divas kopas nav vienādas.
		# Atgriež False, ja divas kopas ir vienādas.
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i not in y:
				return True

		for i in x:
			if i not in y:
				return True

		return False

	@staticmethod
	def vai_apakskopa(a, b):
		# Pārbauda vai a ir apakškopa b. A ⊆ B.
		# Atgriež True, ja a ir apakškopa b.
		# Atgriež False, ja a nav apakškopa b.
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i not in y:
				return False
		return True

	@staticmethod
	def vai_stingra_apakskopa(a, b):
		# Pārbauda vai a ir stingra apakškopa b. A ⊂ B. (ja A un B ir vienādas kopas, tad A nav stingra apakškopa B).
		# Atgriež True, ja a ir stingra apakškopa b.
		# Atgriež False, ja a nav stingra apakškopa b.
		# a - 1.kopa (objekts Kopa()).
		# b - 2.kopa (objekts Kopa()).

		x = a.saturs()
		y = b.saturs()
		for i in x:
			if i not in y:
				return False

		if Kopa.vai_vienadas(a, b):
			print(Kopa.vai_vienadas(a, b))
			return False
		else:
			return True


class Seat:
	# Sēdvietu klase.
	def __init__(self, theater, rinda, kolonna):
		# Sēdvietu iniciālizēšana.
		self.status = 0  # Pirmkārt iestāsim, ka visas sēdvietas ir brīvas.
		if random.randint(0, 1) == 1:  # Nejaušam sēdvietu izvietojumam. Nevienmēr būs 50%. Jo random ir katrai sēdvietai, vai nu 0 vai 1 un tāpēc nebūs precīzi 50% katru reizi. Atkarīgs no veiksmes (liekas, ka tas ir labāk, jo interesantāk).
			self.status = 1  # Ja tiek izlozēts 1 (50% varbūtība), tad vieta ir aizņemta.
			self.button = tkinter.Button(theater, bg="#A00000", text="╳", width=5, height=2)  # Izkrāsojam vietu ar sarkanu krāsu un liksim ╳ simbolu.
		else:  # Ja netika izlozēts 1 (tad izlozēts 0), tad vieta nebūs aizņemta.
			self.button = tkinter.Button(theater, bg="green", text="○", width=5, height=2, command=self.change_status)  # Izkrāsojam vietu ar zaļu krāsu un liksim ○ simbolu.
		self.button.grid(row=rinda, column=kolonna)  # Definēsim, kur likt pogu.

	def change_status(self):
		# Izmaina pogas stātusu no 0 -> 2, no 2 -> 0, no 1 -> 1.
		# 0 - brīva vieta.
		# 1 - aizņemta vieta.
		# 2 - izvēlēta vieta.

		if self.status == 0:  # 0 -> 2 (brīva vieta uz izvelētu vietu)
			self.status = 2
			self.button.config(bg="yellow")  # dzeltens reprezentē izvēlētu vietu.
		elif self.status == 2:  # 2 -> 0 (izvelēta uz brīvu, atcelt)
			self.status = 0
			self.button.config(bg="green", text="○")  # zaļš reprezentē brīvo vieta.
		elif self.status == 1:  # Aizņemts. To nevar izmainīt. 1 -> 1.
			pass

	def occupy(self):
		# Komanda sēdvietas aizņemšanai.

		self.status = 1  # Pogas (vietas) statuss ir 1 (aizņemts).
		self.button.configure(bg="#A00000", text="╳")  # Izmainām krāsu uz sarkanu un izmainām tekstu uz pogas uz "╳".


class Teatris:
	# Teātra klase.
	def __init__(self, theater, rindas, kolonnas):
		self.seats = []
		self.selected_seats = []  # Izvelētas sēdvietas saraksts.
		self.num_occupied_seats = 0  # Nepieciešams, lai sekot līdzi aizņemto sēdvietu skaitam.

		for i in range(rindas):  # Izmantojot pilno pārlasi pārbaudam, vai visas vietas nav aizņemtas (varbūt ka "paveicas" un uzreiz viss ir izpārdots).
			rinda = []
			for j in range(kolonnas):
				seat = Seat(theater, i, j)
				if seat.status == 1:
					self.num_occupied_seats += 1  # Ja sēdvieta sākotnēji ir aizņemta, tad palieliniet skaitītāju.
				rinda.append(seat)
			self.seats.append(rinda)
		self.buy_button = tkinter.Button(theater, text="Nopirkt izvēlētās biļetes", command=self.buy_tickets)  # Nopirkšanas poga.
		self.buy_button.grid(row=rindas + 1, column=0, columnspan=kolonnas)
		self.all_seat_quantity = len(self.seats) * len(self.seats[0])  # Lai zinātu cik ir kopējais sēdvietu skaits.
		self.check_occupied()  # Izsaucam check_occupied, lai atjauninātu nopirkšanas pogas stāvokli (ja visas ir aizņemtas vietas, tad bloķēt pogu).

	def read_selection(self):
		# Atgriež sarakstu ar izvēlētam sēdvietam izmantojot pilnu pārlasi caur kātru vietu (rindu un kolonnu).
		selected_seats = []  # Tukšais saraksts ar izvēlētam sēdvietam.
		for row in self.seats:  # Iterējam caur katru rindu un kolonnu (pilnā pārlase)
			for seat in row:
				if seat.status == 2:  # Un izmantojot pilno pārlasi, ja sēdvietai ir piekārtots 2 (izvelēta), tad .append sēdvietu sarakstam selected_seats (izvēlētas sēdvietas)
					selected_seats.append(seat)  # Pievienojam sarakstam atrasto izvēlēto vietu.
		return selected_seats  # Atgriezt izvēlētas sēdvietas.

	def buy_tickets(self):
		# Komanda pirkšanas pogai. Izsauc seat.occupy() visiem sēdvietam kas ie izvēlētas un palielina num_occupied_seats par katru izvēlēto vietu (tas ir nepieciešāms, lai jā visas vietās ir aizņemtas, tad bloķēt pogu).
		self.selected_seats = self.read_selection()  # Saraksts ar visam izvēlētam sēdvietam.
		for seat in self.selected_seats:  # Izmainām vērtības visam izvēlētam vietam (izmainām 2 -> 1) un palielinām self.num_occupied_seats par vienu.
			seat.occupy()  # Izmainīt sēdvietas stavokļi uz ieņemtu.
			self.num_occupied_seats += 1  # Palielinam aizņemto vietu skaitītāju par katru tikko aizņemto vietu.
		self.check_occupied()  # Izsaukt check_occupied, lai atjauninātu etiķetes un pogas stāvokli.

	def check_occupied(self):
		# Komanda pārbauda vai visas vietas jau ir izpārdotas. Ja ir, tad bloķē pirkšanas pogu.
		if self.num_occupied_seats == self.all_seat_quantity:  # Ja visas vietas ir aizņemtas, tad nobloķēt pirkšanas pogu. Salidzina aizņemto vietu skaititāju, ar visu sēdvietu skaitu. Ja sakrīt tad, bloķēt pogu.
			self.buy_button.config(text="Visas vietas izpārdotas!", state="disabled")  # Bloķēt pirkšanas pogu un izmainīt tekstu uz pogas.


class Define_Theater:
	# Klase teātra definēšanai.
	@staticmethod
	def izveidot_teatri():
		# Metode, kas nolasa ievādītas rindas un kolonnu vērtības no entry, nodzēs palīglogu teātra definēšanai, un izveido "zale" windows un izsauc klasi Teatris.
		rindas = int(rindas_entry.get())  # Nolasam vērtības no rindas entry.
		kolonnas = int(kolonnas_entry.get())  # Nolasam vērtības no kolonnas (sēdvietas) entry.

		logs.destroy()  # Nodzēsam logu, kur mēs prāsījam lietotājam ievādīt rindas un sēdvietu skaitu.

		zale = tkinter.Tk()  # Izveidojam jauno logu teātrim.
		zale.title("Zāle")  # Jauna loga virsraksts.
		Teatris(zale, rindas, kolonnas)  # Izsauc Teātra klasi ar lietotāja ievādītam rindam un kolonnam.
		zale.mainloop()  # Lai jauns logs būtu redzāms.

import tkinter
import random


class Seat:
	# Sēdvietu klase.
	def __init__(self, theater, rinda, kolonna):
		# Sēdvietu iniciālizēšana.
		self.status = 0  # Pirmkārt iestāsim, ka visas sēdvietas ir brīvas.
		if random.randint(0, 1) == 1:  # Nejaušam sēdvietu izvietojumam. Nevienmēr būs 50%. Jo random ir katrai sēdvietai, vai nu 0 vai 1 un tāpēc nebūs precīzi 50% katru reizi. Atkarīgs no veiksmes (liekas, ka tas ir labāk, jo interesantāk).
			self.status = 1  # Ja tiek izlozēts 1 (50% varbūtība), tad vieta ir aizņemta.
			self.button = tkinter.Button(theater, bg="#A00000", text="╳", width=5, height=2)  # Izkrāsojam vietu ar sarkanu krāsu un liksim ╳ simbolu.
		else:  # Ja netika izlozēts 1 (tad izlozēts 0), tad vieta nebūs aizņemta.
			self.button = tkinter.Button(theater, bg="green", text="○", width=5, height=2, command=self.change_status)  # Izkrāsojam vietu ar zaļu krāsu un liksim ○ simbolu.
		self.button.grid(row=rinda, column=kolonna)  # Definēsim, kur likt pogu.

	def change_status(self):
		# Izmaina pogas stātusu no 0 -> 2, no 2 -> 0, no 1 -> 1.
		# 0 - brīva vieta.
		# 1 - aizņemta vieta.
		# 2 - izvēlēta vieta.

		if self.status == 0:  # 0 -> 2 (brīva vieta uz izvelētu vietu)
			self.status = 2
			self.button.config(bg="yellow")  # dzeltens reprezentē izvēlētu vietu.
		elif self.status == 2:  # 2 -> 0 (izvelēta uz brīvu, atcelt)
			self.status = 0
			self.button.config(bg="green", text="○")  # zaļš reprezentē brīvo vieta.
		elif self.status == 1:  # Aizņemts. To nevar izmainīt. 1 -> 1.
			pass

	def occupy(self):
		# Komanda sēdvietas aizņemšanai.

		self.status = 1  # Pogas (vietas) statuss ir 1 (aizņemts).
		self.button.configure(bg="#A00000", text="╳")  # Izmainām krāsu uz sarkanu un izmainām tekstu uz pogas uz "╳".


class Teatris:
	# Teātra klase.
	def __init__(self, theater, rindas, kolonnas):
		self.seats = []
		self.selected_seats = []  # Izvelētas sēdvietas saraksts.
		self.num_occupied_seats = 0  # Nepieciešams, lai sekot līdzi aizņemto sēdvietu skaitam.

		for i in range(rindas):  # Izmantojot pilno pārlasi pārbaudam, vai visas vietas nav aizņemtas (varbūt ka "paveicas" un uzreiz viss ir izpārdots).
			rinda = []
			for j in range(kolonnas):
				seat = Seat(theater, i, j)
				if seat.status == 1:
					self.num_occupied_seats += 1  # Ja sēdvieta sākotnēji ir aizņemta, tad palieliniet skaitītāju.
				rinda.append(seat)
			self.seats.append(rinda)
		self.buy_button = tkinter.Button(theater, text="Nopirkt izvēlētās biļetes", command=self.buy_tickets)  # Nopirkšanas poga.
		self.buy_button.grid(row=rindas + 1, column=0, columnspan=kolonnas)
		self.all_seat_quantity = len(self.seats) * len(self.seats[0])  # Lai zinātu cik ir kopējais sēdvietu skaits.
		self.check_occupied()  # Izsaucam check_occupied, lai atjauninātu nopirkšanas pogas stāvokli (ja visas ir aizņemtas vietas, tad bloķēt pogu).

	def read_selection(self):
		# Atgriež sarakstu ar izvēlētam sēdvietam izmantojot pilnu pārlasi caur kātru vietu (rindu un kolonnu).
		selected_seats = []  # Tukšais saraksts ar izvēlētam sēdvietam.
		for row in self.seats:  # Iterējam caur katru rindu un kolonnu (pilnā pārlase)
			for seat in row:
				if seat.status == 2:  # Un izmantojot pilno pārlasi, ja sēdvietai ir piekārtots 2 (izvelēta), tad .append sēdvietu sarakstam selected_seats (izvēlētas sēdvietas)
					selected_seats.append(seat)  # Pievienojam sarakstam atrasto izvēlēto vietu.
		return selected_seats  # Atgriezt izvēlētas sēdvietas.

	def buy_tickets(self):
		# Komanda pirkšanas pogai. Izsauc seat.occupy() visiem sēdvietam kas ie izvēlētas un palielina num_occupied_seats par katru izvēlēto vietu (tas ir nepieciešāms, lai jā visas vietās ir aizņemtas, tad bloķēt pogu).
		self.selected_seats = self.read_selection()  # Saraksts ar visam izvēlētam sēdvietam.
		for seat in self.selected_seats:  # Izmainām vērtības visam izvēlētam vietam (izmainām 2 -> 1) un palielinām self.num_occupied_seats par vienu.
			seat.occupy()  # Izmainīt sēdvietas stavokļi uz ieņemtu.
			self.num_occupied_seats += 1  # Palielinam aizņemto vietu skaitītāju par katru tikko aizņemto vietu.
		self.check_occupied()  # Izsaukt check_occupied, lai atjauninātu etiķetes un pogas stāvokli.

	def check_occupied(self):
		# Komanda pārbauda vai visas vietas jau ir izpārdotas. Ja ir, tad bloķē pirkšanas pogu.
		if self.num_occupied_seats == self.all_seat_quantity:  # Ja visas vietas ir aizņemtas, tad nobloķēt pirkšanas pogu. Salidzina aizņemto vietu skaititāju, ar visu sēdvietu skaitu. Ja sakrīt tad, bloķēt pogu.
			self.buy_button.config(text="Visas vietas izpārdotas!", state="disabled")  # Bloķēt pirkšanas pogu un izmainīt tekstu uz pogas.


class Define_Theater:
	# Klase teātra definēšanai.
	@staticmethod
	def izveidot_teatri():
		# Metode, kas nolasa ievādītas rindas un kolonnu vērtības no entry, nodzēs palīglogu teātra definēšanai, un izveido "zale" windows un izsauc klasi Teatris.
		rindas = int(rindas_entry.get())  # Nolasam vērtības no rindas entry.
		kolonnas = int(kolonnas_entry.get())  # Nolasam vērtības no kolonnas (sēdvietas) entry.

		logs.destroy()  # Nodzēsam logu, kur mēs prāsījam lietotājam ievādīt rindas un sēdvietu skaitu.

		zale = tkinter.Tk()  # Izveidojam jauno logu teātrim.
		zale.title("Zāle")  # Jauna loga virsraksts.
		Teatris(zale, rindas, kolonnas)  # Izsauc Teātra klasi ar lietotāja ievādītam rindam un kolonnam.
		zale.mainloop()  # Lai jauns logs būtu redzāms.

'''
# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Izveidojam logu, kur paprasām lietotājam ievādīt rindas un kolonnu (sēdvietu) skaitu teātrī. Tas ir nepieciešams teātra izveidošanai.
logs = tkinter.Tk()  # Faktiski tas ir papildlogs, lai lietotājs varētu ievādit rindas un kolonnu skaitu teātrī.
logs.title("Biļešu paradīze")  # Loga virsraksts.
logs.geometry("250x125")  # Loga izmērs.

rindas_label = tkinter.Label(logs, text="Rindu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda rindu skaitu.
rindas_label.pack()

rindas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam rindas ievadei.
rindas_entry.pack()

kolonas_label = tkinter.Label(logs, text="Sēdvietu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda sēdvietu (kolonnu) skaitu.
kolonas_label.pack()

kolonnas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam sēdvietu (kolonnas) ievadei.
kolonnas_entry.pack()

poga_izveidot = tkinter.Button(logs, text="Izveidot teātru", command=Define_Theater.izveidot_teatri)  # Poga "Izveidot teātru" papildlogam. Izsauc komandi "Define_Theater.izveidot_teatri"
poga_izveidot.pack()

logs.mainloop()  # Lai logs būtu redzāms.
'''

class Buyer:
	# Klase pircējam.
	def __init__(self, name, license, is_individual):
		# name - vārds un uzvārds vai kompānija.
		# license - vadītāju apliecības a. "A" vai "B" vai "C" vai "D" vai "nav".
		# is_individual - True - ir fiziska persona. False - juridiska persona.
		# A - vadītāju apliecības kategorija motocikliem (šajā programmā nav motociklus, bet tā ir reāla kategorija, tāpēc to ierākstīju).
		# B - vadītāju apliecības kategorija viegliem automobiļiem.
		# C - vadītāju apliecības kategorija kravas automobiļiem.
		# D - vadītāju apliecības kategorija autobusiem automobiļiem.
		self.name = name
		self.license = license
		self.is_individual = is_individual

		# Pārbauda vai licence nav A vai B vai C vai D vai nav.
		# Ja nav, tad license - nav.
		if self.license != "A" and self.license != "B" and self.license != "C" and self.license != "D" and self.license != "nav":
			if self.is_individual:  # Fiziskām personam.
				print(f"Pievienota fiziskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības fiziskai personai.
			elif not self.is_individual:  # Juridiskām personam.
				print(f"Pievienota juridiskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības juridiskai personai.
			else:  # Kļūda ja netika ierākstīta Boolean vērtība (True vai False).
				print(f"Kļūda! {self.name} personai jābut vai nu fiziskai vai juridiskai!")
			self.license = "nav"

		elif self.license == "A":  # Ja ir A kategorija (motocikliem) apliecībai.
			if self.is_individual:  # Ja ir A kategorija apliecībai un tā ir fiziska persona.
				print(f"Pievienota fiziskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")
			else:   # Ja ir A kategorija apliecībai un tā ir juridiskā persona.
				print(f"Pievienota juridiskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")

		elif self.license == "B":  # Ja ir B (vieglauto) kategorija apliecībai.
			if self.is_individual:  # Ja ir B kategorija apliecībai un tā ir fiziska persona.
				print(f"Pievienota fiziskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")
			else:  # Ja ir B kategorija apliecībai un tā ir juridiskā persona.
				print(f"Pievienota juridiskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")

		elif self.license == "C":  # Ja ir C (kravas automobiļiem) kategorija apliecībai.
			if self.is_individual:  # Ja ir C kategorija apliecībai un tā ir fiziska persona.
				print(f"Pievienota fiziskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")
			else:  # Ja ir C kategorija apliecībai un tā ir juridiskā persona.
				print(f"Pievienota juridiskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")

		elif self.license == "D":  # Ja ir D (autobusiem) kategorija apliecībai.
			if self.is_individual:  # Ja ir D kategorija apliecībai un tā ir fiziska persona.
				print(f"Pievienota fiziskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")
			else:  # Ja ir D kategorija apliecībai un tā ir juridiskā persona.
				print(f"Pievienota juridiskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")

	def print_license(self):
		# Izvadīt vadītāju apliecības kategoriju uz ekrāna.
		if self.license == "nav":  # Ja nav vadītāju apliecības kategoriju cilvēkam, tad izvadam kā nav.
			print(f"{self.name} nav vadītāja apliecības.")
		else:  # Ja vadītāju apliecības kategorija ir cilvēkam, tad izvadam ka ta ir.
			print(f"{self.name} ir vadītāja apliecība kategorijā {self.license}.")

	def return_license(self):
		# Atgriež vadītāju apliecības kategoriju uz ekrāna.
		return self.license

	def return_name(self):
		# Atgriež pircēja vārdu vai uzvārdu.
		return self.name


class Car:
	id_counter = 0  # Lai sekotu līdzi ID numuram.

	def __init__(self, model):
		# model - nosaukums automašīnai.
		self.id = Car.id_counter  # piešķirt automašīnai unikālu ID.
		Car.id_counter += 1  # ID skaitītājs pieaug par vienu nākamajai automašīnai.
		self.model = model
		self.is_rented = False

	def return_name(self):
		# Atgriež automašīnas nosaukumu.
		return self.model


class Truck(Car):
	# Apakšklase Car klasei.
	# Šai klasei ir cargo_capacity (kravas kapacitāte, vai kravas automašīnas ietilpība).
	def __init__(self, model, cargo_capacity):
		# model - automašīnas nosaukums.
		# cargo_capacity - kravas kapacitāte.
		super().__init__(model)
		self.cargo_capacity = cargo_capacity

	def return_name(self):
		# Atgriež kravas automašīnas nosaukumu.
		return self.model


class Bus(Car):
	def __init__(self, model, num_of_seats):
		# model - automašīnas nosaukums.
		# cargo_capacity - vietu skaits automašīnā.
		super().__init__(model)
		self.num_of_seats = num_of_seats

	def return_name(self):
		# Atgriež autobusa nosaukumu.
		return self.model


class Rental_point:
	# Nomas punkta klase.
	def __init__(self):
		self.cars = []  # Saraksts, kurā glabāsim visas automašīnas, kuri ir pieejāmi nomašanai.
		self.buses = []  # Saraksts, kurā glabāsim visus autobusus, kuri ir pieejāmi nomašanai.
		self.trucks = []  # Saraksts, kurā glabāsim visus kravas automašīnas, kuri ir pieejāmi nomašanai.
		self.rented_vehicles = []  # Lai sekotu līdzi iznomātajiem transportlīdzekļiem. Saraksts ar transportlīdzekļiem, kuri nav pieejāmi.

	def add_car(self, car):
		# car - objekts no Car klases.
		print(f"Automašīna {car.model} tika nogādāta nomas punktā!")
		self.cars.append(car)

	def add_bus(self, bus):
		# bus - objekts no Bus klases (apakšklase Car'am).
		print(f"Autobuss {bus.model} tika nogādāts nomas punktā!")
		self.buses.append(bus)

	def add_truck(self, truck):
		# truck - objekts no Truck klases (apakšklase Car'am).
		print(f"Kravas automašīna {truck.model} tika nogādāta nomas punktā!")
		self.trucks.append(truck)

	def remove_car(self, car):
		# Nodzēst vienu noteiktu vieglauto no saraksta ar pieejāmam automašīnam (nodot vieglauto metāllūžņos).
		if car in self.cars:  # Ja tas vieglauto ir sarakstā ar pieejāmam automašīnam.
			print(f"Nomas punkts nodeva {car.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu vieglauto nodzēsam.
			self.cars.remove(car)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu vieglauto.
		else:  # Nevar nodot metallužnos vieglauto, ja tādas nav.
			print(f"Nevar nodot metallužnos automašīnu {car.model}, jo tādas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst vieglauto, kura nav pieejāma.

	def remove_bus(self, bus):
		# Nodzēst vienu noteiktu autobusu no saraksta ar pieejāmam automašīnam (nodot autobusu metāllūžņos).
		if bus in self.buses:  # Ja tas autobuss ir sarakstā ar pieejāmam automašīnam.
			print(f"Nomas punkts nodeva autobusu {bus.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu autobusu nodzēsam.
			self.buses.remove(bus)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu autobusu.
		else:  # Nevar nodot metallužnos autobusu, ja tādu nav.
			print(f"Nevar nodot metallužnos autobusu {bus.model}, jo tāda autobusa nav nomas punktā!")   # Izvadīt informāciju par to, ka nevaram nodzēst autobusu, kurš nav pieejāms.

	def remove_truck(self, truck):
		# Nodzēst vienu noteiktu kravas automašīnu no saraksta ar pieejāmam automašīnam (nodot kravas automašīnu metāllūžņos).
		if truck in self.trucks:  # Ja tas kravas automašīna ir sarakstā ar pieejāmam automašīnam.
			print(f"Nomas punkts nodeva kravas automašīnu {truck.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu kravas automašīnu nodzēsam.
			self.trucks.remove(truck)  # Nodzēst no saraksta kravas automašīnu.
		else:  # Nevar nodot metallužnos kravas automašīnu, ja tādas nav.
			print(f"Nevar nodot metallužnos kravas automašīnu {truck.model}, jo tādas kravas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst kravas automašīnu, kura nav pieejāma.

	def announce_cars(self):
		# Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
		print("Pašlaik nomai pieejami vieglauto:")

		free_auto = []
		for car in self.cars:
			if not car.is_rented:
				free_auto.append(car.model)

		if free_auto:
			for model in free_auto:
				print(model)
		else:
			print("Nav brīvu vieglauto.")
		print()

	def announce_buses(self):
		# Izvadīt (iz-print'ēt) uz ekrāna autobusus.
		print("Pašlaik nomai pieejami autobusi:")

		free_buses = []
		for bus in self.buses:
			if not bus.is_rented:
				free_buses.append(bus.model)

		if free_buses:
			for model in free_buses:
				print(model)
		else:
			print("Nav brīvu autobusu.")
		print()

	def announce_trucks(self):
		# Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
		print("Pašlaik nomai pieejami kravas auto:")

		free_trucks = []
		for truck in self.trucks:
			if not truck.is_rented:
				free_trucks.append(truck.model)

		if free_trucks:
			for model in free_trucks:
				print(model)
		else:
			print("Nav brīvu kravas auto.")

		print()

	def announce_available_vehicles(self):
		# Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
		# Izvadīt (iz-print'ēt) uz ekrāna autobusus.
		# Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
		self.announce_cars()
		self.announce_buses()
		self.announce_trucks()

	def sell_car(self, item, buyer):
		# Automašīnas nodošanai nomā.
		if isinstance(buyer, Buyer):
			if isinstance(item, Car) and not item.is_rented and item in self.cars:
				if buyer.license == "B":
					item.is_rented = True
					self.rented_vehicles.append(item)
					print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
				else:
					print(f"{buyer.name} ir nepieciešamas B kategorijas vadītāja apliecība, lai nomātu vieglauto {item.model}.")

			elif isinstance(item, Bus) and not item.is_rented and item in self.buses:
				if buyer.license == "D":
					item.is_rented = True
					self.rented_vehicles.append(item)
					print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
				else:
					print(f"{buyer.name} ir nepieciešamas D kategorijas vadītāja apliecība, lai nomātu autobusu {item.model}.")

			elif isinstance(item, Truck) and not item.is_rented and item in self.trucks:
				if buyer.license == "C":
					item.is_rented = True
					self.rented_vehicles.append(item)
					print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}." + str(buyer.return_license()))
				else:
					print(f"{buyer.name} ir nepieciešamas C kategorijas vadītāja apliecība, lai nomātu kravas automašīnu {item.model}." + str(buyer.return_license()))
			else:
				if isinstance(item, Bus):
					print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejams autobusu nomas punktā!")
				else:
					print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejama automašīnas nomas punktā!")
		else:
			print(f"Kļūda! {buyer.name} ir nepieciešama noteikta vadītāja apliecības kategorija, lai nomātu {item.model}!")

	def return_vehicle(self, vehicle):
		# Atgriezt transportlīdzekļu automašīnas nomai.
		if vehicle in self.rented_vehicles:
			vehicle.is_rented = False
			self.rented_vehicles.remove(vehicle)
			print(f"{vehicle.model} tika atgriezts nomas punktā.")
		else:
			print(f"{vehicle.model} nebija nomāts šajā nomas punktā!")
import math


class Taisnsturis:
	# Taisnstūris.
	def __init__(self, garums, platums):
		self.garums = garums
		self.platums = platums

	def perimetrs(self):
		# Aprēķina taisnstūra perimetru.
		return (self.garums + self.platums) * 2

	def laukums(self):
		# Aprēķina taisnstūra laukumu.
		return self.garums * self.platums


class Regular_pentagon:
	# Regulārs piecstūris.
	def __init__(self, side_length):
		self.side_length = side_length

	def perimetrs(self):
		# Aprēķina regulāra piecstūra perimetru.
		return 5 * self.side_length

	def laukums(self):
		# Aprēķina regulāra piecstūra laukumu.
		return ((math.sqrt(5) * math.sqrt(5 + 2 * math.sqrt(5))) / 4) * (self.side_length * self.side_length)
		# Formulas avots:
		# https://en.wikipedia.org/wiki/Pentagon


class Regular_hexagon:
	# Regulārs sešstūris.
	def __init__(self, side_length):
		self.side_length = side_length

	def perimetrs(self):
		# Aprēķina regulāra sešstūra perimetru.
		return 6 * self.side_length

	def laukums(self):
		# Aprēķina regulāra sešstūra laukumu.
		return (3 * math.sqrt(3) / 2) * (self.side_length * self.side_length)


class Regular_polygon:
	# Regulārs n-stūris.
	def __init__(self, side_length, num_sides):
		# num_sides - n-stūra malu skaits (vai leņķu skaits) n-stūra n skaitlis.
		# side_lenght - vienas malas garums.
		self.side_length = side_length
		self.num_sides = num_sides

	def perimetrs(self):
		# Aprēķina regulāra n-stūra perimetru.
		return self.num_sides * self.side_length

	def laukums(self):
		# Aprēķina regulāra n-stūra laukumu.
		return 0.25 * self.num_sides * self.side_length * self.side_length / math.tan(math.pi / self.num_sides)
		# Formulas avots:
		# https://en.wikipedia.org/wiki/Regular_polygon


class Trapece:
	def __init__(self, a, b, c, d):
		# Iniciālizē a, b, c, d.
		# a - trapeces pirmās malas garums.
		# b - trapeces otrais malas garums.
		# c - trapeces trešais malas garums.
		# d - trapeces trešais malas garums.
		# self - trapece.
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def perimetrs(self):
		# Aprēķina trijstūra perimetru.
		return self.a + self.b + self.c + self.d

	def laukums(self):
		# Aprēķina trapeces laukumu
		d = self.b - self.a
		k = (d * d + self.c * self.c - self.d * self.d) / (2 * self.c * d)
		k = k * k
		t = 1 - k
		m = math.sqrt(t)
		p = ((self.a + self.b) / 2) * self.c
		return p * m
		# Laukuma formulas avots:
		# https://math.stackexchange.com/questions/2637690/is-there-a-formula-to-calculate-the-area-of-a-trapezoid-knowing-the-length-of-al


class Trijsturis:
	# Trijstūra klase.
	def __init__(self, a, b, c):
		# Iniciālizē a, b, c.
		# a - trijstūra pirmās malas garums.
		# b - trijstūra otrais malas garums.
		# c - trijstūra trešais malas garums.
		# self - trijstūris.
		self.a = a
		self.b = b
		self.c = c

	def pusperimetrs(self):
		# Aprēķina trijstūra pusperimetru.
		p = (self.a + self.b + self.c) / 2
		return p

	def laukums(self):
		# Aprēķina trijstūra laukumu ar Herona formulu.
		p = Trijsturis.pusperimetrs(self)
		return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # self.garums * self.platums

	def perimetrs(self):
		# Aprēķina trijstūra perimetru.
		return self.a + self.b + self.c

	def ievilkta_rinka_radiuss(self):
		# Aprēķina trijstūra ievilkta riņķa līnijas rādiusu r.
		return Trijsturis.laukums(self) / Trijsturis.pusperimetrs(self)  # regulāram r = (a*sqrt(3))/6

	def apvilkta_rinka_radiuss(self):
		# Aprēķina trijstūra apvilkta riņķa līnijas rādiusu R.
		return self.a * self.b * self.c / (4 * Trijsturis.laukums(self))  # regulāram R = (a*sqrt(3))/6


class Rinkis:
	def __init__(self, radiuss):
		self.radiuss = radiuss

	def perimetrs(self):
		# Aprēķina riņķa līnijas perimetru (riņķa līnijas garumu) ar formulu pi*r*r = pi*r^2.
		return 6.283 * self.radiuss  # 2*pi*r

	def laukums(self):
		# Aprēķina riņķa līnijas laukumu ar formulu pi*r*r = pi*r^2.
		return 3.1415 * self.radiuss * self.radiuss  # pi*r*r = pi*r^2


def izdrukat_laukumu(figura):
	print("Šīs figūras laukums ir:", figura.laukums())


def izdrukat_perimetru(figura):
	print("Šīs figūras perimetrs ir:", figura.perimetrs())

def fill_array_randomly(n, m):
	# Nejauši aizpilda n x m matricu ar naturāliem skaitļiem no 1 līdz 9.
	# [1, 2, 3, 4, 5, 6, 7, 8, 9].
	# n - rindu skaits matricā (sudoku ir 9 rindas) (int).
	# m - kolonnu skaits matricā (sudoku ir 9 kolonnas) (int).
	# Atgriež aizpildīto masīvu ar nejaušiem naturāliem skaitļiem no 1 līdz 9.

	# Izveidojam tukšu 9x9 divdimensijas masīvu (matricu).
	a = numpy.zeros((n, m), dtype=int)

	# Ejam ciklā cauri katrai masīva rindai un kolonnai.
	for i in range(n):
		for j in range(m):
			# Ģenerējam nejaušu naturālu skaitli no 1 līdz 9.
			random_number = numpy.random.randint(1, 10)
			# Piešķiram [i][j] vietā nejaušu naturālu skaitli no 1 līdz 9.
			a[i][j] = random_number

	# Atgriež aizpildīto masīvu ar nejaušiem naturāliem skaitļiem no 1 līdz 9.
	return a


def check_array_rows_and_columns(a):
	# Pārbauda vai matricā katra rindā un kolonnā visi skaitļi ir dažādi, izmantojot kopas.
	# Atgriež True, ja visi skaitļi visas rindas un kolonnas ir dažādi.
	# Atgriež False, ja ir kādi divi skaitļi kāda rinda vai kolonna kuri sakrīt.
	# a - divdimensijas masīvs (matrica).

	for i in range(9):
		# Pārbauda, vai katrā rindā nav skaitļu dublikātu (nav vienādu skaitļu).
		# Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
		if len(set(a[i])) != 9:
			print(str(i + 1) + ". rindā ir cipari, kas atkārtojas.")  # Izvadam, kur tika atrāsta kļūda.
			return False

	for j in range(9):
		# Pārbauda, vai katrā kolonnā nav skaitļu dublikātu (nav vienādu skaitļu).
		# Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
		col_numbers = [a[i][j] for i in range(9)]
		if len(set(col_numbers)) != 9:
			print(str(j + 1) + ". kolonnā ir cipari, kas atkārtojas.")
			return False

	return True


def check_submatrix(matrix, i, j):
	# Atgriež True ja 3x3 apakšmatricā (apakšmatricas ir paradītas zemāk) visi skaitļi ir dažādi.
	# Atgriež False ja 3x3 apakšmatricā kādi divi skaitļi ir vienādi.
	# Sudoku 3x3 apakšmatricas.
	# matrix - pilnā 9x9 matrica (divdimensijas masīvs).
	# i - no kuras rīndas sāksim (int).
	# j - no kuras kolonnas sāksim (int).

	submatrix = []
	for row in range(i, i + 3):
		for col in range(j, j + 3):
			submatrix.append(matrix[row][col])
	return len(set(submatrix)) == 9


def check_3x3_submatrixes(a):
	# Pārbaudam katru 3x3 apakšmatricu un paziņojam lietotājam kāda apakšmatrica skaitļi ir dažādi un kurā ir vienādi.
	# Izsauc check_submatrix(a, i, j) un paziņo lietotājam "Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.",
	# vai "Ne visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi."
	# Atgriež True, ja nav nevienas apakšmatricas, kurai iekšā ir divi vienādi skaitļi.
	# Atgriež False, ja ir kaut viena apakšmatrica, kurai iekšā ir divi vienādi skaitļi.
	# a - divdimensiju masīvs.

	# Sudoku deviņas apakšmatricas:
	# [0][0] [0][1] [0][2]   [0][3] [0][4] [0][5]   [0][6] [0][7] [0][8]
	# [1][0] [1][1] [1][2]   [1][3] [1][4] [1][5]   [1][6] [1][7] [1][8]
	# [2][0] [2][1] [2][2]   [2][3] [2][4] [2][5]   [2][6] [2][7] [2][8]

	# [3][0] [3][1] [3][2]   [3][3] [3][4] [3][5]   [3][6] [3][7] [3][8]
	# [4][0] [4][1] [4][2]   [4][3] [4][4] [4][5]   [4][6] [4][7] [4][8]
	# [5][0] [5][1] [5][2]   [5][3] [5][4] [5][5]   [5][6] [5][7] [5][8]

	# [6][0] [6][1] [6][2]   [6][3] [6][4] [6][5]   [6][6] [6][7] [6][8]
	# [7][0] [7][1] [7][2]   [7][3] [7][4] [7][5]   [7][6] [7][7] [7][8]
	# [8][0] [8][1] [8][2]   [8][3] [8][4] [8][5]   [8][6] [8][7] [8][8]

	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			if check_submatrix(a, i, j):
				print(f"Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.")
			else:
				print(f"Kļūda! Apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir divi vienādi skaitļi!")
				return False
	return True


def input_sudoku_matrix():
	# Paprasa lietotājam ievādīt veselu skaitļi no 1 līdz 9 katrai "šūnas" vērtībai 9x9 matricai.
	# Atgriež aizpildītu ar lietotāja ievādītam vērtībam matricu ar veseliem skaitļiem no 1 līdz 9.
	# Ejam ciklā caur katru masīva rindu un kolonnu.

	for i in range(9):
		for j in range(9):
			# Turpinam palūgt ievadi, līdz tiek norādīts derīgs skaitlis (cipars no 1 līdz 9).
			while True:
				# Palūdzam lietotājam ievadīt pašreizējās pozīcijas skaitļi (cipars no 1 līdz 9).
				number = input("Ievadiet veselu skaitli no 1 līdz 9 pozīcijai [" + str(i) + "][" + str(j) + "]: ")
				# Pārbaudam, vai ievadītais skaitlis ir no 1 līdz 9 un vai vispār tas ir cipars.
				if number.isdigit() and 1 <= int(number) <= 9:
					# Konvertējam ievadi par veselu skaitli un piešķiram to masīvam.
					a[i][j] = int(number)
					break
				else:
					print("Nepareiza ievade! Lūdzu, ievadiet veselu skaitli no 1 līdz 9.")

	# Agriež aizpildītu ar lietotāja ievādītam vērtībam matricu ar veseliem skaitļiem no 1 līdz 9.
	return a


def matrix_to_string_float_3x3(matrix):
	# Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam.
	# Ja vērtība ir vesels skaitlis, tā tiek parādīta bez komata. Pretējā gadījumā tas tiek parādīts ar decimālzīmi.
	# Funkcija arī atrod maksimālo vērtību garumu matricā un aizpilda nepieciešamās atstarpes " ", lai tās glīti izlīdzinātu (glītas atkāpes).
	# Ja matricā ir 0, tas tiek aizstāts ar simbolu ∙.
	# matrix - matrica (divdimensiju numpy masīvs ar izmēriem n x m).

	# Piemērs, kāda veida tiek atgriezta simbolu virkne:
	# 1 6 3  9 3 4  3 6 6
	# 4 9 9  2 7 3  9 9 5
	# 3 5 9  5 2 7  9 7 4
	#
	# 4 6 6  3 3 8  2 5 3
	# 1 5 6  8 9 2  4 8 3
	# 9 3 9  6 8 7  2 8 2
	#
	# 7 4 9  3 9 3  7 1 1
	# 1 3 5  2 6 3  1 3 1
	# 6 5 3  8 9 7  7 1 8

	rindas = len(matrix)
	kolonnas = len(matrix[0])
	max_len = 0

	for i in range(rindas):  # atrod max_len, lai noteiktu nepieciešamo atkāpi.
		for j in range(kolonnas):
			number = matrix[i][j]
			if number == int(number):
				value_len = len(str(int(number)))
			else:
				value_len = len(str(float(number)))
			if value_len > max_len:
				max_len = value_len

	# Izveido matricas virknes attēlojumu, kur katra rinda tiek atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam
	sv = ""
	for i in range(rindas):
		for j in range(kolonnas):
			number = matrix[i][j]
			if number == 0:
				number = '∙'
			elif number == int(number):
				number = int(number)
			else:
				number = str(float(number))
			atkape = " " * (max_len - len(str(number)))
			sv += atkape + str(number)
			if j < kolonnas - 1 and (j + 1) % 3 != 0:
				sv = sv + " "
			elif j < kolonnas - 1 and (j + 1) % 3 == 0:
				sv = sv + "  "
		sv = sv + "\n"
		if (i + 1) % 3 == 0 and i < rindas - 1:
			sv += "\n"

	return sv
class ComplexNumber:
	# Kompleksu skaitļu klase.
	def __init__(self, re=0, im=0):
		# Pēc noklusējuma izveido tukšu komplēksa skaitli (0 + 0i)
		# Ja ir norādots citādi, tad izveido tā, ka ievadīja lietotājs.
		self.re = re
		self.im = im

	def __repr__(self):
		# print()
		# Kompleksā skaitļu izvadīšanai lietotājam.
		if self.re != 0:  # Ja ir kāda reāla daļa, tad izvadam komplēkso skaitli ar realu daļu (neviss 0 + i*n)

			if self.im > 0 and self.im != 1:  # Ja imagināra daļa nav 1 un tā ir lielāka par 0, tad rakstām n + i, neviss n + k*i
				return f"{self.re} + {self.im}i"

			elif self.im == 1:  # Ja imagināra daļa ir 1, tad rakstām n + i, neviss n + 1*i
				return f"{self.re} + i"

			elif self.im == 0:  # Ja imagināra daļa ir 0, tad rakstām tikai reālu daļu n
				return f"{self.re}"

			elif self.im == -1:  # Ja imagināra daļa ir -1, tad rakstām n - i, neviss n - 1*i
				return f"{self.re} - i"

			else:  # Citā gadījumā rakstām n - k*i
				return f"{self.re} - {-self.im}i"

		else:  # Ja nav reālas daļas, tad nav jēgas rakstīt 0 + k*i, tad izvadam komplēkso skaitli tikai ar imagināru daļu k*i
			if self.im > 0 and self.im != 1:  # Ja imagināra daļa ir pozitīva un nav viens, tad izvadam k*i, neviss 0 + k*i
				return f"{self.im}i"

			elif self.im == 1:  # Ja imagināra daļa ir 1, tad izvadam i, neviss 0 + 1*i
				return "i"

			elif self.im == 0:  # Ja imagināra daļa ir 0, tad izvadam 0, neviss 0 + 0*i
				return "0"

			elif self.im == -1:  # Ja imagināra daļa ir 1, tad izvadam -i, neviss 0 - 1*i
				return "-i"

			else:  # Citādi izvādam -k*i (nav realas daļas un imagināra daļa ir negatīva un nav -1)
				return f"-{-self.im}i"

	def arg(self):
		# Atgriež komplēksa skaitļa argumentu.
		return math.atan2(self.im, self.re)

	def __add__(self, other):
		# +
		# Atgriež komplēksa skaitļa summu (self + other).
		real_sum = self.re + other.re
		imaginary_sum = self.im + other.im
		return ComplexNumber(real_sum, imaginary_sum)

	def __iadd__(self, other):
		# +=
		# Atgriež komplēksa skaitļa summu (self + other), bet kā __iadd__ (+=).
		# Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
		self.re += other.re
		self.im += other.im
		return self

	def __sub__(self, other):
		# -
		# Atgriež komplēksa skaitļa starpību (self - other).
		real_diff = self.re - other.re
		imaginary_diff = self.im - other.im
		return ComplexNumber(real_diff, imaginary_diff)

	def __isub__(self, other):
		# -=
		# Atgriež komplēksa skaitļa summu (self - other), bet kā __isub__ (-=).
		# Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
		self.re -= other.re
		self.im -= other.im
		return self

	def __mul__(self, other):
		# *
		# Atgriež komplēksa skaitļa reizinājumu (self * other).
		real_product = (self.re * other.re) - (self.im * other.im)
		imaginary_product = (self.re * other.im) + (self.im * other.re)
		return ComplexNumber(real_product, imaginary_product)

	def __imul__(self, other):
		# *=
		# Atgriež komplēksa skaitļa reizinājumu (self * other) bet kā __imul__ (*=).
		# Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
		re1 = self.re
		im1 = self.im
		self.re = (re1 * other.re) - (im1 * other.im)
		self.im = (re1 * other.im) + (im1 * other.re)
		return self

	def __truediv__(self, other):
		# /
		# Atgriež komplēksa skaitļa dalījumu (self / other).
		denominator = (other.re * other.re) + (other.im * other.im)
		real_quotient = ((self.re * other.re) + (self.im * other.im)) / denominator
		imaginary_quotient = ((self.im * other.re) - (self.re * other.im)) / denominator
		return ComplexNumber(real_quotient, imaginary_quotient)

	def __itruediv__(self, other):
		# /=
		# Atgriež komplēksa skaitļa dalījumu (self / other) bet kā __itruediv__ (/=).
		# Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
		denominator = (other.re ** 2) + (other.im ** 2)
		real_quotient = ((self.re * other.re) + (self.im * other.im)) / denominator
		imaginary_quotient = ((self.im * other.re) - (self.re * other.im)) / denominator
		self.re = real_quotient
		self.im = imaginary_quotient
		return self

	def __abs__(self):
		# Atgriež komplēksa skaitļa moduli.
		return math.sqrt(self.re * self.re + self.im * self.im)

	def conjugate(self):
		# Atgriež komplēksa skaitļas komplēksa saistīto skaitli.
		return ComplexNumber(self.re, -self.im)

	def __pow__(self, power):
		# Atgriež komplēksa skaitļi, kurš tika pacēlts naturāla pakāpe.
		modulus = self.__abs__() ** power
		arg = power * self.arg()
		re = modulus * math.cos(arg)
		im = modulus * math.sin(arg)
		return ComplexNumber(re, im)

	def complex_power(z, n):
		# Atgriež komplēksa skaitļi, kurš tika pacēlts pakāpe.
		r = math.sqrt(z.re**2 + z.im**2)
		theta = math.atan2(z.im, z.re)
		re = r ** n * math.cos(n * theta)
		im_part = r ** n * math.sin(n * theta)
		return ComplexNumber(re, im_part)

	def n_roots(self, n):
		# Atgriež sarakstu, ar visiem komplēksa skaitļa saknēm.
		# n - kuru sakni gribām izvilkt
		roots = []
		modulus = abs(self)
		arg = self.arg()
		for k in range(n):
			root_argument = (arg + 2 * k * math.pi) / n
			re = modulus * math.cos(root_argument)
			im_part = modulus * math.sin(root_argument)
			roots.append(ComplexNumber(re, im_part))
		return roots

	def trigonometric_form(self):
		# Izvadīt lietotājam komplēksu skaitli trigonometriskajā formā.
		r = abs(self)
		theta = self.arg()
		return f"{r:.2f}(cos({theta:.2f}) + isin({theta:.2f}))"

	def exponent_form(self):
		# Izvadīt lietotājam komplēksu skaitli eksponenciāla formā.
		modulus = abs(self)
		arg = self.arg()
		return f"{modulus} * e^({arg}i)"

	def exp(self):
		re = math.cos(self.im)
		im = math.sin(self.im)
		return ComplexNumber(re, im)

def area_using_shoelace_methode_dict(vardnica, n):
	# Aprēķina laukumu daudzstūrim, kurā punktu koordinātas ir definētas vārdnīcā, šādā veidā {"Koordinātas nosaukums" : (x, y)}.
	# Atgriež daudzstūra laukumu izmantojot "Shoelace formula".
	# vardnica - vārdnīca, kurā ir saraksts ar koordinātam šadā veidā {"Koordinātas nosaukums" : (x, y)}.
	# n - naturāls skaitlis - daudzstūra virsotņu skaits.
	# Atgriež daudzstūra laukumu.

	s = 0

	for i in range(0, n):
		# Izmantojot Gausa formulu atrodam laukumu daudzstūrim (Shoelace formula).
		x = vardnica[t[i]].x + vardnica[t[i - 1]].x
		y = vardnica[t[i]].y - vardnica[t[i - 1]].y
		s = s + x * y

	s = abs(s) / 2

	return s


def create_dict_with_coords(n):
	# Paprasa lietotājam ievadīt virsotnes nosaukumus un tā X un Y koordinātas.
	# Izveido vārdnīcu tāda veidā {"Virsotnes nosaukums" : (x, y)}, kur katru "Virsotnes nosaukums" ievada lietotājs, (x, y) arī ievada lietotājs.
	# Atgriež vārdnīcu tāda veidā  {"Virsotnes nosaukums" : (x, y)}.
	# n - naturāls skaitlis - daudzstūra virsotņu skaits.

	i = 0

	for i in range(i, n):
		name = input("Ievadiet " + str(i + 1) + ". virsotnes nosaukumu ==> ")
		punkts = types.SimpleNamespace()

		temp_x = input("Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")
		while not is_real_check(temp_x):
			temp_x = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")

		temp_x = float(temp_x)

		temp_y = input("Ievadiet " + str(i + 1) + ". virsotnes Y koordināti ==> ")
		while not is_real_check(temp_y):
			temp_y = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i + 1) + ". virsotnes X koordināti ==> ")

		temp_y = float(temp_y)

		punkts.x = temp_x
		punkts.y = temp_y

		vardnica.update({name: punkts})

		t.append(name)

	t.append("Fiktīvais punkts")
	vardnica["Fiktīvais punkts"] = vardnica[t[n - 1]]

	return vardnica


def input_polygon_coords(n):
	# Paprasa lietotājam ievadīt virsotnes X un Y koordinātas.
	# Atgriež ierakstu a, ar lietotāja ievadītam X un Y koordinātam.
	# n - naturāls skaitlis - daudzstūra virsotņu skaits.

	for i in range(1, n + 1):
		punkts = types.SimpleNamespace()

		temp_x = input("Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")
		while not is_real_check(temp_x):
			temp_x = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")

		temp_x = float(temp_x)

		temp_y = input("Ievadiet " + str(i) + ". virsotnes Y koordināti ==> ")
		while not is_real_check(temp_y):
			temp_y = input("Kļūda! Ievadiet reālu skaitli! Ievadiet " + str(i) + ". virsotnes X koordināti ==> ")

		temp_y = float(temp_y)

		print()

		punkts.x = temp_x
		punkts.y = temp_y

		a[i] = punkts

	return a


def area_using_shoelace_methode_list(a):
	# Aprēķina laukumu daudzstūrim, kurā punktu koordinātas ir definētas ierakstā a.
	# a - ieraksts, kurā glābajas daudzstūra koordinātas.
	# Ieraksta piemērs: [0 namespace(x=1.0, y=2.0) namespace(x=3.0, y=4.0)].
	# Atgriež daudzstūra laukumu izmantojot "Shoelace formula".

	a[0] = a[n]  # Fiktīvais punkts.

	s = 0

	for i in range(n):
		x = a[i].x + a[i + 1].x
		y = a[i].y - a[i + 1].y
		s = s + x * y

	s = abs(s) / 2

	return s
class Veikals:
	# Klase veikals.
	def __init__(self):
		# Izveidojam preces un selected_preces (izvelētas preces) vārdnīcas.
		# self.preces - vārdnica ar visam precem veikalā.
		# self.selected_preces - vārdnica ar lietotāja izvelētam precem.

		self.preces = dict()
		self.selected_preces = dict()

	def pievienot_preces(self, prece, cena, daudzums):
		# Metode veikala īpašniekam.
		# Preces pievienošana veikalām. Atjaunojam vārdnicu self.preces, preci, ar norādītu cenu un daudzumu.
		# prece - preces nosaukums (str).
		# cena - preces cena par vienu vienumu (float).
		# daudzums - cik daudz preci jāpiegāda veikalām (naturāls skaitlis lielāks par 0) (int).

		self.preces[prece] = {"cena": cena, "daudzums": daudzums}

	def dzest_preces(self, prece):
		# Metode veikala īpašniekam.
		# Nodzēs norādītu preci no veikalā, nodzēs noradītu preci no saraksta.
		# prece - preces nosaukums (str).

		print(f"Prece \"{prece}\" tika izmesta Getliņu izgāztuvē.")
		del self.preces[prece]

	def paradit_izveletas_preces(self):
		# Izdruka visas lietotaja izvelētas preces.

		print("Jūsu izvelētas preces:")
		for prece, info in self.selected_preces.items():
			cena = info["cena"]
			daudzums = info["daudzums"]
			print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

	def paradit_preces(self):
		# Izdruka visas veikalā pieejamas preces lietotājam.

		print("Pieejamas preces veikalā:")
		for prece, info in self.preces.items():
			cena = info["cena"]
			daudzums = info["daudzums"]
			print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

	def izveleties_preces(self, prece, daudzums):
		# Metode preces izvelēšanai lietotājam, jāizvēlas preci un to daudzumu.
		# prece - preces nosaukums (str).
		# daudzums - preces daudzums (int).

		if prece in self.preces:  # Ja tāda prece ir pieejama veikalā, tad tālak pārbaudam.
			if daudzums > self.preces[prece]["daudzums"]:  # Ja pieprasītais daudzums ir lielāks nekā ir veikalā, tad paziņojam, ka nevar nopirkt.
				print(f"Kļūda! Veikalā nav tik daudz preču! Precei \"{prece}\" pieejamais daudzums: {self.preces[prece]['daudzums']}")
			else:
				self.preces[prece]["daudzums"] -= daudzums  # Atņēmam nopirktu daudzumu.
				if prece not in self.selected_preces:
					self.selected_preces[prece] = {"cena": self.preces[prece]["cena"], "daudzums": daudzums}
				else:
					self.selected_preces[prece]["daudzums"] += daudzums  # Pievienojam daudzumu, cik daudz preces izvelējamies nopirkt.
				print(f"Izvēlētas preces: {prece}, cena: " + str(format(self.preces[prece]["cena"], ".2f")) + f"€ , daudzums: {daudzums}")
		else:
			print(f"Kļūda! Prece \"{prece}\" nav pieejama veikalā!")  # Ja tādas preces nav veikalā, tad paziņojam to.

	def atteikt_prece(self, prece, daudzums=None):
		# Lietotājs var atgriezt veikālā kādu no jau izvelētam precem ar norādīto daudzumu.
		# Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
		# prece - preces nosaukums (str).
		# daudzums - preces daudzums (int).

		if prece in self.selected_preces:
			if daudzums is None:  # Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
				daudzums = self.selected_preces[prece]["daudzums"]

			if daudzums > self.selected_preces[prece]["daudzums"]:  # Ja lietotājs grib atgriezt vairāk nekā paņem, tad kļūda.
				print(f"Kļūda! Precei \"{prece}\" ir izvēlēts mazāks daudzums. Nevar atgriezt vairāk nekā paņemat!")
			elif daudzums < 0:  # Ja lietotājs grib atgriezt negatīvu daudzumu, tad kļūda.
				print(f"Kļūda! Nevar atgriezt negatīvu daudzumu!")
			elif daudzums == 0:  # Ja lietotājs grib atgriezt neko, tad kļūda.
				print(f"Kļūda! Nevar atgriezt neko!")
			else:
				self.selected_preces[prece]["daudzums"] -= daudzums  # Atņēmam noradītu daudzumu no izvelētam precēm.
				self.preces[prece]["daudzums"] += daudzums  # Pievienojam noradītu daudzumu par izvelētam precēm.
				if self.selected_preces[prece]["daudzums"] == 0:  # Ja atņēmam tik daudz, ka vairāk tadas preces nav (nav izvelēta), tad nodzēsam to.
					del self.selected_preces[prece]
				print(f"Izvēlētā prece \"{prece}\" tika atgriezta veikalā. Atgrieztais daudzums: {daudzums}")  # Paziņojam lietotājam informāciju.
		else:
			print(f"Kļūda! Prece netika \"{prece}\" izvēlēta.")  # Paziņojam lietotājam.

	def pirkumu_cekis(self):
		# Izdruka pirkumu lietotājam "pirkumu čeku", ar izvelētam precēm.
		total_price = 0

		print("---------------- ČEKS ----------------")
		print("SIA \"MAKSIMA\" Latvija")
		print("Veikals \"Maksima\"")
		print("Dārza iela 21, Bauska, t.22813371")
		print("Juridiskā adrese: \"Abras\", Krustkalni,")
		print("Ķekavas pagasts, Ķekavas novads, LV-2222")
		print("Čeks " + str(randint(100, 999)) + "/" + str(randint(100, 999)) + "                   #" + str(randint(10000000, 99999999)))
		print("==========================================")

		for prece, info in self.selected_preces.items():
			cena = info["cena"]
			daudzums = info["daudzums"]
			preces_cena = cena * daudzums
			total_price += preces_cena
			print(f"{prece} - cena: {cena:.2f}€, daudzums: {daudzums}, {preces_cena:.2f}€")

		print("==========================================")
		print(f"Kopā apmaksai: {total_price:.2f}€")
		print(f"Nopelnīta \"MAKSIMA\" nauda: {total_price * 0.01:.2f}€")
		print("---------------------------------------")


def matrix_to_string_float_3x3(matrix):
	# Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam.
	# Ja vērtība ir vesels skaitlis, tā tiek parādīta bez komata. Pretējā gadījumā tas tiek parādīts ar decimālzīmi.
	# Funkcija arī atrod maksimālo vērtību garumu matricā un aizpilda nepieciešamās atstarpes " ", lai tās glīti izlīdzinātu (glītas atkāpes).
	# Ja matricā ir 0, tas tiek aizstāts ar simbolu ∙.
	# matrix - matrica (divdimensiju masīvs ar izmēriem n x m).

	# Piemērs, kāda veida tiek atgriezta simbolu virkne:
	# 1 6 3  9 3 4  3 6 6
	# 4 9 9  2 7 3  9 9 5
	# 3 5 9  5 2 7  9 7 4
	#
	# 4 6 6  3 3 8  2 5 3
	# 1 5 6  8 9 2  4 8 3
	# 9 3 9  6 8 7  2 8 2
	#
	# 7 4 9  3 9 3  7 1 1
	# 1 3 5  2 6 3  1 3 1
	# 6 5 3  8 9 7  7 1 8

	rindas = len(matrix)
	kolonnas = len(matrix[0])
	max_len = 0

	for i in range(rindas):  # atrod max_len, lai noteiktu nepieciešamo atkāpi.
		for j in range(kolonnas):
			number = matrix[i][j]
			if number == int(number):
				value_len = len(str(int(number)))
			else:
				value_len = len(str(float(number)))
			if value_len > max_len:
				max_len = value_len

	# Izveido matricas virknes attēlojumu, kur katra rinda tiek atdalīta ar \n un izlīdzināta atbilstoši maksimālās vērtības garumam
	sv = ""
	for i in range(rindas):
		for j in range(kolonnas):
			number = matrix[i][j]
			if number == 0:
				number = "∙"
			elif number == int(number):
				number = int(number)
			else:
				number = str(float(number))
			atkape = " " * (max_len - len(str(number)))
			sv += atkape + str(number)
			if j < kolonnas - 1 and (j + 1) % 3 != 0:
				sv = sv + " "
			elif j < kolonnas - 1 and (j + 1) % 3 == 0:
				sv = sv + "  "
		sv = sv + "\n"
		if (i + 1) % 3 == 0 and i < rindas - 1:
			sv = sv + "\n"

	return sv





def check_array_rows_and_columns(a):
	# Pārbauda vai matricā katra rindā un kolonnā visi skaitļi ir dažādi, izmantojot kopas.
	# Atgriež True, ja visi skaitļi visas rindas un kolonnas ir dažādi.
	# Atgriež False, ja ir kādi divi skaitļi kāda rinda vai kolonna kuri sakrīt.
	# a - divdimensijas masīvs (matrica).

	for i in range(9):
		# Pārbauda, vai katrā rindā nav skaitļu dublikātu (nav vienādu skaitļu).
		# Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
		if len(set(a[i])) != 9:
			print(str(i + 1) + ". rindā ir cipari, kas atkārtojas.")  # Izvadam, kur tika atrāsta kļūda.
			return False

	for j in range(9):
		# Pārbauda, vai katrā kolonnā nav skaitļu dublikātu (nav vienādu skaitļu).
		# Izmantojam kopas. Ja kopā nav ar gārumu 9, tad ir cipari kas atkartojas.
		col_numbers = [a[i][j] for i in range(9)]
		if len(set(col_numbers)) != 9:
			print(str(j + 1) + ". kolonnā ir cipari, kas atkārtojas.")
			return False

	return True


def check_submatrix(matrix, i, j):
	# Atgriež True ja 3x3 apakšmatricā (apakšmatricas ir paradītas zemāk) visi skaitļi ir dažādi.
	# Atgriež False ja 3x3 apakšmatricā kādi divi skaitļi ir vienādi.
	# Sudoku 3x3 apakšmatricas.
	# matrix - pilnā 9x9 matrica (divdimensijas masīvs).
	# i - no kuras rīndas sāksim (int).
	# j - no kuras kolonnas sāksim (int).

	submatrix = []
	for row in range(i, i + 3):
		for col in range(j, j + 3):
			submatrix.append(matrix[row][col])
	return len(set(submatrix)) == 9


def check_3x3_submatrixes(a):
	# Pārbaudam katru 3x3 apakšmatricu un paziņojam lietotājam kāda apakšmatrica skaitļi ir dažādi un kurā ir vienādi.
	# Izsauc check_submatrix(a, i, j) un paziņo lietotājam "Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.",
	# vai "Ne visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi."
	# Atgriež True, ja nav nevienas apakšmatricas, kurai iekšā ir divi vienādi skaitļi.
	# Atgriež False, ja ir kaut viena apakšmatrica, kurai iekšā ir divi vienādi skaitļi.
	# a - divdimensiju masīvs.

	# Sudoku deviņas apakšmatricas:
	# [0][0] [0][1] [0][2]   [0][3] [0][4] [0][5]   [0][6] [0][7] [0][8]
	# [1][0] [1][1] [1][2]   [1][3] [1][4] [1][5]   [1][6] [1][7] [1][8]
	# [2][0] [2][1] [2][2]   [2][3] [2][4] [2][5]   [2][6] [2][7] [2][8]

	# [3][0] [3][1] [3][2]   [3][3] [3][4] [3][5]   [3][6] [3][7] [3][8]
	# [4][0] [4][1] [4][2]   [4][3] [4][4] [4][5]   [4][6] [4][7] [4][8]
	# [5][0] [5][1] [5][2]   [5][3] [5][4] [5][5]   [5][6] [5][7] [5][8]

	# [6][0] [6][1] [6][2]   [6][3] [6][4] [6][5]   [6][6] [6][7] [6][8]
	# [7][0] [7][1] [7][2]   [7][3] [7][4] [7][5]   [7][6] [7][7] [7][8]
	# [8][0] [8][1] [8][2]   [8][3] [8][4] [8][5]   [8][6] [8][7] [8][8]

	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			if check_submatrix(a, i, j):
				pass
				#print(f"Visi skaitļi apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir atšķirīgi.")
			else:
				#print(f"Kļūda! Apakšmatricā [{i//3 + 1}][{j//3 + 1}] ir divi vienādi skaitļi!")
				return False
	return True


def generate_sudoku():
	# Izveidojam 9x9 nulles matricu.
	matrix = []
	for i in range(9):
		row = [0] * 9
		matrix.append(row)

	# Aizpildam matricu, sākot no augšējā kreisā stūra.
	fill_matrix(matrix, 0, 0)

	return matrix


def fill_matrix(matrix, i, j):
	# Aizpildām nulles matricu ar (backtracking algorithm) algoritmu tā, lai visas rindas būtu atšķirīgi skaitli.

	if i == 9:
		return True

	# Aprēķina nākamo "šūnu" indeksus.
	next_i = i + (j + 1) // 9
	next_j = (j + 1) % 9

	# Izveidot sarakstu ar veseliem skaitļiem no 1 līdz 9.
	list_random = list(range(1, 10))
	# Sajaucam sarakstā vērtības.
	random.shuffle(list_random)

	# Mēgīnām ielikt pēc kārtas katru ciparu no nejauši sajaukta saraksta.
	for number in list_random:
		# Pārbaudam, vai skaitlis ir derīgs (ar karogu "valid").
		valid = True

		# Pārbaudam rindas.
		for k in range(9):
			if matrix[i][k] == number:
				valid = False  # Ja sakrīt kāds skaitlīs rindā ar izvelēto skaitli, tad karogs ir False, vajag paņemt citu skaitli no list_random (ņēm pēc kārtas).
				break

		# Pārbaudam kolonnas.
		for k in range(9):
			if matrix[k][j] == number:
				valid = False  # Ja sakrīt kāds skaitlīs kolonna ar izvelēto skaitli, tad karogs ir False, vajag paņemt citu skaitli no list_random (ņēm pēc kārtas).
				break

		# Pārbaudam 3x3 noteiktas apakšmatricas.
		sub_i = i // 3 * 3  # "apakš_i"
		sub_j = j // 3 * 3  # "apakš_j"

		for k in range(sub_i, sub_i + 3):
			for l in range(sub_j, sub_j + 3):
				if matrix[k][l] == number:
					valid = False
					break

		# Ja skaitlis ir derīgs, aizpildam to "šūnu" un rekursīvi sākam aizpildīt nākamo "šūnu".
		if valid:
			matrix[i][j] = number
			if fill_matrix(matrix, next_i, next_j):
				return True

	# Ja esam izmēģinājuši visus skaitļus un neviens nedēr, tad jāatkāpjas par vienu soli atpakāļ, un jau citus skaitļus likt. (backtracking algorithm)
	matrix[i][j] = 0
	return False


def delete_cells(matrix, delete_count):
	# Izveidojam matricu, kas piepildīta ar nullēm
	result = []
	for i in range(len(matrix)):
		row = [0] * len(matrix[0])
		result.append(row)

	# Aizpildam noteiktu skaitu "šūnu" ar skaitļiem no 1 līdz 9
	fill_count = len(matrix) * len(matrix[0]) - delete_count
	for k in range(fill_count):
		i = random.randint(0, 8)
		j = random.randint(0, 8)
		while result[i][j] != 0:
			i = random.randint(0, 8)
			j = random.randint(0, 8)
		result[i][j] = matrix[i][j]

	return result


def read_student_data(file_name):
	# Šī funkcija nolasa skolēna datus no CSV faila un sakārto tos vārdnīcā.
	# file_name - ceļš līdz failām (.csv datne).
	# Piemēram:
	# file_name = "C:\\Users\\User\\Desktop\\student_data.csv"
	# Tas atgriež skolēna datu vārdnīcu.
	# return student_data

	student_data = {}  # Definējam tukšu vārdnicu

	with open(file_name, 'r', newline='', encoding='utf-8-sig') as file:
		# Datu izvilkšana no CSV rindām un kārtošana vārdnīcā
		# Katrs skolēns tiek identificēts ar unikālu  skolēna kodu

		reader = csv.DictReader(file, delimiter=';')
		for row in reader:
			# Izvelcam attiecīgos datus no katras CSV faila rindas un sakārtojam tos vārdnīcā

			student_code = row['Personas kods']  # Izvelcam skolēna unikālo ID identifikatoru (Personas kodu) no kolonnas "Personas kods"
			student_name = row['Vārds']  # Izvelcam skolēna uzvārdu no rindas "Vārds".
			student_last_name = row['Uzvārds']  # Izvelcam skolēna uzvārdu no rindas "Uzvārds".
			student_class = row['Klase']  # Izvelcam skolēna klasi no rindas "Klase".
			math_grades = [int(grade) for grade in row['Matemātika'].split()]  # Izņemam matemātikas atzīmes no rindas "Matemātika" un pārveidojam "int" skaitļos
			science_grades = [int(grade) for grade in row['Dabaszinības'].split()]  # Izņemam dabaszīnibas atzīmes no rindas "Dabaszinības" un pārveidojam "int" skaitļos
			history_grades = [int(grade) for grade in row['Vēsture'].split()]  # Izņemam vēstures atzīmes no rindas "Vēsture" un pārveidojam "int" skaitļos
			geo_grades = [int(grade) for grade in row['Ģeogrāfija'].split()]  # Izņemam ģeogrāfijas atzīmes no rindas "Ģeogrāfija" un pārveidojam "int" skaitļos
			computer_grades = [int(grade) for grade in row['Datorika'].split()]  # Izņemam datorika atzīmes no rindas "Datorika" un pārveidojam "int" skaitļos

			# Izveido vārdnīcu ar nosaukumu subject_grades, lai saglabātu katra priekšmeta atzīmes. Vārdnīca ir strukturēta šādi:
			# Priekšmets: Atzīmē priekšmeta nosaukumu ('Matemātika', 'Dabaszinības', 'Vēsture', 'Ģeogrāfija', 'Datorika').
			# Atzīmes: atspoguļo attiecīgajam mācību priekšmetam atbilstošo atzīmju sarakstu.
			subject_grades = {
			    'Matemātika': math_grades,
			    'Dabaszinības': science_grades,
			    'Vēsture': history_grades,
			    'Ģeogrāfija': geo_grades,
			    'Datorika': computer_grades
			}

			# Pievienojam skolēna informāciju un atzīmes vārdnīcai student_data
			student_data[student_code] = {'Vārds': student_name, 'Uzvārds': student_last_name, 'Klase': student_class, 'Marks': subject_grades}

	return student_data


def print_student_grades_by_code(student_data, student_code):
	# Šī funkcija izdrukā skolēna atzīmes, kas identificētas pēc skolēna koda.
	# student_data: vārdnīca, kurā ir skolēna dati.
	# studenta_kods: skolēna unikālais identifikators (Skolēna ID (Personas kods)).
	# Atgriež: None

	if student_code in student_data:  # Pārbaudam, vai skolēna datu vārdnīcā ir šāds skolēna kods (vai tāds skolēns eksistē)
		student_info = student_data[student_code]  # Iegūvam informāciju par doto skolēna kodu
		student_name = student_info['Vārds']  # Iegūvam informāciju par doto skolēna vārdu
		student_surname = student_info['Uzvārds']  # Iegūvam informāciju par doto skolēna uzvārdu
		student_grades = student_info['Marks']  # Iegūvam informāciju par doto skolēna atzīmem

		print(f"Atzīmes skolēnam: {student_name} {student_surname}")  # Uzrakstām lietotājam skolēna atzīmes.

		for subject, grades in student_grades.items():  # Ejam ciklā caur katru priekšmetu un tām atbilstošam atzīmem un izdrūkam tos
			print(f"Priekšmets: {subject}, Atzīmes: {grades}")  # Izdrukājam priekšmeta nosaukumu un tā atzīmes

	else:  # Izdrukājam paziņojumu, kas norāda, ka skolēns ar norādīto kodu netika atrasts, ja netika atrāsts šāds personas kods.
		print(f"Skolēns ar personas kodu '{student_code}' nav atrāsts.")


def calculate_average(grades):
	# Aprēķina vidējo atzīmi no atzīmju saraksta.
	# Tas atgriež vidējo atzīmi kā noapaļotu līdz veselam skaitlim.
	# (Ja nevajag apoļot, tad return average)
	# Ja atzīmju saraksts ir tukšs, tas atgriež 0.

	total = sum(grades)
	count = len(grades)
	if count == 0:
		return 0  # Gadījums, kad nav atzīmēs.
	average = total / count
	return round(average)


def generate_white_journal(student_data):
	# Ģenerē baltu žurnālu, pamatojoties uz skolēna datiem.
	# Tas atgriež vārdnīcu, kurā ir priekšmeti kā atslēgas, un skolēnu vārdu un vidējo atzīmju vārdnīcu kā vērtības.
	# Atgriež baltu žurnālu.

	white_journal = {}  # Inicializējam tukšu vārdnīcu, lai saglabātu balto žurnālu.

	for student_name, data in student_data.items():  # Iterējam caur katru skolēnu student_datu vārdnīcā.
		student_class = data['Klase']  # Iegūvam skolēna klasi
		subject_grades = data['Marks']  # Iegūvam skolēna atzīmes

		for subject, grades in subject_grades.items():  # Iterējam caur katru priekšmetu un tā atbilstošās atzīmem.
			average_grade = calculate_average(grades)  # Aprēķinam katra priekšmeta vidējo atzīmi un saglabājam to baltajā žurnālā.
			if subject not in white_journal:  # Ja priekšmets vēl nav iekļauts vārdnīcā white_journal, pievienojam to.
				white_journal[subject] = {}
			white_journal[subject][student_name] = average_grade  # Pievienojam skolēna vārdu un vidējo atzīmi attiecīgajam priekšmetam baltajā žurnālā.

	return white_journal  # Atgriež baltu žurnālu.


def generate_testimony(student_data):
	# Šī funkcija ģenerē liecību, pamatojoties uz skolēna datiem.
	# Tas atgriež simbolu virkni, kas satur liecību.
	# Ja skolēnam vidēja atzīme ir 0 (visas atzīmes ir 0), tad tas priekšmēts neparadīsies (vajag ierākstīt 0 priekšmētos kurus nav skolēnam).

	testimony = ""

	for student_name, data in student_data.items():
		student_class = data['Klase']
		subject_grades = data['Marks']

		testimony = testimony + f"Liecība ID: {student_name} (Klase: {student_class}):\n"
		for subject, grades in subject_grades.items():
			average_grade = calculate_average(grades)
			if average_grade != 0:
				testimony = testimony + f"Priekšmets: {subject}, Vidējā atzīme: {average_grade}\n"
		testimony = testimony + "\n"

	return testimony


def write_testimony_to_file(testimony, file_name):
	# Ieraksta ģenerēto liecību .txt failā (file_name)
	# Tas neatgriež nekādu vērtību (atgriež None)

	with open(file_name, 'w', encoding='utf-8') as file:
		file.write(testimony)

def input_lines_by_user():
	# Metode, kas paprasā lietotājam ievādīt jaunu tekstu pa rindiņam un atgriež katru rindu, kā saraksta elementu.
	# (Prasa ievadit i + 1 rindu, lai 0.rindu būtu uzrakstīta kā 1.rinda).
	# Kad tiek uzrakstīts "...", tad apstāšana.
	# Var izmantot datnes nolasīšanai un apstrādei.
	# Atgriež sarakstu, kurā katrs elements ir rindas teksts (0.elements ir 0.rindas teksts, 1.elements ir 1.rindas teksts utt.)

	lines = []
	while True:
		ievade = input(f"Ievadiet {len(lines) + 1}. rindas tekstu. Ja vēlies pabeigt, ievadi \"...\": ")
		if ievade == "...":
			break
		lines.append(ievade)

	return lines


def write_to_new_file_list(datne, lines):
	# DZĒŠ VISU SATURU NO FAILĀ un ierāksta failā "datne" (piemēram, .txt failā) lines saraksts, kur katrs saraksta elements ir rindas teksts.
	# lines - saraksts, kur katrs saraksta elements ir rindas teksts.
	# datne - datnes fails (.txt)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	with open(datne, mode="w", encoding="utf-8") as datne:
		for line in lines:
			datne.write(line + "\n")


def print_text_from_data_by_rows(datne):
	# Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
	# datne - datnes fails (piemēram, .txt fails)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	with open(datne, mode="r", encoding="utf-8") as datne:
		for rinda in datne:
			print(rinda, end='')


def write_to_file_list(lines, datne):
	# Ierāksta datne failā (piemēram, .txt failā) lines saraksts, kur katrs saraksta elements ir rindas teksts.
	# lines - saraksts, kur katrs saraksta elements ir rindas teksts.
	# datne - datnes fails (.txt)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	with open(datne, mode="a", encoding="utf-8") as datne:
		for line in lines:
			datne.write(line + "\n")


def print_text_from_data_by_rows(datne):
	# Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
	# datne - datnes fails (piemēram, .txt fails)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	with open(datne, mode="r", encoding="utf-8") as datne:
		for rinda in datne:
			print(rinda, end='')


def tekstu_parkopesena_no_datne1_to_datne2(datne1, datne2):
	# Pārkope tekstu no datne1 -> datne2.
	# Atgriež None
	# datne1 - no kurā failā gribām paņemt informāciju.
	# datne2 - kurā failā gribām informāciju no datne1 pārkopēt.
	# Piemēram:
	# datne1 = "C:\\Users\\User\\Desktop\\teksts.txt"
	# datne2 = "C:\\Users\\User\\Desktop\\teksts2.txt"

	with open(datne1, mode="r", encoding="utf-8") as datne1:
		with open(datne2, mode="w", encoding="utf-8") as datne2:
			for rinda in datne1:
				datne2.write(rinda)


def read_student_data(file_name):
	# Šī funkcija nolasa skolēna datus no CSV faila un sakārto tos vārdnīcā.
	# file_name - ceļš līdz failām (.csv datne).
	# Piemēram:
	# file_name = "C:\\Users\\User\\Desktop\\student_data.csv"
	# Tas atgriež skolēna datu vārdnīcu.
	# return student_data

	student_data = {}  # Definējam tukšu vārdnicu

	with open(file_name, 'r', newline='', encoding='utf-8-sig') as file:
		# Datu izvilkšana no CSV rindām un kārtošana vārdnīcā
		# Katrs skolēns tiek identificēts ar unikālu  skolēna kodu

		reader = csv.DictReader(file, delimiter=';')
		for row in reader:
			# Izvelcam attiecīgos datus no katras CSV faila rindas un sakārtojam tos vārdnīcā

			student_code = row['Personas kods']  # Izvelcam skolēna unikālo ID identifikatoru (Personas kodu) no kolonnas "Personas kods"
			student_name = row['Vārds']  # Izvelcam skolēna uzvārdu no rindas "Vārds".
			student_last_name = row['Uzvārds']  # Izvelcam skolēna uzvārdu no rindas "Uzvārds".
			student_class = row['Klase']  # Izvelcam skolēna klasi no rindas "Klase".
			math_grades = [int(grade) for grade in row['Matemātika'].split()]  # Izņemam matemātikas atzīmes no rindas "Matemātika" un pārveidojam "int" skaitļos
			science_grades = [int(grade) for grade in row['Dabaszinības'].split()]  # Izņemam dabaszīnibas atzīmes no rindas "Dabaszinības" un pārveidojam "int" skaitļos
			history_grades = [int(grade) for grade in row['Vēsture'].split()]  # Izņemam vēstures atzīmes no rindas "Vēsture" un pārveidojam "int" skaitļos
			geo_grades = [int(grade) for grade in row['Ģeogrāfija'].split()]  # Izņemam ģeogrāfijas atzīmes no rindas "Ģeogrāfija" un pārveidojam "int" skaitļos
			computer_grades = [int(grade) for grade in row['Datorika'].split()]  # Izņemam datorika atzīmes no rindas "Datorika" un pārveidojam "int" skaitļos

			# Izveido vārdnīcu ar nosaukumu subject_grades, lai saglabātu katra priekšmeta atzīmes. Vārdnīca ir strukturēta šādi:
			# Priekšmets: Atzīmē priekšmeta nosaukumu ('Matemātika', 'Dabaszinības', 'Vēsture', 'Ģeogrāfija', 'Datorika').
			# Atzīmes: atspoguļo attiecīgajam mācību priekšmetam atbilstošo atzīmju sarakstu.
			subject_grades = {
			    'Matemātika': math_grades,
			    'Dabaszinības': science_grades,
			    'Vēsture': history_grades,
			    'Ģeogrāfija': geo_grades,
			    'Datorika': computer_grades
			}

			# Pievienojam skolēna informāciju un atzīmes vārdnīcai student_data
			student_data[student_code] = {'Vārds': student_name, 'Uzvārds': student_last_name, 'Klase': student_class, 'Marks': subject_grades}

	return student_data


def print_student_grades_by_code(student_data, student_code):
	# Šī funkcija izdrukā skolēna atzīmes, kas identificētas pēc skolēna koda.
	# student_data: vārdnīca, kurā ir skolēna dati.
	# studenta_kods: skolēna unikālais identifikators (Skolēna ID (Personas kods)).
	# Atgriež: None

	if student_code in student_data:  # Pārbaudam, vai skolēna datu vārdnīcā ir šāds skolēna kods (vai tāds skolēns eksistē)
		student_info = student_data[student_code]  # Iegūvam informāciju par doto skolēna kodu
		student_name = student_info['Vārds']  # Iegūvam informāciju par doto skolēna vārdu
		student_surname = student_info['Uzvārds']  # Iegūvam informāciju par doto skolēna uzvārdu
		student_grades = student_info['Marks']  # Iegūvam informāciju par doto skolēna atzīmem

		print(f"Atzīmes skolēnam: {student_name} {student_surname}")  # Uzrakstām lietotājam skolēna atzīmes.

		for subject, grades in student_grades.items():  # Ejam ciklā caur katru priekšmetu un tām atbilstošam atzīmem un izdrūkam tos
			print(f"Priekšmets: {subject}, Atzīmes: {grades}")  # Izdrukājam priekšmeta nosaukumu un tā atzīmes

	else:  # Izdrukājam paziņojumu, kas norāda, ka skolēns ar norādīto kodu netika atrasts, ja netika atrāsts šāds personas kods.
		print(f"Skolēns ar personas kodu '{student_code}' nav atrāsts.")


def calculate_average(grades):
	# Aprēķina vidējo atzīmi no atzīmju saraksta.
	# Tas atgriež vidējo atzīmi kā noapaļotu līdz veselam skaitļim.
	# (Ja nevajag apoļot, tad return average)
	# Ja atzīmju saraksts ir tukšs, tas atgriež 0.

	total = sum(grades)
	count = len(grades)
	if count == 0:
		return 0  # Gadījums, kad nav atzīmēs.
	average = total / count
	return round(average)


def generate_white_journal(student_data):
	# Ģenerē baltu žurnālu, pamatojoties uz studenta datiem.
	# Tas atgriež vārdnīcu, kurā ir priekšmeti kā atslēgas, un skolēnu vārdu un vidējo atzīmju vārdnīcu kā vērtības.
	# Atgriež baltu žurnālu.

	white_journal = {}  # Inicializējam tukšu vārdnīcu, lai saglabātu balto žurnālu.

	for student_name, data in student_data.items():  # Iterējam caur katru skolēnu student_datu vārdnīcā.
		student_class = data['Klase']  # Iegūvam skolēna klasi
		subject_grades = data['Marks']  # Iegūvam skolēna atzīmes

		for subject, grades in subject_grades.items():  # Iterējam caur katru priekšmetu un tā atbilstošās atzīmem.
			average_grade = calculate_average(grades)  # Aprēķinam katra priekšmeta vidējo atzīmi un saglabājam to baltajā žurnālā.
			if subject not in white_journal:  # Ja priekšmets vēl nav iekļauts vārdnīcā white_journal, pievienojiet to.
				white_journal[subject] = {}
			white_journal[subject][student_name] = average_grade  # Pievienojam skolēna vārdu un vidējo atzīmi attiecīgajam priekšmetam baltajā žurnālā.

	return white_journal  # Atgriež baltu žurnālu.


def generate_testimony(student_data):
	# Šī funkcija ģenerē liecību, pamatojoties uz skolēna datiem.
	# Tas atgriež simbolu virkni, kas satur liecību.
	# Ja skolēnam vidēja atzīme ir 0 (visas atzīmes ir 0), tad tas priekšmēts neparadīsies (vajag ierākstīt 0 priekšmētos kurus nav skolēnam).

	testimony = ""

	for student_name, data in student_data.items():
		student_class = data['Klase']
		subject_grades = data['Marks']

		testimony = testimony + f"Liecība ID: {student_name} (Klase: {student_class}):\n"
		for subject, grades in subject_grades.items():
			average_grade = calculate_average(grades)
			if average_grade != 0:
				testimony = testimony + f"Priekšmets: {subject}, Vidējā atzīme: {average_grade}\n"
		testimony = testimony + "\n"

	return testimony


def write_testimony_to_file(testimony, file_name):
	# Ieraksta ģenerēto liecību .txt failā (file_name)
	# Tas neatgriež nekādu vērtību (atgriež None)

	with open(file_name, 'w', encoding='utf-8') as file:
		file.write(testimony)


def change_student_marks(file_name, student_id, subject, new_marks):
	# Izmainā skolēna atzīmes noteiktā priekšmeta uz jaunajām.
	# Atgriež True, ja netika atrāsta neviena kļūda.
	# Atgriež False, ja tika atrāsta kļūda.
	# file_name - .csv failā ceļš
	# student_id - skolēna personas kods
	# subject - skolas priekšmēts
	# new_marks - jaunās atzīmes
	student_data = read_student_data(file_name)  # Nolasa skolēnu datus no CSV faila

	if student_id in student_data:  # Pārbauda, vai skolēna ID ir iekšā student_data
		# Iegūst skolēna informāciju un atzīmes
		student_info = student_data[student_id]
		student_grades = student_info['Marks']

		# Pārbauda, vai priekšmets pastāv skolēna atzīmēs
		if subject in student_grades:
			# Atjaunina atzīmes ar jaunajām atzīmēm
			student_grades[subject] = new_marks

			# Ieraksta atjauninātos skolēna datus atpakaļ CSV failā
			with open(file_name, 'w', newline='', encoding='utf-8-sig') as file:
				kolonnas_nosaukumi = ['Personas kods', 'Vārds', 'Uzvārds', 'Klase', 'Matemātika', 'Dabaszinības', 'Vēsture', 'Ģeogrāfija', 'Datorika']
				writer = csv.DictWriter(file, fieldnames=kolonnas_nosaukumi, delimiter=';')
				writer.writeheader()

				for student_code, student_info in student_data.items():
					# Ieraksta skolēna informāciju un atzīmes CSV failā

					writer.writerow({
					    'Personas kods': student_code,  # Ierakstam skolēna unikālo identifikatoru kolonnā "Personas kods".
					    'Vārds': student_info['Vārds'],  # Ailē 'Vārds' ierakstiet skolēna vārdu
					    'Uzvārds': student_info['Uzvārds'],  # Ailē 'Uzvārds' ierakstiet skolēna uzvārdu
					    'Klase': student_info['Klase'],  # Ierakstam skolēna klasi kolonnā "Klase".
					    'Matemātika': ' '.join(str(grade) for grade in student_info['Marks']['Matemātika']),  # Konvertējam un savienojam visas matemātikas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Matemātika"
					    'Dabaszinības': ' '.join(str(grade) for grade in student_info['Marks']['Dabaszinības']),  # Konvertējam un savienojam visas dabaszīnibas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Dabaszinības"
					    'Vēsture': ' '.join(str(grade) for grade in student_info['Marks']['Vēsture']),  # Konvertējam un savienojam visas vēstures atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Vēsture"
					    'Ģeogrāfija': ' '.join(str(grade) for grade in student_info['Marks']['Ģeogrāfija']),  # Konvertējam un savienojam visas ģeogrāfijas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Ģeogrāfija"
					    'Datorika': ' '.join(str(grade) for grade in student_info['Marks']['Datorika'])  # Konvertējam un savienojam visas datorikas atzīmes ar atstarpi atdalītā simbolu virknē un ierakstisim to rindiņa "Datorika"
					})

			return True  # Atgriež True, lai norādītu uz veiksmīgu skolēna atzīmju izmainīšanu

		else:
			print(f"Skolēns ar personas kodu '{student_id}' nav atrasts priekšmetā '{subject}'.")
	else:
		print(f"Skolēns ar personas kodu '{student_id}' nav atrasts.")

	return False  # Atgriež False, lai norādītu uz neveiksmigu skolēnu atzīmju izmainīšanu

class SymbolCount:
	def __init__(self, burts, skaits):
		# Inicializācija.
		# Instancei ir burts un skaits vērtības.
		# Strāda lidzīgi kortēžam ("burts", skaits), piemēram ("A", 0).

		self.burts = burts
		self.skaits = skaits

	def __repr__(self):
		# Izvada lietotājam instances burtu un skaitu, izmantojot print.
		# Piemēram:
		# print(alphabet[0])
		# Izvada:
		# ("A", 24422)

		return f'("{self.burts}", {self.skaits})'

	@staticmethod
	def create_latin_alphabet():
		# Atgriež sarakstu ar lieliem latiņu alfabētu burtiem alfabētiska secība, kur katram burtam ir piekārtots skaits 0.
		# Lidzīgi kā atgriež tādu sarakstu ar kortežiem:
		# [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0), ("F", 0), ("G", 0), ("H", 0), ("I", 0), ("J", 0), ("K", 0), ("L", 0), ("M", 0), ("N", 0), ("O", 0), ("P", 0), ("Q", 0), ("R", 0), ("S", 0), ("T", 0), ("U", 0), ("V", 0), ("W", 0), ("X", 0), ("Y", 0), ("Z", 0)]
		# Izmanto chr funkciju.

		saraksts = []
		for i in range(26):
			burts = chr(i + 65)
			skaits = 0
			saraksts.append(SymbolCount(burts, skaits))

		return saraksts

	@staticmethod
	def update_symbol_count(alphabet, symbol):
		# Atjauno (palielinā par vienu) simbolu (burtu) skaitu alphabet mainīgajā, konkrētāja vietā (kur ir tās noteikts kortežs ar atbilstošu burtu un skaitu).
		# alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
		# alphabet = SymbolCount.create_latin_alphabet()
		# symbol - simbols, kurš ir uzrakstīts ar Unicode skaitļi. Izvelēsimies kādu simbolu skaitu atjaunosim.

		symbol = symbol.upper()
		kods = ord(symbol)
		if 65 <= kods <= 90:
			index = kods - 65
			alphabet[index].skaits += 1

	@staticmethod
	def update_symbol_count_for_all_text(alphabet, text):
		# Atjauno simbolu (burtu) skaitu visam tekstam mainīgajā alphabet.
		# text - simbolu virkne (str), kurai atjaunosim visu burtu biežumu vērtības.
		# alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
		# alphabet = SymbolCount.create_latin_alphabet()

		for char in text:
			SymbolCount.update_symbol_count(alphabet, char)

	@staticmethod
	def print_symbols_by_frequency(alphabet):
		# Izvada lietotājam alphabeta visus burtus dilstoša secība pēc burtu biežuma. Izmanto print.
		# alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
		# alphabet = SymbolCount.create_latin_alphabet()
		# Atgriež None
		# Izvada jau sakartotu alfabētu, piemēram šādi:
		# E 10
		# T 5
		# A 4
		# I 3
		# N 3
		# ... (utt)

		sorted_alphabet = SymbolCount.sort_sella_dilstosa(alphabet)
		for obj in sorted_alphabet:
			print(obj.burts, obj.skaits)

	@staticmethod
	def sort_sella_dilstosa(a):
		# Sakārto masīvu dilstošā secībā, izmantojot Šellas metodi (Shell sort)
		# a - saraksts (masīvs).
		# Atgriež sakartotu masīvu dilstošā secībā.

		n = len(a)
		solis = (3 ** math.floor(math.log(2 * n + 1, 3)) - 1) // 2
		while solis >= 1:
			for k in range(0, solis):
				for i in range(solis + k, n, solis):
					if a[i - solis].skaits < a[i].skaits:
						x = a[i]
						j = i
						while a[j - solis].skaits < x.skaits:
							a[j] = a[j - solis]
							j = j - solis
							if j == k:
								break
						a[j] = x
			solis = (solis - 1) // 3

		return a


	def encrypt(text_non_sifrets, atslega, burti):
		# Atgriež aizifrētu (sifrets) str tekstu, pamatojoties uz text_non_sifrets, atslega un burti.
		# Tas ej ciklā (pa indeksiem) pa katru burtu text_non_sifrets uz atslega skaitu un tāda veida pa burtiem izveido jau aizšifrētu (sifrets) tekstu.
		# Ej pa indeksiem uz priekšu uz atslega skaitu.
		# text_non_sifrets - str teksts, kas nav šifrēts.
		# atslega - simbolu virkne (str), kas sastāv no cipariem no 0 līdz 9 un tas nav lielāka nekā text_sifrets.
		# burti - saraksts ar visiem alfabēta burtiem, pec kuriem gribat aizšifrēt.
		# Piemēram:
		# burti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]
	
		sifrets = ""  # Tukšais str, kuru piepildīsim ar aizšifrētiem burtiem.
	
		for i in range(len(text_non_sifrets)):  # Ej ciklā pa text_non_sifrets visiem burtiem.
			char = text_non_sifrets[i]  # char - i-tajs burts text_non_sifrets str tekstā.
			if char in burti:  # Pārbaudam vai rakstzīme (simbols) ir in burti list.
				key = int(atslega[i % len(atslega)])  # Iegūstam atbilstošo atslēgas ciparu, izmantojot moduļ (%) operatoru.
				encrypted_char_index = (burti.index(char) + key) % len(burti)  # Aprēķinam aizšifrēto rakstzīmju indeksu.
				encrypted_char = burti[encrypted_char_index]  # Iegūstam aizšifrētu rakstzīmi.
				sifrets += encrypted_char  # Pievienojam aizšifrētu burtu simbolu virknei sifrets.
			else:
				sifrets += char  # Pievienojam rakstzīmi tādu, kāds tas ir, ja tas nav in burti list.
	
		return sifrets  # Atgriež str simbolu virkni sifrets.
	
	
	def decrypt(text_sifrets, atslega, burti):
		# Atgriež atšifrētu (nav_sifrets) str tekstu, pamatojoties uz text_sifrets, atslega un burti.
		# Tas ej ciklā (pa indeksiem) pa katru burtu text_sifreta uz atslega skaitu un tāda veida pa burtiem izveido jau atšifrētu (nav_sifrets) tekstu.
		# Ej pa indeksiem atpakaļ uz atslega skaitu.
		# text_sifrets - str teksts, kas ir šifrēts.
		# atslega - simbolu virkne (str), kas sastāv no cipariem no 0 līdz 9 un tas nav lielāka nekā text_sifrets.
		# burti - saraksts ar visiem alfabēta burtiem, pec kuriem gribat atšifrēt.
		# Piemēram:
		# burti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]
	
		nav_sifrets = ""  # Tukšais str, kuru piepildīsim ar atšifrētiem burtiem.
	
		for i in range(len(text_sifrets)):  # Ej ciklā pa text_sifrets visiem burtiem.
			char = text_sifrets[i]  # char - i-tajs burts text_sifrets str tekstā.
			if char in burti:  # Pārbaudam vai rakstzīme (simbols) ir in burti list.
				key = int(atslega[i % len(atslega)])  # Iegūstam atbilstošo atslēgas ciparu, izmantojot modules (%) operatoru.
				decrypted_char_index = (burti.index(char) - key) % len(burti)  # Aprēķinam atšifrēto rakstzīmju indeksu.
				decrypted_char = burti[decrypted_char_index]  # Iegūstam atšifrētu rakstzīmi.
				nav_sifrets += decrypted_char  # Pievienojam atšifrētu burtu simbolu virknei nav_sifrets.
			else:  # Ja burts nav in burti list, tad vienkarši pievienojam to rakstzīmi nav_sifrets simbolu virknei.
				nav_sifrets += char  # Pievienojam to pašu burtu simbolu virknei nav_sifrets (ja tas burts nav in burti list)
	
		return nav_sifrets  # Atgriež str simbolu virkni nav_sifrets.
	
	
	def input_cypher_or_decrypt():
		# Prasa lietotājam vai lietotājs grib aizšifrēt (encrypt) tekstu vai atšifrēt (decrypt) tekstu.
		# Ja lietotājs ievādīs "c" vai "C", tad viņš grib aizšifrēt (encrypt).
		# Ja lietotājs ievādīs "d" vai "D", tad viņš grib atšifrēt (decrypt).
		# Atgriež True, ja ir ievādīts "c" vai "C" (str).
		# Atgriež False, ja ir ievādīts "d" vai "D" (str).
	
		cypher_or_decrypt = ""
		while cypher_or_decrypt.lower() != "c" and cypher_or_decrypt.lower() != "d":
			cypher_or_decrypt = input("Ievadiet vai gribāt aizšifrēt (c) vai atšifrēt (d) tekstu ==> ")
			if cypher_or_decrypt.lower() == "c":
				return True
			elif cypher_or_decrypt.lower() == "d":
				return False
	
	
	def input_atslega(text_non_sifrets):
		# Prasa lietotājam ievādīt atslēgu kāmer tas nav lielāka par text_non_sifrets vai kāmēr tā tav simbolu virkne bez cipariem.
		# text_non_sifrets - str teksts, kas nav šifrēts (kuru gribat aizšifrēt).
		# Atgriež atslega, kuru ievada lietotājs.
	
		atslega = input("Ievadiet atslēgu ==> ")
		while len(atslega) > len(text_non_sifrets) or not atslega.isdigit():
			print("Kļūda! Ievadiet atslēgu kā ciparu virkni no 0 līdz 9, kas nav garāka par tekstu!")
			atslega = input("Ievadiet atslēgu ==> ")
	
		return atslega
	
	
	def cypher_main():
		# Encryption.
		# Ieraksta failā ir_sifrets_txt = "C:\\Users\\User\\Desktop\\ir_sifrets_1.txt" aizšifrētu tekstu.
		# Ieraksta failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_1.txt" atslēgu, kuru ievādīs lietotājs, izmantojot input_atslega funkciju.
	
		text_non_sifrets = save_text_from_data_by_rows_to_variable(nav_sifrets_txt)  # Saglabam mainīgajā text_non_sifrets no nav_sifrets_txt datnes. Saglabam kā str virkni.
		text_non_sifrets = text_non_sifrets.upper()  # Visu str simbolus pārveidojam par lieliem burtiem.
	
		print("\nNav šifrēts teksts:")  # Informācija lietotājam par to, kads tagad teksts nav šifrēts (kuru mes aizšifrēsim pēc atslēgas).
		print(text_non_sifrets)  # Izvadam pagaidam nav aizšifrētu tekstu, ka simbolu virkni.
		print()  # Atstarpe glītumam.
	
		atslega = input_atslega(text_non_sifrets)  # Prasam lietotājam ievādīt atslegu.
	
		sifrets = encrypt(text_non_sifrets, atslega, burti)  # Aizšifrējam sifrets simbolu virkni.
		print()
	
		print(f"Teksts tika aizšifrēts ar atslēgu {atslega}:")
		print(sifrets)  # Izvadam aizšifrētu tekstu lietotājam.
		write_text_to_file(ir_sifrets_txt, sifrets)  # Ierakstam failā ir_sifrets_txt = "C:\\Users\\User\\Desktop\\ir_sifrets_1.txt" aizšifrētu tekstu.
		write_text_to_file(atslega_txt, atslega)  # Ierakstam failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_1.txt" atslegas kodu.
	
	
	def decrypt_main():
		# Decryption.
		# Ieraksta failā nav_sifrets_txt = "C:\\Users\\User\\Desktop\\nav_sifrets_1.txt" atšifrētu tekstu.
		# Ieraksta failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_1.txt" atslēgu, kuru ievādīs lietotājs, izmantojot input_atslega funkciju.
	
		text_sifrets = save_text_from_data_by_rows_to_variable(ir_sifrets_txt)  # Saglabam mainīgajā text_sifrets no ir_sifrets_txt datnes. Saglabam kā str virkni.
		text_sifrets = text_sifrets.upper()  # Visu str simbolus pārveidojam par lieliem burtiem.
	
		print("\nŠifrēts teksts:")  # Informācija lietotājam par to, kā aizskatās šifrēts teksts (kuru mes atšifrēsim pēc atslēgas).
		print(text_sifrets)  # Izvadam pagaidam nav atšifrētu tekstu, ka simbolu virkni.
		print()  # Atstarpe glītumam.
	
		atslega = input_atslega(text_sifrets)  # Prasam lietotājam ievādīt atslegu.
	
		nav_sifrets = decrypt(text_sifrets, atslega, burti)  # Atšifrējam nav_sifrets simbolu virkni.
		print()
	
		print(f"Teksts tika atšifrēts ar atslēgu {atslega}:")
		print(nav_sifrets)  # Izvadam atšifrētu tekstu lietotājam.
		write_text_to_file(nav_sifrets_txt, nav_sifrets)  # Ierakstam failā nav_sifrets_txt = "C:\\Users\\User\\Desktop\\nav_sifrets_1.txt" atšifrētu tekstu.



def encrypt_to_morse_code(non_encrypted_text, morse_code_dictionary):
	# Funkcija, kas pārvērš neaizšifrētu tekstu par Morzes kodu, izmantojot Morzes kodu vārdnīcu.
	# Atgriež aizšifrētu tekstu kā Morzes kodu (str).
	# Ieraksta .txt datnē aizsifrets_to_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\morzes_kods_save.txt" tekstu, kas tika aizšifrēts.
	# non_encrypted_text - str teksts, kuru gribam pārverst par Morzes kodu.
	# morse_code_dictionary - vārdnica ar parastu simbolu : atbilstošu Morzes kodu
	# Piemēram: {"A" : ".-", "B": "-..." , utt. }

	encrypted_text = ""  # Sākumā aizšifrētais teksts ir tukšs.
	for symbol in non_encrypted_text:  # Pārskatām katru simbolu nešifrētajā tekstā.
		sym = symbol.upper()  # Pārveidojam simbolu tā, lai viņš būtu liels burts.
		if sym in morse_code_dictionary:  # Ja simbols ir Morzes koda vārdnīcā.
			encrypted_text = encrypted_text + morse_code_dictionary[sym] + " "  # Pievienojam aizšifrētu ar Morzes kodu burtu encrypted_text simbolu virknei ar atstarpi.
		else:
			encrypted_text = encrypted_text + sym + " "  # Ja simbols nav Morzes kodā, tad vienkarši pievienojam to nešifrētu burtu kopā ar atstarpi.

	write_text_to_file(aizsifrets_to_morses_kods_save_txt, encrypted_text)  # Ieraksta .txt datnē aizsifrets_to_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\morzes_kods_save.txt" tekstu, kas tika atšifrēts.

	return encrypted_text  # Atgriežam aizšifrētu Morzes kodu.


def decrypt_from_morse_code(encrypted_text, morse_code_dictionary):
	# Funkcija, kas atšifrē Morzes kodu (pārverš par vienkaršu str tekstu), izmantojot Morzes kodu vārdnīcu.
	# Atgriež atšifrētu tekstu no Morzes kodu kā parastu tekstu (str).
	# Ieraksta .txt datnē atsifrets_no_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\atsifrets_no_morzes_koda_save.txt" tekstu, kas tika atšifrēts.
	# encrypted_text - str Morzes kods, kuru gribam pārverst par parastu tekstu.
	# morse_code_dictionary - vārdnica ar parastu simbolu : atbilstošu Morzes kodu
	# Piemēram: {"A" : ".-", "B": "-..." , utt. }

	decrypted_text = ""  # Sākumā atšifrētais teksts ir tukšs.
	morse_code = ""  # Sākumā Morzes kods ir tukšs.
	for symbol in encrypted_text:  # Pārskatām katru simbolu aizšifrētajā tekstā.
		if symbol != " ":  # Ja simbols nav atstarpe.
			morse_code = morse_code + symbol  # Pievienojam simbolu Morzes kodam.
		else:
			if morse_code in morse_code_dictionary.values():  # Ja Morzes kods ir atrodams Morzes koda vārdnīcā.
				for key, value in morse_code_dictionary.items():  # Pārskatām katru pāri (atslēga, vērtība) vārdnīcā.
					if value == morse_code:  # Ja vērtība atbilst Morzes kodam.
						decrypted_text = decrypted_text + key  # Pievienojam vārdnicas noteiktu "atslēgu" (key) (key - value vārdnīca) atšifrētajam tekstam.
						break  # Pārtraucam meklēšanu pēc "atslēgas" (key).
			else:
				decrypted_text = decrypted_text + morse_code  # Ja Morzes kods nav atrodams vārdnīcā, pievienojam to atšifrētajam tekstam.

			morse_code = ""

	# Pārbaudam, vai teksta non_encrypted_text beigās nav palicis Morzes kods.
	if morse_code != "":
		if morse_code in morse_code_dictionary.values():  # Ja Morzes kods ir atrodams vārdnīcā.
			for key, value in morse_code_dictionary.items():  # Pārskatām katru pāri (atslēga, vērtība) vārdnīcā.
				if value == morse_code:  # Ja vērtība atbilst Morzes kodam.
					decrypted_text = decrypted_text + key  # Pievienojam vārdnicas noteiktu "atslēgu" (key) (key - value vārdnīca) atšifrētajam tekstam.
					break  # Pārtraucam meklēšanu pēc "atslēgas" (key).
		else:
			decrypted_text = decrypted_text + morse_code  # Ja Morzes kods nav atrodams vārdnīcā, pievienojam to atšifrētajam tekstam.

	write_text_to_file(atsifrets_no_morses_kods_save_txt, decrypted_text)  # Ieraksta .txt datnē atsifrets_no_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\atsifrets_no_morzes_koda_save.txt" tekstu, kas tika atšifrēts.

	return decrypted_text  # Atgriežam atšifrēto tekstu


def input_cypher_to_morse_or_decrypt_from_morse():
	# Prasa lietotājam vai lietotājs grib aizšifrēt (encrypt) tekstu vai atšifrēt (decrypt) tekstu.
	# Ja lietotājs ievādīs "c" vai "C", tad viņš grib aizšifrēt (encrypt).
	# Ja lietotājs ievādīs "d" vai "D", tad viņš grib atšifrēt (decrypt).
	# Atgriež True, ja ir ievādīts "c" vai "C" (str).
	# Atgriež False, ja ir ievādīts "d" vai "D" (str).

	cypher_or_decrypt = ""
	while cypher_or_decrypt.lower() != "c" and cypher_or_decrypt.lower() != "d":
		cypher_or_decrypt = input("Ievadiet vai gribāt aizšifrēt tekstu ar Morzes kodu (c) vai atšifrēt (d) tekstu no Morzes koda ==> ")
		if cypher_or_decrypt.lower() == "c":
			return True
		elif cypher_or_decrypt.lower() == "d":
			return False


class SymbolCountLv:
	def __init__(self, burts, skaits):
		# Inicializācija.
		# Instancei ir burts un skaits vērtības.
		# Strāda lidzīgi kortēžam ("burts", skaits), piemēram ("A", 0).

		self.burts = burts
		self.skaits = skaits

	def __repr__(self):
		# Izvada lietotājam instances burtu un skaitu, izmantojot print.
		# Piemēram:
		# print(alphabet[0])
		# Izvada:
		# ("A", 972)

		return f'("{self.burts}", {self.skaits})'

	@staticmethod
	def create_latvian_alphabet():
		# Atgriež sarakstu ar lieliem latviešu alfabētu burtiem alfabētiska secība, kur katram burtam ir piekārtots skaits 0.
		# Lidzīgi kā atgriež tādu sarakstu ar kortežiem:
		# [("A", 0), ("Ā", 0), ("B", 0), ("C", 0), ("Č", 0), ("D", 0), ("E", 0), ("Ē", 0), ("F", 0), ("G", 0), ("Ģ", 0), ("H", 0), ("I", 0), ("Ī", 0), ("J", 0), ("K", 0), ("L", 0), ("Ļ", 0), ("M", 0), ("N", 0), ("Ņ", 0), ("O", 0), ("P", 0), ("R", 0), ("S", 0), ("Š", 0), ("T", 0), ("U", 0), ("V", 0), ("Z", 0), ("Ž", 0)]
		# Izmanto chr funkciju.

		mas = []
		lv = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]

		for i in range(len(lv)):
			burts = lv[i]
			skaits = 0
			mas.append(SymbolCountLv(burts, skaits))

		return mas

	@staticmethod
	def update_symbol_count(alphabet, x):
		# Atjauno (palielinā par vienu) simbolu (burtu) skaitu alphabet mainīgajā, konkrētāja vietā (kur ir tās noteikts kortežs ar atbilstošu burtu un skaitu).
		# alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCountLv.create_latvian_alphabet()
		# alphabet = SymbolCountLv.create_latvian_alphabet()
		# symbol - simbols, kurš ir uzrakstīts ar Unicode skaitļi. Izvelēsimies kādu simbolu skaitu atjaunosim.

		lv = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]

		x = x.upper()
		if x in lv:
			index = lv.index(x)
			alphabet[index].skaits += 1

	@staticmethod
	def update_symbol_count_for_all_text(alphabet, text):
		# Atjauno simbolu (burtu) skaitu visam tekstam mainīgajā alphabet.
		# text - simbolu virkne (str), kurai atjaunosim visu burtu biežumu vērtības.
		# alphabet - saraksts, kas izveidots ar latiņu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCount.create_latin_alphabet()
		# alphabet = SymbolCount.create_latin_alphabet()

		for char in text:
			SymbolCountLv.update_symbol_count(alphabet, char)

	@staticmethod
	def print_symbols_by_frequency(alphabet):
		# Izvada lietotājam alphabeta visus burtus dilstoša secība pēc burtu biežuma. Izmanto print.
		# alphabet - saraksts, kas izveidots ar latviešu alfabēta burtiem alfabētiska secība, kur katram burtam ir piekārtots skaitlis, kas parāda to burta biežumu.
		# alphabet tiek izveidots izmantojot SymbolCountLv.create_latvian_alphabet()
		# alphabet = SymbolCountLv.create_latvian_alphabet()
		# Atgriež None
		# Izvada jau sakartotu alfabētu, piemēram šādi:
		# L 2
		# Ļ 2
		# B 1
		# A 1
		# I 0
		# ... (utt)

		sorted_alphabet = SymbolCountLv.sort_sella_dilstosa(alphabet)
		for obj in sorted_alphabet:
			print(obj.burts, obj.skaits)

	@staticmethod
	def sort_sella_dilstosa(a):
		# Sakārto masīvu dilstošā secībā, izmantojot Šellas metodi (Shell sort)
		# a - saraksts (masīvs).
		# Atgriež sakartotu masīvu dilstošā secībā.

		n = len(a)
		solis = (3 ** math.floor(math.log(2 * n + 1, 3)) - 1) // 2
		while solis >= 1:
			for k in range(0, solis):
				for i in range(solis + k, n, solis):
					if a[i - solis].skaits < a[i].skaits:
						x = a[i]
						j = i
						while a[j - solis].skaits < x.skaits:
							a[j] = a[j - solis]
							j = j - solis
							if j == k:
								break
						a[j] = x
			solis = (solis - 1) // 3

		return a


def save_text_from_data_by_rows_to_variable(datne):
	# Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
	# datne - datnes fails (piemēram, .txt fails)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	a = ""
	with open(datne, mode="r", encoding="utf-8") as datne:
		for rinda in datne:
			a = a + rinda
	return a


def encrypt(text_non_sifrets, atslega, burti):
	# Atgriež aizifrētu (sifrets) str tekstu, pamatojoties uz text_non_sifrets, atslega un burti.
	# Tas ej ciklā (pa indeksiem) pa katru burtu text_non_sifrets uz atslega skaitu un tāda veida pa burtiem izveido jau aizšifrētu (sifrets) tekstu.
	# Ej pa indeksiem uz priekšu uz atslega skaitu.
	# text_non_sifrets - str teksts, kas nav šifrēts.
	# atslega - simbolu virkne (str), kas sastāv no cipariem no 0 līdz 9 un tas nav lielāka nekā text_sifrets.
	# burti - saraksts ar visiem alfabēta burtiem, pec kuriem gribat aizšifrēt.
	# Piemēram:
	# burti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

	sifrets = ""  # Tukšais str, kuru piepildīsim ar aizšifrētiem burtiem.

	for i in range(len(text_non_sifrets)):  # Ej ciklā pa text_non_sifrets visiem burtiem.
		char = text_non_sifrets[i]  # char - i-tajs burts text_non_sifrets str tekstā.
		if char in burti:  # Pārbaudam vai rakstzīme (simbols) ir in burti list.
			key = int(atslega[i % len(atslega)])  # Iegūstam atbilstošo atslēgas ciparu, izmantojot moduļ (%) operatoru.
			encrypted_char_index = (burti.index(char) + key) % len(burti)  # Aprēķinam aizšifrēto rakstzīmju indeksu.
			encrypted_char = burti[encrypted_char_index]  # Iegūstam aizšifrētu rakstzīmi.
			sifrets += encrypted_char  # Pievienojam aizšifrētu burtu simbolu virknei sifrets.
		else:
			sifrets += char  # Pievienojam rakstzīmi tādu, kāds tas ir, ja tas nav in burti list.

	return sifrets  # Atgriež str simbolu virkni sifrets.


def decrypt(text_sifrets, atslega, burti):
	# Atgriež atšifrētu (nav_sifrets) str tekstu, pamatojoties uz text_sifrets, atslega un burti.
	# Tas ej ciklā (pa indeksiem) pa katru burtu text_sifreta uz atslega skaitu un tāda veida pa burtiem izveido jau atšifrētu (nav_sifrets) tekstu.
	# Ej pa indeksiem atpakaļ uz atslega skaitu.
	# text_sifrets - str teksts, kas ir šifrēts.
	# atslega - simbolu virkne (str), kas sastāv no cipariem no 0 līdz 9 un tas nav lielāka nekā text_sifrets.
	# burti - saraksts ar visiem alfabēta burtiem, pec kuriem gribat atšifrēt.
	# Piemēram:
	# burti = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

	nav_sifrets = ""  # Tukšais str, kuru piepildīsim ar atšifrētiem burtiem.

	for i in range(len(text_sifrets)):  # Ej ciklā pa text_sifrets visiem burtiem.
		char = text_sifrets[i]  # char - i-tajs burts text_sifrets str tekstā.
		if char in burti:  # Pārbaudam vai rakstzīme (simbols) ir in burti list.
			key = int(atslega[i % len(atslega)])  # Iegūstam atbilstošo atslēgas ciparu, izmantojot modules (%) operatoru.
			decrypted_char_index = (burti.index(char) - key) % len(burti)  # Aprēķinam atšifrēto rakstzīmju indeksu.
			decrypted_char = burti[decrypted_char_index]  # Iegūstam atšifrētu rakstzīmi.
			nav_sifrets += decrypted_char  # Pievienojam atšifrētu burtu simbolu virknei nav_sifrets.
		else:  # Ja burts nav in burti list, tad vienkarši pievienojam to rakstzīmi nav_sifrets simbolu virknei.
			nav_sifrets += char  # Pievienojam to pašu burtu simbolu virknei nav_sifrets (ja tas burts nav in burti list)

	return nav_sifrets  # Atgriež str simbolu virkni nav_sifrets.


def input_cypher_or_decrypt():
	# Prasa lietotājam vai lietotājs grib aizšifrēt (encrypt) tekstu vai atšifrēt (decrypt) tekstu.
	# Ja lietotājs ievādīs "c" vai "C", tad viņš grib aizšifrēt (encrypt).
	# Ja lietotājs ievādīs "d" vai "D", tad viņš grib atšifrēt (decrypt).
	# Atgriež True, ja ir ievādīts "c" vai "C" (str).
	# Atgriež False, ja ir ievādīts "d" vai "D" (str).

	cypher_or_decrypt = ""
	while cypher_or_decrypt.lower() != "c" and cypher_or_decrypt.lower() != "d":
		cypher_or_decrypt = input("Ievadiet vai gribāt aizšifrēt (c) vai atšifrēt (d) tekstu ==> ")
		if cypher_or_decrypt.lower() == "c":
			return True
		elif cypher_or_decrypt.lower() == "d":
			return False


def input_atslega(text_non_sifrets):
	# Prasa lietotājam ievādīt atslēgu kāmer tas nav lielāka par text_non_sifrets vai kāmēr tā tav simbolu virkne bez cipariem.
	# text_non_sifrets - str teksts, kas nav šifrēts (kuru gribat aizšifrēt).
	# Atgriež atslega, kuru ievada lietotājs.

	atslega = input("Ievadiet atslēgu ==> ")
	while len(atslega) > len(text_non_sifrets) or not atslega.isdigit():
		print("Kļūda! Ievadiet atslēgu kā ciparu virkni no 0 līdz 9, kas nav garāka par tekstu!")
		atslega = input("Ievadiet atslēgu ==> ")

	return atslega


def cypher_main():
	# Encryption.
	# Ieraksta failā ir_sifrets_txt = "C:\\Users\\User\\Desktop\\ir_sifrets_2.txt" aizšifrētu tekstu.
	# Ieraksta failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_2.txt" atslēgu, kuru ievādīs lietotājs, izmantojot input_atslega funkciju.

	text_non_sifrets = save_text_from_data_by_rows_to_variable(nav_sifrets_txt)  # Saglabam mainīgajā text_non_sifrets no nav_sifrets_txt datnes. Saglabam kā str virkni.
	text_non_sifrets = text_non_sifrets.upper()  # Visu str simbolus pārveidojam par lieliem burtiem.

	print("\nNav šifrēts teksts:")  # Informācija lietotājam par to, kads tagad teksts nav šifrēts (kuru mes aizšifrēsim pēc atslēgas).
	print(text_non_sifrets)  # Izvadam pagaidam nav aizšifrētu tekstu, ka simbolu virkni.
	print()  # Atstarpe glītumam.

	atslega = input_atslega(text_non_sifrets)  # Prasam lietotājam ievādīt atslegu.

	sifrets = encrypt(text_non_sifrets, atslega, burti)  # Aizšifrējam sifrets simbolu virkni.
	print()

	print(f"Teksts tika aizšifrēts ar atslēgu {atslega}:")
	print(sifrets)  # Izvadam aizšifrētu tekstu lietotājam.
	write_text_to_file(ir_sifrets_txt, sifrets)  # Ierakstam failā ir_sifrets_txt = "C:\\Users\\User\\Desktop\\ir_sifrets_1.txt" aizšifrētu tekstu.
	write_text_to_file(atslega_txt, atslega)  # Ierakstam failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_1.txt" atslegas kodu.


def decrypt_main():
	# Decryption.
	# Ieraksta failā nav_sifrets_txt = "C:\\Users\\User\\Desktop\\nav_sifrets_2.txt" atšifrētu tekstu.
	# Ieraksta failā atslega_txt = "C:\\Users\\User\\Desktop\\atslega_2.txt" atslēgu, kuru ievādīs lietotājs, izmantojot input_atslega funkciju.

	text_sifrets = save_text_from_data_by_rows_to_variable(ir_sifrets_txt)  # Saglabam mainīgajā text_sifrets no ir_sifrets_txt datnes. Saglabam kā str virkni.
	text_sifrets = text_sifrets.upper()  # Visu str simbolus pārveidojam par lieliem burtiem.

	print("\nŠifrēts teksts:")  # Informācija lietotājam par to, kā aizskatās šifrēts teksts (kuru mes atšifrēsim pēc atslēgas).
	print(text_sifrets)  # Izvadam pagaidam nav atšifrētu tekstu, ka simbolu virkni.
	print()  # Atstarpe glītumam.

	atslega = input_atslega(text_sifrets)  # Prasam lietotājam ievādīt atslegu.

	nav_sifrets = decrypt(text_sifrets, atslega, burti)  # Atšifrējam nav_sifrets simbolu virkni.
	print()

	print(f"Teksts tika atšifrēts ar atslēgu {atslega}:")
	print(nav_sifrets)  # Izvadam atšifrētu tekstu lietotājam.
	write_text_to_file(nav_sifrets_txt, nav_sifrets)  # Ierakstam failā nav_sifrets_txt = "C:\\Users\\User\\Desktop\\nav_sifrets_2.txt" atšifrētu tekstu.


def play_beep(duration):
	# Atskaņo pīksteņu ar ilgumu duration.
	# duration - pīksteņu ilgums milisekundes (int).

	frequency = 700  # Pīkstienu frekvence Hz
	winsound.Beep(frequency, duration)


def morse_play(message):
	# Atskaņo Morzes kodu ar pīksteņiem.
	# message - Morzes koda str virkne.

	for symbol in message:  # Iet cikla pa katru simbolu in message. Ja nav zināms simbols, tad atskaņo neko.
		if symbol == ".":
			play_beep(dot_duration)
		elif symbol == "-":
			play_beep(dash_duration)
		elif symbol == " ":
			play_beep(pause_between_letters_duration)
		elif symbol == "/":
			play_beep(pause_between_words_duration)


def print_text_from_data_by_rows(datne):
	# Uzrakstā termināla lietotājam visu tekstu no .txt failā pa rindam.
	# datne - datnes fails (piemēram, .txt fails)
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	with open(datne, mode="r", encoding="utf-8") as datne:
		for rinda in datne:
			print(rinda, end='')


def save_text_from_data_by_rows_to_variable(datne):
	# Atgriež visu nolasītu tekstu no .txt datnes kā vienu str mainīgu.
	# datne - datnes fails (piemēram, .txt fails).
	# Piemēram:
	# datne = "C:\\Users\\User\\Desktop\\teksts.txt"

	a = ""
	with open(datne, mode="r", encoding="utf-8") as datne:
		for rinda in datne:
			a = a + rinda
	return a


def write_text_to_file(filename, text):
	# NODZES VISU INFORMĀCIJU filename DATNE un ieraksta jaunu informāciju no str text mainīga.
	# text - str teksts, kuru gribam ierākstit datnē.
	# filename - faila (datnes) nosaukums.
	# Piemēram:
	# filename = "C:\\Users\\User\\Desktop\\nav_sifrets_1.txt"

	with open(filename, mode='w', encoding='utf-8') as file:
		file.write(text)


def encrypt_to_morse_code(non_encrypted_text, morse_code_dictionary):
	# Funkcija, kas pārvērš neaizšifrētu tekstu par Morzes kodu, izmantojot Morzes kodu vārdnīcu.
	# Atgriež aizšifrētu tekstu kā Morzes kodu (str).
	# Ieraksta .txt datnē aizsifrets_to_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\morzes_kods_save.txt" tekstu, kas tika aizšifrēts.
	# non_encrypted_text - str teksts, kuru gribam pārverst par Morzes kodu.
	# morse_code_dictionary - vārdnica ar parastu simbolu : atbilstošu Morzes kodu
	# Piemēram: {"A" : ".-", "B": "-..." , utt. }

	encrypted_text = ""  # Sākumā aizšifrētais teksts ir tukšs.

	for symbol in non_encrypted_text:  # Pārskatām katru simbolu nešifrētajā tekstā.
		sym = symbol.upper()  # Pārveidojam simbolu tā, lai viņš būtu liels burts.
		if sym in morse_code_dictionary:  # Ja simbols ir Morzes koda vārdnīcā.
			encrypted_text = encrypted_text + morse_code_dictionary[sym] + " "  # Pievienojam aizšifrētu ar Morzes kodu burtu encrypted_text simbolu virknei ar atstarpi.
		else:
			encrypted_text = encrypted_text + sym + " "  # Ja simbols nav Morzes kodā, tad vienkarši pievienojam to nešifrētu burtu kopā ar atstarpi.

	write_text_to_file(aizsifrets_to_morses_kods_save_txt, encrypted_text)  # Ieraksta .txt datnē aizsifrets_to_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\morzes_kods_save.txt" tekstu, kas tika atšifrēts.

	return encrypted_text  # Atgriežam aizšifrētu Morzes kodu.


def decrypt_from_morse_code(encrypted_text, morse_code_dictionary):
	# Funkcija, kas atšifrē Morzes kodu (pārverš par vienkaršu str tekstu), izmantojot Morzes kodu vārdnīcu.
	# Atgriež atšifrētu tekstu no Morzes kodu kā parastu tekstu (str).
	# Ieraksta .txt datnē atsifrets_no_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\atsifrets_no_morzes_koda_save.txt" tekstu, kas tika atšifrēts.
	# encrypted_text - str Morzes kods, kuru gribam pārverst par parastu tekstu.
	# morse_code_dictionary - vārdnica ar parastu simbolu : atbilstošu Morzes kodu
	# Piemēram: {"A" : ".-", "B": "-..." , utt. }

	decrypted_text = ""  # Sākumā atšifrētais teksts ir tukšs.
	morse_code = ""  # Sākumā Morzes kods ir tukšs.

	for symbol in encrypted_text:  # Pārskatām katru simbolu aizšifrētajā tekstā.
		if symbol != " ":  # Ja simbols nav atstarpe.
			morse_code = morse_code + symbol  # Pievienojam simbolu Morzes kodam.
		else:
			if morse_code in morse_code_dictionary.values():  # Ja Morzes kods ir atrodams Morzes koda vārdnīcā.
				for key, value in morse_code_dictionary.items():  # Pārskatām katru pāri (atslēga, vērtība) vārdnīcā.
					if value == morse_code:  # Ja vērtība atbilst Morzes kodam.
						decrypted_text = decrypted_text + key  # Pievienojam vārdnicas noteiktu "atslēgu" (key) (key - value vārdnīca) atšifrētajam tekstam.
						break  # Pārtraucam meklēšanu pēc "atslēgas" (key).
			else:
				decrypted_text = decrypted_text + morse_code  # Ja Morzes kods nav atrodams vārdnīcā, pievienojam to atšifrētajam tekstam.

			morse_code = ""  # Morzes kods atkal ir tukšs.

	# Pārbaudam, vai teksta non_encrypted_text beigās nav palicis Morzes kods.
	if morse_code != "":
		if morse_code in morse_code_dictionary.values():  # Ja Morzes kods ir atrodams vārdnīcā.
			for key, value in morse_code_dictionary.items():  # Pārskatām katru pāri (atslēga, vērtība) vārdnīcā.
				if value == morse_code:  # Ja vērtība atbilst Morzes kodam.
					decrypted_text = decrypted_text + key  # Pievienojam vārdnicas noteiktu "atslēgu" (key) (key - value vārdnīca) atšifrētajam tekstam.
					break  # Pārtraucam meklēšanu pēc "atslēgas" (key).
		else:
			decrypted_text = decrypted_text + morse_code  # Ja Morzes kods nav atrodams vārdnīcā, pievienojam to atšifrētajam tekstam.

	write_text_to_file(atsifrets_no_morses_kods_save_txt, decrypted_text)  # Ieraksta .txt datnē atsifrets_no_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\atsifrets_no_morzes_koda_save.txt" tekstu, kas tika atšifrēts.

	return decrypted_text  # Atgriežam atšifrēto tekstu


def input_cypher_to_morse_or_decrypt_from_morse():
	# Prasa lietotājam vai lietotājs grib aizšifrēt (encrypt) tekstu vai atšifrēt (decrypt) tekstu.
	# Ja lietotājs ievādīs "c" vai "C", tad viņš grib aizšifrēt (encrypt).
	# Ja lietotājs ievādīs "d" vai "D", tad viņš grib atšifrēt (decrypt).
	# Atgriež True, ja ir ievādīts "c" vai "C" (str).
	# Atgriež False, ja ir ievādīts "d" vai "D" (str).

	cypher_or_decrypt = ""
	while cypher_or_decrypt.lower() != "c" and cypher_or_decrypt.lower() != "d":
		cypher_or_decrypt = input("Ievadiet vai gribāt aizšifrēt tekstu ar Morzes kodu (c) vai atšifrēt (d) tekstu no Morzes koda ==> ")
		if cypher_or_decrypt.lower() == "c":
			return True
		elif cypher_or_decrypt.lower() == "d":
			return False

"""
import tkinter
import random


class Seat:
    # Sēdvietu klase.
    def __init__(self, theater, rinda, kolonna):
        # Sēdvietu iniciālizēšana.
        self.status = 0  # Pirmkārt iestāsim, ka visas sēdvietas ir brīvas.
        if random.randint(0, 1) == 1:  # Nejaušam sēdvietu izvietojumam. Nevienmēr būs 50%. Jo random ir katrai sēdvietai, vai nu 0 vai 1 un tāpēc nebūs precīzi 50% katru reizi. Atkarīgs no veiksmes (liekas, ka tas ir labāk, jo interesantāk).
            self.status = 1  # Ja tiek izlozēts 1 (50% varbūtība), tad vieta ir aizņemta.
            self.button = tkinter.Button(theater, bg="#A00000", text="╳", width=5, height=2)  # Izkrāsojam vietu ar sarkanu krāsu un liksim ╳ simbolu.
        else:  # Ja netika izlozēts 1 (tad izlozēts 0), tad vieta nebūs aizņemta.
            self.button = tkinter.Button(theater, bg="green", text="○", width=5, height=2, command=self.change_status)  # Izkrāsojam vietu ar zaļu krāsu un liksim ○ simbolu.
        self.button.grid(row=rinda, column=kolonna)  # Definēsim, kur likt pogu.

    def change_status(self):
        # Izmaina pogas stātusu no 0 -> 2, no 2 -> 0, no 1 -> 1.
        # 0 - brīva vieta.
        # 1 - aizņemta vieta.
        # 2 - izvēlēta vieta.

        if self.status == 0:  # 0 -> 2 (brīva vieta uz izvelētu vietu)
            self.status = 2
            self.button.config(bg="yellow")  # dzeltens reprezentē izvēlētu vietu.
        elif self.status == 2:  # 2 -> 0 (izvelēta uz brīvu, atcelt)
            self.status = 0
            self.button.config(bg="green", text="○")  # zaļš reprezentē brīvo vieta.
        elif self.status == 1:  # Aizņemts. To nevar izmainīt. 1 -> 1.
            pass

    def occupy(self):
        # Komanda sēdvietas aizņemšanai.

        self.status = 1  # Pogas (vietas) statuss ir 1 (aizņemts).
        self.button.configure(bg="#A00000", text="╳")  # Izmainām krāsu uz sarkanu un izmainām tekstu uz pogas uz "╳".


class Teatris:
    # Teātra klase.
    def __init__(self, theater, rindas, kolonnas):
        self.seats = []
        self.selected_seats = []  # Izvelētas sēdvietas saraksts.
        self.num_occupied_seats = 0  # Nepieciešams, lai sekot līdzi aizņemto sēdvietu skaitam.

        for i in range(rindas):  # Izmantojot pilno pārlasi pārbaudam, vai visas vietas nav aizņemtas (varbūt ka "paveicas" un uzreiz viss ir izpārdots).
            rinda = []
            for j in range(kolonnas):
                seat = Seat(theater, i, j)
                if seat.status == 1:
                    self.num_occupied_seats += 1  # Ja sēdvieta sākotnēji ir aizņemta, tad palieliniet skaitītāju.
                rinda.append(seat)
            self.seats.append(rinda)
        self.buy_button = tkinter.Button(theater, text="Nopirkt izvēlētās biļetes", command=self.buy_tickets)  # Nopirkšanas poga.
        self.buy_button.grid(row=rindas + 1, column=0, columnspan=kolonnas)
        self.all_seat_quantity = len(self.seats) * len(self.seats[0])  # Lai zinātu cik ir kopējais sēdvietu skaits.
        self.check_occupied()  # Izsaucam check_occupied, lai atjauninātu nopirkšanas pogas stāvokli (ja visas ir aizņemtas vietas, tad bloķēt pogu).

    def read_selection(self):
        # Atgriež sarakstu ar izvēlētam sēdvietam izmantojot pilnu pārlasi caur kātru vietu (rindu un kolonnu).
        selected_seats = []  # Tukšais saraksts ar izvēlētam sēdvietam.
        for row in self.seats:  # Iterējam caur katru rindu un kolonnu (pilnā pārlase)
            for seat in row:
                if seat.status == 2:  # Un izmantojot pilno pārlasi, ja sēdvietai ir piekārtots 2 (izvelēta), tad .append sēdvietu sarakstam selected_seats (izvēlētas sēdvietas)
                    selected_seats.append(seat)  # Pievienojam sarakstam atrasto izvēlēto vietu.
        return selected_seats  # Atgriezt izvēlētas sēdvietas.

    def buy_tickets(self):
        # Komanda pirkšanas pogai. Izsauc seat.occupy() visiem sēdvietam kas ie izvēlētas un palielina num_occupied_seats par katru izvēlēto vietu (tas ir nepieciešāms, lai jā visas vietās ir aizņemtas, tad bloķēt pogu).
        self.selected_seats = self.read_selection()  # Saraksts ar visam izvēlētam sēdvietam.
        for seat in self.selected_seats:  # Izmainām vērtības visam izvēlētam vietam (izmainām 2 -> 1) un palielinām self.num_occupied_seats par vienu.
            seat.occupy()  # Izmainīt sēdvietas stavokļi uz ieņemtu.
            self.num_occupied_seats += 1  # Palielinam aizņemto vietu skaitītāju par katru tikko aizņemto vietu.
        self.check_occupied()  # Izsaukt check_occupied, lai atjauninātu etiķetes un pogas stāvokli.

    def check_occupied(self):
        # Komanda pārbauda vai visas vietas jau ir izpārdotas. Ja ir, tad bloķē pirkšanas pogu.
        if self.num_occupied_seats == self.all_seat_quantity:  # Ja visas vietas ir aizņemtas, tad nobloķēt pirkšanas pogu. Salidzina aizņemto vietu skaititāju, ar visu sēdvietu skaitu. Ja sakrīt tad, bloķēt pogu.
            self.buy_button.config(text="Visas vietas izpārdotas!", state="disabled")  # Bloķēt pirkšanas pogu un izmainīt tekstu uz pogas.


class Define_Theater:
    # Klase teātra definēšanai.
    @staticmethod
    def izveidot_teatri():
        # Metode, kas nolasa ievādītas rindas un kolonnu vērtības no entry, nodzēs palīglogu teātra definēšanai, un izveido "zale" windows un izsauc klasi Teatris.
        rindas = int(rindas_entry.get())  # Nolasam vērtības no rindas entry.
        kolonnas = int(kolonnas_entry.get())  # Nolasam vērtības no kolonnas (sēdvietas) entry.

        logs.destroy()  # Nodzēsam logu, kur mēs prāsījam lietotājam ievādīt rindas un sēdvietu skaitu.

        zale = tkinter.Tk()  # Izveidojam jauno logu teātrim.
        zale.title("Zāle")  # Jauna loga virsraksts.
        Teatris(zale, rindas, kolonnas)  # Izsauc Teātra klasi ar lietotāja ievādītam rindam un kolonnam.
        zale.mainloop()  # Lai jauns logs būtu redzāms.


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Izveidojam logu, kur paprasām lietotājam ievādīt rindas un kolonnu (sēdvietu) skaitu teātrī. Tas ir nepieciešams teātra izveidošanai.
logs = tkinter.Tk()  # Faktiski tas ir papildlogs, lai lietotājs varētu ievādit rindas un kolonnu skaitu teātrī.
logs.title("Biļešu paradīze")  # Loga virsraksts.
logs.geometry("250x125")  # Loga izmērs.

rindas_label = tkinter.Label(logs, text="Rindu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda rindu skaitu.
rindas_label.pack()

rindas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam rindas ievadei.
rindas_entry.pack()

kolonas_label = tkinter.Label(logs, text="Sēdvietu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda sēdvietu (kolonnu) skaitu.
kolonas_label.pack()

kolonnas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam sēdvietu (kolonnas) ievadei.
kolonnas_entry.pack()

poga_izveidot = tkinter.Button(logs, text="Izveidot teātru", command=Define_Theater.izveidot_teatri)  # Poga "Izveidot teātru" papildlogam. Izsauc komandi "Define_Theater.izveidot_teatri"
poga_izveidot.pack()

logs.mainloop()  # Lai logs būtu redzāms.

"""


"""
import random


def choose_pair(students_prepare):
    # Atgriež pirmu masīva students_prepare lementu un nodzes to no saraksta students_prepare.
    # students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
    # students_prepare ir saraksts ar kortēžiem iekšā. [(studenta numurs, biļete), (studenta numurs, biļete), ... (studenta numurs, biļete)],

    first_pair = students_prepare[0]  # Paņem pirmo kortēžu ar studentu un biļeti.
    students_prepare.remove(first_pair)  # Nodzēs studentu no saraksta kuri gatavojas (jo viņš jau atbild),
    return first_pair


def choose_random_pair(students_prepare, students, exam_tickets):
    # Atgriež nejaušu (student, exam_ticket) kortēžu, no saraksta students (studenti, kas vel nav nokārtojusi eksāmenu un vēl nav eksāmena telpā).
    # Nejauši izvēlas studentu no tiem, kas vēl nav nokārtojusi eksāmenu un nesež telpā. Atgriež kortežu ar studentu un eksāmena biļeti. (student, exam_ticket),
    # students_prepare - saraksts (list) ar studentiem telpā (kuri gatavojas eksāmenam un sež ar biļētem).
    # students - kopa ar visiem studenti kuri nav eksāmena telpā un pagaidam nav nokārtojusi eksāmenu.
    # exam_tickets - kopa ar visam biļetem no A līdz Z.

    if len(students) == 0:
        return None
    student = students.pop()
    exam_ticket = exam_tickets.pop()
    return (student, exam_ticket)


def print_pairs(pairs):
    # Glīti izvāda sarakstu pairs, kas reprēzentē studentus ar biļētem kuri sēž telpā un gatavojas eksāmenam.
    # Piemērs:
    # Ievade tāds saraksts: [(36, S), (50, T), (37, D), (42, R), (19, W), (22, U), (41, M), (44, Q), (52, P), (38, H)].
    # Funkcija atgriež tādu simbolu virkni: 36-S, 50-T, 37-D, 42-R, 19-W, 22-U, 41-M, 44-Q, 52-P, 38-H
    # pairs - saraksts ar kortežiem ar divam vērtībam [(students, biļete), (students, biļete), ... , (students, biļete)].

    for i in range(len(pairs)):
        if i == len(pairs) - 1:
            print(str(pairs[i][0]) + "-" + str(pairs[i][1]))
        else:
            print(str(pairs[i][0]) + "-" + str(pairs[i][1]) + ", ", end="")


def convert_int_to_str_in_set_in_range(n, m, kopa):
    # Metode (neko neatgriež), kura izmaina visas int vērtības kopā uz str.
    # Piemēram:
    # {5, 33, 14, 13, 11} -> {'5', '33', '14', '13', '11'}.
    # convert_int_to_str_in_set_in_range(1, 55, students).
    # kopa - set, kopa, kurai gribāt visas int vērtības izmainīt uz str. Piemēram: 1 -> "1"
    # n - int, no cik (parasti no 1).
    # m - int, līdz cik līdz m-1 (šeit līdz 55, bet funkcijai izmainīs int uz str līdz 54).

    for i in range(n, m):
        kopa.add(str(i))


def exam_tickets_words_in_range(n, m, exam_tickets):
    # Metode (neko neatgriež), kura piepildina tukšo kopu exam_tickets ar simboliem no ASCII koda no n līdz m str veidā.
    # exam_tickets - tukša kopa, kurai jābut kopai ar eksāmena biļētiem no A līdz Z.
    # n - int, no cik (ASCII kods simbols).
    # m - int, līdz cik (ASCII kods).
    # (65, 91) - lielajiem latiņu burtiem.
    # Piemērs: exam_tickets_words_in_range(65, 91, exam_tickets).

    for i in range(n, m):
        exam_tickets.add(chr(i))


def start_students_number(n, students, exam_tickets):
    # Atgriež students_prepare sarakstu, kura sastav no kortēžiem [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
    # un šeit ir n šādu kortežu (student, exam_ticket).
    # n - int, cik "start" studentus paņemt? (10 šajā gadījumā). Tas ir cik studentus "izlozēsim" kartot eksāmenu pirmājiem.
    # students - set, kopa ar visiem studentiem, kuri nav ienākuši eksāmenas telpā un vēl nav nokārtojusi eksāmenu. No viņiem paņemsim pirmus 10 studentu.
    # exam_tickets - set, kopa ar visiem eksāmena biļētem, kuri nav pie studentiem.

    for i in range(n):
        student = students.pop()
        exam_ticket = exam_tickets.pop()
        students_prepare.append((student, exam_ticket))
    return students_prepare


def exam_simulation(students_prepare):
    # Simulē eksāmena norisināšanas.
    # students_prepare - saraksts veidā [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)].
    # Kad 1. students atbildējis, viņa biļete tiek atlikta atpakaļ eksāmena biļešu "kaudzē" un nāk nākamais students un izvēlās uz labu laimi vienu eksāmena biļeti no eksāmena biļešu "kaudzes".
    # Tā process tiek atkārtots, kamēr visi studenti ir noeksaminēti.
    # Paziņo uz ekrāna, kādā secība studenti tika eksaminēti un kādu eksāmena biļeti katrs students saņēma.

    exam = True  # Karogs ir True, kamēr students_prepare != 0 (kāmer eksamenācijas telpā ir palikuši cilvēki, tad eksāmens turpinās).
    while exam:  # Kamēr eksāmens ir True
        if len(students_prepare) == 0:  # Ja nav nevienu cilvēku eksamenācijas telpā, tad eksāmens beidzās.
            print("Eksāmens beidzās!")
            exam = False  # eksāmens beidzās.
        else:
            pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
            print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam informāciju, kurš students atbild (kreisāis) un ar kādu biļeti viņš ir.
            exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
            print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.

            if len(students) == 0:  # Ja visi studenti jau ir ienākuši eksāmenā telpā, tad jau mēs vairs nevienu neaicināsim atkāl uz eksāmenu. (jo tie ir pēdējie studenti, kuri karto eksāmenu).
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.
                pair = choose_pair(students_prepare)  # Izvēlas pirmo pāriti (kreiso parīti) (students, biļete) no studentiem, kuri gatavojas eksāmenam un sež telpā ar biļetem.
                print("Atbild " + str(pair[0]) + ". students ar biļeti " + str(pair[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atbild un ar kādu biļeti.
                exam_tickets.add(pair[1])  # Pievienojam biļeti no korteža eksāmena biļetes kaudzītei (studenta biļeti, kurš ir atbildējis uz jautājumu).
                print("Biļete", pair[1], "tiek atlikta biļešu \"kaudzē\".\n")  # Izvadam informāciju, kura biļete tika atlikta kaudzē.
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.

            else:
                atnac = choose_random_pair(students_prepare, students, exam_tickets)  # Ja nav visi studenti ir ienākuši eksāmenā telpā, tad vajag aicināt nākamos (atnac) studentus uz eksāmenu (jo tie ir palikuši un vēl nenokārtoja eksāmenu). Nejauši izvelāmies studentu un viņam biļēti, no tiem, kuri vēl nav nokārtojuši.
                print("Atnāc " + str(atnac[0]) + ". students un izvilka biļeti " + str(atnac[1]) + ".")  # Izvadam lietotājam informāciju, kurš students atnāca un kādu biļeti paņēma.
                students_prepare.append(atnac)  # Pievienojam sarakstam ar kortēžiem students_prepare [(student, exam_ticket), (student, exam_ticket), ... , (student, exam_ticket)] jauno kortēžu, ar studentu kurš atnāca un izvēlējas biļeti.
                print_pairs(students_prepare)  # Glīti izvadīt informāciju lietotājam par to, kuri cilvēki sēž un gatavojas eksāmenam iekšā telpā.


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


students = set()  # Tukša kopa ar visiem studentiem, tā tiek piepildīta ar str numuriem vēlāk šeit "convert_int_to_str_in_set_in_range(1, 55, students)".
exam_tickets = set()  # Tukša kopa ar visiem eksāmena biļētem (kaudzē ar biļetem). Tā tiek piepildīta ar str burtiem no A līdz Z šeit "exam_tickets_words_in_range(65, 91, exam_tickets)".
students_prepare = []  # Tukšais saraksts, kur glābāsies visi kortēži [(studentu, biļeti), (studentu, biļeti), ... (studentu, biļeti)]. Tas tiek piepildīts ar start_students_number.

convert_int_to_str_in_set_in_range(1, 55, students)  # Lai visi skaitļi kopā, būtu uztvērti ka simbolu virknes (str). Citādi pop funkcijas nestrādās pareizi.
exam_tickets_words_in_range(65, 91, exam_tickets)  # Izveido biļetes numurus no A līdz Z. Tā tiek piepildīta ar str burtiem no A līdz Z.

# print("Studentu kopa:", students) # TESTĒŠANAI.
# print("Eksāmena biļešu kopa:", exam_tickets) # TESTĒŠANAI.

start_students_number(10, students, exam_tickets)  # Izveido sakotnēju studentu sarakstu ar [(studentu, biļeti), (studentu, biļeti), ... (studentu, biļeti)].
print("Eksāmena simulācija.\nFormāts: ([Studenta numurs]-[Izvilkta biļete])\n")  # Paskaidrojums lietotājam.
print("Pirmie desmit studenti ar izvilktam biļētem:")  # Informācija lietotājam.

print_pairs(students_prepare)  # Glīti izvada pirmus 10 studentus.
exam_simulation(students_prepare)  # Sākt eksāmenu.

"""
"""
import numpy
import random


def is_natural_and_less_than_10(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav.
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.

    if str(n).isdigit() and float(n) == int(n) and int(n) > 0 and int(n) < 11:
        return True
    else:
        return False


def ievadiet_n_skaitlus_seta(n, max_num):
    # Procedura kura ļauj ievādit n skaitļus un ieliekt tos kop (set'ā)
    # Atgriež jau aizpildīto kopu (set'u) a ar lietotāja ievādītajiem naturāliem skaitliem robēžas no 1 līdz max_num ieskaitot.
    # n - cik skaitļus ievādīt lietotājam (int)
    # max_num - maksimālais skaitlis līdz kuram tiek veikta loterija (int)

    a = set()
    for i in range(1, n + 1):
        while True:
            b = input("Ievadiet " + str(i) + ". skaitli ==> ")
            try:
                b = int(b)
                if b < 1 or b > max_num:
                    print("Skaitlim jābūt veselam skaitlim no 1 līdz " + str(max_num) + ".")
                elif b in a:
                    print("Šis skaitlis jau eksistē, lūdzu ievadiet citu skaitli!")
                else:
                    a.add(b)
                    break
            except ValueError:
                print("Ievadei jābūt skaitlim!")
                continue

    return a


def speles_likmes():
    # Paprasam izvēlēties spēlēs likmi no piedāvātiem.
    # Pārbauda to, vai tāda eksistē un atgriež to, kā float.

    while True:
        n = input("Izvēlēties, Jūsu spēles likmi € ==> ")
        try:
            float(n)
        except:
            print("Kļūda! Ievādiet reālo likmi no piedāvatiem!")
        else:
            n = float(n)
            if n == 0.2:
                likme = 0.2
                return likme

            elif n == 0.3:
                likme = 0.3
                return likme

            elif n == 0.5:
                likme = 0.5
                return likme

            elif n == 1:
                likme = 1
                return likme

            elif n == 2:
                likme = 2
                return likme

            elif n == 3:
                likme = 3
                return likme

            elif n == 5:
                likme = 5
                return likme

            elif n == 10:
                likme = 10
                return likme

            else:
                print("Kļūda! Ievādiet likmi no piedāvatiem!")


def laimestu_matrica(izveleto_skaits, atmineto_skaits):
    # Atgriež reizinātāju pamatojoties uz laimestu sadalījuma matricas.
    # Reizinātajs ir atkarīgs no tā, cik skaitļus jus izvēlējaties un cik jus atminējat.
    # Reizinātāji ir pārādīta šājā matricā.

    laimesti = numpy.array([[0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                            [1.5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 4.5, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 8, 1, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 20, 2, 2, 1, 0, 0, 0],
                            [0, 0, 0, 0, 45, 12, 3, 3, 1, 1],
                            [0, 0, 0, 0, 0, 175, 30, 5, 2, 2],
                            [0, 0, 0, 0, 0, 0, 700, 100, 40, 5],
                            [0, 0, 0, 0, 0, 0, 0, 3000, 350, 55],
                            [0, 0, 0, 0, 0, 0, 0, 0, 10000, 550],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 60000]])

    reizinatajs = laimesti[atmineto_skaits, izveleto_skaits - 1]  # Izvēlāmies nepieciešāmo rūtiņu un tas arī būs reizinātajs.

    return reizinatajs


def naudas_balva(likme, reizinatajs):
    # Atgriež naudas balvu likmi reizinot ar reizinātaju.
    # likme - likme (float reāls skaitlis lielāks par 0, piemēram,
    # 0.20
    # 0.30
    # 0.50
    # 1.00
    # 2.00
    # 3.00
    # 5.00
    # 10.00)
    # reizinātajs - float reāls skaitlis lielāks vai vienāds par 0

    return likme * reizinatajs


def random_set_numbers_skaita_n_from_1_to_m(n, m):
    # Atgriež kopu ar n nejaušiem skaitļiem, kuri neatkartojas no 1 līdz m. [1, m].
    # n - cik nejaušus skaitļus vajag loterijai
    # m - kāda ir augšēja robeža skaitlim, kuru vajadzīgi uzminēt (vislielākais iespējamais skaitlis loterija)

    a = set()
    while len(a) < n:
        b = random.randint(1, m)
        if b not in a:
            a.add(b)

    return a


def cik_atminejat(a, b):
    # Atgriež cik skaitļus Jūs laimējat (atrod kopas šķēlumu)
    # a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
    # b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

    x = a.intersection(b)
    len1 = len(x)

    return len1


def print_set(a):
    # Izvada (print) uz ekrāna kopu. Bet tas to neatgriež.
    # Jāizsauc vienkarši print_set(a)
    # a - kopa (set)

    elements = sort_ievietosana_augosa(list(a))
    # Iterējam cauri elementu indeksiem un izdrukājiem tos, atdalot tos ar komatiem
    for i in range(len(elements)):
        if i == len(elements) - 1:
            # Ja elements ir pēdējais, izdrukām to bez komata
            print(elements[i])
        else:
            # Ja elements nav pēdējais, izdrukājam to ar komatu. end="", lai nebūtu pārejas uz jauno rindu kā \n
            print(str(elements[i]) + ", ", end="")


def sort_ievietosana_augosa(a):
    # Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
    # a - viendimensijas masīvs

    n = len(a)
    for i in range(1, n):
        if a[i - 1] > a[i]:
            x = a[i]
            j = i
            while a[j - 1] > x:
                a[j] = a[j - 1]
                j = j - 1
                if j == 0:
                    break
            a[j] = x
    return a


def izlozu_skaits():
    # Paprasam izvēlēties izložu skaitu no piedāvātiem.
    # Pārbauda to, vai tāda eksistē un atgriež to, kā float.

    while True:
        n = input("Izvēlēties, izložu skaitu ==> ")
        try:
            int(n)
        except:
            print("Kļūda! Ievādiet reālo izložu skaitu no piedāvatiem!")
        else:
            n = int(n)
            if n == 1:
                izlozu_skaits = 1
                return izlozu_skaits

            elif n == 2:
                izlozu_skaits = 2
                return izlozu_skaits

            elif n == 3:
                izlozu_skaits = 3
                return izlozu_skaits

            elif n == 4:
                izlozu_skaits = 4
                return izlozu_skaits

            elif n == 6:
                izlozu_skaits = 6
                return izlozu_skaits

            elif n == 12:
                izlozu_skaits = 12
                return izlozu_skaits

            elif n == 21:
                izlozu_skaits = 21
                return izlozu_skaits

            else:
                print("Kļūda! Ievādiet izložu skaitu no piedāvatiem!")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Izvēlēties, cik skaitļus nosvītrot (no 1 līdz 10) ==> ")
while not is_natural_and_less_than_10(n):
    n = input("Kļūda! Izvēlēties, cik skaitļus nosvītrot (no 1 līdz 10) ==> ")
print("Ievādiet Jūsu skaitļus. Skaitlim jābūt veselam skaitlim no 1 līdz 62.")
n = int(n)

rezultats = random_set_numbers_skaita_n_from_1_to_m(20, 62)
# print("TESTĒŠANAI:")  # TESTĒŠANAI
# print_set(rezultats)  # TESTĒŠANAI

players_numbers = ievadiet_n_skaitlus_seta(n, 62)

print("\nSpēles likmes:\n0.20 €\n0.30 €\n0.50 €\n1.00 €\n2.00 €\n3.00 €\n5.00 €\n10.00 €\n")
likme = speles_likmes()

print("\nIzložu skaits:\n1\n2\n3\n4\n6\n12\n21\n")
piedalisanas_reizes = izlozu_skaits()

print("\nJūsu skaitļi:")
print_set(players_numbers)

total_laimests = 0

for i in range(piedalisanas_reizes):

    rezultats = random_set_numbers_skaita_n_from_1_to_m(20, 62)  # Noņemt testēšanai
    print("\nIzlozētie skaitļi:")
    print_set(rezultats)

    atmineto_skaits = cik_atminejat(players_numbers, rezultats)

    if atmineto_skaits == 1:  # Pareizam locijumam
        word = " skaitļi."
    else:
        word = " skaitļus."

    print("\nJūs atminējat " + str(atmineto_skaits) + word)
    reizinatajs = laimestu_matrica(n, atmineto_skaits)
    print("Reizinātājs:", reizinatajs)

    laimests = naudas_balva(likme, reizinatajs)
    print("Jūsu laimests:", laimests, "€")
    total_laimests += laimests

    if piedalisanas_reizes == 1:
        pass
    elif i + 1 == piedalisanas_reizes:
        if piedalisanas_reizes == 21:  # Pareizam locijumam
            word = "izlozi"
        else:
            word = "izlozem"
        print("\nJūsu kopējais laimests par", piedalisanas_reizes, word, "ir:", total_laimests, "€")
"""


"""

import tkinter
import numpy
import random

# global mainīgo saraksts:
# root, a, label2, buy_button


def result():
    # Komanda tiek izsaukta pēc "submit_button" nospiešanas ( = ).
    # Paņemt n un m no lietotāja un izveido matricu, kur aptuvēni 50% no matricas ir 1.
    # Izveido globālu mainīgu a un tas ir tās matrica.
    # Izsauc komandu show_array()

    global a
    n = input_rindas_skaits.get()
    m = input_kolonnas_skaits.get()
    n = int(n)
    m = int(m)
    arr = numpy.ones((n, m))
    num_ones = int(n * m * 0.5)
    ones_count = 0

    for i in range(n):
        for j in range(m):
            if ones_count < num_ones and random.random() < 0.5:
                arr[i][j] = 0
                ones_count = ones_count + 1
    a = arr
    show_array(a)


def toggle_button(poga):
    # Pogas sēdvietas izvelēšanai
    # 1 -> 1 "Vieta aizņemta!"
    # 0 -> X "Biļete izvelēta!"
    # X -> 0 "Biļete atcelta!"
    # check_button_text() pārbauda vai uz visām pogām ir uzrakstīts "1". (pilnā pārlase).
    # Ja uz visiem, tad blokēt pogas un uzrakstīt kā visas biļetes ir izpārdotas.

    if poga["text"] == "0":
        poga["text"] = "X"
        label2.config(text="Biļete izvelēta!")
        check_button_text()

    elif poga["text"] == "1":
        poga["text"] = "1"
        label2.config(text="Vieta aizņemta!")
        check_button_text()

    elif poga["text"] == "X":
        poga["text"] = "0"
        label2.config(text="Biļete atcelta!")
        check_button_text()


def change_button_text():
    # Pārlasa visas pogas root'ā un izmainā "X" uz "1" (izvelētus uz aizņemts)
    # Izmainām label2 tekstu uz "Nopirkts!"
    # Tiek izmantots globals mainīgais root

    global root

    for poga in root.grid_slaves():  # Parlasam visas pogas
        if type(poga) == tkinter.Button:
            if poga.cget("text") == "X":  # cget dot iespēju pārbaudit vai teksts uz pogas ir "X"
                poga.configure(text="1")

    label2.config(text="Nopirkts!")

    check_button_text()


def check_button_text():
    # Izmantojot divus karogus, pārbaudam vai uz visiem pogam ir uzrakstīts "1". (Pogas pilnā pārlase)
    # Ja uz visām ir "1", tad visas pogas bloķēt un uzrakstīt "Visas biļetes ir izpārdotas!"

    all_ones = True
    has_two = False  # two == X (jo pirmkārts tika izmantots 0 - brīvs, 1 - aizņemts, 2 - izvelēts)

    for poga in root.grid_slaves():  # Pilnā pārlase pogiem un label'iem kuri ir grid'ā izmantojot in root.grid_slaves() (atrādu internētā tādu funkciju)
        if poga.cget("text") == "1 - aizņemta vieta\n0 - brīva vieta\nX - izvelētas vietas pirkšanai\nIzvēlieties vietas pirkšanai!":
            continue
        if poga.cget("text") == "Nopirkt izvelētas biļetes":
            continue
        if poga.cget("text") == "Nopirkts!":
            continue
        if poga.cget("text") == "Biļete izvelēta!":
            continue
        if poga.cget("text") == "X":
            has_two = True
        if poga.cget("text") != "1":
            all_ones = False

    if all_ones:
        label3 = tkinter.Label(root, text="Visas biļetes ir izpārdotas!", font=("Arial", 12), anchor="ne")
        label3.place(relx=1.0, rely=0.0, anchor="ne")
        buy_button.config(state="disabled")

        for poga in root.grid_slaves():  # grid_slave() palīdz visas pogas bloķēt
            poga.config(state="disabled")

    elif not has_two:
        buy_button.config(state="disabled")

    else:
        buy_button.config(state="normal")


def button_callback(poga):
    # Definē callback() funkciju kas izsauc toggle_button(poga). Jā tieši tā neuzrakstīt, tad programma nestrādās
    def callback():
        toggle_button(poga)
    return callback


def show_array(a):
    # Izveido jaunu logu "root", un izveido tajā pogas (sēdvietas) nepieciešamā skaitā, ar komandu button_callback
    # Parada jaunu logu "root".
    # Tiek izveidota poga "Nopirkt izvelētas biļetes", pēc tas nospiešanas tiek izsaukta komanda change_button_text
    # Pogas ir dizaktivētas (disabled) pēc noklusējumā.
    # label2 ir izveidots tukšs un globāls, lai pēc tam to mainītu uz "Nopirkts!" vai uz "".
    # label4 ir izveidots informatīvam nolūkam
    # tiek izveidoti trīs globāli mainīgie
    global root, label2, buy_button

    root = tkinter.Tk()
    root.title("Teātris")

    rindas = len(a)
    kolonnas = len(a[0])
    pogas = []
    for i in range(rindas):
        for j in range(kolonnas):
            poga = tkinter.Button(root, text=str(int(a[i][j])), width=2, height=1)
            poga.config(command=button_callback(poga))
            poga.grid(row=i, column=j)
            pogas.append(poga)

    label2 = tkinter.Label(root, text="")
    label2.grid(row=i + 1, column=j + 1)

    label4 = tkinter.Label(root, text="1 - aizņemta vieta\n0 - brīva vieta\nX - izvelētas vietas pirkšanai\nIzvēlieties vietas pirkšanai!")
    label4.grid(row=i + 3, column=j + 3, sticky="s")

    buy_button = tkinter.Button(root, text="Nopirkt izvelētas biļetes", width=20, bd=1, command=change_button_text, state="disabled")
    buy_button.grid(row=i + 2, column=j + 2)

    check_button_text()

    root.mainloop()


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()  # Tkinter (lai izmantotu to komandas)
logs.geometry("170x130")  # Loga izmēra definēšana
logs.title("Biļešu nopirkšana")  # Windows "loga" nosaukums


# Labels teātrim
label_teatris = tkinter.Label(logs, text="Teātris", font=("Arial", 12))
label_teatris.place(x=20, y=6)

label_teatra_izmers = tkinter.Label(logs, text="Teātra izmērs:", font=("Arial", 12))
label_teatra_izmers.place(x=20, y=30)

label_x = tkinter.Label(logs, text="x", font=("Arial", 15))
label_x.place(x=56, y=58)


# Entry logi
input_rindas_skaits = tkinter.Entry(logs, width=3)
input_rindas_skaits.place(x=30, y=65)

input_kolonnas_skaits = tkinter.Entry(logs, width=3)
input_kolonnas_skaits.place(x=75, y=65)

# -----------------------------------------

submit_button = tkinter.Button(logs, text="=", width=20, bd=1, command=result)  # Izmantojam definētas komandas, lai pēc pogas nospiešanas tā komanda tiek izpildīta
submit_button.place(x=110, y=62, width=25)  # Parādam, kur poga tiks attēlota

logs.mainloop()  # lai logs būtu redzāms visu laiku

"""

"""
# performing ramanujan's infinite series to 
#generate a numerical approximation of 1/pi:
#1/pi = (2*sqrt(2))/9801) * (4*k)!*(1103+26390k)/(((k!)**4)*396**(4k))

def factorial_1(k):
    if k==0:
        return 1
    else:
        result = k* factorial_1(k-1)
        return result

def estimate_pi():
    k=int(input("enter the value of k = "))
    total=0
    while True:
        n=(2*math.sqrt(2)/9801)
        m=factorial_1(4*k)*(1103+26390*k)
        o=((factorial_1(k))**4)*(396**(4*k))
        result=n*(m/o)
        total+=result #assigning result to a new variable to keep track of changes
        epsilon=1e-15
        if abs(result)<epsilon:
            break
        k+=1 #updating value of k, to improve result & total for each loop.
    return 1/total # Return's pi=3.14 only if k=0
print(estimate_pi())
"""

'''
# Neoptimizēts kods.
# Pirmā idēja.
txt = ""
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_e = 0
count_f = 0
count_g = 0
count_h = 0
count_i = 0
count_j = 0
count_k = 0
count_l = 0
count_m = 0
count_n = 0
count_o = 0
count_p = 0
count_q = 0
count_r = 0
count_s = 0
count_t = 0
count_u = 0
count_v = 0
count_w = 0
count_x = 0
count_y = 0
count_z = 0
for i in range(len(txt)):
    if i == "A" or i == "a":
        count_a += 1
    elif i == "B" or i == "b":
        count_b += 1
    elif i == "C" or i == "c":
        count_c += 1
    elif i == "D" or i == "d":
        count_d += 1
    elif i == "E" or i == "e":
        count_e += 1
    elif i == "F" or i == "f":
        count_f += 1
    elif i == "G" or i == "g":
        count_g += 1
    elif i == "H" or i == "h":
        count_h += 1
    elif i == "I" or i == "i":
        count_i += 1
    elif i == "J" or i == "j":
        count_j += 1
    elif i == "K" or i == "k":
        count_k += 1
    elif i == "L" or i == "l":
        count_l += 1
    elif i == "M" or i == "m":
        count_m += 1
    elif i == "N" or i == "n":
        count_n += 1
    elif i == "O" or i == "o":
        count_o += 1
    elif i == "P" or i == "p":
        count_p += 1
    elif i == "Q" or i == "q":
        count_q += 1
    elif i == "R" or i == "r":
        count_r += 1
    elif i == "S" or i == "s":
        count_s += 1
    elif i == "T" or i == "t":
        count_t += 1
    elif i == "U" or i == "u":
        count_u += 1
    elif i == "V" or i == "v":
        count_v += 1
    elif i == "W" or i == "w":
        count_w += 1
    elif i == "X" or i == "x":
        count_x += 1
    elif i == "Y" or i == "y":
        count_y += 1
    elif i == "Z" or i == "z":
        count_z += 1
'''



"""
ATSLEGA CEZARA SIFRS

text = input('TEXT => ')
burti = [' ', 'ā', 'ž', 'š', 'ē', 'ģ', 'ņ', 'ū', 'ī', 'ķ', 'ļ', 'Ā', 'Ž', 'Š', 'Ē', 'Ģ', 'Ņ', 'Ū', 'Ī', 'Ķ', 'Ļ']
for j in range(26):
    burti.append(chr(j + 65))
    burti.append(chr(97 + j))
atsl1 = input('Atslega => ')
n = len(atsl1)
atslegas = list(atsl1)


skt = 0
ska = 0
sv = ''
for s in text:
    ska = (ska + 1) % n
    if s in burti:
        y = burti.index(s)
        y = (y + int(atslegas[ska])) % len(burti)
        s = burti[y]
    sv += s
print(sv)

ska = 0
txt = ''
for s in sv:
    ska = (ska + 1) % n
    if s in burti:
        y = burti.index(s)
        y = (y - int(atslegas[ska])) % len(burti)
        s = burti[y]
    txt += s

print(txt)

"""

"""
"""
"""
Teātris tika papildināts ar to, ka tagad var izvēlēties teātra izmērus sakum izveidotāja papildus logā, 
kurš tiek dzēsts, kad lietotājs izveido teātri. Programma ir papildināta ar pārbaudi vai visas vietas ir aizņemtas. 
Ja visas ir aizņemtas, tad nopirkšanas poga tiek bloķēta teksts uz pogas tiek izmainīts uz “Visas vietas izpārdotas!”. 
Grafiski tiek veiktas šādas izmaiņas: uz pogām ir X (aizņemts) vai O (brīvs vai izvēlēts), 
krāsas tika izmainītas uz sarkanu – aizņemtu , zaļu – brīvu, dzeltenais palika par izvēlēto.
"""
"""

import tkinter
import random


class Seat:
    # Sēdvietu klase.
    def __init__(self, theater, rinda, kolonna):
        # Sēdvietu iniciālizēšana.
        self.status = 0  # Pirmkārt iestāsim, ka visas sēdvietas ir brīvas.
        if random.randint(0, 1) == 1:  # Nejaušam sēdvietu izvietojumam. Nevienmēr būs 50%. Jo random ir katrai sēdvietai, vai nu 0 vai 1 un tāpēc nebūs precīzi 50% katru reizi. Atkarīgs no veiksmes (liekas, ka tas ir labāk, jo interesantāk).
            self.status = 1  # Ja tiek izlozēts 1 (50% varbūtība), tad vieta ir aizņemta.
            self.button = tkinter.Button(theater, bg="#A00000", text="╳", width=5, height=2)  # Izkrāsojam vietu ar sarkanu krāsu un liksim ╳ simbolu.
        else:  # Ja netika izlozēts 1 (tad izlozēts 0), tad vieta nebūs aizņemta.
            self.button = tkinter.Button(theater, bg="green", text="○", width=5, height=2, command=self.change_status)  # Izkrāsojam vietu ar zaļu krāsu un liksim ○ simbolu.
        self.button.grid(row=rinda, column=kolonna)  # Definēsim, kur likt pogu.

    def change_status(self):
        # Izmaina pogas stātusu no 0 -> 2, no 2 -> 0, no 1 -> 1.
        # 0 - brīva vieta.
        # 1 - aizņemta vieta.
        # 2 - izvēlēta vieta.

        if self.status == 0:  # 0 -> 2 (brīva vieta uz izvelētu vietu)
            self.status = 2
            self.button.config(bg="yellow")  # dzeltens reprezentē izvēlētu vietu.
        elif self.status == 2:  # 2 -> 0 (izvelēta uz brīvu, atcelt)
            self.status = 0
            self.button.config(bg="green", text="○")  # zaļš reprezentē brīvo vieta.
        elif self.status == 1:  # Aizņemts. To nevar izmainīt. 1 -> 1.
            pass

    def occupy(self):
        # Komanda sēdvietas aizņemšanai.

        self.status = 1  # Pogas (vietas) statuss ir 1 (aizņemts).
        self.button.configure(bg="#A00000", text="╳")  # Izmainām krāsu uz sarkanu un izmainām tekstu uz pogas uz "╳".


class Teatris:
    # Teātra klase.
    def __init__(self, theater, rindas, kolonnas):
        self.seats = []
        self.selected_seats = []  # Izvelētas sēdvietas saraksts.
        self.num_occupied_seats = 0  # Nepieciešams, lai sekot līdzi aizņemto sēdvietu skaitam.

        for i in range(rindas):  # Izmantojot pilno pārlasi pārbaudam, vai visas vietas nav aizņemtas (varbūt ka "paveicas" un uzreiz viss ir izpārdots).
            rinda = []
            for j in range(kolonnas):
                seat = Seat(theater, i, j)
                if seat.status == 1:
                    self.num_occupied_seats += 1  # Ja sēdvieta sākotnēji ir aizņemta, tad palieliniet skaitītāju.
                rinda.append(seat)
            self.seats.append(rinda)
        self.buy_button = tkinter.Button(theater, text="Nopirkt izvēlētās biļetes", command=self.buy_tickets)  # Nopirkšanas poga.
        self.buy_button.grid(row=rindas + 1, column=0, columnspan=kolonnas)
        self.all_seat_quantity = len(self.seats) * len(self.seats[0])  # Lai zinātu cik ir kopējais sēdvietu skaits.
        self.check_occupied()  # Izsaucam check_occupied, lai atjauninātu nopirkšanas pogas stāvokli (ja visas ir aizņemtas vietas, tad bloķēt pogu).

    def read_selection(self):
        # Atgriež sarakstu ar izvēlētam sēdvietam izmantojot pilnu pārlasi caur kātru vietu (rindu un kolonnu).
        selected_seats = []  # Tukšais saraksts ar izvēlētam sēdvietam.
        for row in self.seats:  # Iterējam caur katru rindu un kolonnu (pilnā pārlase)
            for seat in row:
                if seat.status == 2:  # Un izmantojot pilno pārlasi, ja sēdvietai ir piekārtots 2 (izvelēta), tad .append sēdvietu sarakstam selected_seats (izvēlētas sēdvietas)
                    selected_seats.append(seat)  # Pievienojam sarakstam atrasto izvēlēto vietu.
        return selected_seats  # Atgriezt izvēlētas sēdvietas.

    def buy_tickets(self):
        # Komanda pirkšanas pogai. Izsauc seat.occupy() visiem sēdvietam kas ie izvēlētas un palielina num_occupied_seats par katru izvēlēto vietu (tas ir nepieciešāms, lai jā visas vietās ir aizņemtas, tad bloķēt pogu).
        self.selected_seats = self.read_selection()  # Saraksts ar visam izvēlētam sēdvietam.
        for seat in self.selected_seats:  # Izmainām vērtības visam izvēlētam vietam (izmainām 2 -> 1) un palielinām self.num_occupied_seats par vienu.
            seat.occupy()  # Izmainīt sēdvietas stavokļi uz ieņemtu.
            self.num_occupied_seats += 1  # Palielinam aizņemto vietu skaitītāju par katru tikko aizņemto vietu.
        self.check_occupied()  # Izsaukt check_occupied, lai atjauninātu etiķetes un pogas stāvokli.

    def check_occupied(self):
        # Komanda pārbauda vai visas vietas jau ir izpārdotas. Ja ir, tad bloķē pirkšanas pogu.
        if self.num_occupied_seats == self.all_seat_quantity:  # Ja visas vietas ir aizņemtas, tad nobloķēt pirkšanas pogu. Salidzina aizņemto vietu skaititāju, ar visu sēdvietu skaitu. Ja sakrīt tad, bloķēt pogu.
            self.buy_button.config(text="Visas vietas izpārdotas!", state="disabled")  # Bloķēt pirkšanas pogu un izmainīt tekstu uz pogas.


class Define_Theater:
    # Klase teātra definēšanai.
    @staticmethod
    def izveidot_teatri():
        # Metode, kas nolasa ievādītas rindas un kolonnu vērtības no entry, nodzēs palīglogu teātra definēšanai, un izveido "zale" windows un izsauc klasi Teatris.
        rindas = int(rindas_entry.get())  # Nolasam vērtības no rindas entry.
        kolonnas = int(kolonnas_entry.get())  # Nolasam vērtības no kolonnas (sēdvietas) entry.

        logs.destroy()  # Nodzēsam logu, kur mēs prāsījam lietotājam ievādīt rindas un sēdvietu skaitu.

        zale = tkinter.Tk()  # Izveidojam jauno logu teātrim.
        zale.title("Zāle")  # Jauna loga virsraksts.
        Teatris(zale, rindas, kolonnas)  # Izsauc Teātra klasi ar lietotāja ievādītam rindam un kolonnam.
        zale.mainloop()  # Lai jauns logs būtu redzāms.


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Izveidojam logu, kur paprasām lietotājam ievādīt rindas un kolonnu (sēdvietu) skaitu teātrī. Tas ir nepieciešams teātra izveidošanai.
logs = tkinter.Tk()  # Faktiski tas ir papildlogs, lai lietotājs varētu ievādit rindas un kolonnu skaitu teātrī.
logs.title("Biļešu paradīze")  # Loga virsraksts.
logs.geometry("250x125")  # Loga izmērs.

rindas_label = tkinter.Label(logs, text="Rindu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda rindu skaitu.
rindas_label.pack()

rindas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam rindas ievadei.
rindas_entry.pack()

kolonas_label = tkinter.Label(logs, text="Sēdvietu skaits:")  # Etiķete, lai lietotājs zinātu, ka jāievāda sēdvietu (kolonnu) skaitu.
kolonas_label.pack()

kolonnas_entry = tkinter.Entry(logs)  # Entry (ievaddlaukums) lietotājam sēdvietu (kolonnas) ievadei.
kolonnas_entry.pack()

poga_izveidot = tkinter.Button(logs, text="Izveidot teātru", command=Define_Theater.izveidot_teatri)  # Poga "Izveidot teātru" papildlogam. Izsauc komandi "Define_Theater.izveidot_teatri"
poga_izveidot.pack()

logs.mainloop()  # Lai logs būtu redzams.
"""

"""
class Buyer:
    # Klase pircējam.
    def __init__(self, name, license, is_individual):
        # name - vārds un uzvārds vai kompānija.
        # license - vadītāju apliecības a. "A" vai "B" vai "C" vai "D" vai "nav".
        # is_individual - True - ir fiziska persona. False - juridiska persona.
        # A - vadītāju apliecības kategorija motocikliem (šajā programmā nav motociklus, bet tā ir reāla kategorija, tāpēc to ierākstīju).
        # B - vadītāju apliecības kategorija viegliem automobiļiem.
        # C - vadītāju apliecības kategorija kravas automobiļiem.
        # D - vadītāju apliecības kategorija autobusiem automobiļiem.
        self.name = name
        self.license = license
        self.is_individual = is_individual

        # Pārbauda vai licence nav A vai B vai C vai D vai nav.
        # Ja nav, tad license - nav.
        if self.license != "A" and self.license != "B" and self.license != "C" and self.license != "D" and self.license != "nav":
            if self.is_individual:  # Fiziskām personam.
                print(f"Pievienota fiziskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības fiziskai personai.
            elif not self.is_individual:  # Juridiskām personam.
                print(f"Pievienota juridiskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības juridiskai personai.
            else:  # Kļūda ja netika ierākstīta Boolean vērtība (True vai False).
                print(f"Kļūda! {self.name} personai jābut vai nu fiziskai vai juridiskai!")
            self.license = "nav"

        elif self.license == "A":  # Ja ir A kategorija (motocikliem) apliecībai.
            if self.is_individual:  # Ja ir A kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")
            else:   # Ja ir A kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")

        elif self.license == "B":  # Ja ir B (vieglauto) kategorija apliecībai.
            if self.is_individual:  # Ja ir B kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")
            else:  # Ja ir B kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")

        elif self.license == "C":  # Ja ir C (kravas automobiļiem) kategorija apliecībai.
            if self.is_individual:  # Ja ir C kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")
            else:  # Ja ir C kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")

        elif self.license == "D":  # Ja ir D (autobusiem) kategorija apliecībai.
            if self.is_individual:  # Ja ir D kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")
            else:  # Ja ir D kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")

    def print_license(self):
        # Izvadīt vadītāju apliecības kategoriju uz ekrāna.
        if self.license == "nav":  # Ja nav vadītāju apliecības kategoriju cilvēkam, tad izvadam kā nav.
            print(f"{self.name} nav vadītāja apliecības.")
        else:  # Ja vadītāju apliecības kategorija ir cilvēkam, tad izvadam ka ta ir.
            print(f"{self.name} ir vadītāja apliecība kategorijā {self.license}.")

    def return_license(self):
        # Atgriež vadītāju apliecības kategoriju uz ekrāna.
        return self.license

    def return_name(self):
        # Atgriež pircēja vārdu vai uzvārdu.
        return self.name


class Car:
    id_counter = 0  # Lai sekotu līdzi ID numuram.

    def __init__(self, model):
        # model - nosaukums automašīnai.
        self.id = Car.id_counter  # piešķirt automašīnai unikālu ID.
        Car.id_counter += 1  # ID skaitītājs pieaug par vienu nākamajai automašīnai.
        self.model = model
        self.is_rented = False

    def return_name(self):
        # Atgriež automašīnas nosaukumu.
        return self.model


class Truck(Car):
    # Apakšklase Car klasei.
    # Šai klasei ir cargo_capacity (kravas kapacitāte, vai kravas automašīnas ietilpība).
    def __init__(self, model, cargo_capacity):
        # model - automašīnas nosaukums.
        # cargo_capacity - kravas kapacitāte.
        super().__init__(model)
        self.cargo_capacity = cargo_capacity

    def return_name(self):
        # Atgriež kravas automašīnas nosaukumu.
        return self.model


class Bus(Car):
    def __init__(self, model, num_of_seats):
        # model - automašīnas nosaukums.
        # cargo_capacity - vietu skaits automašīnā.
        super().__init__(model)
        self.num_of_seats = num_of_seats

    def return_name(self):
        # Atgriež autobusa nosaukumu.
        return self.model


class Rental_point:
    # Nomas punkta klase.
    def __init__(self):
        self.cars = []  # Saraksts, kurā glabāsim visas automašīnas, kuri ir pieejāmi nomašanai.
        self.buses = []  # Saraksts, kurā glabāsim visus autobusus, kuri ir pieejāmi nomašanai.
        self.trucks = []  # Saraksts, kurā glabāsim visus kravas automašīnas, kuri ir pieejāmi nomašanai.
        self.rented_vehicles = []  # Lai sekotu līdzi iznomātajiem transportlīdzekļiem. Saraksts ar transportlīdzekļiem, kuri nav pieejāmi.

    def add_car(self, car):
        # car - objekts no Car klases.
        print(f"Automašīna {car.model} tika nogādāta nomas punktā!")
        self.cars.append(car)

    def add_bus(self, bus):
        # bus - objekts no Bus klases (apakšklase Car'am).
        print(f"Autobuss {bus.model} tika nogādāts nomas punktā!")
        self.buses.append(bus)

    def add_truck(self, truck):
        # truck - objekts no Truck klases (apakšklase Car'am).
        print(f"Kravas automašīna {truck.model} tika nogādāta nomas punktā!")
        self.trucks.append(truck)

    def remove_car(self, car):
        # Nodzēst vienu noteiktu vieglauto no saraksta ar pieejāmam automašīnam (nodot vieglauto metāllūžņos).
        if car in self.cars:  # Ja tas vieglauto ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva {car.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu vieglauto nodzēsam.
            self.cars.remove(car)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu vieglauto.
        else:  # Nevar nodot metallužnos vieglauto, ja tādas nav.
            print(f"Nevar nodot metallužnos automašīnu {car.model}, jo tādas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst vieglauto, kura nav pieejāma.

    def remove_bus(self, bus):
        # Nodzēst vienu noteiktu autobusu no saraksta ar pieejāmam automašīnam (nodot autobusu metāllūžņos).
        if bus in self.buses:  # Ja tas autobuss ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva autobusu {bus.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu autobusu nodzēsam.
            self.buses.remove(bus)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu autobusu.
        else:  # Nevar nodot metallužnos autobusu, ja tādu nav.
            print(f"Nevar nodot metallužnos autobusu {bus.model}, jo tāda autobusa nav nomas punktā!")   # Izvadīt informāciju par to, ka nevaram nodzēst autobusu, kurš nav pieejāms.

    def remove_truck(self, truck):
        # Nodzēst vienu noteiktu kravas automašīnu no saraksta ar pieejāmam automašīnam (nodot kravas automašīnu metāllūžņos).
        if truck in self.trucks:  # Ja tas kravas automašīna ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva kravas automašīnu {truck.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu kravas automašīnu nodzēsam.
            self.trucks.remove(truck)  # Nodzēst no saraksta kravas automašīnu.
        else:  # Nevar nodot metallužnos kravas automašīnu, ja tādas nav.
            print(f"Nevar nodot metallužnos kravas automašīnu {truck.model}, jo tādas kravas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst kravas automašīnu, kura nav pieejāma.

    def announce_cars(self):
        # Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
        print("Pašlaik nomai pieejami vieglauto:")

        free_auto = []
        for car in self.cars:
            if not car.is_rented:
                free_auto.append(car.model)

        if free_auto:
            for model in free_auto:
                print(model)
        else:
            print("Nav brīvu vieglauto.")
        print()

    def announce_buses(self):
        # Izvadīt (iz-print'ēt) uz ekrāna autobusus.
        print("Pašlaik nomai pieejami autobusi:")

        free_buses = []
        for bus in self.buses:
            if not bus.is_rented:
                free_buses.append(bus.model)

        if free_buses:
            for model in free_buses:
                print(model)
        else:
            print("Nav brīvu autobusu.")
        print()

    def announce_trucks(self):
        # Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
        print("Pašlaik nomai pieejami kravas auto:")

        free_trucks = []
        for truck in self.trucks:
            if not truck.is_rented:
                free_trucks.append(truck.model)

        if free_trucks:
            for model in free_trucks:
                print(model)
        else:
            print("Nav brīvu kravas auto.")

        print()

    def announce_available_vehicles(self):
        # Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
        # Izvadīt (iz-print'ēt) uz ekrāna autobusus.
        # Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
        self.announce_cars()
        self.announce_buses()
        self.announce_trucks()

    def sell_car(self, item, buyer):
        # Automašīnas nodošanai nomā.
        if isinstance(buyer, Buyer):
            if isinstance(item, Car) and not item.is_rented and item in self.cars:
                if buyer.license == "B":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
                else:
                    print(f"{buyer.name} ir nepieciešamas B kategorijas vadītāja apliecība, lai nomātu vieglauto {item.model}.")

            elif isinstance(item, Bus) and not item.is_rented and item in self.buses:
                if buyer.license == "D":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
                else:
                    print(f"{buyer.name} ir nepieciešamas D kategorijas vadītāja apliecība, lai nomātu autobusu {item.model}.")

            elif isinstance(item, Truck) and not item.is_rented and item in self.trucks:
                if buyer.license == "C":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}." + str(buyer.return_license()))
                else:
                    print(f"{buyer.name} ir nepieciešamas C kategorijas vadītāja apliecība, lai nomātu kravas automašīnu {item.model}." + str(buyer.return_license()))
            else:
                if isinstance(item, Bus):
                    print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejams autobusu nomas punktā!")
                else:
                    print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejama automašīnas nomas punktā!")
        else:
            print(f"Kļūda! {buyer.name} ir nepieciešama noteikta vadītāja apliecības kategorija, lai nomātu {item.model}!")

    def return_vehicle(self, vehicle):
        # Atgriezt transportlīdzekļu automašīnas nomai.
        if vehicle in self.rented_vehicles:
            vehicle.is_rented = False
            self.rented_vehicles.remove(vehicle)
            print(f"{vehicle.model} tika atgriezts nomas punktā.")
        else:
            print(f"{vehicle.model} nebija nomāts šajā nomas punktā!")

"""

"""
import math


class Taisnsturis:
    # Taisnstūris.
    def __init__(self, garums, platums):
        self.garums = garums
        self.platums = platums

    def perimetrs(self):
        # Aprēķina taisnstūra perimetru.
        return (self.garums + self.platums) * 2

    def laukums(self):
        # Aprēķina taisnstūra laukumu.
        return self.garums * self.platums


class Regular_pentagon:
    # Regulārs piecstūris.
    def __init__(self, side_length):
        self.side_length = side_length

    def perimetrs(self):
        # Aprēķina regulāra piecstūra perimetru.
        return 5 * self.side_length

    def laukums(self):
        # Aprēķina regulāra piecstūra laukumu.
        return ((math.sqrt(5) * math.sqrt(5 + 2 * math.sqrt(5))) / 4) * (self.side_length * self.side_length)
        # Formulas avots:
        # https://en.wikipedia.org/wiki/Pentagon


class Regular_hexagon:
    # Regulārs sešstūris.
    def __init__(self, side_length):
        self.side_length = side_length

    def perimetrs(self):
        # Aprēķina regulāra sešstūra perimetru.
        return 6 * self.side_length

    def laukums(self):
        # Aprēķina regulāra sešstūra laukumu.
        return (3 * math.sqrt(3) / 2) * (self.side_length * self.side_length)


class Regular_polygon:
    # Regulārs n-stūris.
    def __init__(self, side_length, num_sides):
        # num_sides - n-stūra malu skaits (vai leņķu skaits) n-stūra n skaitlis.
        # side_lenght - vienas malas garums.
        self.side_length = side_length
        self.num_sides = num_sides

    def perimetrs(self):
        # Aprēķina regulāra n-stūra perimetru.
        return self.num_sides * self.side_length

    def laukums(self):
        # Aprēķina regulāra n-stūra laukumu.
        return 0.25 * self.num_sides * self.side_length * self.side_length / math.tan(math.pi / self.num_sides)
        # Formulas avots:
        # https://en.wikipedia.org/wiki/Regular_polygon


class Trapece:
    def __init__(self, a, b, c, d):
        # Iniciālizē a, b, c, d.
        # a - trapeces pirmās malas garums.
        # b - trapeces otrais malas garums.
        # c - trapeces trešais malas garums.
        # d - trapeces trešais malas garums.
        # self - trapece.
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetrs(self):
        # Aprēķina trijstūra perimetru.
        return self.a + self.b + self.c + self.d

    def laukums(self):
        # Aprēķina trapeces laukumu
        d = self.b - self.a
        k = (d * d + self.c * self.c - self.d * self.d) / (2 * self.c * d)
        k = k * k
        t = 1 - k
        m = math.sqrt(t)
        p = ((self.a + self.b) / 2) * self.c
        return p * m
        # Laukuma formulas avots:
        # https://math.stackexchange.com/questions/2637690/is-there-a-formula-to-calculate-the-area-of-a-trapezoid-knowing-the-length-of-al


class Trijsturis:
    # Trijstūra klase.
    def __init__(self, a, b, c):
        # Iniciālizē a, b, c.
        # a - trijstūra pirmās malas garums.
        # b - trijstūra otrais malas garums.
        # c - trijstūra trešais malas garums.
        # self - trijstūris.
        self.a = a
        self.b = b
        self.c = c

    def pusperimetrs(self):
        # Aprēķina trijstūra pusperimetru.
        p = (self.a + self.b + self.c) / 2
        return p

    def laukums(self):
        # Aprēķina trijstūra laukumu ar Herona formulu.
        p = Trijsturis.pusperimetrs(self)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # self.garums * self.platums

    def perimetrs(self):
        # Aprēķina trijstūra perimetru.
        return self.a + self.b + self.c

    def ievilkta_rinka_radiuss(self):
        # Aprēķina trijstūra ievilkta riņķa līnijas rādiusu r.
        return Trijsturis.laukums(self) / Trijsturis.pusperimetrs(self)  # regulāram r = (a*sqrt(3))/6

    def apvilkta_rinka_radiuss(self):
        # Aprēķina trijstūra apvilkta riņķa līnijas rādiusu R.
        return self.a * self.b * self.c / (4 * Trijsturis.laukums(self))  # regulāram R = (a*sqrt(3))/6


class Rinkis:
    def __init__(self, radiuss):
        self.radiuss = radiuss

    def perimetrs(self):
        # Aprēķina riņķa līnijas perimetru (riņķa līnijas garumu) ar formulu pi*r*r = pi*r^2.
        return 6.283 * self.radiuss  # 2*pi*r

    def laukums(self):
        # Aprēķina riņķa līnijas laukumu ar formulu pi*r*r = pi*r^2.
        return 3.1415 * self.radiuss * self.radiuss  # pi*r*r = pi*r^2


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


def izdrukat_laukumu(figura):
    print("Šīs figūras laukums ir:", figura.laukums())


def izdrukat_perimetru(figura):
    print("Šīs figūras perimetrs ir:", figura.perimetrs())


f1 = Rinkis(1)
f2 = Taisnsturis(1, 2)
f3 = Trijsturis(1, 1, 1)
f4 = Trapece(11, 6.403, 5.385, 5)
f5 = Regular_pentagon(1)
f6 = Regular_hexagon(1)
f7 = Regular_polygon(1, 8)
f8 = Regular_polygon(1, 3)
f9 = Regular_polygon(1, 10)
f10 = Regular_polygon(1, 4)

print("Riņķis ar rādiusu 1:")
izdrukat_perimetru(f1)
izdrukat_laukumu(f1)
print()

print("Taisnstūris(1,2):")
izdrukat_perimetru(f2)
izdrukat_laukumu(f2)
print()

print("Trijsturis(1, 1, 1):")
izdrukat_perimetru(f3)
izdrukat_laukumu(f3)
print()

print("Trapece(11, 6,403, 5,385, 5):")
izdrukat_perimetru(f4)
izdrukat_laukumu(f4)
print()

print("Regulārs piecstūris(1):")
izdrukat_perimetru(f5)
izdrukat_laukumu(f5)
print()

print("Regulārs sešstūris(1):")
izdrukat_perimetru(f6)
izdrukat_laukumu(f6)
print()

print("Regulārs 8-stūris(1):")
izdrukat_perimetru(f7)
izdrukat_laukumu(f7)
print()

print("Regulārs 3-stūris(1):")
izdrukat_perimetru(f8)
izdrukat_laukumu(f8)
print()

print("Regulārs 10-stūris(1):")
izdrukat_perimetru(f9)
izdrukat_laukumu(f9)
print()

print("Regulārs 4-stūris(1):")
izdrukat_perimetru(f10)
izdrukat_laukumu(f10)
print()
"""

"""
from random import randint


class Veikals:
    # Klase veikals.
    def __init__(self):
        # Izveidojam preces un selected_preces (izvelētas preces) vārdnīcas.
        # self.preces - vārdnica ar visam precem veikalā.
        # self.selected_preces - vārdnica ar lietotāja izvelētam precem.

        self.preces = dict()
        self.selected_preces = dict()

    def pievienot_preces(self, prece, cena, daudzums):
        # Metode veikala īpašniekam.
        # Preces pievienošana veikalām. Atjaunojam vārdnicu self.preces, preci, ar norādītu cenu un daudzumu.
        # prece - preces nosaukums (str).
        # cena - preces cena par vienu vienumu (float).
        # daudzums - cik daudz preci jāpiegāda veikalām (naturāls skaitlis lielāks par 0) (int).

        self.preces[prece] = {"cena": cena, "daudzums": daudzums}

    def dzest_preces(self, prece):
        # Metode veikala īpašniekam.
        # Nodzēs norādītu preci no veikalā, nodzēs noradītu preci no saraksta.
        # prece - preces nosaukums (str).

        print(f"Prece \"{prece}\" tika izmesta Getliņu izgāztuvē.")
        del self.preces[prece]

    def paradit_izveletas_preces(self):
        # Izdruka visas lietotaja izvelētas preces.

        print("Jūsu izvelētas preces:")
        for prece, info in self.selected_preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

    def paradit_preces(self):
        # Izdruka visas veikalā pieejamas preces lietotājam.

        print("Pieejamas preces veikalā:")
        for prece, info in self.preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            print(f"{prece} - cena: {cena:.2f}€ , daudzums: {daudzums}")

    def izveleties_preces(self, prece, daudzums):
        # Metode preces izvelēšanai lietotājam, jāizvēlas preci un to daudzumu.
        # prece - preces nosaukums (str).
        # daudzums - preces daudzums (int).

        if prece in self.preces:  # Ja tāda prece ir pieejama veikalā, tad tālak pārbaudam.
            if daudzums > self.preces[prece]["daudzums"]:  # Ja pieprasītais daudzums ir lielāks nekā ir veikalā, tad paziņojam, ka nevar nopirkt.
                print(f"Kļūda! Veikalā nav tik daudz preču! Precei \"{prece}\" pieejamais daudzums: {self.preces[prece]['daudzums']}")
            else:
                self.preces[prece]["daudzums"] -= daudzums  # Atņēmam nopirktu daudzumu.
                if prece not in self.selected_preces:
                    self.selected_preces[prece] = {"cena": self.preces[prece]["cena"], "daudzums": daudzums}
                else:
                    self.selected_preces[prece]["daudzums"] += daudzums  # Pievienojam daudzumu, cik daudz preces izvelējamies nopirkt.
                print(f"Izvēlētas preces: {prece}, cena: " + str(format(self.preces[prece]["cena"], ".2f")) + f"€ , daudzums: {daudzums}")
        else:
            print(f"Kļūda! Prece \"{prece}\" nav pieejama veikalā!")  # Ja tādas preces nav veikalā, tad paziņojam to.

    def atteikt_prece(self, prece, daudzums=None):
        # Lietotājs var atgriezt veikālā kādu no jau izvelētam precem ar norādīto daudzumu.
        # Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
        # prece - preces nosaukums (str).
        # daudzums - preces daudzums (int).

        if prece in self.selected_preces:
            if daudzums is None:  # Ja lietotājs nenorāda daudzumu, tad tiek atgriezti visas preces.
                daudzums = self.selected_preces[prece]["daudzums"]

            if daudzums > self.selected_preces[prece]["daudzums"]:  # Ja lietotājs grib atgriezt vairāk nekā paņem, tad kļūda.
                print(f"Kļūda! Precei \"{prece}\" ir izvēlēts mazāks daudzums. Nevar atgriezt vairāk nekā paņemat!")
            elif daudzums < 0:  # Ja lietotājs grib atgriezt negatīvu daudzumu, tad kļūda.
                print(f"Kļūda! Nevar atgriezt negatīvu daudzumu!")
            elif daudzums == 0:  # Ja lietotājs grib atgriezt neko, tad kļūda.
                print(f"Kļūda! Nevar atgriezt neko!")
            else:
                self.selected_preces[prece]["daudzums"] -= daudzums  # Atņēmam noradītu daudzumu no izvelētam precēm.
                self.preces[prece]["daudzums"] += daudzums  # Pievienojam noradītu daudzumu par izvelētam precēm.
                if self.selected_preces[prece]["daudzums"] == 0:  # Ja atņēmam tik daudz, ka vairāk tadas preces nav (nav izvelēta), tad nodzēsam to.
                    del self.selected_preces[prece]
                print(f"Izvēlētā prece \"{prece}\" tika atgriezta veikalā. Atgrieztais daudzums: {daudzums}")  # Paziņojam lietotājam informāciju.
        else:
            print(f"Kļūda! Prece netika \"{prece}\" izvēlēta.")  # Paziņojam lietotājam.

    def pirkumu_cekis(self):
        # Izdruka pirkumu lietotājam "pirkumu čeku", ar izvelētam precēm.
        total_price = 0

        print("---------------- ČEKS ----------------")
        print("SIA \"MAKSIMA\" Latvija")
        print("Veikals \"Maksima\"")
        print("Dārza iela 21, Bauska, t.22813371")
        print("Juridiskā adrese: \"Abras\", Krustkalni,")
        print("Ķekavas pagasts, Ķekavas novads, LV-2222")
        print("Čeks " + str(randint(100, 999)) + "/" + str(randint(100, 999)) + "                   #" + str(randint(10000000, 99999999)))
        print("==========================================")

        for prece, info in self.selected_preces.items():
            cena = info["cena"]
            daudzums = info["daudzums"]
            preces_cena = cena * daudzums
            total_price += preces_cena
            print(f"{prece} - cena: {cena:.2f}€, daudzums: {daudzums}, {preces_cena:.2f}€")

        print("==========================================")
        print(f"Kopā apmaksai: {total_price:.2f}€")
        print(f"Nopelnīta \"MAKSIMA\" nauda: {total_price * 0.01:.2f}€")
        print("---------------------------------------")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


veikals = Veikals()

veikals.pievienot_preces("Āboli", 1.00, 50)
veikals.pievienot_preces("Piens", 1.40, 20)
veikals.pievienot_preces("Olas", 1.50, 30)
veikals.pievienot_preces("Pipari", 1.00, 100)

veikals.paradit_preces()
print()

veikals.dzest_preces("Piens")
print()

veikals.paradit_preces()
print()

veikals.izveleties_preces("Olas", 60)
veikals.izveleties_preces("Olas", 30)
veikals.izveleties_preces("Vārdnīca", 1)
veikals.izveleties_preces("Āboli", 50)
veikals.izveleties_preces("Pipari", 66)
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", 30)
veikals.atteikt_prece("Olas")
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", -10)
print()

veikals.paradit_izveletas_preces()
print()

veikals.atteikt_prece("Āboli", 0)
veikals.paradit_izveletas_preces()
print()
print()

veikals.pirkumu_cekis()
print()
print()

veikals.paradit_preces()

"""