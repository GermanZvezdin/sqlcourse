import os

if __name__ == '__main__':

    # Specify the path to your project folder
    project_folder = '.'

    # '.' - current folder
    # '..' - parent folder

    # your current path: C:\project\
    # '.' = C:\project\
    # '..' = C:\

    # '.':
    # Книги/Гарри Поттер/ - папка в которой мы находимся - '.'
    # - Кубок Огня  - файл
    # - Дары смерти часть 1 - файл
    # '..' - родительский каталог или папка в которой лежит наша папка:
    # - Гарри Поттер - папка

    # List all files and directories in the project folder
    # обход файловой системы
    # обход текущей директории
    for root, dirs, files in os.walk(project_folder):
        for file in files:
            print(os.path.join(root, file))
        for directory in dirs:
            print(os.path.join(root, directory))

    # Specify the directory path you want to create
    directory_to_create = './name-of-folder'

    if not os.path.exists(directory_to_create):
        # If it doesn't exist, create the directory
        os.makedirs(directory_to_create)
        print(f"Directory '{directory_to_create}' created successfully.")
    else:
        print(f"Directory '{directory_to_create}' already exists.")

    file_path = './name-of-file'
    with open(file_path, 'w') as new_file:
        new_file.write("This is the content of the new file.")

        # <...>
        new_file.close()






