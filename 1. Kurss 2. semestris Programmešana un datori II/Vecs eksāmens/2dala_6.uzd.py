
# Open the files: datne1 for reading and datne2 for writing
datne1 = open("C:\\Users\\User\\Desktop\\OGAS.txt", mode="r", encoding="utf-8")
datne2 = open("C:\\Users\\User\\Desktop\\POGAS.txt", mode="w", encoding="utf-8")

simbols = datne1.read(1)
while simbols != "":
    space_count = 0

    while simbols == " ":
        space_count += 1
        simbols = datne1.read(1)

    if space_count > 0:
        simbols = " " + simbols

    datne2.write(simbols)

    simbols = datne1.read(1)

datne1.close()
datne2.close()


'''
# atver datnes
# datne1 no kuras nolasa datus un datne2, kurā ieraksta datus.
datne1 = open("C:\\Users\\User\\Desktop\\OGAS.txt", mode="r", encoding="utf-8")
datne2 = open("C:\\Users\\User\\Desktop\\POGAS.txt", mode="w", encoding="utf-8")
# no datne1 nolasa datus pa vienam simbolam
simbols = datne1.readline(1)
while simbols != "":  # kamēr simbols nav nekas
    sk = 0  # ievieš skaitītāju, kas uzskaita atstarpju skaitu
    while simbols == " ":  # kamēr simbols ir atstarpe, nolasa nākamo simbolu
        sk = sk + 1
        simbols = datne1.readline(1)
    else:
        if sk > 0:
            # ja skaitītājs nav 0
            # tad bijušas vairākas atstarpes, kuras tika dzēstas
            # nepieciešams pievienot atstarpi pirms simbola
            simbols = " " + simbols

    datne2.write(simbols)
    simbols = datne1.readline(1)

datne1.close()
datne2.close()
'''
