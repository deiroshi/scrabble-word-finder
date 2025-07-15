# Scrabble Word Finder

This project is a Python script that finds all valid **Scrabble words** you can make from a given set of letters.  
It uses a pre-loaded dictionary file and ensures that each letter is only used as many times as it appears in your input.


## Features

- Accepts any string of letters as input (case-insensitive)
- Searches a full dictionary of official Scrabble words
- Filters results based on available letter counts
- Sorts results alphabetically and displays total word count


## How It Works

1. **Input Letters**  
   The user enters a string of letters (e.g. `TABIND`)

2. **Dictionary Lookup**  
   The script loads a word list from `scrabble_dictionary.txt`

3. **Validation**  
   For each word, it checks whether the word can be made using the input letters  
   (taking letter frequency into account)

4. **Output**  
   Prints an alphabetically sorted list of valid words  
   Shows the total number of words found


## Notes

- Input letters can be lowercase or uppercase - it doesn’t matter
- Each letter is used only as many times as it appears in the input
- You can swap in a different word list by replacing `scrabble_dictionary.txt`


## Files

`main.py` - Main Python script that handles input and word filtering  
`scrabble_dictionary.txt` - Text file with one valid Scrabble word per line (all uppercase)
