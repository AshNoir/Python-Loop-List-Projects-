# Student Marks Analyzer
# This program takes marks of multiple subjects
# and calculates total, average, highest, lowest
# and counts passed/failed subjects


# Empty list to store marks
subs = []


# Taking number of subjects from user
sub = int(input("How many subjects: "))


# Taking marks input and storing in list
for i in range(1, sub + 1):
    
    mark = int(input(f"Enter the marks of subject {i}: "))
    
    # Adding marks into list
    subs.append(mark)



# Calculate total marks
total = sum(subs)


# Calculate average marks
average = total / len(subs)



# Assume first mark is highest and lowest initially
highest = subs[0]
lowest = subs[0]


# Checking highest and lowest marks
for mark in subs:

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark



# Variables for pass/fail count
passed = 0
failed = 0


# Checking pass/fail subjects
# Passing criteria = 33 marks
for mark in subs:

    if mark >= 33:
        passed += 1

    else:
        failed += 1



# Display result
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Passed Subjects: {passed}")
print(f"Failed Subjects: {failed}")
