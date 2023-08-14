FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# when we need some commands to be executed from the functions module
# then write it as if conditional block. Otherwise when the import is used in main code file
# these commands will be executed first. To avoid that use the following lines
# __name__ is a built-in variable which contains a string __main__
# basically tells us what happens when a code blcok is run directly or indirectly (using import)


if __name__ == "__main__":
    print('hello')
