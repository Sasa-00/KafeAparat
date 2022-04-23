import menu
import time

run = True


# Funkcija "racunanje" se pokrece nakon unosa zeljene kafe, i novca, pa se te informacije uzimaju kao parametri
def racunanje(deset, dvadeset, pedeset, sto, dvesta, vrsta_kafe):
    deset = deset * 10
    dvadeset = dvadeset * 20
    pedeset = pedeset * 50
    sto = sto * 100
    dvesta = dvesta * 200

    # Izracunavanje ukupnog stanja novca
    ukupno_para = menu.resursi["novac"] + deset + dvadeset + pedeset + sto + dvesta

    cena = 0

    # Smestanje cene izabrane kafe u promenljivu "cena"
    for j in menu.menu:
        if j == vrsta_kafe:
            cena = menu.menu[vrsta_kafe]["cena"]

    # Izracunavanje razlike izmedju kredita u aparatu i cene izabranog napitka
    razlika = ukupno_para - cena

    # Pravljenje kafe, odnosno uzimanje potrebnih resursa
    menu.resursi["voda"] -= menu.menu[vrsta_kafe]["sastojci"]["voda"]
    menu.resursi["kafa"] -= menu.menu[vrsta_kafe]["sastojci"]["kafa"]
    menu.resursi["mleko"] -= menu.menu[vrsta_kafe]["sastojci"]["mleko"]

    # if petlja zaduzena za upozorenje korisnika da nema dovoljno resursa, odnosno za skidanje
    # novca ukoliko ih ima (else)
    if menu.resursi["voda"] < 0:
        print("Izvinite, nema dovoljno vode")
        menu.resursi["voda"] += menu.menu[vrsta_kafe]["sastojci"]["voda"]
        menu.resursi["kafa"] += menu.menu[vrsta_kafe]["sastojci"]["kafa"]
        menu.resursi["mleko"] += menu.menu[vrsta_kafe]["sastojci"]["mleko"]
        return -1
    elif menu.resursi["kafa"] < 0:
        print("Izvinite, nema dovoljno kafe")
        menu.resursi["voda"] += menu.menu[vrsta_kafe]["sastojci"]["voda"]
        menu.resursi["kafa"] += menu.menu[vrsta_kafe]["sastojci"]["kafa"]
        menu.resursi["mleko"] += menu.menu[vrsta_kafe]["sastojci"]["mleko"]
        return -1
    elif menu.resursi["mleko"] < 0:
        print("Izvinite, nema dovoljno mleka")
        menu.resursi["voda"] += menu.menu[vrsta_kafe]["sastojci"]["voda"]
        menu.resursi["kafa"] += menu.menu[vrsta_kafe]["sastojci"]["kafa"]
        menu.resursi["mleko"] += menu.menu[vrsta_kafe]["sastojci"]["mleko"]
        return -1
    elif razlika < 0:
        print("Izvinite, nema dovoljno para")
        menu.resursi["voda"] += menu.menu[vrsta_kafe]["sastojci"]["voda"]
        menu.resursi["kafa"] += menu.menu[vrsta_kafe]["sastojci"]["kafa"]
        menu.resursi["mleko"] += menu.menu[vrsta_kafe]["sastojci"]["mleko"]
        menu.resursi["novac"] = deset + dvadeset + pedeset + sto + dvesta
        return -1
    else:
        menu.resursi["novac"] -= cena
        # Funkcija vraca kusur
        return razlika


# Ispisivanje menija u konzoli
print(f"""
Espresso: {menu.menu["espresso"]["cena"]}din
Latte: {menu.menu["latte"]["cena"]}din
Cappuccino: {menu.menu["cappuccino"]["cena"]}din
""")
print("Unesite 'provera' za proveru stanja")


while run:
    vrsta_kafe = input("Sta zelite da pijete? (espresso/latte/cappuccino): ")
    # "off" komanda sluzi samo za "majstore", i samo je oni znaju, pa zato ne izlazi na konzoli.
    # If petlja ispod sluzi za citanje unosa i izvrsavanje odgovarajuceg dela u odnosu na isti
    if vrsta_kafe == "off":
        print("Gasenje masine...")
        time.sleep(5)
        print("Masina je ugasena")
        run = False
    # Deo petlje za proveru resursa, ukoliko se trazi
    elif vrsta_kafe == "provera":
        for i in menu.resursi:
            if i == "voda" or i == "mleko":
                print(f"{i}: {menu.resursi[i]}ml")
            elif i == "kafa":
                print(f"{i}: {menu.resursi[i]}g")
            elif i == "novac":
                print(f"{i}: {menu.resursi[i]} din")
        continue
    # Potvrda koja je kafa izabrana, pa ubacivanje posebnih novcanica
    elif vrsta_kafe == "espresso" or vrsta_kafe == "latte" or vrsta_kafe == "cappuccino":
        print("Molimo unesite novac.\nMozete uneti novac u vrednosti od 10/20/50/100/200 dinara")
        deset = int(input("Koliko novcanica od 10 dinara unosite?: "))
        dvadeset = int(input("Koliko novcanica od 20 dinara unosite?: "))
        pedeset = int(input("Koliko novcanica od 50 dinara unosite?: "))
        sto = int(input("Koliko novcanica od 100 dinara unosite?: "))
        dvesta = int(input("Koliko novcanica od 200 dinara unosite?: "))
        # Pokretanje funkcije "racunanje" i smestanje u promenljivu "kusur"
        kusur = racunanje(deset, dvadeset, pedeset, sto, dvesta, vrsta_kafe)
        # Ako je kusur veci ili jednak nuli program se nastavlja dalje, ukoliko nije vraca se na pocetak while petlje
        if kusur >= 0:
            pass
        else:
            continue
        print(f"Imate {kusur} din kusura")
        print(f"Izvolite vas {vrsta_kafe} ☕ Uzivajte!")
        # Ostatak novca se smesta u resurse
        menu.resursi["novac"] = kusur
        continue
    else:
        # Obavestenje i povratak na pocetak while petlje
        print("Niste uneli ispravne podatke!")
        continue


