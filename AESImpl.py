import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(key, text):
    cipher = AES.new(key, AES.MODE_ECB)

    byte_text = text.encode("utf-8")
    pad_text = pad(byte_text, AES.block_size)

    enc_text = cipher.encrypt(pad_text)
    return enc_text

def decrypt(key, enc_text):
    cipher = AES.new(key, AES.MODE_ECB)
    dec_text = cipher.decrypt(enc_text)

    text = unpad(dec_text, AES.block_size)
    text = text.decode("utf-8")

    return text

def get_hashed_key(key):
    key = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
    return key.encode("utf-8")
