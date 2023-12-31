import ast


def create_example_file():
    example = [1, 2, 3, 'hello', [1, 2, 3], True, {'a': 1}, -6]

    with open("example_59_generated", 'w') as file:
        file.write(str(example))


def main():
    with open('59_example', 'r') as file:
        data = file.read()

        #дессериализация данных
        data = ast.literal_eval(data)

        number = []
        not_number = []

        for elem in data:
            if isinstance(elem, (int, float)):
                number.append(elem)
            else:
                not_number.append(elem)

        number.sort()

        result = number + not_number

        with open('59_result.txt', 'w') as output:
            output.write(str(result))

    create_example_file()


if __name__ == '__main__':
    main()