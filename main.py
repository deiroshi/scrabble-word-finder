"""
Scrabble Word Finder Project

PPOJECT OBJECTIVE:
Develop a program that takes a letter combination (like "tabind") and creates 
an alphabetical list of all words from a Scrabble dictionary that can be 
found with those letters.

PLAN:
1. Take input: Letter combination (tabind itc.)
2. Load Scrabble dictionary: List of valid words
3. Find all possible words: That can be made with the given letters
4. Display results: Alphabetical list of valid words
5. Print results

FETURES TO ADD
- Load real Scrabble dictionary from a file
- Handle duplicate letters corrctly
- Sort results alphabetically
- Count total words found

NOTES:
- Each letter can be used only as many times as it appears in the input
- Not case sensitive
- Need to find dictionary file online
"""

# Take input/Convert input to lowercase so it doesnt matter how they type it
letters = input("Enter letters: ").upper()

# Load Scrabble dictionary 
def scrabble_dictionary():
    with open("scrabble_dictionary.txt", "r") as file:     # Reads the file     # "r" - read mode     # with - automatically closes the file when done
        words = set()                                      # Create Python set  
        for line in file:                                  # Goes through every line in the file
            word = line.strip().upper()                    # Remove \n and convert to uppercase
            words.add(word)                                # Add the word to the set
        return words                                       

# Find/sort all possible words
from collections import Counter
def find_words(letters, scrabble_dictionary):
    letters_count = Counter(letters)                       # Count letters in the input
    valid_words = []                                       # Create a list to store valid words
    for word in scrabble_dictionary:                       # Go through each word in the dictionary
        word_count = Counter(word)                         # Count letters in the word
        if all(word_count[char] <= letters_count[char] for char in word_count):  # Check if each letter in the word can be formed with the input letters
            valid_words.append(word)                       # If valid, add to the list
    return sorted (valid_words)                            # Return the list sorted alphabetically

results = find_words(letters, scrabble_dictionary())      

# Print results
print("You can make",len(results),"words from",letters)
for word in results:
    print("-", word)

