# vigenere-cipher
This repository contains encryption tool. This tool uses vigenere cipher with user-defined keys. This repository is intended for academic purposes only and should not be used for any malicious activities.

# How vigenere cipher works
The Vigenère Cipher works as follows: 

Your key is a keyword, which you then translate into corresponding letter values 0 – 25. Then, to encrypt, you will your message on one row (letters 0 – 25), and repeatedly write the keyword below it, adding each column, taking the result mod 26. 

These resultant numbers are the ciphertext. Here is a small example: 

Message: LETSGOTOTHESHOW 11 4 19 18 6 14 19 14 19 7 4 18 7 14 22 
Key: TICKET 19 8 2 10 4 19 19 8 2 10 4 19 19 8 2 
Add: 30 12 21 28 10 33 38 22 21 17 8 37 26 22 24 
Mod: 4 12 21 2 10 7 12 22 21 17 8 11 0 22 24 
Ciphertext: E M V C K H M W V R I L A W Y

# How the code works

This program asks the user for the plaintext (all uppercase letters, no spaces) and the keyword (all uppercase letters) and produce the ciphertext using the Vigenère cipher. Give the output of your program for the following message and key:

Message: THISISTHELASTTASKHOORDAY 
Key: KNIGHTS


# Installation
To run the program, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer.

**Note: I used [VS Code](https://code.visualstudio.com/download) to create and run the program.**

# Packages needed to install
You'll also need to install the following modules:

I. PyFiglet: pip install pyfiglet
II. Colorama: pip install colorama

# Usage
1. Clone or download the repository to your local machine.
2. Open a terminal window and navigate to the directory where the program is located.
3. Run the program by typing python vigenere_cipher.py and pressing Enter.
4. Enter your message and key when prompted.
5. The program will encrypt your message using the Vigenere cipher and display the encrypted text.
