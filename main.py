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
    
def menu_hapus_produk():
    print("\n=== Hapus Produk ===")
    kode = input("Kode produk yang akan dihapus: ")
    nama = produk.ambil_nama_produk(kode)
    
    if nama is None:
        print(f"Produk dengan kode '{kode.strip()}' tidak ditemukan")
        return
    
    # Tampilkan nama dulu, lalu minta konfirmasi sebelum benar-benar dihapus
    konfirmasi = input(f"Hapus produk '{nama}'? (y/n): ").strip().lower()
    if konfirmasi == "y":
        _, pesan = produk.hapus_produk(kode)
        print(pesan)
    else:
        print("Penghappusan dibatalkan.")
        
def tampilkan_menu():
    print("\n" + "=" * 40)
    print("   SISTEM MANAJEMEN TOKO / IVENTORI")
    print("=" * 40)
    print("1. Tambah produk baru")
    print("2. Tampilkan semua produk")
    print("3. Cari produk")
    print("4. Update tok produk")
    print("5. Update harga produk")
    print("6. Hapus produk")
    print("0. Keluar")
    print("-" * 40)
        
def main():
    # Pilihan menu dipetakan ke fungsinya masing-masing
    aksi_menu = {
        "1": menu_tambah_produk,
        "2": menu_tampilkan_semua,
        "3": menu_cari_produk,
        "4": menu_update_stok,
        "5": menu_update_harga,
        "6": menu_hapus_produk,
    }
    
    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (0-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan")
            break
        
        if pilihan == "0":
            print("Terima kasih. Data produk tidak disimpan permanen")
            break
        elif pilihan in aksi_menu:
            try:
                aksi_menu[pilihan]()
            except (EOFError, KeyboardInterrupt):
                print("\nProses dibatalkan")
        else:
            print("Pilihan tidak vvalid. Masukan angka 0 sampai 6")
            
if __name__ == "__main__":
    main()    
            