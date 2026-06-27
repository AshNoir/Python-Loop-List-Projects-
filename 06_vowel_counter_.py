# Vowel Counter 🔤
# This program counts the frequency of each vowel
# in a given text


# Taking input from user
text = input("Enter a word: ")


# Converting text into lowercase
# so that A and a are treated the same
text = text.lower()


# Storing all vowels
vowels = "aeiou"


# Empty dictionary to store vowel counts
vowel_diary = {}



# Loop through each vowel
for v in vowels:

    # Counting how many times current vowel appears
    count = text.count(v)


    # Storing vowel and its count in dictionary
    vowel_diary[v] = count



# Displaying vowel frequency
for v, count in vowel_diary.items():

    print(f"{v} - {count}")
