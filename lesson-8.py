# Исходная матрица
matrix = [
    [1, -2, 3],
    [4, 5, 6],
    [7, 8, -9]
]

# Шаг 1: Находим все столбцы, содержащие только положительные элементы
positive_columns = []
for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    # Проверяем, все ли элементы столбца положительные
    if all(element > 0 for element in column):
        positive_columns.append(j)

# Шаг 2: Если найдены столбцы с положительными элементами, меняем местами столбец 1 и последний из них
if positive_columns:
    last_positive_column = positive_columns[-1]
    for i in range(len(matrix)):
        # Обмен местами элементов в столбцах
        matrix[i][0], matrix[i][last_positive_column] = matrix[i][last_positive_column], matrix[i][0]

# Выводим полученную матрицу
for row in matrix:
    print(row)
