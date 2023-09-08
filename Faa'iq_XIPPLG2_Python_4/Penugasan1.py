import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x300")
window.resizable(False, False)
window.title("Hitung Total Harga Barang")

# Membuat variabel untuk harga barang dan kuantitas
HARGA_BARANG = tk.DoubleVar()
KUANTITAS = tk.IntVar()
TOTAL_HARGA = tk.DoubleVar(value=0)

def hitung_total():
    harga_barang = HARGA_BARANG.get()
    kuantitas = KUANTITAS.get()
    
    if harga_barang > 0 and kuantitas > 0:
        total_harga = harga_barang * kuantitas
        TOTAL_HARGA.set(total_harga)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

harga_barang_label = ttk.Label(input_frame, text="Harga:")
harga_barang_label.pack(padx=10, pady=(10, 0), fill="x", expand=True)

harga_barang_entry = ttk.Entry(input_frame, textvariable=HARGA_BARANG)
harga_barang_entry.pack(padx=10, fill="x", expand=True)

kuantitas_label = ttk.Label(input_frame, text="Kuantitas:")
kuantitas_label.pack(padx=10, fill="x", expand=True)

kuantitas_entry = ttk.Entry(input_frame, textvariable=KUANTITAS)
kuantitas_entry.pack(padx=10, fill="x", expand=True)

hitung_tombol = ttk.Button(input_frame, text="Hitung Total", command=hitung_total)
hitung_tombol.pack(fill='x', expand=True, padx=10, pady=10)

total_label = ttk.Label(input_frame, text="Total Harga:")
total_label.pack(padx=10, pady=(10, 0), anchor="w")

total_harga_label = ttk.Label(input_frame, textvariable=TOTAL_HARGA)
total_harga_label.pack(padx=10, pady=5, anchor="w")

window.mainloop()
