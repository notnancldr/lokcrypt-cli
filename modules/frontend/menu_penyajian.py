from pathlib import Path


def menu_hasil_teks(teks: str) -> None:
    print('=' * 60)
    print('Hasil Enkripsi/Dekripsi Teks')
    print('=' * 60)
    print(teks)

    path = input('Simpan hasil ke file (kosongkan untuk melewati): ').strip()
    if not path:
        return

    try:
        Path(path).write_text(teks, encoding='utf-8')
    except OSError as error:
        print(f'Gagal menyimpan hasil: {error}')
        return

    print(f'Hasil berhasil disimpan ke {path}')


def menu_hasil_file(path: str) -> None:
    print('=' * 60)
    print('Hasil Enkripsi/Dekripsi File')
    print('=' * 60)
    
    try:
        hasil = Path(path).read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError) as error:
        print(f'Gagal membaca hasil dari {path}: {error}')
        return

    
    print(hasil)
