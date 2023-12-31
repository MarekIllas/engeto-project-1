'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author = Marek Illáš
email: m.illas@post.cz
discord: Marek I 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


oddelovac = "-" * 70


print (oddelovac)
print ("Vítáme Vás v aplikaci textový analyzátor slov. Prosím přihlaste se:".center(70).upper())
print (oddelovac)

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
jmeno = input("Zadejte prosím své uživatelské jméno: ")
heslo = input("Zadejte prosím své heslo: ")
hesla = uzivatele.get(jmeno)

if jmeno in uzivatele and heslo in hesla:
    print(oddelovac)
    print("Máme 3 texty k analýze.")
    vyber = int(input("Zadej prosím číslo od 1 do 3: "))
    print(oddelovac)

    index = vyber - 1
    rozdeleni = TEXTS[index].split()
    velka_pismena = []
    prvni_pismeno = []
    mala_pismena = []
    cisla = []
    print("Délka analyzovaného textu je:", len(rozdeleni), "slov.")

    for i in rozdeleni:
        if i.istitle():
            prvni_pismeno.append(i)
        elif i.isupper():
            velka_pismena.append(i)
        elif i.islower():
            mala_pismena.append(i)
        elif i.isnumeric():
            cisla.append(i)
    print("Text obsahuje", len(prvni_pismeno), "slov(a) s prvním velkým písmenem.")
    print("Text obsahuje", len(velka_pismena), "slov(a) napsaných velkými písmeny.")
    print("Text obsahuje", len(mala_pismena), "slov(a) napsaných malými pismeny.")
    print("Text obsahuje", len(cisla), "číslo(a).")
    print(oddelovac)

    vyskyt_cisel = []
    slovnik_cisel = {}
    for slovo in rozdeleni:
        delka_slova = len(slovo)
        vyskyt_cisel.append(delka_slova)
    for i in vyskyt_cisel:
        slovnik_cisel[i] = vyskyt_cisel.count(i)
    serazeny_slovnik = sorted(slovnik_cisel.items())
    for key, value in serazeny_slovnik:
        print(key, "*" * value, value)
    print(oddelovac)
    sectene_cislo = 0
    for i in rozdeleni:
        if i.isnumeric():
            sectene_cislo = float(sectene_cislo) + float(i)
    print("Pokud sečteme všechna čísla v textu tak získáme číslo:".upper(), sectene_cislo)
    print(oddelovac)

else:
    print("Bohužel nejste registrovaný, přístup zamítnut!".upper())