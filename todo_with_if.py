def get_todos(filepath='todos.txt'):
    """Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
print(help(get_todos))

def write_todos(todos, filepath='todos.txt'):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)

text = """
Here is a multy line text which is 
stored in text and the reason we can 
do this is the 3 double cotations!
"""

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action.strip("add ")

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action.strip("edit "))
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        number = int(user_action.strip("complete "))

        try:
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")
print("Bye")

