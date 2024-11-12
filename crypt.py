import pickle

import AESImpl


def encrypt(text, filename="message.txt"):
    key = input("Enter key to be used for encryption: ")
    key = AESImpl.get_hashed_key(key)
    enc_text = AESImpl.encrypt(key, text)

    with open(filename[:-4] + ".enc", "wb") as enc_file:  
        # <filename>.txt ---> <filename>.enc
        pickle.dump(enc_text, enc_file)

    print(f"\nThe encrypted file has been stored in {filename[:-4]}.enc")


def existing_file_encrypt():
    filename = input("\nEnter filename (<name>.txt): ")

    try:
        with open(filename, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("The file does not exist. Create the file first and enter the name correctly. For eg: \"message.txt\".")
        exit()

    encrypt(text, filename)


def new_message_encrypt():
    print("\nEnter message (type __exit__ to stop): ")
    text = ""

    while True:
        i = input()
        if i == "__exit__":
            break
        text += i + "\n"

    encrypt(text.strip())


def existing_file_decrypt():
    filename = input("\nEnter filename (<name>.enc): ")

    try:
        with open(filename, "rb") as enc_file:
            enc_text = pickle.load(enc_file)
    except FileNotFoundError:
        print("The file does not exist. Make sure you have typed the name correctly. For eg: \"message.enc\"")
        exit()

    key = input("Enter key to be used for encryption: ")
    key = AESImpl.get_hashed_key(key)
    text = AESImpl.decrypt(key, enc_text)

    print("\n" + text)
