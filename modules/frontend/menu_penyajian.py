from pathlib import Path


def minta_path_penyimpanan(path_default: str | None = None) -> str | None:
    """Minta path tujuan penyimpanan. Return None jika dilewati/dibatalkan."""
    while True:
        if path_default is None:
            prompt = 'Simpan hasil ke file (kosongkan untuk melewati): '
        else:
            prompt = f'Simpan hasil ke (Enter = {path_default}, "-" = batal): '

        path = input(prompt).strip().strip('"')

        if path == '-':
            return None
        if path == '':
            if path_default is None:
                return None
            path = path_default

        tujuan = Path(path)
        if tujuan.is_dir():
            print('Path tersebut adalah folder, masukkan nama file lengkap.')
            continue
        if not tujuan.parent.exists():
            print(f'Folder tujuan tidak ditemukan: {tujuan.parent}')
            continue
        if tujuan.exists():
            jawaban = input(f'File "{tujuan}" sudah ada. Timpa? (y/n): ').strip().lower()
            if jawaban not in ['y', 'ya']:
                continue

        return str(tujuan)


def menu_hasil_teks(teks: str) -> None:
    print('=' * 60)
    print('Hasil Enkripsi/Dekripsi Teks')
    print('=' * 60)
    print(teks)

    path = minta_path_penyimpanan()
    if path is None:
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
        print(f'Hasil tidak dapat ditampilkan sebagai teks: {error}')
        print(f'File hasil tetap tersimpan di {path}')
        return

    
    print(hasil)
