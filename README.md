# Scrabble Word Finder
A Python script that finds all valid Scrabble words you can make from a set of letters.  
It uses a word list (`scrabble_dictionary.txt`) and checks that no letter is used more than once unless it appears multiple times in your input.

## What it does
- Takes your input letters
- Looks through a big dictionary of Scrabble words
- Finds all words that can be made with your letters
- Sorts them alphabetically and tells you how many were found

## Files
- `main.py` — Main Python code
- `scrabble_dictionary.txt` — Word list (one word per line, all uppercase)
- You can also replace the dictionary file if you want to use a different word list. Just swap out `scrabble_dictionary.txt`.

## Notes
- It doesn't matter if you use lowercase or uppercase letters
- Each letter is used only as often as it appears in your input
- No special libraries needed besides `collections.Counter`, which is built into Python
