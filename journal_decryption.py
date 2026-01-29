import os

####################################################################################################
##
# File operations
##
####################################################################################################

def read_text_file(file_path: str) -> str:

    if not os.path.exists(file_path):
        return ""
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(file_path: str, content: str) -> None:
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


####################################################################################################
##
# Crypto Operations
##
####################################################################################################


def decrypt(ciphertext: str, password: str) -> str:

    result = []
    password = password.lower()
    key_len = len(password)
    key_index = 0

    for char in ciphertext:

        if char.isalpha():
            base = ord('a') # starts from 'a', and ensure the alphabet is 0-25
            ciphertext_value = ord(char.lower()) - base # numerical value of the ciphertext character
            key_value = ord(password[key_index % key_len]) - base # shift value from password

            plaintext_value = (ciphertext_value - key_value) % 26 # numerical value of the plaintext character by finding remainder
            decrypted_char = chr(plaintext_value + base) # convert numerical value back to character

            # preserve original case
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            result.append(decrypted_char)
            key_index += 1

        else: # keep non-alphabetic characters (spaces or punctuations) unchanged
            result.append(char)

    return "".join(result)


####################################################################################################
##
# Body
##
####################################################################################################

def main():

    password = "saturn"

    text = read_text_file("journal_encrypted.txt")

    decrypted_result = decrypt(text, password)

    print(decrypted_result)
    write_text_file("journal_decrypted.txt", decrypted_result)


if __name__ == "__main__":

    main()