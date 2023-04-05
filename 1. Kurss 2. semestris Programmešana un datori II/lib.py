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


def can_make_triangle(a, b, c): # malu garumi a b c nevis koordinatas
	if (a + b > c) and (b + c > a) and (a + c > b):
		return True
	else:
		return False

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

def is_natural_or_zero_long(s):
	# Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
	# Atgriež True, ja virkne reprezentē naturālo skaitli.
	# Atgriež False, ja nereprezentē naturālo skaitli.
	# s - pārbaudama simbolu virkne

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