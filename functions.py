# CONSTANTS
FILEPATH = 'todos.txt'
#FILEPATH = "C:/Users/Rahul Joshi/PycharmProjects/webapp1/todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read todos list from the text file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write todos list into the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello from functions")