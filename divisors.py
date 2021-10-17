number = int(input('Введите положительное число: '));

get_enter = []

for n in range(number, 0, -1):
    if number % n == 0:
        get_enter.append(n)

print(get_enter)
