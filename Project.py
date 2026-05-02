data_kendaraan = {
    "1": {"nama": "Golongan I (Mobil/Bus kecil)", "tarif": 1200},
    "2": {"nama": "Golongan II (Truk 2 gandar)", "tarif": 2000},
    "3": {"nama": "Golongan III (Truk 3 gandar)", "tarif": 2500},
    "4": {"nama": "Golongan IV (Truk 4 gandar)", "tarif": 3000},
    "5": {"nama": "Golongan V (Truk ≥5 gandar)", "tarif": 3200}
}

def hitung_diskon(kode, jarak, hari):
    tarif = data_kendaraan[kode]["tarif"]
    total = tarif * jarak
    diskon = 0

    if hari == "weekend":
        diskon += 0.2

    if jarak > 50:
        diskon += 0.1

    if kode in ["3", "4", "5"]:
        diskon += 0.05

    potongan = total * diskon
    bayar = total - potongan

    return total, diskon, potongan, bayar


print("=== PROGRAM TARIF TOL ===")
print("Golongan kendaraan:")
for k, v in data_kendaraan.items():
    print(f"{k}. {v['nama']}")


while True:
    kode = input("Masukkan golongan (1-5): ")
    if kode in data_kendaraan:
        break
    print("❌ Golongan tidak valid!")

while True:
    try:
        jarak = float(input("Masukkan jarak (km): "))
        if jarak > 0:
            break
        print("❌ Jarak harus lebih dari 0!")
    except:
        print("❌ Input harus angka!")


while True:
    hari = input("Hari (weekday/weekend): ").lower()
    if hari in ["weekday", "weekend"]:
        break
    print("❌ Input hari tidak valid!")

total, diskon, potongan, bayar = hitung_diskon(kode, jarak, hari)


print("\n=== STRUK PEMBAYARAN ===")
print("Kendaraan :", data_kendaraan[kode]["nama"])
print(f"Jarak     : {jarak:.0f} km")
print(f"Tarif/km  : Rp {data_kendaraan[kode]['tarif']:,.0f}".replace(",", "."))
print(f"Tarif awal: Rp {total:,.0f}".replace(",", "."))
print(f"Diskon    : {diskon*100:.0f}%")
print(f"Potongan  : Rp {potongan:,.0f}".replace(",", "."))
print(f"Total bayar: Rp {bayar:,.0f}".replace(",", "."))