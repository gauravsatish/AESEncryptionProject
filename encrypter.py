import hashlib
import pickle

from AESImpl import AESImpl

def encrypt(text, filename="message.enc"):
    key = input("Enter the key to use for encryption: ")
    key = AESImpl.get_hashed_key(key)
    enc_text = AESImpl.encrypt(key, text)

    enc_file = open(filename[-5::-1][::-1] + ".enc", 'wb')
    pickle.dump(enc_text, enc_file)
    enc_file.close()


def existing_file_encrypt():
    filename = input("Enter filename (<name>.txt): ")
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    text = ""
    for line in lines:
        text = text + line
    encrypt(text, filename)
    print("The encrypted file has been stored in message.enc")


def new_message_encrypt():
    print("Enter message (type __exit__ to stop): ")
    text = ""
    while True:
        i = input()
        if i == "__exit__":
            break
        text = text + i + "\n"

    encrypt(text)



def existing_file_decrypt():
    filename=  input("Enter filename (<name>.enc): ")
    enc_file = open(filename, 'rb')
    enc_text = pickle.load(enc_file)
    key = input("Enter the key to use for encryption: ")
    key = AESImpl.get_hashed_key(key)
    text = AESImpl.decrypt(key, enc_text)
    print(text)