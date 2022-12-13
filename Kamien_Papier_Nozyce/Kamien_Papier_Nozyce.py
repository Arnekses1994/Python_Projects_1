Gracz1_wynik = 0
Gracz2_wynik = 0
opcje = ['papier','kamień','nożyce']
print ('[-- Do wybory - kamień, papier, nożyce --]')
print ('[-- Gramy do - 3 zwyciestwa --]')

def pobierz_wybor(gracz):
    while True:
        wybor_gracza = input(f'{gracz} podaj swój wybór: ')
        if wybor_gracza in opcje:
                return wybor_gracza

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == wybor_gracza2:
        print('remis')
        return 0

    wynik = {
        ('papier', 'kamień') : 1,
        ('kamień', 'nożyce') : 1,
        ('nożyce', 'papier') : 1
    }
    return wynik.get ((wybor_gracza1, wybor_gracza2), -1)
         
while Gracz1_wynik != 3 and Gracz2_wynik != 3:
    wybor_gracza1 = pobierz_wybor('Gracz 1')
    wybor_gracza2 = pobierz_wybor('Gracz 2')
    wynik = sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik == 1:
        print ('Wygrał Gracz 1')
        Gracz1_wynik += 1
    elif wynik == -1:
        print ('Wygrał Gracz 2')
        Gracz2_wynik += 1

if Gracz1_wynik > Gracz2_wynik:
    print('Cała grę wygrał Gracz 1')
else:
    print('Cała grę wygrał Gracz 2')
    