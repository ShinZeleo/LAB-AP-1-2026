class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = float(nilai_kill)
        self.nilai_assist = float(nilai_assist)
        self.nilai_objective = float(nilai_objective)
        self.level = self.tentukan_level() 

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return round(skor, 2)

    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tentukan_level(self):
        skor = self.hitung_skor_akhir()
        if skor >= 85:
            return "Diamond"
        elif skor >= 70:
            return "Platinum"
        elif skor >= 60:
            return "Gold"
        else:
            return "Bronze"

    def tampilkan_data(self):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        self.level = self.tentukan_level() 
        return f"{self.nama}".ljust(12) + " | " + f"{self.id_pemain}".ljust(10) + " | " + f"{self.role}".ljust(10) + " | " + f"{skor:.2f}".ljust(10) + " | " + f"{status}".ljust(16) + " | " + f"{self.level}".ljust(10) + " | "

data_pemain = []
print("--- SISTEM PENILAIAN PERFORMA PEMAIN ---")

while True:
    try:
        jumlah_pemain = int(input("\nMasukkan Jumlah Pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input Tidak Valid! Masukkan angka bulat untuk jumlah pemain.")

pemain = 1
while pemain <= jumlah_pemain:
    print(f"\n--Data Pemain ke-{pemain}--")
    data_nama = input("Nama".ljust(16) + ": ")
    data_id = input("ID Pemain".ljust(16) + ": ")
    data_role = input("Role".ljust(16) + ": ")
    
    while True:
        try:
            n_kill = float(input("Nilai Kill".ljust(16) + ": "))
            n_assist = float(input("Nilai Assist".ljust(16) + ": "))
            n_obj = float(input("Nilai Objective".ljust(16) + ": "))
            break
        except ValueError:
            print("Input nilai tidak valid! Masukkan angka.")

    p = Pemain(data_nama, data_id, data_role, n_kill, n_assist, n_obj)
    data_pemain.append(p)
    pemain += 1

print("\n" + "="*85)
print("REKAPITULASI PERFORMA PEMAIN".center(85))
print("="*85)
print("Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " | " + "Level".ljust(10) + " | ")
print("-"*85)
for p in data_pemain:
    print(p.tampilkan_data())
print("="*85)

print("\n*** PENCARIAN PEMAIN ***\n")
cari_id = input("Masukkan ID Pemain: ")

pemain_ditemukan = None

for p in data_pemain:
    if p.id_pemain == cari_id:
        pemain_ditemukan = p
        break

if pemain_ditemukan:
    print("\nData Pemain Ditemukan!\n")
    print("Nama".ljust(12) + f": {pemain_ditemukan.nama}")
    print("ID".ljust(12) + f": {pemain_ditemukan.id_pemain}")
    print("Role".ljust(12) + f": {pemain_ditemukan.role}")
    print("Skor Akhir".ljust(12) + f": {pemain_ditemukan.hitung_skor_akhir():.2f}")
    print("Status".ljust(12) + f": {pemain_ditemukan.status_performa()}")
else:
    print("\nPemain tidak ditemukan!")

total_pemain = len(data_pemain)
jumlah_unggul = 0
jumlah_evaluasi = 0
total_skor = 0

for p in data_pemain:
    skor = p.hitung_skor_akhir()
    status = p.status_performa()
    total_skor += skor
    
    if status == "Unggul":
        jumlah_unggul += 1
    elif status == "Perlu Evaluasi":
        jumlah_evaluasi += 1

rata_rata_skor = total_skor / total_pemain if total_pemain > 0 else 0

print("\n=== STATISTIK PERTANDINGAN ===\n")
print("Total Pemain".ljust(16) + f": {total_pemain}")
print("Pemain Unggul".ljust(16) + f": {jumlah_unggul}")
print("Perlu Evaluasi".ljust(16) + f": {jumlah_evaluasi}")
print("Rata-rata Skor".ljust(16) + f": {rata_rata_skor:.2f}")