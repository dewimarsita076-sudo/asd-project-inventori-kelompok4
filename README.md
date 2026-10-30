# asd-project-inventori-kelompok4
Program ini dirancang untuk inventori toko dengan memudahkan mengelola data produk di toko, mulai dari mencatat produk baru, memperbarui stok, mencari produk, hingga menampilkan seluruh daftar inventori. dengan berbasis sistem CRUD

1. Nama & Anggota Kelompok
Nama sistem: Sistem Manajemen Toko / Inventori Kelompok: Kelompok 4

1	Dewi Marsita - 25083000076 (@dewimarsita076-sudo) 
2	Rangga Ramadhani - 25083000064 (@RanggaMldhn) 
3	Moh. Rozan Istazada Firdausy - 25083000060 (@PeachyFizzz) 
4	Ahmad Budi Setiawan - 25083000046 (@AhmadBudi227) 
5 Arbi Maulana - 25083000070 (@Kyrbibot)

2. Deskripsi sistem
Sistem ini adalah program terminal berbasis Python untuk membantu operator toko mengelola data produk, mulai dari menambah, menampilkan, dan mencari produk sampai memperbarui stok dan harga serta menghapus produk yang tidak dijual lagi. Setiap produk disimpan sebagai dict (struct) dengan atribut kode_produk, nama, kategori, harga, dan stok, lalu seluruh produk dikumpulkan dalam satu list (Array of Struct). Data hanya disimpan di memori, sehingga hilang saat program ditutup.

3. Cara menjalankan python
git clone https://github.com/dewimarsita076-sudo/asd-project-inventori-kelompok4.git
cd asd-project-inventori-kelompok4
python main.py

4. Fitur yang sudah ada
F1 Tambah produk baru: validasi kode (tidak kosong dan tidak duplikat), nama, kategori, harga (angka lebih dari 0), dan stok (bilangan bulat tidak negatif)
F2 Tampilkan semua produk: ditampilkan dalam bentuk tabel, atau pesan khusus jika data kosong
F3 Cari produk: berdasarkan kode (exact match) atau nama (partial match)
F4 Update stok produk: mengganti stok ke nilai baru
F5 Update harga produk: mengganti harga ke nilai baru
F6 Hapus produk: dengan konfirmasi (y/n) sebelum dihapus

Catatan: pengecekan kode produk tidak membedakan huruf besar dan kecil, sehingga prd001 dianggap sama dengan PRD001.

5. Pembagian tugas
- dewimarsita076-sudo -> Kerangka project (main.py bagian menu_tambah_produk dan menu_hapus_produk, produk.py), F1 Tambah produk beserta fungsi bantu validasi dan format harga, dan F6 Hapus produk, penyusunan readme
- AhmadBudi227	F2 -> Tampilkan semua produk
- Kyrbibot F3 -> Mencari produk
- RanggaMldhn	F4 Update stok produk, UPDATE tabel untuk input produk
- PeachyFizzz	F5 Update harga produk

asd-project-inventori-kelompok4/
|-- main.py      # Entry point, menu utama dan input operator
|-- produk.py    # Data produk, validasi, dan logika F1 sampai F6
`-- README.md    # Dokumentasi project
