import pymysql.cursors
from pymysql.cursors import DictCursor


def create_connection(host, user_name, user_pass, character, db_name):
    connection = pymysql.connect(host=host,
                                 user=user_name,
                                 password=user_pass,
                                 charset=character,
                                 db=db_name)
    return connection


def create_table(cursor, table_name, parameters):
    command = f"CREATE TABLE {table_name}(\n"

    command += "ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL, \n"

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


def get_last_inserted_id(cursor, table_name):
    try:
        query = f"SELECT LAST_INSERT_ID() FROM {table_name};"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            last_inserted_id = result[0]
            return last_inserted_id
        else:
            print(f"{table_name} - пустая")
            return 0
    except pymysql.Error as e:
        print(f"Ошибка: {e}")
        return 0


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
    try:
        cursor.execute(command, tuple(values.values()))
    except pymysql.Error as e:
        print(f"Ошибка 57 строка: {e}")


if __name__ == '__main__':
    connection = create_connection('localhost', 'root', 'root', 'utf8', 'Q')

    # Если таблицы нет то 1 раз нужно выполнить функцию
    with connection.cursor() as cursor:
        print('h')
        # С отступом мы работаем с cursor
        # Иначе это будет не тот cursor и поведение не определено

        # Если таблицы в выбранной базе данных нет то ее нужно создать:
        create_table(cursor, "Book6", {"NAME": "VARCHAR(255)", "AUTHOR": "VARCHAR(255)"})

        insert_into_table(cursor, "book6", {"NAME": "y", "AUTHOR": "k"})
    connection.commit()

