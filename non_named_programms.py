number_one = int(input('Введите первое число) '))
number_two = int(input('Введите второе число) '))
plus = number_one + number_two

if plus < 1000 :
    print(plus)
elif plus > 1000 :
    print(number_one * number_two)



# 



first_list = [1, 6, 8, 2, 4, 7]
second_list = [0]
third_list = [3, 2]

if first_list[-1] % 2 == 0:
    print(f'Последнее число {first_list[-1]} - Четное')
else :
    print(f'Последнее число {first_list[-1]} - Нечетное')

if second_list[-1] % 2 == 0:
    print(f'Последнее число {second_list[-1]} - Четное')
else :
    print(f'Последнее число {second_list[-1]} - Нечетное')
    
if third_list[-1] % 2 == 0:
    print(f'Последнее число {third_list[-1]} - Четное')
else :
    print(f'Последнее число {third_list[-1]} - Нечетное')



# 



name = input('Имя: ')
_class = input('Класс- актер, ведущий, гость: ')
number = input('Шоу- шокеры, красная комната, суфлер, меняй: ')
guest = input('Гость- с, без: ')

pers = {f'{name}': {f'{_class}': {'number': f'{number}', 'guest': f'{guest}'}}}
print(pers)


# 


numbers = (list(range(20)))
greater_five = []
greater_five = numbers[5:20]
print(greater_five) 