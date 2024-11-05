from crypt import existing_file_decrypt, existing_file_encrypt, new_message_encrypt

print("""Welcome to message encryption and decryption
Select an option:
    1. Encrypt
    2. Decrypt
""")

choice = input()
if choice == "1":
    print("""\nSelect an option
    1. Encrypt an existing .txt file
    2. Create a new message in console and encrypt""")
    c = input()
    if c == "1":
        existing_file_encrypt()
    elif c == "2":
        new_message_encrypt()
    else:
        print("Invalid choice")
        exit()
elif choice == "2":
    existing_file_decrypt()
else:
    print("Invalid choice")
    exit()
