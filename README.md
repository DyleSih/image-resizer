# Image Resizer

Perkecil ukuran gambar lewat terminal tanpa membuatnya gepeng. Kamu isi ukuran maksimal dan nama file hasilnya sendiri. Python 3, dependensi: `pillow`.

## Instal

```
git clone https://github.com/<user>/image-resizer.git
cd image-resizer
pip install pillow
```

## Pakai

Taruh gambar di folder yang sama dengan `resize.py`, lalu jalankan:

```
python resize.py
```

Program menanyakan nama file gambar, ukuran maksimal, dan nama file hasil:

```
Nama file gambar: foto.jpg
Lebar maksimal (px): 500
Nama file hasil (tanpa .jpg): foto_kecil
Selesai! Disimpan sebagai foto_kecil.jpg
```

Foto 4000x3000 dengan angka 500 menjadi 500x375. Hasilnya tersimpan di folder yang sama.

## Catatan

- Ketik nama hasil tanpa `.jpg` atau `.png`, karena akhirannya ditambah otomatis. Kalau kamu ketik `foto_kecil.jpg`, hasilnya jadi `foto_kecil.jpg.jpg`.
- Jangan pakai nama yang sama dengan file asli. Kalau sama, file asli akan tertimpa.
- Angka yang kamu isi adalah batas untuk sisi terpanjang gambar. Gambar yang sudah lebih kecil tidak dibesarkan.
- Format hasil sama dengan file asli.
- Muncul error `No such file or directory`? Cek nama filenya, dan pastikan gambarnya satu folder dengan `resize.py`.
