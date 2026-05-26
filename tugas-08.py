user = input("Siapa nama Anda? ")

print(f"/n1. PAPAN CATUR INPUT AKTIVITAS {user}")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"/n2. DAFTAR AKTIVITAS {user}")

daftar_aktivitas = []
jumlah_aktivitas = int(input("Berapa banyak aktivitas yang ingin Anda tambahkan? "))

for i in range(jumlah_aktivitas):
    print()
    print(f"\nAktivitas ke-{i+1}")

    Nama_aktivitas = input("Nama aktivitas: ")
    Waktu_aktivitas = input("Waktu aktivitas: ")
    Tempat_aktivitas = input("Tempat aktivitas: ")

    aktivitas = {
        "aktivitas" : Nama_aktivitas,
        "waktu" : Waktu_aktivitas,
        "tempat" : Tempat_aktivitas
    }
    daftar_aktivitas.append(aktivitas)
print()

print("🌸 DAFTAR AKTIVITAS YANG TELAH DIMASUKKAN {user} 🌸")

for i in range(len(daftar_aktivitas)):
    print(f"AKTIVITAS {i + 1}")
    print(f"Nama Aktivitas: {daftar_aktivitas[i]['aktivitas']}")
    print(f"Waktu Aktivitas: {daftar_aktivitas[i]['waktu']}")
    print(f"Tempat Aktivitas: {daftar_aktivitas[i]['tempat']}")
print()