# Wordmint automator
Designed to automatically enter a bunch of question-answer pairs into word mint's website
- This has only been tested with the Crossword form!
- Use with caution, the website *will* lag with many inputs.

## Config
Every question-answer pair is in the form of `question;answer` read from `qa.txt`
<br/>Example:
```txt
4 * 8 ; 32
29 * 2 ; 58
```

## Dependencies
- python 3
- pyautogui
