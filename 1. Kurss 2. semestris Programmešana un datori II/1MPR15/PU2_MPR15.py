# Programmas nosaukums: Teksta šifrēšana (Latviešu burti)
# PU2. uzdevums (1MPR15_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas veic teksta, kas sastāv no latviešu alfabēta burtiem, aizšifrēšanu un atšifrēšanu,
# atbilstoši 2.uzdevuma nosacījumiem.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


def write_text_to_file(filename, text):
    # NODZES VISU INFORMĀCIJU filename DATNE un ieraksta jaunu informāciju no str text mainīga.
    # text - str teksts, kuru gribam ierākstit datnē.
    # filename - faila (datnes) nosaukums.
    # Piemēram:
    # filename = "C:\\Users\\User\\Desktop\\nav_sifrets_2.txt"

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)


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


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


nav_sifrets_txt = "C:\\Users\\User\\Desktop\\nav_sifrets_2.txt"  # Šajā vietā lietotājs ievadīs tekstu kas nav šifrēts.
ir_sifrets_txt = "C:\\Users\\User\\Desktop\\ir_sifrets_2.txt"  # Šajā vietā būs aizšifrēts teksts.
atslega_txt = "C:\\Users\\User\\Desktop\\atslega_2.txt"  # Šajā vietā glabāsies atslega no aizšifrētam tekstam.
burti = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž", "_"]  # Latviešu alfabēts ar svitriņu.

# ievade - boolean vertība, ja True, tad encryption (atšifrēts -> aizšifrēts). Ja False, tad decryption (aizšifrēts -> atšifrēts)
ievade = input_cypher_or_decrypt()  # Prasa lietotājam vai lietotājs grib aizšifrēt (encrypt) tekstu vai atšifrēt (decrypt) tekstu.

if ievade:  # Ja ievade ir True, tad lietotājs grib aizšifrēt tekstu.
    cypher_main()
elif not ievade:  # Ja ievade ir False, tad lietotājs grib atšifrēt tekstu.
    decrypt_main()
else:
    print("Neparedzamā kļūda!")
