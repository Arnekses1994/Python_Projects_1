import sys
import random
import string

password = []
characters_left = -1

def update_character_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziału", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print ("Pozostało znaków", characters_left)

password_legth = int(input("Jak długie ma byc hasło? "))

if password_legth < 5:
    print ("Hasło musi mieć minimum 5 znaków - Spróbuj jeszcze raz")
    sys.exit(0)
else:
    characters_left = password_legth

lowercase_letters = int(input("Ile małych liter ma mieć hasło: "))

update_character_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło: "))

update_character_left(uppercase_letters)

special_characters = int(input("Ile specialnych znaków ma mieć hasło: "))

update_character_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło: "))

update_character_left(digits)

if characters_left > 0:
    print ("--------")
    print ("Nie wszystkie znaki zostały wykorzystane hasło zostanie uzupełnione małymi literami")
    lowercase_letters += characters_left

print ()
print ("Długość hasła", password_legth)
print ("Małe litery", lowercase_letters)
print ("Duże litery", uppercase_letters)
print ("Znaki specialne", special_characters)
print ("Cyfry", digits)

for _ in range (password_legth):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.uppercase_letters))
        lowercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1


