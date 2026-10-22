# Array of Struct: seluruh produk disimpan di sini
daftar_produk = []

# ---------------------------------------------------------------------------
# Fungsi bantu: validasi & format
# ---------------------------------------------------------------------------
def parse_harga(teks):
    """Ubah teks menjadi float harga. Return (nilai, pesan_error)."""
    try:
        harga = float(teks.strip().replace(",", "."))
    except ValueError:
        return None, "Harga harus berupa angka"
    if harga != harga or harga in (float("inf"), float("-inf")):
        return None, "Harga harus berupa angka yang valid"
    if harga <= 0:
        return None, "Harga harus lebih dari 0"
    return harga, None

def parse_stok(teks):
    """Ubah teks menjadi int stok. Return (nilai, pesan_error)."""
    try:
        stok = int(teks.strip())
    except ValueError:
        return None, "Stok harus berupa angka bulat"
    if stok < 0:
        return None, "Stok tidak boleh negatif"
    return stok, None

def format_rupiah(harga):
    """Format angka ke gaya Rupiah, contoh: 15000.0 -> 'Rp 15.000'."""
    if harga == int(harga):
        teks = f"{int(harga):,}"
    else:
        teks = f"{harga:,.2f}"
    teks = teks.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"Rp {teks}"

# ---------------------------------------------------------------------------
# Fungsi pencarian internal
# ---------------------------------------------------------------------------
def cari_index_by_kode(kode):
    """Cari index produk berdasarkan kode (exact match, tidak peka huruf besar/kecil).
    Return index, atau -1 jika tidak ditemukan."""
    kode_bersih = kode.strip().casefold()
    for index, produk in enumerate(daftar_produk):
        if produk["kode_produk"].casefold() == kode_bersih:
            return index
    return -1

# ---------------------------------------------------------------------------
# F1: Tambah produk
# ---------------------------------------------------------------------------
def tambah_produk(kode_produk, nama, kategori, harga, stok):
    kode = kode.strip()
    nama = nama.strip()
    kategori = kategori.strip()
    
    if not kode:
        return False, "Kode produk tidak boleh kosong"
    if cari_index_by_kode(kode) != -1:
        return False, f"Kode produk '{kode}' sudah digunakan"
    if not nama:
        return False, "Nama produk tidak boleh kosong"
    if not kategori:
        return False, "Kategori tidak boleh kosong"
    
    harga, error = parse_harga(harga)
    if error:
        return False, error
    stok, error = parse_stok(stok)
    if error:
        return False, error
    
    daftar_produk.append({
        "kode_produk": kode,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
    })
    return True, f"Produk {nama} berhasil ditambahkan."


# ---------------------------------------------------------------------------
# F2: Tampilkan semua produk
# ---------------------------------------------------------------------------
def tampilkan_semua_produk():
    """Return string tabel semua produk, atau pesan jika data kosong."""
    if not daftar_produk:
        return "Belum ada produk yang tersimpan."

    # Siapkan baris data (sudah dalam bentuk teks)
    baris = []
    for no, p in enumerate(daftar_produk, start=1):
        baris.append((
            str(no),
            p["kode_produk"],
            p["nama"],
            p["kategori"],
            format_rupiah(p["harga"]),
            str(p["stok"]),
        ))

    header = ("No", "Kode", "Nama", "Kategori", "Harga", "Stok")

    # Lebar kolom menyesuaikan teks terpanjang di tiap kolom
    lebar = [
        max(len(header[i]), *(len(b[i]) for b in baris))
        for i in range(len(header))
    ]

    def format_baris(isi):
        # No & Stok rata kanan, Harga rata kanan, sisanya rata kiri
        kolom = [
            isi[0].rjust(lebar[0]),
            isi[1].ljust(lebar[1]),
            isi[2].ljust(lebar[2]),
            isi[3].ljust(lebar[3]),
            isi[4].rjust(lebar[4]),
            isi[5].rjust(lebar[5]),
        ]
        return " | ".join(kolom)

    garis = "-+-".join("-" * l for l in lebar)

    hasil = [format_baris(header), garis]
    hasil.extend(format_baris(b) for b in baris)
    return "\n".join(hasil)

# ---------------------------------------------------------------------------
# F4: Update stok produk
# ---------------------------------------------------------------------------
def update_stok_produk(kode, stok_baru):
    """Update stok produk berdasarkan kode. Return (berhasil, pesan)."""
    kode = kode.strip()

    if not kode:
        return False, "Kode produk tidak boleh kosong"

    index = cari_index_by_kode(kode)
    if index == -1:
        return False, f"Produk dengan kode '{kode}' tidak ditemukan"

    stok_baru, error = parse_stok(stok_baru)
    if error:
        return False, error

    produk = daftar_produk[index]
    stok_lama = produk["stok"]
    nama = produk["nama"]
    produk["stok"] = stok_baru

    return True, f"Stok produk {nama} berhasil diperbarui: {stok_lama} menjadi {stok_baru}"

# ---------------------------------------------------------------------------
# Fitur 5: Update harga produk
# ---------------------------------------------------------------------------
def update_harga_produk(kode_produk, harga_baru_teks):
    """
    Memperbarui harga produk berdasarkan kode_produk.
    Return (status_sukses, pesan).
    """
    kode = kode_produk.strip()
    
    # 1. Validasi keberadaan kode produk
    index = cari_index_by_kode(kode)
    if index == -1:
        return False, f"Produk dengan kode '{kode}' tidak ditemukan."
    
    # 2. Validasi input harga baru
    harga_baru, error = parse_harga(harga_baru_teks)
    if error:
        return False, error
    
    # 3. Simpan harga lama lalu perbarui ke harga baru
    item = daftar_produk[index]
    harga_lama = item["harga"]
    item["harga"] = harga_baru
    
    # 4. Format pesan output sukses
    pesan_sukses = (
        f"Harga produk {item['nama']} berhasil diperbarui: "
        f"{format_rupiah(harga_lama)} menjadi {format_rupiah(harga_baru)}"
    )
    return True, pesan_sukses