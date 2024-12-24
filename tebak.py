# NAMA: FATIH FIRDAUS
# NIM: 241351132
# TIF PAGI A

kata_rahasia = "hitam"

print("Selamat datang di permainan tebak kata!")
print("Coba tebak kata rahasia. Petunjuk: Ini adalah nama bahasa pemrograman.")

while True:
    tebakan = input("Masukkan tebakan Anda: ")

    if tebakan.lower() == kata_rahasia:
        print("Selamat! Tebakan Anda benar.")
        break
    else:
        print("Tebakan salah, coba lagi!")
