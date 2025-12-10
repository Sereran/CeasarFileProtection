import sys
import argparse
import os
from tqdm import tqdm

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
        output_file = input_file[:-4]
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

    parser.add_argument("path", help="Path to the input file or folder")
    parser.add_argument("key", type=int, help="Numeric shift key (integer)")
    parser.add_argument("mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")

    args = parser.parse_args()

    if os.path.isfile(args.path):
        filename = args.path

        if args.mode == 'decrypt' and not filename.endswith('.enc'):
            print("Error: You can only decrypt .enc files!")

        elif args.mode == 'encrypt' and not filename.endswith('.txt'):
            print("Error: You can only encrypt .txt files!")

        else:
            print(f"Processing single file: {args.path}")
            new_file = process_file(args.path, args.key, args.mode)
            print(f"Success! Saved as: {new_file}")

    elif os.path.isdir(args.path):
        print(f"Processing folder: {args.path}")

        files_to_process = []

        for root, dirs, files in os.walk(args.path):
            for file in files:
                full_path = os.path.join(root, file)
                if args.mode == 'encrypt':
                    if file.endswith('.txt') and not file.endswith('.enc'):
                        files_to_process.append(full_path)
                elif args.mode == 'decrypt':
                    if file.endswith('.enc'):
                        files_to_process.append(full_path)

        if not files_to_process:
            print("No suitable files found to process!")
        else:
            for current_file in tqdm(files_to_process, desc="Processing Files"):
                process_file(current_file, args.key, args.mode)
            print("Folder processing complete!")

    else:
        print("Error: The path provided does not exist.")
