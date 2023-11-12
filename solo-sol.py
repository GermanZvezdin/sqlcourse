import pymysql.cursors
from pymysql.cursors import Cursor
import os

import pandas as pd

def create_connection(host, user_name, user_pass, character, db_name):
    connection = pymysql.connect(host=host,
                                 user=user_name,
                                 password=user_pass,
                                 charset=character,
                                 db=db_name)
    return connection

def create_table(cursor, table_name, parameters):
    command = f"CREATE TABLE {table_name}(\n"

    command += "ID INT PRIMARY KEY NOT NULL, \n"

    for i in range(0, len(parameters)):  #
        param_name, param_type = list(parameters.keys())[i], list(parameters.values())[i]
        command += f"{param_name} {param_type} NOT NULL"
        if i != len(parameters) - 1:
            command += ", \n"

    command += ");"

    try:
        cursor.execute(command)
    except pymysql.Error as e:  #
        print(f"Ошибка 38 строка: {e}")


def insert_into_table(cursor, table_name, values):
    command = f"INSERT INTO {table_name} ("

    for i in range(0, len(values)):
        value_name = list(values.keys())[i]
        command += f"{value_name}"
        if i != len(values) - 1:
            command += ", "

    command += ") VALUES ("

    value_to_insert = ()

    for i in range(0, len(values)):
        value = list(values.values())[i]
        value_to_insert += (value,)

        command += f"%s"
        if i != len(values) - 1:
            command += ", "

    command += ");"
    print(command)
    print(tuple(values.values()))
    try:
        cursor.execute(command, tuple(values.values()))
    except pymysql.Error as e:
        print(f"Ошибка 57 строка: {e}")


def select_data(cursor, table_name):
    # Выбираем все данные
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    return rows

def save_to_excel(rows, excel_file_name):
    # Create a pandas DataFrame from the rows
    df = pd.DataFrame(rows)
    print(df)

    # Define the Excel writer (you can customize options if needed)
    writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')

    # Convert the DataFrame to an Excel object
    df.to_excel(writer, sheet_name='6_pr', index=False)

    # Save the Excel file
    writer.save()


def creating_a_file():
    with open("Egor-1point.txt", "w+", encoding="utf-8") as m:
        for i in range (0, 55):
            m.writelines(str("Привет!"))
            break

    with open("Egor-1point.txt", "r", encoding="utf-8") as m:
        while True:
            # считываем строку
            line = m.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            print(line.strip())

def input_fails():
    print("Все папки и файлы, находящиеся в этом проекте:", os.listdir()) #так ли нужно писать тело функции? просто я нигде, вроде, не указываю дирректорию

def rename_fail():
    try:
        os.rename("Egor-1point.txt", "Egor-2points.txt")
        print("Файл 'Egor-1point.txt' успешно переименован в 'Egor-2points.txt' ")
    except:
        print("Файла не существует")

def create_folder():
    if not os.path.isdir("Kirill-3points"):
        os.mkdir("Kirill-3points")
    print("Все папки из проекта: ", os.listdir("Kirill-3points"))

def replace_folder():
    try:
        os.replace("Egor-2points.txt", "Kirill-3points")
        print("Файл 'Egor-2points.txt' перемещен в папку 'Kirill-3points'")
    except:
        print("Папки Egor-2points.txt не существует")

def size_of_folder():
    if os.path.exists("Egor-2points.txt"):
        print("Размер файла 'Egor-2points.txt' -", os.stat("Egor-2points.txt").st_size)
    else:
        print("Файла Egor-2points.txt не существует")

def from_file_to_table(cursor, table_name):
    with open("Egor-1point.txt", "r", encoding="utf-8") as f:
        while True:
            # считываем строку
            line = f.readline()

            if not line:
                break

            insert_into_table(cursor, table_name, {"Content": line.strip()})


if __name__ == '__main__':

    connection = create_connection('localhost', 'root', 'root', 'utf8mb4', 'Q')

    table_name = "pr_6"

    with connection.cursor() as cursor:

        create_table(cursor, table_name, {"Content": "VARCHAR(255)"})

        while True:
            print("Выберите действие:")
            print("1. Создать файл с названием и расширением «Egor-1point.txt» и внести туда 55 разных строк")
            print("2. Вывести все папки и файлы, находящиеся в данном проекте")
            print("3. Переименовать файл «Egor-1point.txt» в «Egor-2points.txt» и вывести все файлы текущей директории")
            print("4. Создать папку (каталог) с названием «Kirill-3points» и вывести все папки (из проекта)")
            print("5. Переместить файл «Egor-2points.txt» в папку «Kirill-3points»")
            print("6. Вывести на экран размер файла «Egor-2points.txt»")
            print("7. Сохранить содержимое из MySQL в Excel и вывести из Excel на экран в виде таблицы")
            print("8. Выйти")

            choice = input()

            if choice == '1':
                creating_a_file()
            elif choice == '2':
                input_fails()
            elif choice == '3':
                rename_fail()
            elif choice == '4':
                create_folder()
            elif choice == '5':
                replace_folder()
            elif choice == '6':
                size_of_folder()
            elif choice == '7':
                from_file_to_table(cursor, table_name) #не понимаю, что нужно передать в sql и как это сделать
                #не понимаю, как передать в sql 55 строк, они же генерируются самостоятельно
                connection.commit()
            elif choice == '8':
                break



