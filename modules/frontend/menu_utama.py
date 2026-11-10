from modules.frontend.tampilan import menu_header, GARIS
from modules.frontend.menu_proses_teks import menu_proses_teks
from modules.frontend.menu_proses_file import menu_proses_file
from modules.frontend.menu_panduan import menu_panduan


def menu_utama() -> None:
    while True:
        menu_header()
        print('Pilih bentuk data yang akan Anda enkripsi/dekripsi!')
        print('1. Teks')
        print('2. File')
        print('3. Panduan')
        print('0. Keluar')
        print(GARIS)
        pilihan = input('Pilih menu (0-3): ').strip()

        if pilihan not in ['0', '1', '2', '3']:
            print('Pilihan tidak valid, coba lagi.\n')
            continue

        number = int(pilihan)
        if number == 0:
            print('Terima kasih telah menggunakan Lokcrypt. Sampai jumpa!')
            break

        pilih_menu(number)


def pilih_menu(number: int) -> None:
    if number == 1:
        menu_proses_teks()
    elif number == 2:
        menu_proses_file()
    elif number == 3:
        menu_panduan()
        input('Tekan Enter untuk kembali...')
