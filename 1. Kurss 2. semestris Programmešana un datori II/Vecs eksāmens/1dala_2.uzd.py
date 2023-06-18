# 2.uzd.

'''
комменты
берёт каждый третий индекс с конца и выводит его(то есть четвёртый)
выделяет его и выводит
<-
[0] [1] [2] [3] <- 
'''

'''
Originals
n = int(input("Cik skaitļus ievadīsiet?: "))
s = ""
for i in range(n):
    x = int(input("Ievadiet skaitli: "))
    s = s + str(x)
rez = ""
for i in range(n - 3, -1, -3):
    rez = rez + s[i] + ","
print(rez)
'''


# берёт все третьи числа reversed <-
n = int(input("Skaitļu daudzums ==> "))

sv = ""

for i in range(n):
    sk = int(input("Skaitlis ==> "))
    sk = str(sk)
    sv += sk

print(sv)  # skaitlis ievaditais

endsv = ""

for i in range(n - 3, -1, -3):  # ņem katru trešu no gala
    # print(sv[i])
    endsv += sv[i] + " "

print(endsv)


