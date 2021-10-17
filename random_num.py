from random import randint

game = True
num = randint(1, 100)

file = open('txt', 'w+', encoding='utf8')
file.write('Угадай число 1-100\n')
print('Угадай число 1 - 100')

while game:
    guess = int(input('Ваше предположение'))
    if guess == num:
        print('Вы угадали верно')
        game = False
    elif guess < num:
        print(f'Ответ неверный, попробуй число больше чем {guess}')
        file.write(f'Ответ неверный, попробуй число больше чем {guess}\n')
    elif guess > num:
        print(f'Ответ неверный, пробуй число меньше чем {guess}')
        file.write(f'Ответ неверный, попробуй число меньше чем {guess}\n'50)

file.close()