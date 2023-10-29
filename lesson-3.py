import pymysql.cursors
from pymysql.cursors import DictCursor
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
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the Excel file
    writer.save()


if __name__ == '__main__':
    connection = create_connection('localhost', 'root', 'root', 'utf8', 'Task9')
    table_name = "solution2"
    with connection.cursor() as cursor:
        while True:
            print('Выберите действие: ')
            print('1. Создать базу данных и таблицу в cursorMySQL')
            print(
                '2. Ввести необходимые данные (ID, Направление подготовки, ФИО, Номер студенческого билета, Группа) сохранить их и вывести из MySQL в виде таблицы')
            print('3. Сохранить данные из MySQL в Excel и вывести на экран в виде таблицы')
            print('4. Выход')

            choice = input("Введите номер действия: ")

            if choice == "1":
                create_table(cursor, table_name,
                             {"DOF": "VARCHAR(255)", "FIO": "VARCHAR(255)", "STUDENT_ID": "INT", "GROUP_ID": "INT"})
            elif choice == "2":
                id = input('Введите номер ID: ')
                print(id)

                direction_of_training = input('Введите направление подготовки: ')
                print(direction_of_training)

                FIO = input('Введите ФИО: ')
                print(FIO)

                Student_ID_number = input('Введите номер студенческого билета: ')
                print(Student_ID_number)

                Group1 = input('Введите группу: ')
                print(Group1)

                insert_into_table(coursor, table_name,
                                  {"ID": id, "DOF": direction_of_training, "FIO": FIO, "STUDENT_ID": Student_ID_number,
                                   "GROUP_ID": Group1})
                connection.commit()

            elif choice == "3":
                rows = select_data(cursor, table_name)
                save_to_excel(rows, "table_in_exce")
            elif choice == "4":
                break