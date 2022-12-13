pogoda = int(input('Podaj temperature od -30 do +30: '))

if pogoda <= 0 and pogoda >= 10:
    print ('Jesiennie')
if pogoda <= 20 and pogoda >= 11:
    print ('Lato')
if pogoda <= 30 and pogoda >= 21:
    print ('Upał')
if pogoda >= 31:
    print ('Za duży wynik !')