import sys
import argparse

lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def process_file(input_file, shift, mode):
    with open(input_file, 'r') as file:
        text = file.read()

    if mode == 'encrypt':
        output_file = input_file + '.enc'
        with open(output_file, 'w') as file:
            file.write(encrypt(text, shift))
        return output_file
    elif mode == 'decrypt':
        output_file = input_file + '.dec'
        with open(output_file, 'w') as file:
            file.write(decrypt(text, shift))
        return output_file
    else:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")

def encrypt(text, shift):
    result = ""

    for char in text:
        if char in lower_alphabet:
            index = lower_alphabet.index(char)
            new_index = (index + shift) % 26
            result += lower_alphabet[new_index]
        elif char in upper_alphabet:
            index = upper_alphabet.index(char)
            new_index = (index + shift) % 26
            result += upper_alphabet[new_index]
        else:
            result += char

    return result

def decrypt(text, shift):
    result = ""

    for char in text:
        if char in lower_alphabet:
            index = lower_alphabet.index(char)
            new_index = (index - shift) % 26
            result += lower_alphabet[new_index]
        elif char in upper_alphabet:
            index = upper_alphabet.index(char)
            new_index = (index - shift) % 26
            result += upper_alphabet[new_index]
        else:
            result += char

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CaesarEncryption",
        description="Caesar Cipher File Encryptor")

    parser.add_argument("file", help="Path to the input file")
    parser.add_argument("key", type=int, help="Numeric shift key (integer)")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")

    args = parser.parse_args()

    new_file = process_file(args.file, args.key, args.mode)

    print(f"Success! Processed file saved as: {new_file}")