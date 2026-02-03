import json

FILE = "data_uang.json"

# ===== LOAD & SAVE DATA =====
def simpan_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file)

def muat_data():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "saldo": 0,
            "pemasukan": [],
            "pengeluaran": []
        }

data = muat_data()

# ===== FUNGSI SESUAI KERANGKA GURU =====
def tambah_pemasukan():
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    data["saldo"] += jumlah
    data["pemasukan"].append(jumlah)
    simpan_data(data)
    print(f"Pemasukan Rp{jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > data["saldo"]:
        print("⚠️ Saldo tidak cukup!")
    else:
        data["saldo"] -= jumlah
        data["pengeluaran"].append(jumlah)
        simpan_data(data)
        print(f"Pengeluaran Rp{jumlah} berhasil dicatat!")

def lihat_saldo():
    print(f"Saldo saat ini: Rp{data['saldo']}")

def laporan():
    print("\n=== Laporan Keuangan ===")
    print(f"Total pemasukan   : Rp{sum(data['pemasukan'])}")
    print(f"Total pengeluaran : Rp{sum(data['pengeluaran'])}")
    print(f"Saldo akhir       : Rp{data['saldo']}")

def menu():
    print("\n=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan keuangan")
    print("5. Keluar")

# ===== PROGRAM UTAMA =====
while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
