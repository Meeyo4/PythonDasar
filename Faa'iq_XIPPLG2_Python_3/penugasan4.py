import turtle

# Fungsi untuk menggambar pohon Fibonacci
def fibonacci_tree(t, branch_length, levels):
    if levels > 0:
        t.forward(branch_length)
        t.right(30)
        fibonacci_tree(t, branch_length - 10, levels - 1)
        t.left(60)
        fibonacci_tree(t, branch_length - 10, levels - 1)
        t.right(30)
        t.backward(branch_length)

# Inisialisasi turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum

# Pindah ke posisi awal
t.penup()
t.goto(0, -200)
t.pendown()

# Atur sudut awal
t.setheading(90)

# Panggil fungsi untuk menggambar pohon Fibonacci
fibonacci_tree(t, 100, 5)

# Menutup jendela ketika selesai
turtle.done()
