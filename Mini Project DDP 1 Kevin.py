jadwal_penerbangan = [
    ("BA123", "Jakarta", "Samarinda", "08:00"),
    ("TOA987", "Bandung", "Jogja", "12:30"),
    ("ID789", "Balikpapan", "Malang", "14:15")
]

while True:
    print("\nCRUD Jadwal Penerbangan")
    print("1. Read (Lihat Jadwal Penerbangan)")
    print("2. Create (Tambah Jadwal Penerbangan)")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")
    if pilihan == "1":
        print("\n--- Daftar Jadwal Penerbangan ---")
        if len(jadwal_penerbangan) == 0:
            print("Belum ada jadwal yang tersedia.")
        else:
            i = 0
            while i < len(jadwal_penerbangan):
                print(f"{i+1}. {jadwal_penerbangan[i]}")
                i += 1

    elif pilihan == "2":
        kode = input("Masukkan kode penerbangan: ")
        asal = input("Masukkan kota asal: ")
        tujuan = input("Masukkan kota tujuan: ")
        jam = input("Masukkan jam berangkat: ")
        jadwal_penerbangan.append((kode, asal, tujuan, jam))
        print("Jadwal berhasil ditambahkan!")

    elif pilihan == "3":
        print("Keluar dari program.")

    else:
        print("Pilihan tidak valid.")
