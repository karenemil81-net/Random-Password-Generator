# Random Password Generator

A desktop password generator built with **Python** and **Tkinter**.

This application creates secure random passwords using Python's `secrets` module and provides a simple graphical interface for customizing password generation.

## Features

* Generate cryptographically secure passwords
* Choose password length (8–128 characters)
* Select character types:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Exclude ambiguous characters (O, 0, I, l, 1)
* Password strength indicator
* Copy password to clipboard
* Show/Hide password
* Password history (last 5 generated passwords)
* Reset and Clear options
* User-friendly Tkinter interface

## Technologies Used

* Python 3
* Tkinter
* secrets
* string
* pyperclip

## How It Works

1. Choose the desired password length.
2. Select at least two character categories.
3. Optionally exclude ambiguous characters.
4. Click **Generate**.
5. The generated password is automatically copied to the clipboard.
6. View the password strength and generation history.

## Password Strength

The application evaluates password strength based on:

* Password length (12+ characters)
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

Strength is displayed as:

* Weak
* Medium
* Strong

## Project Structure

```
Random-Password-Generator/
│
├── main.py
├── README.md
└── screenshots/
```

