# import modules
import pyfiglet
from colorama import Fore, Style
import time

# title
vigenere_title = "VIGENERE CIPHER"
title = pyfiglet.figlet_format(vigenere_title, font="slant", width=250)
print(Fore.CYAN + title.rjust(50) + Style.RESET_ALL)

# make function that implements Vigenere cipher
def vigenere_cipher(plaintext, keyword):
#   a dictionary to plot letters to integers
    letter_val = {}
    for i in range(26):
        letter_val[chr(i + ord('A'))] = i
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#   convert keyword into a list of integers
    keyword_indexes = []
    for k in keyword:
        keyword_indexes.append(letter_val[k])

#   encrypt using Vigenere cipher
    encrypted_text = ''
    for i, ci in enumerate(plaintext):
        if ci not in letters:
            encrypted_text += ci
            continue
        ki = keyword_indexes[i % len(keyword_indexes)]
        cipher_val = (letter_val[ci] + ki) % 26
        encrypted_text += letters[cipher_val]
    return encrypted_text

# ask user for plaintext and keyword
message = input(Fore.GREEN + "\033[1mEnter your message:\033[0m ").upper().replace(" ", "")
keyword = input(Fore.RED + "\033[1mEnter your key:\033[0m ").upper().replace(" ", "")

# show loading message
print(Fore.YELLOW + "\033[1m\nEncrypting...\033[0m " + Style.RESET_ALL)
time.sleep(3)

# print the encrypted message
encrypted_text = vigenere_cipher(message, keyword)
print("\033[1m\nCiphertext:\033[0m", Fore.MAGENTA + encrypted_text + Style.RESET_ALL, "\n")
ascii_text = pyfiglet.figlet_format(encrypted_text, font="digital", width=300)
encrypted_text2 = Fore.MAGENTA + ascii_text + Style.RESET_ALL
print(encrypted_text2.rjust(50))
