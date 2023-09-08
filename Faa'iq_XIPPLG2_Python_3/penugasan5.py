import turtle

# Membuat objek Turtle
mobil = turtle.Turtle()

# Menggambar badan mobil
mobil.fillcolor("blue")
mobil.begin_fill()
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.left(90)
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.end_fill()

# Menggambar atap mobil (trapesium)
mobil.penup()
mobil.goto(10, 50)  # Pindahkan atap sedikit ke kiri dan bawah
mobil.pendown()
mobil.fillcolor("blue")
mobil.begin_fill()
mobil.goto(70, 90)  # Ubah koordinat untuk membuat atap lebih besar
mobil.goto(130, 90)  # Ubah koordinat untuk membuat atap lebih besar
mobil.goto(190, 50)  # Pindahkan atap sedikit ke kanan dan bawah
mobil.end_fill()

# Menggambar roda mobil (roda kiri)
mobil.penup()
mobil.goto(0, -25)
mobil.pendown()
mobil.fillcolor("black")
mobil.begin_fill()
mobil.circle(25)
mobil.end_fill()

# Menggambar roda mobil (roda kanan)
mobil.penup()
mobil.goto(150, -25)
mobil.pendown()
mobil.fillcolor("black")
mobil.begin_fill()
mobil.circle(25)
mobil.end_fill()

# Menutup jendela Turtle saat di-klik
turtle.exitonclick()
