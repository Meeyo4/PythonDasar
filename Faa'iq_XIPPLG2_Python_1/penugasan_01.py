# Fungsi untuk menghitung keliling persegi
def keliling_persegi(sisi):
    return 4 * sisi

# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    return sisi * sisi

# Fungsi untuk menghitung keliling persegi panjang
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# Fungsi untuk menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi untuk menghitung keliling trapesium
def keliling_trapesium(sisi1, sisi2, sisi3, sisi4):
    return sisi1 + sisi2 + sisi3 + sisi4

# Fungsi untuk menghitung luas trapesium
def luas_trapesium(alas, tinggi, sisi1, sisi2):
    return 0.5 * (alas + sisi1) * tinggi

# Input jenis bangun datar
jenis_bangun = input("Masukkan jenis bangun datar (persegi, persegi panjang, trapesium): ").lower()

# Proses sesuai jenis bangun datar
if jenis_bangun == "persegi":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    print("Keliling persegi:", keliling_persegi(sisi))
    print("Luas persegi:", luas_persegi(sisi))
elif jenis_bangun == "persegi panjang":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    print("Keliling persegi panjang:", keliling_persegi_panjang(panjang, lebar))
    print("Luas persegi panjang:", luas_persegi_panjang(panjang, lebar))
elif jenis_bangun == "trapesium":
    alas = float(input("Masukkan panjang alas trapesium: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    sisi1 = float(input("Masukkan panjang sisi sejajar 1: "))
    sisi2 = float(input("Masukkan panjang sisi sejajar 2: "))
    print("Keliling trapesium:", keliling_trapesium(alas, tinggi, sisi1, sisi2))
    print("Luas trapesium:", luas_trapesium(alas, tinggi, sisi1, sisi2))
else:
    print("Jenis bangun datar tidak valid.")
