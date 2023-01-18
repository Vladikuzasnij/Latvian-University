# Programmas nosaukums: 6. uzd MPR9
# 6. uzdevums MPR9
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro vai lietotāja ievadītā simbolu virkne ir palindroma, t.i., no abām pusēm lasās vienādi, piemēram, SMUKUMS, SULA ARI IRA ALUS
# Versija 1.0


x = input("Ievadi vārdu: ")
y = len(x) # Cik ir garums

atb = "Ir palindroms"
 
for i in range (y//2):
    if x[i] != x[y-1-i]:
        atb ="Nav palindroms"
        break
    
print(atb)
    