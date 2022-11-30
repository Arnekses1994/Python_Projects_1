import sys

no_of_tries = 5
word = "Kamila"
used_letters = []

user_word = []

def find_indexex(word, letter):

    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

# Funkcja enumerate indelsuje każdą litere jaka osoby indeks
# Np K A M I L
#    1 2 3 4 5

    return indexes

def show_state_of_game():
    print ()
    print (user_word)
    print ("Pozostało prób:", no_of_tries)
    print ("Użyte litery: ", used_letters )
    print ()

for _ in word :
    user_word.append("_")

# W miejscu gdzie jest "for _ in word" w miejscu _ powinna być funkcja letter
# ale zamiast tego wpisujemy _ bo jest nie używana - Ta funckja pozwala pokzac całe showoff

while True:
    letter: str = input("Podaj litere:  ")
    used_letters.append(letter)

    found_indexex = find_indexex(word, letter)
    if len(found_indexex) == 0:
        print ("Nie ma takiej litery !")
        no_of_tries -= 1

        if no_of_tries == 0:
            print ("Koniec gry:")
            sys.exit(0)
    else:
        index: int
        for index in found_indexex:
            user_word [index] = letter

        if "".join(user_word) == word:
            print ("-------------")
            print ("!! Brawo to jest to słowo !!")
            sys.exit(0)

    show_state_of_game()

#  - Praca nad projektem -
#  ► Czy nie jest wpisywana cyfra
#  ► Czy nie jest wpisywana jeszcze raz ta sama litera
#  ► Czy nie jest wpissywana wiecej niz jedna litera
#  ► Losowanie kolejnego słowa
#  ► Skorzystać z zewnetrznego zródła losowego
#  ► Restart gry po zakonczeniu
#  ► Ile szans pownieni miec użytkownik - Spytanie na początku
