# Programmas nosaukums: Rekursija ar piecstūrim.
# PU1.1 uzdevums (1MPR03_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido zemāk redzamo attēlu, izmantojot rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math
import tkinter


def zimet_piecsturi_ar_diagonalem(x0, y0, R):
    # uzzīme regulāro piecsturi (nav rotēts)
    # x0 - regulāra piecstūra centra x koordināta
    # y0 - regulāra piecstūra centra y koordināta
    # R - regulāra piecstūra rādiuss

    # t - regulāra piecstūra vienas malas garums (nepieciešams, lai izrēķinātu koordinātas)
    # h - regulāra piecstūra augstuma garums (nepieciešams, lai izrēķinātu koordinātas)

    t = R * math.sqrt((5 - math.sqrt(5)) / 2) # R * 1.17557
    h = (math.tan(math.radians(72)) / 2) * t # 1.539 * t
    k = t * math.sin(math.radians(54)) # k = t*sin(54 degree) (palīgnogriežnis)
    p = t * math.cos(math.radians(54)) # p = t*cos(54 degree) (palīgnogriežnis)

    # piecstura koordinātas
    x1 = x0 - t / 2
    y1 = y0 - R + h

    x2 = x0 - k
    y2 = y0 - R + p

    x3 = x0
    y3 = y0 - R

    x4 = x0 + k
    y4 = y0 - R + p

    x5 = x0 + t / 2
    y5 = y0 - R + h

    # pati piecstūra uzzimēšana
    kanva.create_line(x1, y1, x2, y2)
    kanva.create_line(x2, y2, x3, y3)
    kanva.create_line(x3, y3, x4, y4)
    kanva.create_line(x4, y4, x5, y5)
    kanva.create_line(x5, y5, x1, y1)

    # diagonāles uzzimēšana
    kanva.create_line(x1, y1, x3, y3)
    kanva.create_line(x1, y1, x4, y4)

    kanva.create_line(x2, y2, x4, y4)
    kanva.create_line(x2, y2, x5, y5)

    kanva.create_line(x3, y3, x5, y5)


def zimet_piecsturi_ar_diagonalem_rotets(x0, y0, R):
    # uzzīme regulāro piecsturi (ir rotēts)
    # x0 - regulāra piecstūra centra x koordināta
    # y0 - regulāra piecstūra centra y koordināta
    # R - regulāra piecstūra rādiuss

    # t - regulāra piecstūra vienas malas garums (nepieciešams, lai izrēķinātu koordinātas)
    # h - regulāra piecstūra augstuma garums (nepieciešams, lai izrēķinātu koordinātas)

    t = R * math.sqrt((5 - math.sqrt(5)) / 2) # t aptuvēni = R * 1.17557
    h = (math.tan(math.radians(72)) / 2) * t # h aptuvēni = 1.539 * t
    k = t * math.sin(math.radians(54)) # k = t*sin(54 degree) (palīgnogriežnis)
    p = t * math.cos(math.radians(54)) # p = t*cos(54 degree) (palīgnogriežnis)

    # piecstura koordinātas
    x1 = x0
    y1 = y0 + R

    x2 = x0 - k
    y2 = y0 + R - p

    x3 = x0 - t / 2
    y3 = y0 + R - h

    x4 = x0 + t / 2
    y4 = y0 + R - h

    x5 = x0 + k
    y5 = y0 + R - p

    # pati piecstūra uzzimēšana
    kanva.create_line(x1, y1, x2, y2)
    kanva.create_line(x2, y2, x3, y3)
    kanva.create_line(x3, y3, x4, y4)
    kanva.create_line(x4, y4, x5, y5)
    kanva.create_line(x5, y5, x1, y1)

    # diagonāles uzzimēšana
    kanva.create_line(x1, y1, x3, y3)
    kanva.create_line(x1, y1, x4, y4)

    kanva.create_line(x2, y2, x4, y4)
    kanva.create_line(x2, y2, x5, y5)

    kanva.create_line(x3, y3, x5, y5)


def zimet_piecsturi_rekursivi(x0, y0, R):
    # zime rekursīvi piecstūrus ar diagonālem izsaucot divas citas funkcijas
    # rekursija beigās kad R <= 10
    if R > 10:

        zimet_piecsturi_ar_diagonalem(x0, y0, R)
        zimet_piecsturi_ar_diagonalem_rotets(x0, y0, R * math.pi / 8.25)
        r = R * math.pi / 8.25
        zimet_piecsturi_rekursivi(x0, y0, r * math.pi / 8.25)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


logs = tkinter.Tk()
kanva = tkinter.Canvas(logs, width=1000, height=1000)
kanva.pack()

x0 = 500 # vislielākā (pirmā) piecstūra centra x koordināta
y0 = 525 # vislielākā (pirmā) piecstūra centra y koordināta
R = 500 # vislielākā (pirmā) piecstūra rādiusa vērtība

zimet_piecsturi_rekursivi(x0, y0, R)

logs.mainloop()
