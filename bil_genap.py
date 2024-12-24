# NAMA: FATIH FIRDAUS
# NIM: 241351132
# TIF PAGI A

jumlah_genap = 0
while True:
    input_bilangan = int(input("Masukkan bilangan (-1 untuk berhenti): "))
    if input_bilangan == -1:
        break
    if input_bilangan % 2 == 0:
        jumlah_genap += 1

print(f"Jumlah bilangan genap adalah: {jumlah_genap}")