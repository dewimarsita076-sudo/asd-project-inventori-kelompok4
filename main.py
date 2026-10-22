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

def menu_update_stok():
    print("\n=== Update Stok Produk ===")
    kode = input("Kode produk  : ")
    stok_baru = input("Stok baru    : ")
    _, pesan = produk.update_stok_produk(kode, stok_baru)
    print(pesan)

def menu_update_harga():
    print("\n=== Update Harga Produk ===")
    kode = input("Kode produk     : ")
    harga_baru = input("Harga baru (Rp) : ")
    _, pesan = produk.update_harga_produk(kode, harga_baru)
    print(pesan)