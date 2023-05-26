# Programmas nosaukums: Morzes kods ar pīksteņiem
# PU3. uzdevums (1MPR15_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas veic teksta šifrēšanu, izmantojot Mores kodu, kodu pārraidot kā skaņas un/vai gaismas signālu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import winsound


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


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Morzes koda avots:
# https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
# Tiek izmantota atstārpes rakstzīme " ", lai paradītu pauzi starp rakstzīmēm - trīs vienības.
# Tiek izmantota atstārpes rakstzīme "/", lai paradītu pauzi starp vārdiem - septiņas vienības.
# "." - viena vienība.
# " " - trīs vienības.
# "/" - septiņas vienības, lai paradītu atstārpi " " starp vārdiem, atstājam to ar "/".

morse_code_dictionary = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", '6': "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    " ": "/"  # 3 vienības.
}

# Morzes koda ilgums milisekundēs
dot_duration = 120  # Punkts - viena vienība.
dash_duration = dot_duration * 3  # Svītriņa - trīs vienības.
pause_between_letters_duration = dot_duration  # Pauze starp signāla vienumu - viena vienība.
pause_between_words_duration = dot_duration * 7  # Pauze starp vārdiem - septiņas vienības.


nav_sifrets_to_morse_txt = "C:\\Users\\User\\Desktop\\teksts_to_morze.txt"  # Šajā vietā lietotājs ievadīs tekstu kas nav šifrēts (ievada lietotājs).
ir_sifrets_to_morse_txt = "C:\\Users\\User\\Desktop\\morzes_kods.txt"  # Šajā vietā būs aizšifrēts teksts ar Morzes kodu (ievada lietotājs).

aizsifrets_to_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\morzes_kods_save.txt"  # Šajā vietā būs aizšifrēts teksts ar Morzes kodu (programma šajā datnē ieraksta aizšifrētu tekstu ar Morzes kodu).
atsifrets_no_morses_kods_save_txt = "C:\\Users\\User\\Desktop\\atsifrets_no_morzes_koda_save.txt"  # Šajā vietā būs atšifrēts teksts no Morzes koda (programma šajā datnē ieraksta atšifrētu tekstu no Morzes koda).

print("Teksts kurš ir ierakstīts teksts_to_morze.txt datnē un kuru var aizšifrēt:")
print_text_from_data_by_rows(nav_sifrets_to_morse_txt)

print("\n\nTeksts kurš ir ierakstīts morzes_kods.txt datnē un kuru var atšifrēt:")
print_text_from_data_by_rows(ir_sifrets_to_morse_txt)

print("\n\nJa gribat atšifrēt vai aizšifrēt citu tekstu, tad izmainiet atbilstošu datnes saturu.\n")
print("---------------------------------------------------------------------------------------\n")

ievade = input_cypher_to_morse_or_decrypt_from_morse()

if ievade:  # Ja ievade ir True, tad lietotājs grib aizšifrēt tekstu.
    message_to_encrypt = save_text_from_data_by_rows_to_variable(nav_sifrets_to_morse_txt)  # Saglabājam teksts_to_morze.txt datnes saturu kā str mainīgu message_to_encrypt
    encrypted_text = encrypt_to_morse_code(message_to_encrypt, morse_code_dictionary)  # Aizšifrējam str tekstu message_to_encrypt

    print("\nTeksts:")
    print_text_from_data_by_rows(nav_sifrets_to_morse_txt)

    print("\n\nAizšifrēts teksts ar Morzes kodu:")
    print(encrypted_text)  # Izvadīt aizšifrētu ar Morzes kodu tekstu.

    morse_play(encrypted_text)

elif not ievade:  # Ja ievade ir False, tad lietotājs grib atšifrēt tekstu.
    message_to_decrypt = save_text_from_data_by_rows_to_variable(ir_sifrets_to_morse_txt)  # Saglabājam morzes_kods.txt datnes saturu kā str mainīgu message_to_decrypt
    decrypted_message = decrypt_from_morse_code(message_to_decrypt, morse_code_dictionary)  # Atšifrējam str tekstu message_to_decrypt.

    print("\nAizšifrēts teksts ar Morzes kodu:")
    print_text_from_data_by_rows(ir_sifrets_to_morse_txt)

    print("\n\nAtšifrēts teksts:")
    print(decrypted_message)  # Izvadīt atšifrētu tekstu no Morzes koda.

    morse_play(message_to_decrypt)

else:
    print("Neparedzamā kļūda!")
