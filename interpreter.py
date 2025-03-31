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
    'pour': 'while',
    'recipe?': '=',
    'grow': 'return',
    'say': '(',
    'finish': ')',
    'do': ':'
}
def translate(proga):
    ac = False
    for i in translations.values():
        if i in proga:
            return 'error'
        if i == ':':
            ac = True
    if not ac:
        return 'error2'
    for i in translations.items():
        proga = proga.replace(i[0], i[1])
    return proga
