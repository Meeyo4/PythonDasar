import tkinter as tk
from datetime import datetime


class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Parkir")
        
        self.pelanggan = []
        self.biaya_per_jam = 2000
        
        self.label_cari_knalpot = tk.Label(root, text="Cari No Plat:")
        self.label_cari_knalpot.pack()
        
        self.entry_cari_knalpot = tk.Entry(root)
        self.entry_cari_knalpot.pack()
        
        self.button_cari_knalpot = tk.Button(root, text="Cari", command=self.cari_no_plat)
        self.button_cari_knalpot.pack()
        
        self.label_no_plat = tk.Label(root, text="Nomor Plat Polisi:")
        self.label_no_plat.pack()
        
        self.entry_no_plat = tk.Entry(root)
        self.entry_no_plat.pack()
        
        self.label_waktu_masuk = tk.Label(root, text="Waktu Masuk (HH:MM):")
        self.label_waktu_masuk.pack()
        
        self.entry_waktu_masuk = tk.Entry(root)
        self.entry_waktu_masuk.pack()
        
        self.button_parkir = tk.Button(root, text="Parkir", command=self.parkir)
        self.button_parkir.pack()
        
        self.label_waktu_keluar = tk.Label(root, text="Waktu Keluar (HH:MM):")
        self.label_waktu_keluar.pack()
        
        self.entry_waktu_keluar = tk.Entry(root)
        self.entry_waktu_keluar.pack()
        
        self.button_keluar = tk.Button(root, text="Keluar", command=self.keluar)
        self.button_keluar.pack()
        
        self.label_list_pelanggan = tk.Label(root, text="List Pelanggan Terakhir Keluar:")
        self.label_list_pelanggan.pack()
        
        self.listbox_pelanggan_keluar = tk.Listbox(root, width=40)
        self.listbox_pelanggan_keluar.pack()
        
        self.label_list_banyak_bayar = tk.Label(root, text="List Pelanggan Banyak Bayar:")
        self.label_list_banyak_bayar.pack()
        
        self.listbox_banyak_bayar = tk.Listbox(root, width=40)
        self.listbox_banyak_bayar.pack()
    
    def cari_no_plat(self):
        no_plat = self.entry_cari_knalpot.get()
        found = False
        for pelanggan in self.pelanggan:
            if pelanggan["no_plat"] == no_plat:
                found = True
                self.entry_no_plat.delete(0, tk.END)
                self.entry_no_plat.insert(0, pelanggan["no_plat"])
                break
        if not found:
            self.entry_no_plat.delete(0, tk.END)
            self.entry_no_plat.insert(0, "Tidak ditemukan")
    
    def parkir(self):
        no_plat = self.entry_no_plat.get()
        waktu_masuk = self.entry_waktu_masuk.get()
        
        pelanggan_baru = {
            "knalpot": "",
            "no_plat": no_plat,
            "waktu_masuk": waktu_masuk,
            "waktu_keluar": "",
            "biaya": 0
        }
        self.pelanggan.append(pelanggan_baru)
        
        self.entry_cari_knalpot.delete(0, tk.END)
        self.entry_no_plat.delete(0, tk.END)
        self.entry_waktu_masuk.delete(0, tk.END)
        
        self.listbox_pelanggan_keluar.insert(tk.END, f"No. Plat: {no_plat}, Waktu Masuk: {waktu_masuk}")
    
    def keluar(self):
        no_plat = self.entry_no_plat.get()
        waktu_keluar = self.entry_waktu_keluar.get()
        
        for pelanggan in self.pelanggan:
            if pelanggan["no_plat"] == no_plat:
                pelanggan["waktu_keluar"] = waktu_keluar
                waktu_masuk = datetime.strptime(pelanggan["waktu_masuk"], "%H:%M")
                waktu_keluar = datetime.strptime(waktu_keluar, "%H:%M")
                durasi = waktu_keluar - waktu_masuk
                durasi_jam = durasi.total_seconds() / 3600
                biaya = self.biaya_per_jam * durasi_jam
                pelanggan["biaya"] = biaya
                self.listbox_banyak_bayar.insert(tk.END, f"No. Plat: {no_plat}, Biaya: {biaya}")
                self.listbox_pelanggan_keluar.delete(tk.END)
                break
        
        self.entry_no_plat.delete(0, tk.END)
        self.entry_waktu_keluar.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()
