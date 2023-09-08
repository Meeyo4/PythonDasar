import turtle

# Inisialisasi turtle
t = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang dengan warna merah
def draw_rectangle(length, width):
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

# Fungsi untuk menggambar segitiga dengan warna kuning
def draw_triangle(side_length):
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Fungsi untuk menggambar trapezium dengan warna hijau
def draw_trapezium(base1, base2, height):
    t.fillcolor("green")
    t.begin_fill()
    t.forward(base1)
    t.left(135)
    t.forward(height)
    t.left(45)
    t.forward(base2)
    t.left(135)
    t.forward(height)
    t.end_fill()

# Fungsi untuk menggambar jajar genjang dengan warna biru
def draw_parallelogram(base, height):
    t.fillcolor("blue")
    t.begin_fill()
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.end_fill()

# Fungsi untuk menggambar segilima dengan warna ungu
def draw_pentagon(side_length):
    t.fillcolor("purple")
    t.begin_fill()
    for _ in range(5):
        t.forward(side_length)
        t.right(72)
    t.end_fill()

# Pindah ke posisi untuk menggambar persegi panjang (merah)
t.penup()
t.goto(-150, 100)
t.pendown()
draw_rectangle(100, 50)

# Pindah ke posisi untuk menggambar segitiga (kuning)
t.penup()
t.goto(50, 100)
t.pendown()
draw_triangle(100)

# Pindah ke posisi untuk menggambar trapezium (hijau)
t.penup()
t.goto(-150, -100)
t.pendown()
draw_trapezium(100, 60, 50)

# Pindah ke posisi untuk menggambar jajar genjang (biru)
t.penup()
t.goto(50, -100)
t.pendown()
draw_parallelogram(100, 60)

# Pindah ke posisi untuk menggambar segilima (ungu)
t.penup()
t.goto(100, -50)  # Pindahkan posisi segilima ke kanan agar tidak tumpang tindih
t.pendown()
draw_pentagon(70)

# Menutup jendela ketika menggambar selesai
turtle.done()
