   
import random
translations = {
    'drink_green': 'print',
    'dark': 'input',
    'drink': 'int',
    'store': 'str',
    'grass': 'def',
    'blue': 'if',
    'mix': 'elif',
    'red': 'else',
    'color': 'randint',
    'brew': 'lower',
    'boil': 'upper',
    'cook': 'for',
    'pour': 'while'
}
while True:
    mode = int(input('Введите режим 1 - программу в консоль; Введите режим 2 - из файла '))
    if mode == 2:
        gofile = input('Введите путь к файлу ')
        with open(gofile, 'r') as file:
            proga = file.read()
    if mode == 1:
        proga = input('Введите код ')
    if proga == 'break':
        break
    ac = False
    for i in translations.values():
        if i in proga:
            print('Замечен неверный код')
            break
        if i == 'while':
            ac = True
    if not ac:
        continue
    for i in translations.items():
        proga = proga.replace(i[0], i[1])
    exec(proga)