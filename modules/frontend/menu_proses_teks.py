from modules.frontend.tampilan import menu_header, GARIS


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

        # TODO: ganti dengan menu_password() dari teman
        password = 'placeholder'

        if pilihan == '1':
            # TODO: ganti dengan encrypt(...) dari teman
            hasil = '[placeholder enkripsi] ' + teks
        else:
            # TODO: ganti dengan decrypt(...) dari teman
            hasil = '[placeholder dekripsi] ' + teks

        # TODO: ganti dengan menu_hasil_teks(hasil) dari teman
        print(GARIS)
        print('Hasil:', hasil)
        print(GARIS)
        input('Tekan Enter untuk kembali...')