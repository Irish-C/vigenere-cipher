# import module
import pyfiglet

# title
title = "ALL-TIME DECRYPTION TOOL"
font = pyfiglet.figlet_format(title, font="standard", width = 250)
print(font.center(100))

# function for decrypting text
def decrypted_str(encrypted_str):
    vowels_dict = {'*':'a', '&':"e", '#':'i', '+':'o', '!':'u'}
    decrypted_str = ""
    for i in encrypted_str:
        if i in vowels_dict:
            decrypted_str += vowels_dict[i]
        else:
            decrypted_str += i
    return decrypted_str

# ask user for encrypted texts
# decrypt the user input
# print result