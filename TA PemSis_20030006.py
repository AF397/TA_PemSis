def tampilkan_menu():
    print("\n===== Program Kasir =====")
    print("1. Tambah Produk")
    print("2. Daftar Menu")
    print("3. Pembelian")
    print("4. Keluar")
    print("=========================")

def tambah_produk(daftar_produk):
    kode_produk = input("Masukkan kode produk: ")
    nama_produk = input("Masukkan nama produk: ")
    harga_produk = float(input("Masukkan harga produk: "))
    daftar_produk[kode_produk] = {'nama': nama_produk, 'harga': harga_produk}
    print(f"{nama_produk} telah ditambahkan dengan harga {harga_produk}")

def daftar_menu(daftar_produk):
    print("\n===== Daftar Menu =====")
    for kode, info in daftar_produk.items():
        print(f"Kode: {kode}, Nama: {info['nama']}, Harga: {info['harga']}")
    print("=========================")

def pembelian(daftar_produk):
    daftar_pembelian = {}
    print("\n===== Pembelian =====")
    while True:
        kode_produk = input("Masukkan kode produk yang dibeli (atau 'selesai' untuk berhenti): ")
        if kode_produk == 'selesai':
            break
        if kode_produk in daftar_produk:
            jumlah = int(input(f"Masukkan jumlah {daftar_produk[kode_produk]['nama']} yang dibeli: "))
            if kode_produk in daftar_pembelian:
                daftar_pembelian[kode_produk] += jumlah
            else:
                daftar_pembelian[kode_produk] = jumlah
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan.")

    total = 0
    print("\n===== Daftar Pembelian =====")
    for kode, jumlah in daftar_pembelian.items():
        nama = daftar_produk[kode]['nama']
        harga = daftar_produk[kode]['harga']
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama}: {jumlah} x {harga} = {subtotal}")
    print("============================")
    print(f"Total harga: {total}\n")
    return total

def main():
    daftar_produk = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tambah_produk(daftar_produk)
        elif pilihan == '2':
            daftar_menu(daftar_produk)
        elif pilihan == '3':
            pembelian(daftar_produk)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program kasir.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
