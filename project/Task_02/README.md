# Password Security Check Program

## Description

This program reads passwords from a text file and verifies their security by asking the user to enter **three random letters** from each password that is **9 characters or longer**. Passwords shorter than 9 characters are skipped. The program will terminate immediately if an incorrect letter is entered.

## How to Run

1. Open a terminal
2. Navigate to the program folder
3. Execute the program with:


python password_check.py passwords.txt

## Input File

* One password per line
* Passwords must be **at least 9 characters long**

## Notes

* No external libraries required
* Checks three random letters from each valid password
* Program stops instantly on any incorrect input