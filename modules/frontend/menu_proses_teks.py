from modules.backend.encryption_logic import decrypt_text, derive_key, encrypt_text
from modules.frontend.menu_kesalahan import menu_kesalahan
from modules.frontend.menu_password import menu_password
from modules.frontend.menu_penyajian import menu_hasil_teks
from modules.frontend.tampilan import GARIS, menu_header


def minta_teks() -> str:
    while True:
        teks = input('Masukkan teks: ')
        if teks.strip() == '':
            print('Teks tidak boleh kosong!')
        else:
            return teks


def menu_proses_teks() -> None:
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

        teks = minta_teks()
        password = menu_password()

        if password == '':
            menu_kesalahan('Password tidak boleh kosong!')
            input('Tekan Enter untuk kembali...')
            continue

        key = derive_key(password)

        try:
            if pilihan == '1':
                hasil = encrypt_text(key, teks)
            else:
                hasil = decrypt_text(key, teks)
        except (ValueError, UnicodeDecodeError) as error:
            menu_kesalahan(
                'Gagal memproses teks. Pastikan password dan format data benar. '
                f'({error})'
            )
            input('Tekan Enter untuk kembali...')
            continue

        menu_hasil_teks(hasil)
        input('Tekan Enter untuk kembali...')
