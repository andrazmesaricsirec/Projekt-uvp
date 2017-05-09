import string
def razdeli(besedilo):
    if besedilo == "":
        return ("","")
    vse_besede=besedilo.split()
    prva_beseda=vse_besede[0]
    preostanek=" ".join(vse_besede[1:])
    return(prva_beseda, preostanek)

def prevedi(besedilo, slovar): 
    if besedilo == "": return ""
    else: (prva_beseda, preostanek) = razdeli(besedilo) # prevedemo prvo besedo
    if prva_beseda in slovar: prevod_prve_besede = slovar[prva_beseda]
    else: prevod_prve_besede = "???" # prevemo preostanek
    prevod_preostanka = prevedi(preostanek, slovar) # sestavimo skupaj
    return prevod_prve_besede + (" " if prevod_preostanka != "" else "") + prevod_preostanka
    

slovar={
"piton" : "el pitón",
"število" :  "el número",
"seznam" : "la lista",
"niz" : "la cadena",
"slovar" : "el diccionario",
"je" : "es",
"krasen" : "maravilloso"}

def naprednejsi_prevajalnik():
      # Najprej pridobimo ukaz: TODO
    ukaz=str(input("Ukaz: "))
    ukaz = ukaz.upper()
      # Ločimo primere glede na ukaz
    if ukaz == "DODAJ":
          # Pridobimo tujo besedo in njen prevod: TODO
        tuja_beseda=input("Tuja beseda: ")
        slovenska_beseda=input("Slovenska_beseda: ")
          # Posodobimo slovar
        slovar[slovenska_beseda] = tuja_beseda
          # Rekurzivno poženemo program
        naprednejsi_prevajalnik() 
    elif ukaz == "PPREVEDI":
        beseda=input("Vnesi besedo: ")
          # Prevedemo stavek: TODO
        print(prevedi(beseda))
          # Prevod izpišemo: TODO
          # Rekurzivno poženemo program
        naprednejsi_prevajalnik()
    elif ukaz == "IZHOD":
          # Zaključimo izvajanje programa
        print("Prevajalnik se zapira.")
    else:
        print("Neveljaven ukaz.")
          # Rekurzivno poženemo program
        naprednejsi_prevajalnik()

  # V zadnji vrstici poženemo funkcijo naprednejsi_prevajalnik, ki se bo klicala rekurzivno
naprednejsi_prevajalnik()
