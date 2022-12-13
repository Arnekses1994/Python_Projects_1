user_choice = -1
tasks = []

def show_tasks(tasks_index=None):
    import os
    while os.path.getsize('tasks.txt') == 0:
            print ("----------------")
            print("Indeks jest pusty")
            break

    task_index = 0
    for task in tasks:
        print ("----------------")
        print("►  " + task + " [" + str(task_index) + "]" )
        task_index += 1

def add_task():
    print ("----------------")
    task = input("Wpisz treść zadania: ")
     
    tasks.append(task)
    print ("----------------")
    print("Dodano zadanie! ")

    file = open("tasks.txt","w")
    for task in tasks:
        file.write(task+"\n")
    file.close()

def delate_task():
    try:
        print ("----------------")
        task_index = int(input("Podaj index zadania do usunięcia "))

        if task_index < 0 or task_index > len(tasks) -1:
            print ("----------------")
            print ("Zadanie o tym indeksie nie istnieje")
            return

        tasks.pop (task_index)
        print ("----------------")
        print ("Usunięto zadanie " )

        file = open("tasks.txt","w")
        for task in tasks:
            file.write(task+"\n")
        file.close()

    except ValueError:
        print("----------------")
        print ("Podajemy tylko liczby !")

def delete_all_tasks():

    tasks.clear()
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

    print ("----------------")
    print("Usunięto wszystko ")

def load_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()

while user_choice != 5:
    try:

        print ("----------------")
        print ("1. Pokaż zadadania")
        print ("2. Dodaj zadanie")
        print ("3. Usuń zadanie")
        print ("4. Usuń wszystko")
        print ("5. Wyjdz")
        print("----------------")

        user_choice = int(input("Wybierz liczbę: "))

        if user_choice == 1:
            show_tasks()

        if user_choice == 2:
            add_task()

        if user_choice == 3:
            delate_task()

        if user_choice == 4:
            delete_all_tasks()

        if user_choice == 5:
            print("----------------")
            print("- Koniec Kalendarza -")
            break

        if user_choice > 5 or user_choice < (-1) or user_choice == -1 or user_choice == 0:
            print ("----------------")
            print ("Podajemy tylko index !")

    except ValueError:
        print ("----------------")
        print ("Podajemy tylko liczby !")

 #  █  Informacja o podwójnej informacji o wpisaniu złych danych ( Dublowanie sie komunikatu )
 #  █  Informacja o wpisaniu stringu do indexu
 #  █  Informacja o wpisaniu złych danych do indexu ( liczby wieksze i mnieszej )
 #  █  Informacja o pustej liście ( Wczytywanie z pliku txt )
 #  █  Usuwanie naraz całej listy przez jedna opcje
 #  █  Automatyczny zapis wpisu do pliku
 #  █  Bład ponownego wczytywania zadań mimo usuniecia
 #  █  Usprawnienia w kwesti wizualnej

 #  ►  Kategoria Zadań ( Stworzyć liste - Dom / Praca / Sport )
 #  ►