FILEPATH = 'todo output.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        files = file.readlines()
    return files


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as files:
        files.writelines(todos_arg)
