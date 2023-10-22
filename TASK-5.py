#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to calculate the total number of Vowels and Count of each individual vowel A, E, I, O, U in the string "Guvi Geeks Network Private Limited"?

# Input string
input_string = "Guvi Geeks Network Private Limited"

# Convert the input string to lowercase to handle both uppercase and lowercase vowels
input_string = input_string.lower()

# Initialize counters for each vowel
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate through each character in the string
for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

# Calculate the total number of vowels
total_vowels = count_a + count_e + count_i + count_o + count_u

# Print the results
print("Total number of vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)


# In[2]:


# 2. Create a Pyramid of Numbers from 1 to 20 using For loop?

# Set the maximum number for the pyramid
max_num = 20

# Iterate through the rows
for i in range(1, max_num+1):
    # Print spaces to center-align the pyramid
    print(" " * (max_num - i), end="")

    # Print numbers in increasing order
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print numbers in decreasing order
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    # Move to the next line for the next row
    print()


# In[3]:


# 3. Write a function that takes a string and returns a new string with all the vowels removed.

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels, both lowercase and uppercase
    result_string = ""  # Initialize an empty string to store the result

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel and add it to the result_string
        if char not in vowels:
            result_string += char

    return result_string  # Return the string with all the vowels removed


input_string = "Guvi Geeks Network Private Limited"
result_string = remove_vowels(input_string)
print(result_string)


# In[4]:


# 4. Write a function that takes a string and returns the number of unique characters in it.

def count_unique_characters(input_string):
    unique_chars = set(input_string)  # Convert the string to a set to get unique characters
    return len(unique_chars)  # Return the number of unique characters

input_string = "Guvi Geeks Network Private Limited"
unique_count = count_unique_characters(input_string)
print(f"The number of unique characters is: {unique_count}")


# In[5]:


# 5. Write a function that takes a string and returns True if it is a palindrome, False otherwise.

def is_palindrome(input_string):
    # Convert the string to lowercase and remove spaces
    processed_string = input_string.lower().replace(" ", "")
    # Check if the processed string is equal to its reverse
    return processed_string == processed_string[::-1]

input_string = "Radar"
result = is_palindrome(input_string)
if result:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")


# In[6]:


#6. Write a function that takes two strings and returns the longest common substring between them.

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store lengths of the longest common suffixes of substrings
    # Initialize a table with zeros
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring and its ending position
    max_length = 0
    end_position = 0

    # Fill the table and update the variables accordingly
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_position = i
            else:
                table[i][j] = 0

    # Extract the longest common substring from the end position and length
    longest_common_substring = str1[end_position - max_length: end_position]

    return longest_common_substring

str1 = "Administration"
str2 = "Institutions"
result = longest_common_substring(str1, str2)
print("Longest common substring between two strings", str1, "and", str2, "is:", result)


# In[7]:


#7. Write a function that takes a string and returns the most frequent character in it.

def most_frequent_char(input_string):
    char_freq = {}
    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    max_freq = 0
    most_frequent_char = None
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_char = char

    return most_frequent_char

input_string = "abracadabra"
result = most_frequent_char(input_string)
print(f"The most frequent character in the string is '{result}'")


# In[8]:


#8. Write a function that takes a string and returns True if it is an anagram of another string, False otherwise.

def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the two strings are equal
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"

result = are_anagrams(string1, string2)
print("Are they anagrams?", result)


# In[9]:


#9. Write a function that takes a string and returns the number of words in it.
def count_words(input_string):
    words = input_string.split()
    return len(words)
str = "Guvi Geeks Network Private Limited"
word_count = count_words(str)
print("Number of words:", word_count)

