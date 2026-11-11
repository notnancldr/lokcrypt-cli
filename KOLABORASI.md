# Panduan Kolaborasi

## Persyaratan Pengembangan
- **Python interpreter:** Software untuk menjalankan kode program python.

---

## Panduan Kolaborasi

### Branching
- Masing-masing kolaborator pakai branch tersendiri
- Branch diberi nama menggunakan nama panggilan

### Konvensi Commit
*Panduan commit lengkap ada [di link ini](https://www.conventionalcommits.org/en/v1.0.0/).*

**Commit pakai format:**
```text
<type>[optional scope]: <description>
```
| Parameter | Sifat | Keterangan |
| --- | --- | -- |
| `<type>` | WAJIB | Tipe perubahan yang dilakukan. |
| `[optional scope]` | OPSIONAL | Cakupan perubahan. |
| `<description>` | WAJIB | Deskripsi dari perubahan. |

**Contoh pesan commit:**
```text
feat: fungsi enkripsi berrbasis AES-256
```
| Parameter | Sifat | Keterangan |
| --- | --- | -- |
| `<type>` | WAJIB | `feat`, penambahan fitur. |
| `[optional scope]` | OPSIONAL | - |
| `<description>` | WAJIB | `fungsi enkripsi berbasis AES-256` |

**Contoh pesan commit menggunakan `optional scope`:**
```text
fix(dekripsi): hasil dekripsi berantakan
```
| Parameter | Sifat | Keterangan |
| --- | --- | -- |
| `<type>` | WAJIB | `fix`, fix bug. |
| `[optional scope]` | OPSIONAL | `dekripsi` |
| `<description>` | WAJIB | `hasil dekripsi berantakan` (keterangan atau bug yang diselesaikan) |

**Contoh penerapan commit menggunakan konvensi:**
```bash
git commit -m "feat(enkripsi): validasi kesalahan format"
```

---

# Catatan
*Sisa panduan dan dokumentasi yang belum tercantum dalam README.md bersifat menyesuaikan dan fleksibel.*