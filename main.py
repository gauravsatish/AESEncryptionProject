#TODO: add exception handling
from encrypter import existing_file_decrypt, existing_file_encrypt, new_message_encrypt

intro = """Welcome to message encryption and decryption
Select an option:
1. Encrypt
2. Decrypt
"""

print(intro)

choice = int(input())
if choice == 1:
    print("""Select an option
    1. Encrypt an existing .txt file
    2. Create a new message in console and encrypt""")
    c = int(input())
    if c == 1:
        existing_file_encrypt()
    elif c==2:
        new_message_encrypt()

elif choice == 2:
    existing_file_decrypt()

