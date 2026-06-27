# Number Guess Analyzer
# This program takes numbers from user
# and searches for a specific number in the list


# Empty list to store numbers
numbers = []


# Taking number of elements from user
n = int(input("How many numbers do you want: "))


# Taking numbers input and adding them to list
for i in range(n):

    num = int(input(f"Enter number {i+1}: "))

    # Adding number into list
    numbers.append(num)



# Taking number to search
search = int(input("Enter the number you want to search: "))



# Checking whether number exists in list
if search in numbers:

    print("Number Found ✅")


    # Finding position of number
    # +1 converts Python indexing (0-based)
    # into normal position counting
    position = numbers.index(search) + 1

    print("Position:", position)


else:

    print("Number Not Found ❌")
