import sys
from random import randint
from interpreter import *

def main():
    if len(sys.argv) > 1:
        # Режим выполнения файла
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            line = file.read()
            code = translate(line)
            exec(code)
    else:
        while True:
            line = input('>>>')
            code = translate(line)
            exec(code)

if __name__ == "__main__":
    main()