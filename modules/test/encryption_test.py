from os import urandom
import base64
from pathlib import Path
import sys

parent_path = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_path)

from backend.encryption_logic import *

def text_encryption_test(text: str):
    iv = urandom(32)

    key = urandom(32)

    try:
        encrypted_text = encrypt_text(key, text)
        decrypted_text = decrypt_text(key, encrypted_text)

        print(f"Plain text : {text}")
        print(f"Key        : {base64.b64encode(key).decode()}")
        print(f"Encrypted  : {encrypted_text}")
        print(f"Decrypted  : {decrypted_text}")
    except:
        assert False
    else:
        assert text == decrypted_text
        print("SUCCESS, data and result match")
    finally:
        print()

def binary_encryption_testt(data: bytes):
    iv = urandom(32)

    key = urandom(32)

    try:
        encrypted_data = encrypt(key, data)
        decrypted_data = decrypt(key, encrypted_data)

        print(f"Plain data : {data}")
        print(f"Key        : {base64.b64encode(key).decode()}")
        print(f"Encrypted  : {encrypted_data}")
        print(f"Decrypted  : {decrypted_data}")
    except:
        assert False
    else:
        assert data == decrypted_data
        print("SUCCESS, data and result match")
    finally:
        print()

def invalid_encryption_test(text: str):
    iv = urandom(32)
    
    key = urandom(32)
    key2 = urandom(32)

    try:
        encrypted_text = encrypt_text(key, text)
        decrypted_text = decrypt_text(key2, encrypted_text)

        print(f"Plain text : {text}")
        print(f"Key        : {base64.b64encode(key).decode()}")
        print(f"Encrypted  : {encrypted_text}")
        print(f"Decrypted  : {decrypted_text}")
    except:
        assert False
    else:
        assert text != decrypted_text
        print("SUCCESS, invalid key resolves to error")
    finally:
        print()

def invalid_binary_encryption_test(data: bytes):
    iv = urandom(32)
    
    key = urandom(32)
    key2 = urandom(32)

    try:
        encrypted_data = encrypt(key, data)
        decrypted_data = decrypt(key2, encrypted_data)

        print(f"Plain data : {data}")
        print(f"Key        : {base64.b64encode(key).decode()}")
        print(f"Encrypted  : {encrypted_data}")
        print(f"Decrypted  : {decrypted_data}")
    except:
        assert False
    else:
        assert data != decrypted_data
        print("SUCCESS, different key resolves to invalid result")
    finally:
        print()

if __name__ == "__main__":
    text_encryption_test("Hello World!")
    text_encryption_test("!@#$%^&*()")
    text_encryption_test("abcdefghijklmnopqrstuvwxyz")
    
    binary_encryption_testt(b"Hello World!")
    binary_encryption_testt(b"!@#$%^&*()")
    binary_encryption_testt(b"abcdefghijklmnopqrstuvwxyz")
    
    invalid_encryption_test("Hello World!")
    invalid_encryption_test("!@#$%^&*()")
    invalid_encryption_test("abcdefghijklmnopqrstuvwxyz")

    invalid_binary_encryption_test(b"Hello World!")
    invalid_binary_encryption_test(b"!@#$%^&*()")
    invalid_binary_encryption_test(b"abcdefghijklmnopqrstuvwxyz")