inp_percent = int(input('Под какой процент вы кладете деньги? '))
inp_money = int(input('Сколько вы хотите положить денег в банк? '))
inp_years = int(input('На сколько лет вы хотите положить деньги в банк? '))
percentes = inp_money * (inp_percent * 0.01)
years = list(range(inp_years))
print(years)

for p in years:
    print(f'Год {p + 1}. На вашем счету {inp_money + int(percentes)}')
    inp_money += int(percentes)
    
