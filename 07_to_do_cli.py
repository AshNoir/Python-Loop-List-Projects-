# To Do List CLI 📝
# This program allows user to:
# 1. Add tasks
# 2. Show tasks
# 3. Delete tasks
# 4. Exit program


# Empty list to store tasks
tasks = []


# Display menu
print('--- TO DO LIST ---')
print('1. Add Task')
print('2. Show Tasks')
print('3. Delete Task')
print('4. Exit')



# Loop keeps program running until user exits
while True:


    # Taking user choice
    choice = int(input('Choose option: '))



    # Exit option
    if choice == 4:

        print('Thank you! Exiting...')
        break



    # Add task option
    elif choice == 1:


        # Taking task input
        task = input("Enter task: ")


        # Adding task into list
        tasks.append(task)


        print("Task Added ✅")




    # Show tasks option
    elif choice == 2:


        print("Your Tasks:")


        # Checking if task list is empty
        if len(tasks) == 0:

            print("No Tasks Available")


        else:

            # Displaying tasks with numbering
            for number, item in enumerate(tasks, start=1):

                print(f"{number}. {item}")




    # Delete task option
    elif choice == 3:


        # Asking which task to delete
        dlt = int(input("Which task do you want to delete? "))


        # Removing task
        # -1 because list indexing starts from 0
        tasks.pop(dlt - 1)


        print("Task Deleted ✅")




    # Handling invalid input
    else:

        print("Invalid Choice ❌")
