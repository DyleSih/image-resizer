import os
from PIL import Image

nama_file = input("Nama file gambar: ")
lebar = int(input("Lebar maksimal (px): "))
nama_baru = input("Nama file hasil (tanpa .jpg): ")

gambar = Image.open(nama_file)
gambar.thumbnail((lebar, lebar))

ekstensi = os.path.splitext(nama_file)[1]
gambar.save(nama_baru + ekstensi)
print("Selesai! Disimpan sebagai", nama_baru + ekstensi)