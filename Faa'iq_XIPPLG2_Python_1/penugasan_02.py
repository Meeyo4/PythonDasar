import math


# Fungsi untuk menghitung volume tabung
def volume_tabung(radius, height):
    return math.pi * radius**2 * height

# Fungsi untuk menghitung volume balok
def volume_balok(length, width, height):
    return length * width * height

# Input jenis bangun ruang
jenis_bangun = input("Masukkan jenis bangun ruang (tabung, balok): ").lower()

# Proses sesuai jenis bangun ruang
if jenis_bangun == "tabung":
    radius = float(input("Masukkan jari-jari tabung: "))
    height = float(input("Masukkan tinggi tabung: "))
    print("Volume tabung:", volume_tabung(radius, height))
elif jenis_bangun == "balok":
    length = float(input("Masukkan panjang balok: "))
    width = float(input("Masukkan lebar balok: "))
    height = float(input("Masukkan tinggi balok: "))
    print("Volume balok:", volume_balok(length, width, height))
else:
    print("Jenis bangun ruang tidak valid.")
