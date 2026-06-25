# This program takes multiple numbers from user
# and analyzes:
# 1. Count of even numbers
# 2. Count of odd numbers
# 3. Total sum of numbers
# 4. Maximum number


# Empty list to store user numbers
numbers = []

# Taking how many numbers user wants to enter
n = int(input("How many numbers do you want: "))


# Loop runs n times and takes input
for i in range(n):
    num = int(input("Enter the number: "))
    
    # Adding each number into list
    numbers.append(num)



# Variables to store results
even = 0
odd = 0
total = 0

# Assuming first number is maximum initially
maximum = numbers[0]


# Loop through every number in list
for num in numbers:

    # Checking even or odd
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1


    # Adding every number to total
    total += num


    # Checking maximum number
    if maximum < num:
        maximum = num



# Display final results
print("Even:", even)
print("Odd:", odd)
print("Total:", total)
print("Maximum:", maximum)
