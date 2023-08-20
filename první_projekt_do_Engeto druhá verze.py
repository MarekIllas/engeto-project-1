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


uživatelé = {"bob": "123","ann": "pass123","mike": "password123","liz": "pass123"}

print(80 * "-")
print ("Vítáme Vás v aplikaci textový analyzátor slov. Prosím přihlaste se:".center(70).upper())
for i in range(3):
    jméno = input("Zadejte prosím své uživatelské jméno:")
    heslo = input("Zadejte prosím své heslo:")
    if uživatelé.get(jméno) == heslo:
        break
    else:
        print("Špatné uživatelské jméno nebo heslo !!!".upper())
print(80 * '-')


print("Máme 3 texty k analýze:".upper())
while True:
    try:
        choice = int(input("Zadejte prosím číslo od 1 do 3:"))
        if choice in range(1, 4):
            break
    except ValueError:
        print("Zadejte číslo !!!")
print(80 * '-')


text = TEXTS[choice - 1]
words = text.split()
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
numbers = []
word_lens = {}

for word in words:
    word = word.strip(" .,")
    if word.istitle():
        titlecase += 1
    if word.isupper():
        uppercase += 1
    if word.islower():
        lowercase += 1
    if word.isnumeric():
        numeric += 1
        numbers.append(int(word))
    word_len = len(word)
    word_lens[word_len] = word_lens.get(word_len, 0) + 1

print("Text obsahuje {} slov(a) ve vybraném textu.".format(len(words)))
print("Text obsahuje {} slov(a) s prvním velkým písmenem.".format(titlecase))
print("Text obsahuje {} slov(a) napsaných velkými písmeny.".format(uppercase))
print("Text obsahuje {} slov(a) napsaných malými pismeny.".format(lowercase))
print("Text obsahuje {} číslo(a).".format(numeric))
print(80 * '-')


lens = list(word_lens)
lens.sort()

for item in lens:
    print("{:>2}  {}  {}".format(item,
                                 word_lens[item] * "*",
                                 word_lens[item]))
print(80 * "-")


print("Pokud sečteme všechna čísla v textu tak získáme číslo:{}".format(sum(numbers)))
print(80 * "-")    