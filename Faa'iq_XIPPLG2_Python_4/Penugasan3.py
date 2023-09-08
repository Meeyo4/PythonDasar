import tkinter as tk


class DataSiswaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Data Siswa")
        
        self.label_nama = tk.Label(root, text="Nama Lengkap:")
        self.label_nama.pack()
        
        self.entry_nama = tk.Entry(root)
        self.entry_nama.pack()
        
        self.label_tanggal_lahir = tk.Label(root, text="Tanggal Lahir:")
        self.label_tanggal_lahir.pack()
        
        self.entry_tanggal_lahir = tk.Entry(root)
        self.entry_tanggal_lahir.pack()
        
        self.label_asal_sekolah = tk.Label(root, text="Asal Sekolah:")
        self.label_asal_sekolah.pack()
        
        self.entry_asal_sekolah = tk.Entry(root)
        self.entry_asal_sekolah.pack()
        
        self.label_nisn = tk.Label(root, text="NISN:")
        self.label_nisn.pack()
        
        self.entry_nisn = tk.Entry(root)
        self.entry_nisn.pack()
        
        self.label_nama_ayah = tk.Label(root, text="Nama Ayah:")
        self.label_nama_ayah.pack()
        
        self.entry_nama_ayah = tk.Entry(root)
        self.entry_nama_ayah.pack()
        
        self.label_nama_ibu = tk.Label(root, text="Nama Ibu:")
        self.label_nama_ibu.pack()
        
        self.entry_nama_ibu = tk.Entry(root)
        self.entry_nama_ibu.pack()
        
        self.label_no_telepon = tk.Label(root, text="No Telepon / HP:")
        self.label_no_telepon.pack()
        
        self.entry_no_telepon = tk.Entry(root)
        self.entry_no_telepon.pack()
        
        self.label_alamat = tk.Label(root, text="Alamat:")
        self.label_alamat.pack()
        
        self.entry_alamat = tk.Entry(root)
        self.entry_alamat.pack()
        
        self.button_simpan = tk.Button(root, text="Simpan", command=self.simpan_data)
        self.button_simpan.pack()
        
        self.button_hapus = tk.Button(root, text="Hapus", command=self.hapus_data)
        self.button_hapus.pack()
        
        self.text_hasil = tk.Text(root, height=10, width=40)
        self.text_hasil.pack()
        
    def simpan_data(self):
        nama = self.entry_nama.get()
        tanggal_lahir = self.entry_tanggal_lahir.get()
        asal_sekolah = self.entry_asal_sekolah.get()
        nisn = self.entry_nisn.get()
        nama_ayah = self.entry_nama_ayah.get()
        nama_ibu = self.entry_nama_ibu.get()
        no_telepon = self.entry_no_telepon.get()
        alamat = self.entry_alamat.get()
        
        data_siswa = f"Nama Lengkap: {nama}\nTanggal Lahir: {tanggal_lahir}\nAsal Sekolah: {asal_sekolah}\nNISN: {nisn}\nNama Ayah: {nama_ayah}\nNama Ibu: {nama_ibu}\nNo Telepon / HP: {no_telepon}\nAlamat: {alamat}\n"
        
        self.text_hasil.insert(tk.END, data_siswa)
        
    def hapus_data(self):
        self.entry_nama.delete(0, tk.END)
        self.entry_tanggal_lahir.delete(0, tk.END)
        self.entry_asal_sekolah.delete(0, tk.END)
        self.entry_nisn.delete(0, tk.END)
        self.entry_nama_ayah.delete(0, tk.END)
        self.entry_nama_ibu.delete(0, tk.END)
        self.entry_no_telepon.delete(0, tk.END)
        self.entry_alamat.delete(0, tk.END)
        self.text_hasil.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataSiswaApp(root)
    root.mainloop()
