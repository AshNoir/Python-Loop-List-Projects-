# Character Frequency Counter
# This program counts how many times
# each character appears in a given text


# Taking text input from user
text = input("Enter the word: ")


# Empty dictionary to store character counts
char_counts = {}


# Loop through every character in text
for char in text:


    # Checking if character already exists in dictionary
    if char in char_counts:

        # Increase its count by 1
        char_counts[char] += 1


    else:

        # If character is new,
        # add it with initial count 1
        char_counts[char] = 1



# Display character frequency
print("Character Frequency:")

print(char_counts)
