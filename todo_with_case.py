while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'show':
            # file = open("todos.txt", 'r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            # file = open("todos.txt", 'r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # file = open("todos.txt", 'w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'complete':
            number = int(input("Number of todo to complete: "))
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break
print("Bye")

