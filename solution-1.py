import pymysql


# Функция для создания базы данных и таблицы MySQL
def create_database_and_table():
    conn = pymysql.connect(host='localhost', user='username', password='password')
    cursor = conn.cursor()

    # Создаем базу данных
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
    cursor.execute("USE mydatabase")

    # Создаем таблицу
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS strings (id INT AUTO_INCREMENT PRIMARY KEY, original_string VARCHAR(255), substring VARCHAR(255))")

    conn.commit()
    conn.close()


# Функция для вставки данных в таблицу
def insert_data(original_string, substring):
    conn = pymysql.connect(host='localhost', user='username', password='password', database='mydatabase')
    cursor = conn.cursor()

    # Вставляем строку и подстроку
    cursor.execute("INSERT INTO strings (original_string, substring) VALUES (%s, %s)", (original_string, substring))

    conn.commit()
    conn.close()


# Функция для выборки данных из таблицы
def select_data():
    conn = pymysql.connect(host='localhost', user='username', password='password', database='mydatabase')
    cursor = conn.cursor()

    # Выбираем все данные
    cursor.execute("SELECT * FROM strings")
    rows = cursor.fetchall()

    conn.close()

    return rows


# Функция для выполнения операций над строкой
def perform_operations(original_string, substring, index):
    # Найти подстроку в строке
    if original_string.find(substring) != -1:
        print("Подстрока найдена в строке.")
    else:
        print("Подстрока не найдена в строке.")

    # Длина строки и подстроки
    print(f"Длина строки: {len(original_string)}")
    print(f"Длина подстроки: {len(substring)}")

    # Подстрока, продублированная
    duplicated_substring = substring * 2
    print(f"Продублированная подстрока: {duplicated_substring}")

    # Элемент с задаваемым индексом
    if 0 <= index < len(original_string):
        print(f"Элемент с индексом {index}: {original_string[index]}")
    else:
        print(f"Индекс {index} вне диапазона.")

    # Срез строки 0:8
    slice_result = original_string[0:8]
    print(f"Срез строки 0:8: {slice_result}")

    # Преобразование строки в верхний и нижний регистр
    upper_case_string = original_string.upper()
    lower_case_string = original_string.lower()
    print(f"Строка в верхнем регистре: {upper_case_string}")
    print(f"Строка в нижнем регистре: {lower_case_string}")

if __name__ == "__main__":
    create_database_and_table()

    while True:
        print("Выберите действие:")
        print("1. Ввести строку и подстроку")
        print("2. Выполнить операции над строкой")
        print("3. Сохранить данные в MySQL и вывести на экран")
        print("4. Завершить программу")

        choice = input("Введите номер действия: ")

        if choice == '1':
            original_string = input("Введите первую строку (от 30 символов и больше): ")
            substring = input("Введите вторую строку (от 15 символов): ")
        elif choice == '2':
            index = int(input("Введите индекс элемента: "))
            perform_operations(original_string, substring, index)
        elif choice == '3':
            insert_data(original_string, substring)
            data_from_mysql = select_data()
            for row in data_from_mysql:
                print(f"ID: {row[0]}, Original String: {row[1]}, Substring: {row[2]}")
        elif choice == '4':
            break
