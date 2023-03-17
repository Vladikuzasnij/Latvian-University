# Programmas nosaukums: 4. uzd MPR9
# 4. uzdevums MPR9
# Uzdevuma formulējums: Aprēķināt C n m divos veidos, t.i., izmantojot faktoriālu aprēķināšanu un veicot pakāpenisku reizināšanu un dalīšanu
# Versija 1.0

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