"""Logika enkripsi dan dekripsi data berbasis AES-256-CFB."""
from hashlib import sha256
from os import urandom

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.decrepit.ciphers import modes

from modules.backend.encoder import base64_decode, base64_encode

IV_SIZE = 16
KEY_SIZE = 32


def derive_key(password: str) -> bytes:
    """Ubah password teks menjadi kunci AES-256 (32 byte)."""
    return sha256(password.encode('utf-8')).digest()


def encrypt(key: bytes, data: bytes) -> bytes:
    iv = urandom(IV_SIZE)

    cipher = Cipher(algorithms.AES(key), mode=modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    cipherbytes = encryptor.update(data) + encryptor.finalize()

    return iv + cipherbytes


def decrypt(key: bytes, encrypted_data: bytes) -> bytes:
    iv = encrypted_data[:IV_SIZE]
    cipherbytes = encrypted_data[IV_SIZE:]

    cipher = Cipher(algorithms.AES(key), mode=modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(cipherbytes) + decryptor.finalize()
    return decrypted_data


def encrypt_text(key: bytes, text: str) -> str:
    data_bytes = text.encode('utf-8')
    encrypted_bytes = encrypt(key, data_bytes)
    return base64_encode(encrypted_bytes)


def decrypt_text(key: bytes, encrypted_text: str) -> str:
    encrypted_bytes = base64_decode(encrypted_text)
    decrypted_bytes = decrypt(key, encrypted_bytes)
    return decrypted_bytes.decode('utf-8')
