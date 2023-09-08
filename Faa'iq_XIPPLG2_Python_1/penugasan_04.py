# Fungsi untuk mencetak segitiga bintang
def print_triangle(n):
  # Loop untuk setiap baris
  for i in range(1, n+1):
    # Cetak spasi kosong sebelum bintang
    for j in range(n-i):
      print(" ", end="")
    # Cetak bintang sesuai baris
    for k in range(i):
      print("* ", end="")
    # Pindah ke baris berikutnya
    print()

# Minta input dari pengguna
n = int(input("Masukkan jumlah baris: "))
# Panggil fungsi print_triangle dengan input n
print_triangle(n)
