# Programmas nosaukums: 4. uzd MPR11
# 4. uzdevums MPR11
# Uzdevuma formulējums: Sastādit programmu, kas atrod N ciparu pēc kārtas bez atstarpēm uzrakstītajā Fibonači skaitļu virknē. Skaitli N ievada lietotājs.
# Versija 1.0

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