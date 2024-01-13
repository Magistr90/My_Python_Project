# создаем калькулятор
import time

def calculator():
    while True:
        num1 = float(input('Введите первое число: '))
        if num1 != type(float) and num1 != type(int):
            continue
        time.sleep(1)
        operator = input('Введите оператор, который хотите использовать (+, -, /, *): ')
        if operator not in ['+', '-', '/', '*']:
            operator = input('Введите предложенный оператор: ')
        else:
            break
    time.sleep(1)
    num2 = float(input('Введите второе число: '))
    time.sleep(1)
# теперь считаем, что у нас получается

    if operator == '+':
        print(f'Это равно: {num1 + num2}')
    elif operator == '-':
        print(f'Это равно: {num1 - num2}')
    elif operator == '/':
        print(f'Это равно: {num1 / num2}')
    elif operator == '*':
        print(f'Это равно: {num1 * num2}')
    else:
        print('Invalid operator')
    time.sleep(1)
    print('Мы посчитали, что вы хотели, если что возвращайтесь, всегда рады!!!')
    
calculator()
    