import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def creating_a_file():
    with open("Egor-1point.txt", "w+", encoding="utf-8") as f:
        for i in range(0, 55):
            f.writelines(id_generator() + "\n")

    with open("Egor-1point.txt", "r", encoding="utf-8") as f:
        while True:
            # считываем строку
            line = f.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            print(line.strip())


def factorial (x):
    if x == 0 or x == 1:
        return 1

    return x * factorial(x - 1)


if __name__ == '__main__':
    print(factorial(100))