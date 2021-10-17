i_input = int(input('Под какой процент вы хотите положить деньги: '))
s_input = int(input('Сколько вы хотите положить денег в банк: '))
t_input = int(input('На сколько лет вы хотите положить деньги в банк'))
percentes = s_input * (i_input * 0.01)
years = list(range(1, t_input))

def calc_savings(s, p, t):
    '''
    input: i - integer is float value, example: 2% is equal to 0.02
    default value: 0.02
    s - savings is integer , example: 1000 is eual to 1000 rubles
    t - time for investments in years
    default value: 1 year
    output: number (can be float, can be integer)
    '''
    for l in years:
        summ = s + p
        print(f'Год {l}. На вашем счету {summ}')

calc_savings(s_input, percentes, t_input)