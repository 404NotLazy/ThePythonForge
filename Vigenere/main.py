import string

def vigenere_cipher(text, cipher_key, direction=1):
    alphabet = string.ascii_lowercase
    result = ""
    key_position = 0

    for character in text.lower():
        if not character.isalpha():
            result += character
        else:
            key_char = cipher_key[key_position % len(cipher_key)]
            key_position += 1
            offset = alphabet.index(key_char)
            char_index = alphabet.find(character)

            new_char_index = (char_index + offset * direction) % len(alphabet)

            result += alphabet[new_char_index]

    return result


def encrypt_message(text, cipher_key):
    return vigenere_cipher(text, cipher_key)


def decrypt_message(text, cipher_key):
    return vigenere_cipher(text, cipher_key, -1)


def main():
    user_choice = input("Do you want to encrypt or decrypt (1 or 2): ")
    message = input("Enter the message you want to encrypt/decrypt: ")
    cipher_key = input("Enter the key you want to use: ")

    if user_choice == "1":
        final_message = encrypt_message(message, cipher_key)

    elif user_choice == "2":
        final_message = decrypt_message(message, cipher_key)

    else:
        print("Please enter the correct option!")

    print("Final Message: ", final_message)


if __name__ == "__main__":
    main()
