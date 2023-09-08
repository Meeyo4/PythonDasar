# Meminta pengguna untuk memasukkan batas atas rentang
batas_atas = int(input("Masukkan batas atas rentang: "))

# Inisialisasi list untuk nilai ganjil dan genap
nilai_ganjil = []
nilai_genap = []

# Mengisi list dengan nilai ganjil dan genap dalam rentang
for angka in range(1, batas_atas + 1):
    if angka % 2 == 0:
        nilai_genap.append(angka)
    else:
        nilai_ganjil.append(angka)

# Mencetak nilai ganjil dan genap
print("Nilai ganjil dalam rentang 1 hingga", batas_atas, "adalah:", nilai_ganjil)
print("Nilai genap dalam rentang 1 hingga", batas_atas, "adalah:", nilai_genap)
