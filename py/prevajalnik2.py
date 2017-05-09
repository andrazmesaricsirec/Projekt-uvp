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

def prevajalnik():
      # Uporabnik vpiše niz: TODO
    niz=input()
      # Ločimo primere glede na vpisan niz
    if niz == "Izhod":
          # Zaključimo izvajanje programa
        print("Prevajalnik se zapira.")
    else:
          # Prevedemo niz: TODO
        prevod=prevedi(niz,slovar)
          # Prevod izpišemo: TODO
        print(prevod)
          # Rekurzivno poženemo program
        prevajalnik()

 
prevajalnik()
