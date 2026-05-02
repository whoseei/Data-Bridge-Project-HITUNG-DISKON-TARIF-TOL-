data_kendaraan = {
    "mb": {"nama": "Mobil", "tarif": 8000},
    "tr": {"nama": "Truk", "tarif": 10000},
    "mt": {"nama": "Motor", "tarif": 5000}
}

def hitung_diskon(kode, jarak, hari):
    tarif = data_kendaraan[kode]["tarif"]
    total = tarif * jarak
    diskon = 0

    if hari == "weekend":
        diskon += 0.2

    if jarak > 50:
        diskon += 0.1

    if kode == "tr":
        diskon += 0.05

    potongan = total * diskon
    bayar = total - potongan

    return total, diskon, bayar

print("=== PROGRAM TARIF TOL ===")
print("Kode kendaraan: mb (Mobil), tr (Truk), mt (Motor)")

while True:
    kode = input("Masukkan kode kendaraan: ").lower()
    if kode in data_kendaraan:
        break
    print("❌ Kode tidak valid! (mb/tr/mt)")

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

total, diskon, bayar = hitung_diskon(kode, jarak, hari)

print("\n=== RINCIAN ===")
print("Kendaraan :", data_kendaraan[kode]["nama"])
print(f"Jarak     : {jarak:.0f} km")
print(f"Tarif awal: Rp {total:,.0f}".replace(",", "."))
print(f"Diskon    : {diskon*100:.0f}%")
print(f"Total bayar: Rp {bayar:,.0f}".replace(",", "."))