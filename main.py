import produk

def menu_tambah_produk():
    print("\n=== Tambah Produk Baru ===")
    kode = input("Kode produk   : ")
    nama = input("Nama          : ")
    kategori = input("Kategori      : ")
    harga = input("Harga (Rp)    : ")
    stok = input("Stok          : ")
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
    
    if mode == "1":
        kode = input("Masukkan kode produk: ")
        print(produk.cari_by_kode(kode))
    elif mode == "2":
        nama = input("Masukkan kata kunci nama: ")
        print(produk.cari_by_nama(nama))
    else:
        print("Pilihan mode tidak valid.")

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
        print(f"Produk dengan kode '{kode.strip()}' tidak ditemukan.")
        return
    
    konfirmasi = input(f"Yakin ingin menghapus produk '{nama}'? (y/n): ").strip().lower()
    if konfirmasi == "y":
        _, pesan = produk.hapus_produk(kode)
        print(pesan)
    else:
        print("Penghapusan dibatalkan.")

# ==========================================
# MENU UTAMA PROGRAM
# ==========================================
def main():
    while True:
        print("\n" + "="*30)
        print(" SISTEM MANAJEMEN TOKO INVENTORI ")
        print("="*30)
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Cari Produk")
        print("4. Update Stok Produk")
        print("5. Update Harga Produk")
        print("6. Hapus Produk")
        print("0. Keluar")
        print("="*30)
        
        pilihan = input("Pilih menu (0-6): ").strip()
        
        if pilihan == "1":
            menu_tambah_produk()
        elif pilihan == "2":
            menu_tampilkan_semua()
        elif pilihan == "3":
            menu_cari_produk()
        elif pilihan == "4":
            menu_update_stok()
        elif pilihan == "5":
            menu_update_harga()
        elif pilihan == "6":
            menu_hapus_produk()
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
