datne1 = open("C:\\Users\\37128\\Desktop\\OGAS.txt", mode="r", encoding="utf-8")
datne2 = open("C:\\Users\\37128\\Desktop\\POGAS.txt", mode="w", encoding="utf-8")

simbols = datne1.read(1)
while simbols != "":
    space_count = 0

    while simbols == " ":
        space_count = space_count + 1
        simbols = datne1.read(1)

    if space_count > 0:
        simbols = " " + simbols

    datne2.write(simbols)

    simbols = datne1.read(1)

datne1.close()
datne2.close()