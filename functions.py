def get_todos(filepath):
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
        return todos
    except FileNotFoundError:
        return []


def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

