# пишем камень, ножницы, бумага
import random
import time

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
time.sleep(1.5)   
print() 
print('теперь можно определить победителя')
time.sleep(1.5)
print()
if comp_chois == user_chois:
    print(f'у нас ничья, компьютер и пользователь ввели {user_chois}...')
elif comp_chois == 'камень' and user_chois == 'ножницы':
    print(f'выиграл компьютер, у него {comp_chois}, а у пользователя {user_chois}' )
elif comp_chois == 'ножницы' and user_chois == 'бумага':
    print(f'выиграл компьютер, у него {comp_chois}, а у пользователя {user_chois}')
elif comp_chois == 'бумага' and user_chois == 'камень':
    print(f'выиграл компьютер, у него {comp_chois}, а у пользователя {user_chois}')
else:
    print("выиграл пользователь")
print()
time.sleep(1.5)
print('игра окончена')
