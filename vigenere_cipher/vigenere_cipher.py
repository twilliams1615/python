"""
vigenere_cipher

Encodes and Decodes text using the Vigenere Cipher.

"""

from sys import version_info

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    """Main function.
    message is the message to encode or decode
    cipher_key is the word to use as the key to the cipher
    mode is set to encrypt or decrypt
    """
    message = INPUT("What is the message you would like to use? ").replace(" ", "").lower()
    cipher_key = INPUT("Input the key to be used for the cipher ")
    mode = INPUT("What would you like to do? [encrypt/decrypt] ").lower()

    if mode == 'encrypt':
        translated = encrypt_message(cipher_key, message)
    elif mode == 'decrypt':
        translated = decrypt_message(cipher_key, message)

    print('%sed message:' % (mode.title()))
    print(translated)


def encrypt_message(key, message):
    """ returns the encrypted message """
    return translate_message(key, message, 'encrypt')


def decrypt_message(key, message):
    """ returns the decrypted message """
    return translate_message(key, message, 'decrypt')


def translate_message(key, message, mode):
    """ translates the message using the key """
    translated = [] # stores the encrypted/decrypted message string

    key_index = 0
    key = key.upper()

    for character in message: # loop through each character in message
        num = LETTERS.find(character.upper())
        if num != -1: # -1 means character.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted character to the end of translated.
            if character.isupper():
                translated.append(LETTERS[num])
            elif character.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1 # move to the next letter in the key
            if key_index == len(key):
                key_index = 0
        else:
            # The character was not in LETTERS, so add it to translated as is.
            translated.append(character)

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    INPUT = input
    if version_info[:2] <= (2, 7):
        INPUT = raw_input
    main()
