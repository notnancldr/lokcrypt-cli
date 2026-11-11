"""
BUKAN FINAL, JANGAN PAKAI
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.decrepit.ciphers import modes
from os import urandom
import base64

IV_SIZE = 16

def encrypt(key: bytes, data:  bytes) -> bytes:
    """
    Menyembunyikan data biner doksli dalam bentuk terenkripsi.

    Args:
        key (`bytes`): Kunci enkripsi.
        data (`bytes`): File doksli.

    Returns:
        `str`: Jika hasil valid.
        `None`: Jika hasil tidak valid.
    """
    iv = urandom(IV_SIZE)

    cipher = Cipher(algorithms.AES(key), mode=modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    cipherbytes = encryptor.update(data) + encryptor.finalize()

    return iv + cipherbytes

def decrypt(key: bytes, encrypted_data: bytes) -> bytes:
    """
    **CATATAN:** Tidak menyertakan implementasi validasi key benar/salah,
    key yang salah menyebabkan hasil korup tanpa galat di aplikasi.

    Mengembalikan data biner menjadi doksli.

    Args:
        key (`bytes`): Kunci enkripsi.
        data (`bytes`): Bentuk terenkripsi.

    Returns:
        `str`: Jika hasil valid.
    """
    iv = encrypted_data[:IV_SIZE]
    cipherbytes = encrypted_data[IV_SIZE:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(cipherbytes) + decryptor.finalize()
    return decrypted_data

def encrypt_text(key: bytes, text: str) -> str:
    """
    Men-enkripsi teks doksli menjadi teks terenkripsi.

    Args:
        key (`bytes`): Kunci enkripsi.
        encrypted_text (`str`): Teks doksli.

    Returns:
        `str`: Hasil enkripsi.
    """
    data_bytes = text.encode()
    encrypted_bytes = encrypt(key, data_bytes)
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt_text(key: bytes, encrypted_text: str) -> str | None:
    """
    **CATATAN:** Mengembalikan `None` jika hasil tidak valid.

    Men-dekripsi teks yang sudah terenkripsi menjadi doksli.

    Args:
        key (`bytes`): Kunci enkripsi.
        encrypted_text (`str`): Teks terenkripsi.

    Returns:
        `str`: Hasil dekripsi jika hasil valid.
        `None`: Jika hasil tidak valid.
    """

    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = decrypt(key, encrypted_bytes)
    try:
        return decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return None
