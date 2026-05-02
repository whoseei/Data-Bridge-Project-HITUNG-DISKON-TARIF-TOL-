# Program Hitung Tarif Tol (Golongan Kendaraan)

Program Python untuk menghitung tarif tol berdasarkan golongan kendaraan, jarak tempuh, dan hari, kemudian memberikan diskon sesuai kondisi tertentu.  
Project ini dibuat sebagai implementasi materi dasar Python seperti input/output, percabangan, perulangan, dan fungsi.

---

## Deskripsi Program

Program akan:
- menerima input golongan kendaraan (1–5)
- menerima input jarak tempuh (km)
- menerima input hari (weekday / weekend)
- menghitung tarif tol
- memberikan diskon sesuai aturan
- menampilkan hasil dalam bentuk struk pembayaran

---

## Golongan Kendaraan & Tarif

| Golongan |   Jenis Kendaraan    | Tarif per km |
|----------|----------------------|--------------|
| 1        | Mobil / Bus kecil    | Rp 1.200     |
| 2        | Truk 2 gandar        | Rp 2.000     |
| 3        | Truk 3 gandar        | Rp 2.500     |
| 4        | Truk 4 gandar        | Rp 3.000     |
| 5        | Truk ≥5 gandar       | Rp 3.200     |

---

## Aturan Diskon

- Weekend → diskon 20%  
- Jarak > 50 km → diskon 10%  
- Golongan 3, 4, 5 → diskon tambahan 5%  

---

## Fitur

- Validasi input (tidak bisa salah)
- Perhitungan otomatis
- Output dalam format Rupiah
- Tampilan seperti struk pembayaran
- Menggunakan dictionary & function