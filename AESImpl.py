import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class AESImpl:
    @staticmethod
    def encrypt(key, text):
        cipher = AES.new(key, AES.MODE_ECB) # creating the encryption cipher

        byte_text = text.encode('utf-8') # Encode  UTF string to a byte string
        pad_text = pad(byte_text, AES.block_size) # Padding the string to a multiple of 16 bytes

        enc_text = cipher.encrypt(pad_text)
        return enc_text

    @staticmethod
    def decrypt(key, enc_text):
        cipher = AES.new(key, AES.MODE_ECB)
        dec_text = cipher.decrypt(enc_text)

        text = unpad(dec_text, AES.block_size) # removing the extra padding
        text = text.decode('utf-8') # Converting back to UTF string from byte string

        return text

    @staticmethod
    def get_hashed_key(key):
        key = hashlib.sha256(key.encode('utf-8')).hexdigest()[:16]
        return key.encode('utf-8')