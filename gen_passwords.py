# программа, которая генерирует пароли и имеет три уровня надежности
import random
import time

def pass_gen():
    pass_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'q', 'w', 'e',
                 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E',
                 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
                 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '~', '!', '@',
                 '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '<',
                 '>', '?', '/', '.', ',', '№']
    
    finish_list = []
    
    print('Добро пожаловать в генератор паролей!!!')
    print('-------------------------------------------')
    time.sleep(1)
    print('Необходимо решить, какой уровень сложности будет у пароля! ')
    print('-------------------------------------------')
    time.sleep(1)
    
    
#     while True:
    password = int(input('''Введите: 1 - легкий; 2 - средний; 3 - сложный: '''))
#         if (password == 1 or password == 2 or password == 3) and type(password) == int(password):
#             break
    time.sleep(1)
    
    print('-------------------------------------------')
    print('Генерируется......')
    print('-------------------------------------------')
    time.sleep(3)
    
# теперь необходимо понять, какой генерировать пароль    
    if password == 1:
        password= 5
    elif password == 2:
        password = 7
    elif password == 3:
        password = 10
    
    for i in range(password):
        num = random.choice(pass_list)
        finish_list.append(num)
    print(f'Пароль сгенерирован - {"".join(finish_list)}')
        
        
pass_gen()