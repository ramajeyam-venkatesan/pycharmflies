while True:
     user_action = input("type add, show, complete, exit:")
     user_action = user_action.strip()

     match user_action:
         case 'add':
             todo = input("enter a todo: ") + "\n"

             file = open("todos.txt", 'r')
             todos = file.readline()
             file.close()

             todos.append(todo)
             file = open("todos.txt", 'w')
             file.writelines(todos)
             file.close()

         case 'show':
             file = open("todos.txt", 'r')
             todos = file.readlines()
             file.close()
             for index, item in enumerate(todos):
                 row = f"{index + 1}-{item}"
                 print(row)
         case 'edit' :
             number = int(input("number to edit: "))
             numbers=number-1
             new_todos = input("enter a new todo")
             todos[number] = new_todos
         case 'complete':
             number = int(input("number to complete: "))
             todo.pop(number+1)
         case 'exit':
             break
print("bye")
