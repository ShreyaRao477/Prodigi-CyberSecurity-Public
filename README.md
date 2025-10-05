Caesar Cipher Program

Description: This program encrypts and decrypts messages using the Caesar Cipher. You can choose to either encrypt or decrypt a message by entering a shift value.

Usage:

Run the program.
Select the operation:
'e' for encryption
'd' for decryption
Enter the message to be encrypted or decrypted.
Enter the shift value (positive integer).
The program will display the transformed message.
Requirements:

Python 3.x
Functions:

caesar_cipher(text, shift, action):

Encrypts or decrypts the given text based on the shift value and selected action ('e' or 'd').
main():

Handles user inputs and calls the caesar_cipher function.
Sample Run:

Welcome to the Caesar Cipher program! Select 'e' to encrypt or 'd' to decrypt: e Enter the message: Hello! Enter the shift value (positive integer): 3

Encrypted Message: Khoor!

OR

Welcome to the Caesar Cipher program! Select 'e' to encrypt or 'd' to decrypt: d Enter the message: Khoor! Enter the shift value (positive integer): 3

Decrypted Message: Hello!

Note:

Non-alphabet characters (like spaces, punctuation) are not changed.
Sources:Github - https://github.com/dhairya-gayakwad/Prodigy-InfoTech , Google
