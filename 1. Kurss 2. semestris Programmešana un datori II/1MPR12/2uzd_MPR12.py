# Programmas nosaukums: Automašīnu nomas simulācija.
# 2. uzdevums (1MPR12_Vladislavs_Babaņins).
# Uzdevuma formulējums: Sastādīt programmu, kas realizē vienkāršotu automašīnu nomas punkta darbību.
# Nomas punktā ir vairāku tipu automašīnas - vieglās automašīnas, kravas automašīnas un autobusi.
# Auto nomas punkts var iegādāties jaunas automašīnas un utilizēt nevajadzīgās automašīnas.
# Auto nomas punkts prot paziņot, kādas automašīnas tas pašlaik piedāvā.
# Auto nomas punkta klienti ir juridiskas un fiziskas personas. Auto nomas klients var veikts divas darbības - nomāt tikai Auto nomas punktā esošu automašīnu vai atdot atpakaļ nomāto automašīnu.
# Programmas autors: Vladislavs Babaņins.
# Versija 1.0

"""
Ar vadītāju kategorijām un auto ID.
"""


class Buyer:
    # Klase pircējam.
    def __init__(self, name, license, is_individual):
        # name - vārds un uzvārds vai kompānija.
        # license - vadītāju apliecības a. "A" vai "B" vai "C" vai "D" vai "nav".
        # is_individual - True - ir fiziska persona. False - juridiska persona.
        # A - vadītāju apliecības kategorija motocikliem (šajā programmā nav motociklus, bet tā ir reāla kategorija, tāpēc to ierākstīju).
        # B - vadītāju apliecības kategorija viegliem automobiļiem.
        # C - vadītāju apliecības kategorija kravas automobiļiem.
        # D - vadītāju apliecības kategorija autobusiem automobiļiem.
        self.name = name
        self.license = license
        self.is_individual = is_individual

        # Pārbauda vai licence nav A vai B vai C vai D vai nav.
        # Ja nav, tad license - nav.
        if self.license != "A" and self.license != "B" and self.license != "C" and self.license != "D" and self.license != "nav":
            if self.is_individual:  # Fiziskām personam.
                print(f"Pievienota fiziskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības fiziskai personai.
            elif not self.is_individual:  # Juridiskām personam.
                print(f"Pievienota juridiskā persona {self.name} bez vadītāja apliecību.")  # Ja nesakrīt ne ar vienu reālu apliecības kategoriju, tad nav vadītaja apliecības juridiskai personai.
            else:  # Kļūda ja netika ierākstīta Boolean vērtība (True vai False).
                print(f"Kļūda! {self.name} personai jābut vai nu fiziskai vai juridiskai!")
            self.license = "nav"

        elif self.license == "A":  # Ja ir A kategorija (motocikliem) apliecībai.
            if self.is_individual:  # Ja ir A kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")
            else:   # Ja ir A kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar A kategorijas (motocikli) vadītāja apliecību.")

        elif self.license == "B":  # Ja ir B (vieglauto) kategorija apliecībai.
            if self.is_individual:  # Ja ir B kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")
            else:  # Ja ir B kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar B kategorijas (vieglauto) vadītāja apliecību.")

        elif self.license == "C":  # Ja ir C (kravas automobiļiem) kategorija apliecībai.
            if self.is_individual:  # Ja ir C kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")
            else:  # Ja ir C kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar C kategorijas (kravas automašīnas) vadītāja apliecību.")

        elif self.license == "D":  # Ja ir D (autobusiem) kategorija apliecībai.
            if self.is_individual:  # Ja ir D kategorija apliecībai un tā ir fiziska persona.
                print(f"Pievienota fiziskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")
            else:  # Ja ir D kategorija apliecībai un tā ir juridiskā persona.
                print(f"Pievienota juridiskā persona {self.name} ar D kategorijas (autobuss) vadītāja apliecību.")

    def print_license(self):
        # Izvadīt vadītāju apliecības kategoriju uz ekrāna.
        if self.license == "nav":  # Ja nav vadītāju apliecības kategoriju cilvēkam, tad izvadam kā nav.
            print(f"{self.name} nav vadītāja apliecības.")
        else:  # Ja vadītāju apliecības kategorija ir cilvēkam, tad izvadam ka ta ir.
            print(f"{self.name} ir vadītāja apliecība kategorijā {self.license}.")

    def return_license(self):
        # Atgriež vadītāju apliecības kategoriju uz ekrāna.
        return self.license

    def return_name(self):
        # Atgriež pircēja vārdu vai uzvārdu.
        return self.name


class Car:
    id_counter = 0  # Lai sekotu līdzi ID numuram.

    def __init__(self, model):
        # model - nosaukums automašīnai.
        self.id = Car.id_counter  # piešķirt automašīnai unikālu ID.
        Car.id_counter += 1  # ID skaitītājs pieaug par vienu nākamajai automašīnai.
        self.model = model
        self.is_rented = False

    def return_name(self):
        # Atgriež automašīnas nosaukumu.
        return self.model


class Truck(Car):
    # Apakšklase Car klasei.
    # Šai klasei ir cargo_capacity (kravas kapacitāte, vai kravas automašīnas ietilpība).
    def __init__(self, model, cargo_capacity):
        # model - automašīnas nosaukums.
        # cargo_capacity - kravas kapacitāte.
        super().__init__(model)
        self.cargo_capacity = cargo_capacity

    def return_name(self):
        # Atgriež kravas automašīnas nosaukumu.
        return self.model


class Bus(Car):
    def __init__(self, model, num_of_seats):
        # model - automašīnas nosaukums.
        # cargo_capacity - vietu skaits automašīnā.
        super().__init__(model)
        self.num_of_seats = num_of_seats

    def return_name(self):
        # Atgriež autobusa nosaukumu.
        return self.model


class Rental_point:
    # Nomas punkta klase.
    def __init__(self):
        self.cars = []  # Saraksts, kurā glabāsim visas automašīnas, kuri ir pieejāmi nomašanai.
        self.buses = []  # Saraksts, kurā glabāsim visus autobusus, kuri ir pieejāmi nomašanai.
        self.trucks = []  # Saraksts, kurā glabāsim visus kravas automašīnas, kuri ir pieejāmi nomašanai.
        self.rented_vehicles = []  # Lai sekotu līdzi iznomātajiem transportlīdzekļiem. Saraksts ar transportlīdzekļiem, kuri nav pieejāmi.

    def add_car(self, car):
        # car - objekts no Car klases.
        print(f"Automašīna {car.model} tika nogādāta nomas punktā!")
        self.cars.append(car)

    def add_bus(self, bus):
        # bus - objekts no Bus klases (apakšklase Car'am).
        print(f"Autobuss {bus.model} tika nogādāts nomas punktā!")
        self.buses.append(bus)

    def add_truck(self, truck):
        # truck - objekts no Truck klases (apakšklase Car'am).
        print(f"Kravas automašīna {truck.model} tika nogādāta nomas punktā!")
        self.trucks.append(truck)

    def remove_car(self, car):
        # Nodzēst vienu noteiktu vieglauto no saraksta ar pieejāmam automašīnam (nodot vieglauto metāllūžņos).
        if car in self.cars:  # Ja tas vieglauto ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva {car.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu vieglauto nodzēsam.
            self.cars.remove(car)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu vieglauto.
        else:  # Nevar nodot metallužnos vieglauto, ja tādas nav.
            print(f"Nevar nodot metallužnos automašīnu {car.model}, jo tādas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst vieglauto, kura nav pieejāma.

    def remove_bus(self, bus):
        # Nodzēst vienu noteiktu autobusu no saraksta ar pieejāmam automašīnam (nodot autobusu metāllūžņos).
        if bus in self.buses:  # Ja tas autobuss ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva autobusu {bus.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu autobusu nodzēsam.
            self.buses.remove(bus)  # Nodzēst no saraksta ar pieejāmiem automašīnam šo konkrētu autobusu.
        else:  # Nevar nodot metallužnos autobusu, ja tādu nav.
            print(f"Nevar nodot metallužnos autobusu {bus.model}, jo tāda autobusa nav nomas punktā!")   # Izvadīt informāciju par to, ka nevaram nodzēst autobusu, kurš nav pieejāms.

    def remove_truck(self, truck):
        # Nodzēst vienu noteiktu kravas automašīnu no saraksta ar pieejāmam automašīnam (nodot kravas automašīnu metāllūžņos).
        if truck in self.trucks:  # Ja tas kravas automašīna ir sarakstā ar pieejāmam automašīnam.
            print(f"Nomas punkts nodeva kravas automašīnu {truck.model} metāllūžņos!")  # Izvadīt informāciju par to, kādu kravas automašīnu nodzēsam.
            self.trucks.remove(truck)  # Nodzēst no saraksta kravas automašīnu.
        else:  # Nevar nodot metallužnos kravas automašīnu, ja tādas nav.
            print(f"Nevar nodot metallužnos kravas automašīnu {truck.model}, jo tādas kravas automašīnas nav nomas punktā!")  # Izvadīt informāciju par to, ka nevaram nodzēst kravas automašīnu, kura nav pieejāma.

    def announce_cars(self):
        # Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
        print("Pašlaik nomai pieejami vieglauto:")

        free_auto = []
        for car in self.cars:
            if not car.is_rented:
                free_auto.append(car.model)

        if free_auto:
            for model in free_auto:
                print(model)
        else:
            print("Nav brīvu vieglauto.")
        print()

    def announce_buses(self):
        # Izvadīt (iz-print'ēt) uz ekrāna autobusus.
        print("Pašlaik nomai pieejami autobusi:")

        free_buses = []
        for bus in self.buses:
            if not bus.is_rented:
                free_buses.append(bus.model)

        if free_buses:
            for model in free_buses:
                print(model)
        else:
            print("Nav brīvu autobusu.")
        print()

    def announce_trucks(self):
        # Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
        print("Pašlaik nomai pieejami kravas auto:")

        free_trucks = []
        for truck in self.trucks:
            if not truck.is_rented:
                free_trucks.append(truck.model)

        if free_trucks:
            for model in free_trucks:
                print(model)
        else:
            print("Nav brīvu kravas auto.")

        print()

    def announce_available_vehicles(self):
        # Izvadīt (iz-print'ēt) uz ekrāna automašīnas.
        # Izvadīt (iz-print'ēt) uz ekrāna autobusus.
        # Izvadīt (iz-print'ēt) uz ekrāna kravas automašīnas.
        self.announce_cars()
        self.announce_buses()
        self.announce_trucks()

    def sell_car(self, item, buyer):
        # Automašīnas nodošanai nomā.
        if isinstance(buyer, Buyer):
            if isinstance(item, Car) and not item.is_rented and item in self.cars:
                if buyer.license == "B":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
                else:
                    print(f"{buyer.name} ir nepieciešamas B kategorijas vadītāja apliecība, lai nomātu vieglauto {item.model}.")

            elif isinstance(item, Bus) and not item.is_rented and item in self.buses:
                if buyer.license == "D":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}.")
                else:
                    print(f"{buyer.name} ir nepieciešamas D kategorijas vadītāja apliecība, lai nomātu autobusu {item.model}.")

            elif isinstance(item, Truck) and not item.is_rented and item in self.trucks:
                if buyer.license == "C":
                    item.is_rented = True
                    self.rented_vehicles.append(item)
                    print(f"{item.model} tika nodots nomai! Tagad to noma {buyer.name}." + str(buyer.return_license()))
                else:
                    print(f"{buyer.name} ir nepieciešamas C kategorijas vadītāja apliecība, lai nomātu kravas automašīnu {item.model}." + str(buyer.return_license()))
            else:
                if isinstance(item, Bus):
                    print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejams autobusu nomas punktā!")
                else:
                    print(f"Atvainojiet, {buyer.name}! {item.model} pašlaik nav pieejama automašīnas nomas punktā!")
        else:
            print(f"Kļūda! {buyer.name} ir nepieciešama noteikta vadītāja apliecības kategorija, lai nomātu {item.model}!")

    def return_vehicle(self, vehicle):
        # Atgriezt transportlīdzekļu automašīnas nomai.
        if vehicle in self.rented_vehicles:
            vehicle.is_rented = False
            self.rented_vehicles.remove(vehicle)
            print(f"{vehicle.model} tika atgriezts nomas punktā.")
        else:
            print(f"{vehicle.model} nebija nomāts šajā nomas punktā!")


# TESTA PIEMĒRI.
# Izveidot Pircēja klases instances.
buyer1 = Buyer("Artūrs Kariņš", "A", True)
buyer2 = Buyer("SIA 'RVR'", "B", False)
buyer3 = Buyer("Edgars Pliekšāns", "E", True)
buyer4 = Buyer("AS 'Gosbank'", "D", False)
buyer5 = Buyer("Jāzeps Baumanis", "nav", False)
buyer6 = Buyer("SIA 'OGAS'", "F", False)
buyer7 = Buyer("Lizete Rozenberga", "C", True)
buyer8 = Buyer("SIA 'OBKhSS'", "B", False)

# Auto klases instances izveide.
volga = Car("GAZ-24 Volga")
zhiguli = Car("VAZ-2106 Zhiguli")
moskvich = Car("Moskvich-403")
pioneer = Car("Pioneer 2M")
lamborghini = Car("Lamborghini Diablo")
rolls_royce = Car("Rolls-Royce Phantom")

# Truck klases instances izveide.
hummer = Truck("Hummer H3", 5000)
hanomag = Truck("Hanomag-Henschel F55", 10000)
uaz = Truck("UAZ-452", 1500)

# Autobusu klases instances izveide.
mercedes = Bus("Mercedes-Benz Sprinter", 12)
raf = Bus("RAF-2203", 15)

# Rental_point klases instances izveide.
rental_point = Rental_point()
print()

# Pievienojam automašīnas nomas punktam.
rental_point.add_car(volga)
rental_point.add_car(zhiguli)
rental_point.add_car(moskvich)
rental_point.add_car(pioneer)
rental_point.add_car(lamborghini)
rental_point.add_car(rolls_royce)
print()

# Pārbaude kravas automašīnu pievienošanu nomas punktam.
rental_point.add_truck(hummer)
rental_point.add_truck(hanomag)
rental_point.add_truck(uaz)
print()

# Testē autobusu pievienošanu nomas punktam.
rental_point.add_bus(mercedes)
rental_point.add_bus(raf)
print()

rental_point.announce_available_vehicles()

# Pārbaude automašīnu izņemšanu no nomas punkta.
rental_point.remove_car(lamborghini)
rental_point.remove_car(rolls_royce)

# Kravas automašīnu izņemšanas pārbaude no nomas punkta.
rental_point.remove_truck(hummer)
rental_point.remove_truck(hanomag)

# Autobusu izņemšanas pārbaude no nomas punkta.
rental_point.remove_bus(mercedes)
print()

# Testēšana, paziņojot par pieejamajām automašīnām.
rental_point.announce_cars()

# Testēšana, paziņojot par pieejamajām kravas auto.
rental_point.announce_trucks()

# Testēšana, paziņojot par pieejamiem autobusiem.
rental_point.announce_buses()

# Nomas automašīnu testēšana.
rental_point.sell_car(moskvich, buyer1)
rental_point.sell_car(pioneer, buyer2)
rental_point.sell_car(volga, buyer3)
rental_point.sell_car(zhiguli, buyer4)
rental_point.sell_car(moskvich, buyer5)
rental_point.sell_car(pioneer, buyer6)

# Kravas automašīnu nomas pārbaude.
rental_point.sell_car(hanomag, buyer1)
rental_point.sell_car(hummer, buyer2)
rental_point.sell_car(hanomag, buyer3)

# Pārbauda nomas autobusu pircēju.
rental_point.sell_car(mercedes, buyer4)
rental_point.sell_car(raf, buyer5)
rental_point.sell_car(mercedes, buyer6)

print()
buyer1.print_license()
buyer2.print_license()
buyer3.print_license()
buyer4.print_license()
buyer5.print_license()
buyer6.print_license()
buyer7.print_license()
print()

print("<Izvadīt tikai pieejamus kravas automašīnas>")
rental_point.announce_trucks()

print("<Izvadīt tikai pieejamus autobusus>")
rental_point.announce_buses()

print(str(volga.return_name()) + " ID:")
print(volga.id)
print(str(zhiguli.return_name()) + " ID:")
print(zhiguli.id)
print(str(moskvich.return_name()) + " ID:")
print(moskvich.id)
print(str(pioneer.return_name()) + " ID:")
print(pioneer.id)
print(str(hummer.return_name()) + " ID:")
print(hummer.id)
print(str(hanomag.return_name()) + " ID:")
print(hanomag.id)
print(str(mercedes.return_name()) + " ID:")
print(mercedes.id)
print(str(raf.return_name()) + " ID:")
print(raf.id)
print()

print("<Izvadīt tikai pieejamus vieglauto>")
rental_point.announce_cars()

rental_point.add_bus(mercedes)
rental_point.add_bus(raf)
rental_point.sell_car(mercedes, buyer1)
rental_point.sell_car(mercedes, buyer2)
rental_point.sell_car(mercedes, buyer4)
rental_point.sell_car(mercedes, buyer4)
rental_point.sell_car(moskvich, buyer4)
rental_point.return_vehicle(mercedes)
rental_point.return_vehicle(raf)
