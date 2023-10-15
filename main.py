import random
import psycopg2



def insert_data(name, age, height, weight):
    request = f"""
            INSERT INTO Class (Name, Age, Height, Weight)
            VALUES (
                    ({name}, {age}, {height}, {weight})
                    );
            """
    return request

if __name__ == '__main__':
    connection = psycopg2.connect(dbname='Test',
                                  user='postgres',
                                  password='gera',
                                  host='localhost',
                                  port='5432'
                                 )

    cur = connection.cursor()
    quary = """
        CREATE TABLE class (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL, 
            age  INT NOT NULL, 
            height FLOAT NOT NULL,
            weight FLOAT NOT NULL   
        )
    """

    #cur.execute(quary)

    insert_data_sql = "INSERT INTO class (ID, Name, Age, Height, Weight) VALUES (%s, %s, %s, %s, %s)"
    data = (0, "John", 17, 22.2, 22.2)

    cur.execute(insert_data_sql, data)

    connection.commit()

    cur.close()
    connection.close()
