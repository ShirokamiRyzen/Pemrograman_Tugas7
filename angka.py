# NAMA: FATIH FIRDAUS
# NIM: 241351132
# TIF PAGI A

kata_sandi_benar = "Python123"

percobaan = 0
batas_percobaan = 3

print("Selamat datang! Silakan masukkan kata sandi Anda.")

while percobaan < batas_percobaan:
    kata_sandi = input("Masukkan kata sandi: ")

    if kata_sandi == kata_sandi_benar:
        print("Login berhasil! Selamat datang.")
        break
    else:
        percobaan += 1
        print("Kata sandi salah. Coba lagi.")

        if percobaan == batas_percobaan:
            print("Akun terkunci.")

jumlah_total = 0
jumlah_angka = 0

print("Masukkan angka untuk menghitung jumlah total dan rata-rata.")
print("Ketikkan -1 untuk berhenti.")

while True:
    input_angka = input("Masukkan angka: ")

    if input_angka.isdigit() or (input_angka.startswith('-') and input_angka[1:].isdigit()):
        angka = int(input_angka)

        if angka == -1:
            break

        jumlah_total += angka
        jumlah_angka += 1
    else:
        print("Harap masukkan angka yang valid!")

if jumlah_angka > 0:
    rata_rata = jumlah_total / jumlah_angka
    print(f"Jumlah total angka: {jumlah_total}")
    print(f"Rata-rata angka: {rata_rata:.2f}")
else:
    print("Tidak ada data yang dimasukkan.")
