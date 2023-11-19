import random

def generate_random_fio():
    # Списки с возможными именами, фамилиями и отчествами
    first_names = ['Иван', 'Александр', 'Екатерина', 'Анна', 'Дмитрий', 'Мария', 'Артем', 'Светлана']
    last_names = ['Иванов', 'Петров', 'Смирнов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлова']
    patronymics = ['Иванович', 'Петрович', 'Александрович', 'Дмитриевна', 'Алексеевна', 'Сергеевич']

    # Случайный выбор имени, фамилии и отчества
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    patronymic = random.choice(patronymics)

    # Сборка полного ФИО
    full_name = f'{first_name} {last_name} {patronymic}'

    return full_name

if __name__ == "__main__":
    data = []

    for _ in range(0, 100):
        data.append(generate_random_fio())

    for name in data:
        inp = str(name).split(' ')

        first_name = inp[0]
        last_name = inp[1]
        patronymic = inp[2]

        print(f"{last_name} {first_name[0].capitalize()}. {patronymic[0].capitalize()}.")



    inp = str(input("Введите ФИО")).split(' ')

    # 0 - first_name
    # 1 - last_name
    # 2 - patronymic