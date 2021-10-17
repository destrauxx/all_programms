class Animal():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def sleep(self):
        print(f'{self.name} Zzz..')

    def eat(self):
        print(f'{self.name} Om nom nom...')

class Cat(Animal):
    def say(self):
        print(f'MYAU BLIN!')
class Dog(Animal):
    def say(self):
        print(f'GAV BLIN!')

fluffy = Dog('АНТОХА', 'красный')
smokey = Cat('АРСОХА', 'голубой')

fluffy.sleep()
fluffy.eat()
smokey.sleep()
smokey.eat()
fluffy.say()
smokey.say()