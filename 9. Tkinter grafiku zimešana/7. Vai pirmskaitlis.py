# Programmas nosaukums: 3. uzd MPR9
# 3. uzdevums MPR9
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, vai lietotāja ievadītais skaitlis ir pirmskaitlis.
# Versija 1.0

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