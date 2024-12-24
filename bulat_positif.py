# NAMA: FATIH FIRDAUS
# NIM: 241351132
# TIF PAGI A

def is_valid_number(input_str):
    return input_str.isdigit() or input_str == "-1"

jumlah = 0

while True:
    input_str = input("Masukkan angka bulat positif (-1 untuk berhenti): ")

    if not is_valid_number(input_str):
        print("Input tidak valid! Harap masukkan angka bulat positif.")
        continue

    angka = int(input_str)

    if angka == -1:
        break

    if angka < 0:
        print("Angka tidak valid! Harap masukkan angka bulat positif.")
        continue

    jumlah += angka

print(f"Jumlah angka yang dimasukkan adalah: {jumlah}")
