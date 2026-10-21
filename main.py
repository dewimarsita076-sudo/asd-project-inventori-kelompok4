import produk

def menu_tambah_produk():
    print("\n=== Tambah Produk Baru ===")
    kode = input("Kode produk   : ")
    nama = input("Nama          : ")
    kategori = input("Kategori  : ")
    harga = input("Harga (Rp)   : ")
    stok =input("Stok           : ")
    _, pesan = produk.tambah_produk(kode, nama, kategori, harga, stok)
    print(pesan)

def menu_tampilkan_semua():
    print("\n=== Daftar Semua Produk ===")
    print(produk.tampilkan_semua_produk())
    
def menu_cari_produk():
    print("\n=== Cari Produk ===")
    print("1. Berdasarkan kode (exact match)")
    print("2. Berdasarkan nama (partial match)")
    mode = input("Pilih mode pencarian (1/2): ").strip()
    