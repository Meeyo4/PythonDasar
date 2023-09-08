import turtle

# Inisialisasi turtle
t = turtle.Turtle()

# Fungsi untuk menggambar persegi panjang
def draw_rectangle(length, width):
    for _ in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)

# Fungsi untuk menggambar segitiga
def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Fungsi untuk menggambar trapezium
def draw_trapezium(base1, base2, height):
    t.forward(base1)
    t.left(135)
    t.forward(height)
    t.left(45)
    t.forward(base2)
    t.left(135)
    t.forward(height)

# Fungsi untuk menggambar jajar genjang
def draw_parallelogram(base, height):
    t.forward(base)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(base)
    t.left(45)
    t.forward(height)

# Fungsi untuk menggambar belah ketupat
def draw_rhombus(side_length):
    t.left(30)
    for _ in range(2):
        t.forward(side_length)
        t.left(120)
        t.forward(side_length)
        t.left(60)

# Menggambar persegi panjang
draw_rectangle(100, 50)

# Pindah ke posisi untuk menggambar segitiga
t.penup()
t.goto(150, 0)
t.pendown()

# Menggambar segitiga
draw_triangle(100)

# Pindah ke posisi untuk menggambar trapezium
t.penup()
t.goto(-100, 0)
t.pendown()

# Menggambar trapezium
draw_trapezium(100, 60, 50)

# Pindah ke posisi untuk menggambar jajar genjang
t.penup()
t.goto(150, -100)
t.pendown()

# Menggambar jajar genjang
draw_parallelogram(100, 60)

# Pindah ke posisi untuk menggambar belah ketupat
t.penup()
t.goto(-150, -200)
t.pendown()

# Menggambar belah ketupat
draw_rhombus(70)

# Menutup jendela ketika menggambar selesai
turtle.done()
