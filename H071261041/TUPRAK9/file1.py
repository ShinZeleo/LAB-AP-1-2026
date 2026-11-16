class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective ):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
        self.level = self.tentukan_level()

    def hitung_skor_akhir(self):
        skor_akhir = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor_akhir

    def status_peforma(self):
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
        status = self.status_peforma()
        return (f" {self.nama}".ljust(12) + " | " + self.id_pemain.ljust(10) + " | " + self.role.ljust(10) + " | "  f"{skor:.1f}".ljust(10) + " | " + status.ljust(16) + " | " + self.level.ljust(16) + " | ")

data_pemain = []

print("--- SISTEM PENILAIAN PEFORTMA PEMAIN ---")
while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        else:
            break
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

pemain = 1  #untuk menandai urutan data pemain
while pemain < jumlah_pemain + 1:
    try:
        print(f"\n-- Data Pemain ke-{pemain} --")
        data_nama = input("Nama: ")
        data_id = input("ID Pemain: ")
        data_role = input("Role: ")
        data_kill = int(input("Nilai Kill: "))
        data_assist = int(input("Nilai Assist: "))
        data_objective = int(input("Nilai Objective: "))
        isi_data_pemain = Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective)
        data_pemain.append(isi_data_pemain)
        pemain += 1
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

print("\n--- REKAPITULASI PERFORMA PEMAIN ---")
print("=" * 95)
print("| " + "No".ljust(3) + "|" + " Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " | " + "level".ljust(16) + " | ")
print("=" * 95)
for i, isi in enumerate(data_pemain, start=1):
    print (f"| {i}  |" + isi.tampilkan_data())
print("=" * 95)

print("\n=== PENCARIAN PEMAIN ===")
cari_id = input("Masukkan ID Pemain: ")
data = None

for i in data_pemain:
    if i.id_pemain == cari_id:
        data = i
        break
if data :
    print("\nData Pemain Ditemukan!\n")
    print(f"Nama       : {data.nama}")
    print(f"ID         : {data.id_pemain}")
    print(f"Role       : {data.role}")
    print(f"Skor Akhir : {data.hitung_skor_akhir():.2f}")
    print(f"Status     : {data.status_peforma()}")
else:
    print("\nPemain tidak ditemukan!")

total_pemain = len(data_pemain)
jumlah_unggul = 0
jumlah_evaluasi = 0
total_skor = 0

for i in data_pemain:
    total_skor += i.hitung_skor_akhir()
    if i.status_peforma() == "Unggul":
        jumlah_unggul += 1
    else:
        jumlah_evaluasi += 1

rata_rata_skor = total_skor / total_pemain if total_pemain > 0 else 0

print("\n=== STATISTIK PERTANDINGAN ===")
print(f"Total Pemain       : {total_pemain}")
print(f"Pemain Unggul      : {jumlah_unggul}")
print(f"Perlu Evaluasi     : {jumlah_evaluasi}")
print(f"Rata-rata Skor     : {rata_rata_skor:.2f}")