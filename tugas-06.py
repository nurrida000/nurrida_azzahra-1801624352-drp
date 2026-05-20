from datetime import datetime

print("Yahoo, Sobat Berkembang!")
print("Hari baru, semangat baru!")
print("Sebelum beraktivitas, jangan lupa sarapan, ya :D")
print("Atau kamu mau langsung cuss berangkat ke kantor?")

aktivitas = input("Pilih aktivitasmu: Sarapan atau Kerja)")

if aktivitas.lower() == "sarapan":
    print("Yuk, dipilih dulu menu utama kamu:")
    print("Telur")
    print("Ikan")
    print("Nugget")

    menu = input("Mau pilih menu yang mana?")

    if menu.lower() == "telur" or menu.lower() == "ikan" or menu.lower() == "nugget":
        print("Wah, pilihan yang bagus! Yuk langsung aja kita masak!")
    else:
        print("Menu tidak tersedia di dapur kamu! Tandanya kamu harus pergi untuk beli bahan makanannya dulu!")

elif aktivitas.lower() == "kerja":
    print("Wah, oke deh! Jangan sampai terlambat, ya!")
    waktu = datetime.now()
    print("Jam masuk kerja kamu : 08.00.00 WIB")
    print(f"Jam sekarang: {waktu}")

    if waktu.hour < 08.00:
        print("Kamu masih ada waktu untuk berangkat!")
    elif waktu.hour == 08.00:
        print("Wah! Kamu tepat waktu! Semangat bekerjanya!!!")
    else:
        print("Waduh, kamu sudah terlambat! It's okay. Besok-besok jangan diulangi, ya!")