# tache 2
def solution_2():
    example_input = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]
    output = ''
    i = 0
    n = len(example_input)
    for word in example_input:
        for symbol in word:
            output += symbol
        if i != n - 1:
            output += ','
        i += 1
    print(output)

# tache 14
def solution_14():
    example_input = [(1,3,4), (2,1), (6,), (2,2,2,1)]
    res = [tup if len(tup) % 2 != 0 else tup[:len(tup)-1:]  for tup in example_input ]

    print(res)


# tache 16

# one ordered list | liste chaînée
# root -> next -> next -> next
#
class Node:
    def __init__(self, val):
        self.next: Node = None
        self.value = val

    def remove(self, key):
        root = self
        itr = self
        prev = itr
        while itr != None:
            if key == itr.value:
                if prev == itr:
                    root = root.next
                else:
                    prev.next = itr.next
            prev = itr
            itr = itr.next
        return root



def solution_16():
    example_input = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
    example_input = example_input.lower()
    root = Node(example_input[0])
    itr = root


    for val in example_input[1:]:
        itr.next = Node(val)
        itr = itr.next

    itr = root
    voyelle = ['a', 'e', 'i', 'o', 'u', 'y']

    while itr != None:
        if itr.value in voyelle:
            root = root.remove(itr.value)
        itr = itr.next

    itr = root
    while itr != None:
        print(itr.value, end='')
        itr = itr.next


#tache 18
def par_val(**arg):
    names_list = []
    for name in arg.keys():
        if len(str(arg[name]).split(' ')) > 1:
            names_list.append(name)
    return names_list
def solution_18():
    names = par_val(pp='abba war', fan='oneword', zr='a x')
    print(names)


# tache 20
def psort(**arg):
    values = []
    for name in arg.keys():
        values.append(int(arg[name]))
    values.sort(reverse=True)

    return values

def solution_20():
    sorted = psort(c=21, a=22, ac=17, b=16)
    print(sorted)

# tache 22
def solution_22():
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9 , 10, 11, 12],
              [13, 14, 15, 16]]
    N = 4
    M = 4

    for i in range(0, N):
        for j in range(0, M):
            print(matrix[i][j], end=' ')
        print()

    for i in range(0, int(N / 4) + 1):
        for j in range(0, int(M / 4) + 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i + int(N / 4) + 1][j + int(M / 4) + 1]
            matrix[i + int(N / 4) + 1][j + int(M / 4) + 1] = tmp

    print('--------res--------')
    for i in range(0, N):
        for j in range(0, M):
            print(matrix[i][j], end=' ')
        print()


# tache 26

def solution_26():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    N = 4
    M = 4

    for i in range(0, N):
        for j in range(0, M):
            print(matrix[i][j], end=' ')
        print()

    max = matrix[0][0]
    colum_to_remove = 0

    for i in range(0, N):
        for j in range(0, M):
            if matrix[i][j] > max:
                max = matrix[i][j]
                colum_to_remove = j
    for i in range(0, N):
        del matrix[i][colum_to_remove]

    print('--------res--------')
    for i in range(0, N):
        for j in range(0, M-1):
            print(matrix[i][j], end=' ')
        print()

# tache 27
def solution_27():
    example_input = 'Программа'

    first_part = ''
    last_part = ''

    for i in range(0, len(example_input)):
        if (i + 1) % 2 == 0:
            first_part += example_input[i]
        else:
            last_part += example_input[i]
    res = first_part + last_part[::-1]

    print(res)

# tache 30
def fact(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
def tailor_series_sin(n, x):
    v = ((((-1) ** (n + 1)) * (x ** (2 * n - 1)))) / (fact(2 * n - 1))
    return v
def solution_30():
    x = 3.14 / 2
    r = 0

    for i in range(1, 5):
        r += tailor_series_sin(i, x)
    print(r)


# tache 31
import math
def solution_31():
    values = [x/10 * 3.14 for x in range(-10, 11)]
    y1 = []
    y2 = []

    for x in values:
        y1.append(2 * math.sin(x))
        y2.append(math.cos(2 * x))

    for i in range(0, len(values)):
        print(values[i], y1[i])
    print('-----------------')
    for i in range(0, len(values)):
        print(values[i], y2[i])


# tache 33
from datetime import datetime
def solution_33():
    data = '28-11-2021'
    date_format = '%d-%m-%Y'
    data = datetime.strptime(data, date_format)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    print(weekdays[data.weekday()])

# tache 37
import pandas as pd

def find_by_name(*arg):
    example_data = pd.read_csv('tache-37.csv')
    res = []

    for person in example_data.values:
        for name in arg:
            if person[1] == str(name):
                res.append(list(person))

    print(res)

def solution_37():
    find_by_name('Jane', 'Michael', 'Robert')

# tache 41

def solution_41():
    matrix = [[1, 2], [3, 4]]
    trace = 0
    try:
        N = len(matrix)
        for i in range(0, N):
            if len(matrix[i]) != N:
                raise ValueError('Matrix must be square')
        for i in range(N):
            trace += matrix[i][i]
        print(trace)
    except:
        print('Matrix must be square')

# tache 44
import inspect
def func(inner_func):
    func_signature = inspect.signature(inner_func)
    params = func_signature.parameters

    print(f"Имя функции: {inner_func.__name__}")

    for param_name, param_obj in params.items():
        param_type = param_obj.annotation
        if param_type == inspect._empty:
            param_type = "не указан"

        print(f"Параметр: {param_name}, Тип: {param_type}")

# demonstration
def subfunc(pos_param: int, key_param: float):
    pass
def solution_44():
    func(subfunc)

#tache 46
def cyclic_shift(input_str, shift_count):
    words = input_str.split()

    num_words = len(words)

    shift_count = shift_count % num_words

    shifted_words = words[shift_count:] + words[:shift_count]

    shifted_str = ' '.join(shifted_words)

    return shifted_str
def solution_46():
    example_input = "один два три четыре пять шесть семь"
    res = cyclic_shift(example_input, 3)
    print(res)

# tache 48
def solution_48():
    listlist = [[1, 2, 3], ['a', 'b'], [30, 40, 50, 60]]

    result_list = []
    remaining_elements = []

    while any(list_ for list_ in listlist):
        for lst in listlist:
            if lst:
                result_list.append(lst.pop(0))
            else:
                remaining_elements.extend(lst)

    print(result_list)

# tache 53

def solution_53():
    phones_list = [
        {'name': 'Ivan', 'city': 'Moscow', 'phones': ['232-19-55', '+7 (916) 230-00-75']},
        {'name': 'Anna', 'city': 'Samara', 'phones': ['200-11-15']},
        {'name': 'Anna', 'city': 'Vologda', 'phones': ['+7 (931) 711-00-75']},
        {'name': 'Nikolay', 'city': 'Moscow', 'phones': ['+7 (916) 778-71-05', '331-66-11', '783-33-85']},
        {'name': 'Ivan', 'city': 'Moscow', 'phones': ['+7 (916) 205-41-05', '232-19-55']},
        {'name': 'Anna', 'city': 'Samara', 'phones': ['+7 (916) 105-13-56']}
    ]

    result_dict = {}

    for contact in phones_list:
        city = contact['city']
        phones_dict = {}

        for phone in contact['phones']:
            phones_dict[phone] = contact['name']

        if city in result_dict:
            result_dict[city].update(phones_dict)
        else:
            result_dict[city] = phones_dict

    print(result_dict)

#tache 56

def calc_op(s, oper_d):
    # Разбиваем строку на операнды и оператор
    parts = s.split()

    # Получаем операнды и оператор
    operand1 = int(parts[0])
    operator = parts[1]
    operand2 = int(parts[2])

    # Проверяем, есть ли такой оператор в словаре
    if operator in oper_d:
        # Вызываем соответствующую функцию из словаря и возвращаем результат
        result = oper_d[operator](operand1, operand2)
        return result
    else:
        return "Неподдерживаемая операция"

def solution_56():
    result = calc_op('2 s 10', {'s': lambda x, y: x ** y})
    print(result)
# tache 57
import random

def generate_matrix(rows, cols, min_value, max_value):
    """Генерация матрицы случайных положительных целых чисел."""
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

def calculate_average_and_count_evens(matrix):
    """Подсчет среднего арифметического и количества четных элементов."""
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной!")

    total_sum = 0
    evens_count = 0

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            total_sum += matrix[i][j]
            if matrix[i][j] % 2 == 0:
                evens_count += 1

    average = total_sum / (len(matrix) * (len(matrix) - 1) / 2)  # Среднее арифметическое

    return average, evens_count

def solution_57():
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        min_value = int(input("Введите минимальное значение: "))
        max_value = int(input("Введите максимальное значение: "))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целые числа.")
        exit()

    matrix = generate_matrix(rows, cols, min_value, max_value)
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
    try:
        average, evens_count = calculate_average_and_count_evens(matrix)
        print(f"Среднее арифметическое над главной диагональю: {average}")
        print(f"Количество четных элементов под главной диагональю: {evens_count}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    solution_57()