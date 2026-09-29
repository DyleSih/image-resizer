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

- Ketik nama hasil tanpa akhiran. Akhiran (`.jpg`, `.png`) diambil dari file asli, jadi kalau kamu ketik `foto_kecil.jpg` hasilnya menjadi `foto_kecil.jpg.jpg`.
- Nama hasil yang sama dengan file asli akan menimpa file asli.
- Angka yang kamu masukkan membatasi sisi terpanjang gambar. Gambar yang sudah lebih kecil dari angka itu tidak diperbesar.
- Format mengikuti file asli. JPG, PNG, dan format lain yang didukung Pillow bisa dipakai.
- Error `No such file or directory` berarti nama file salah atau gambarnya tidak ada di folder yang sama dengan `resize.py`.
