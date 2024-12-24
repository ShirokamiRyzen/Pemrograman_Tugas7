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
