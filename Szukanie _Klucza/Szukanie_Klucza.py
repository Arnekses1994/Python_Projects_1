from random import randint

# Funkcja do losowania liczby

GAME_WIDTH = 10
GAME_HIGH = 10

# Tworzenie zmiennych GAME 

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HIGH)

player_X = 0
player_y = 0

# Umieszczenie gracza

player_found_key = False

while not player_found_key:
    print ()
    print ("Możesz udać sie w kierunkach [W.A.S.D]: ")

    move = input ("Dokąd idzesz? ")
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HIGH:
                print ('Auć ! Sciana')
                player_y = GAME_HIGH

        case 's':
            player_y -= 1
            if player_y < 0:
                print ('Auć ! Sciana')
                player_y = 0

        case 'a':
            player_X -= 1:
                if player_y > GAME_WIDTH:
                print ('Auć ! Sciana')
                player_y = GAME_WIDTH

        case 'd':
            player_X += 1
              if player_y > 0:
                print ('Auć ! Sciana')
                player_y = 0


        case 'q':
            print ('Koniec gry')
            quit()
        case ' ':
            print ('Nie wiem dokąd idzesz ') 
            continue       
            
    print(player_X,player_y)                  
