def menu_header() -> None:
    print('='*60)
    print('                     LOKCRYPT PROJECT')
    print('     Aplikasi CLI untuk enkripsi dan dekripsi data anda!')
    print('='*60)

def menu_utama() -> None:
    menu_header()
    print('Pilih bentuk data yang akan anda enkripsi/dekripsi !!')
    print('1. Teks')
    print('2. File')
    print('0. Keluar')
    print('='*60)
    print('Pilih Menu  (0-2): ')

def pilih_menu(number: int) -> None:
    pass