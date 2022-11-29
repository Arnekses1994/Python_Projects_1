import datetime
import calendar

def translate_to_polish(day_name):
    match day_name:
        case 'Monday':
            return 'Wtorek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Środa'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'

def translate_to_polish_old_way(day_name):
    englisch_to_polisch_day_name = {
        'Monday' : 'Poniedziałek',
        'Tuesday' : 'Wtorek',
        'Wednesday' : 'Środa',
        'Thursday' : 'Czwartek',
        'Friday' : 'Piątek',
        'Saturday' : 'Sobota',
        'Sunday' : 'Niedziela',
    }

    return englisch_to_polisch_day_name[day_name]

data_of_birth = input("Podaj date urodzin DD-MM-RRRR: ")
day, month, year = data_of_birth.split("-")

# Sposób podzielenia wpisywanych danych metoda split

data_of_birth = datetime.datetime(int(year), int(month), int(day))

# Importuje poteżna logike z funkcji "datetime "

print ("Dzien tygodnia")
print(data_of_birth.weekday())


# Pokazuje który to dzien tygodnia za pomoca funkcji "weekday"

day_name = calendar.day_name[data_of_birth.weekday()]
print (translate_to_polish_old_way(day_name))