# пишем камень, ножницы, бумага
import random
import time

def game_kam_nozh_bum():
    random_chois = random.randint(0,2)
    if random_chois == 0:
        comp_chois = 'камень'
    elif random_chois == 1:
        comp_chois = 'ножницы'
    elif random_chois == 2:
        comp_chois = 'бумага'
    
# даем ввести пользователю значение
    while True:
        user_chois = input('Введите значение ')
        if user_chois == 'камень' or user_chois == 'ножницы' or user_chois == 'бумага':
            break
        


# теперь сравним и посмотрим, кто же выиграл эту партию    
    time.sleep(1)   
    print() 
    print('теперь можно определить победителя')
    time.sleep(1)
    print()
    if comp_chois == user_chois:
        print(f'у нас ничья, компьютер и пользователь ввели {user_chois.upper()}...')
    elif comp_chois == 'камень' and user_chois == 'ножницы':
        print(f'выиграл компьютер, у него {comp_chois.upper()}, а у пользователя {user_chois.upper()}' )
    elif comp_chois == 'ножницы' and user_chois == 'бумага':
        print(f'выиграл компьютер, у него {comp_chois.upper()}, а у пользователя {user_chois.upper()}')
    elif comp_chois == 'бумага' and user_chois == 'камень':
        print(f'выиграл компьютер, у него {comp_chois.upper()}, а у пользователя {user_chois.upper()}')
    else:
        print(f"выиграл пользователь, у него {user_chois.upper()}, а у компьютера {comp_chois.upper()}")
    print()
    time.sleep(1)
    print('игра окончена')

game_kam_nozh_bum()