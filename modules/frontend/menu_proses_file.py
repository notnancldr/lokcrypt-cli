from pathlib import Path

from modules.backend.encryption_logic import IV_SIZE, decrypt, derive_key, encrypt
from modules.frontend.menu_kesalahan import menu_kesalahan
from modules.frontend.menu_password import menu_password
from modules.frontend.menu_penyajian import menu_hasil_file, minta_path_penyimpanan
from modules.frontend.tampilan import GARIS, menu_header

EKSTENSI_ENKRIPSI = '.lokcrypt'
EKSTENSI_DEKRIPSI = '.hasil'


def minta_path(prompt: str) -> str:
    while True:
        path = input(prompt).strip().strip('"')
        if path == '':
            print('Path tidak boleh kosong!')
        elif not Path(path).is_file():
            print('File tidak ditemukan, coba lagi.')
        else:
            return path


def baca_file(path: str) -> bytes | None:
    try:
        return Path(path).read_bytes()
    except OSError as error:
        menu_kesalahan(f'Gagal membaca file: {error}')
        return None


def tulis_file(path: str, data: bytes) -> bool:
    try:
        Path(path).write_bytes(data)
    except OSError as error:
        menu_kesalahan(f'Gagal menyimpan file: {error}')
        return False
    return True


def tentukan_path_hasil(path: str, operasi: str) -> str:
    sumber = Path(path)
    if operasi == 'enkripsi':
        return str(sumber) + EKSTENSI_ENKRIPSI
    if sumber.suffix == EKSTENSI_ENKRIPSI:
        return str(sumber.with_suffix(''))
    return str(sumber) + EKSTENSI_DEKRIPSI


def menu_proses_file() -> None:
    while True:
        menu_header()
        print('Pilih metode yang akan dipakai:')
        print('1. Enkripsi')
        print('2. Dekripsi')
        print('0. Kembali')
        print(GARIS)
        pilihan = input('Pilih menu (0-2): ').strip()

        if pilihan not in ['0', '1', '2']:
            print('Pilihan tidak valid, coba lagi.\n')
            continue

        if pilihan == '0':
            break

        path = minta_path('Masukkan path file: ')
        password = menu_password()

        if password == '':
            menu_kesalahan('Password tidak boleh kosong!')
            input('Tekan Enter untuk kembali...')
            continue

        data = baca_file(path)
        if data is None:
            input('Tekan Enter untuk kembali...')
            continue

        key = derive_key(password)
        operasi = 'enkripsi' if pilihan == '1' else 'dekripsi'
        path_default = tentukan_path_hasil(path, operasi)

        try:
            if pilihan == '1':
                hasil = encrypt(key, data)
            else:
                if len(data) < IV_SIZE:
                    raise ValueError('File terlalu pendek atau bukan hasil enkripsi Lokcrypt.')
                hasil = decrypt(key, data)
        except ValueError as error:
            menu_kesalahan(f'Gagal melakukan {operasi}: {error}')
            input('Tekan Enter untuk kembali...')
            continue

        path_hasil = minta_path_penyimpanan(path_default)
        if path_hasil is None:
            print('Penyimpanan dibatalkan, hasil tidak disimpan.')
            input('Tekan Enter untuk kembali...')
            continue

        if not tulis_file(path_hasil, hasil):
            input('Tekan Enter untuk kembali...')
            continue

        print(GARIS)
        print(f'File berhasil di{operasi} dan disimpan ke: {path_hasil}')
        print(GARIS)

        if pilihan == '2':
            menu_hasil_file(path_hasil)

        input('Tekan Enter untuk kembali...')
