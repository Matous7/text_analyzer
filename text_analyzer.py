'''
author: Matouš Kopáček
email: matouskopacek@gmail.com
discord: matousk_84638
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

line = 40 * "-"

# Ověření správných zadaných údajů.

udaje = {
    "bob" : "123",
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
    }

jmeno = input("Enter username: ")
heslo = input("Enter password: ")

if jmeno in udaje and heslo == udaje[jmeno]:
    print(line)
    print(f"Welcome to the app, {jmeno.title()}.\nWe have {len(TEXTS)} texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    quit()

print(line)

# Ověření, jestli uživatel zadal čísla od 1 do 3 a ošetření situace, když uživatel nezadá int.
# V případě, že by v proměnné TEXTS bylo více textů, tato situace je ošetřena pomocí len(TEXTS)

choose_text = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if choose_text.isnumeric():
    choose_text = int(choose_text)
    if choose_text >= 1 and choose_text <= len(TEXTS):
        pass
    else:
        print("This number is out of range. Programme will be closed...")
        quit()
else:
    print("Invalid sign. Programme will be closed...")
    quit()

print(line)

# Hodnota získaná od uživatele a odečtena - 1, aby seděla čísla 123 na indexování od 0.

chosen_text = TEXTS[choose_text-1]
chosen_text = chosen_text.split()

title_words_sum = 0
uppercase_words_sum = 0
lowercase_words_sum = 0
numbers_sum = 0
numbers_count_sum = 0
words_sum = len(chosen_text)
chosen_text_vysledek = []

# Cyklus ve kterém je každé slovo nejdřívě očištěno o nepotřebné znaky.
# Dále se hodnoty přičítají do proměnných výše s počáteční nulovou hodnotou.
# Všechna slova se také ukládají do proměnné chosen_text_vysledek, s kterou pak pracuji pro výpočet výskytu slov.

for slovo in chosen_text:
    slovo = slovo.strip(".,?!_-")
    chosen_text_vysledek.append(slovo.lower())
    if slovo.istitle():
        title_words_sum += 1
    elif slovo.isupper():
        uppercase_words_sum += 1
    elif slovo.islower():
        lowercase_words_sum += 1
    elif slovo.isnumeric():
        numbers_sum += 1
        slovo = int(slovo)
        numbers_count_sum += slovo
    
# Výpis výsledků f stringem

print(f"There are {words_sum} words in the selected text.")
print(f"There are {title_words_sum} titlecase words.")
print(f"There are {uppercase_words_sum} uppercase words.")
print(f"There are {lowercase_words_sum} lowercase words.")
print(f"There are {numbers_sum} numeric strings.")
print(f"The sum of all the numbers {numbers_count_sum}")


# Tento cyklus počítá počet znaků v každém slově a dále výskyt slov podle počtu znaků.
# Tyto výsledky ukládá do slovnik_vysledek, klíč -> počet znaků... hodnota -> výskyt

slovnik_vysledek = {}

for slovo in chosen_text_vysledek:
    delka_slova = len(slovo)
    if delka_slova not in slovnik_vysledek:
        slovnik_vysledek[delka_slova] = 1
    else:
        slovnik_vysledek[delka_slova] += 1


# Seřazení slovníku pomocí sorted
slovnik_sorted = dict(sorted(slovnik_vysledek.items()))

# Hlavička grafu
print(line)
print(f"{'LEN':<3}|{'OCCURRENCES':^17}|NR.")
print(line)

# Vytvoření grafu pomocí cyklu.
for delka, pocet in slovnik_sorted.items():
    graf_radek = f"{delka:>3}|{'*' * pocet:<17}|{pocet}"
    print(graf_radek)

print(line)



