class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        # Konversi ke float dilakukan di luar atau di dalam init aman jika input sudah divalidasi
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
print("--- SISTEM PENILAIAN PERFORMA PEMAIN---")

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
            data_kill = float(input("Nilai Kill".ljust(16) + ": "))
            break
        except ValueError:
            print("Input salah! Nilai Kill harus berupa angka.")

   
    while True:
        try:
            data_assist = float(input("Nilai Assist".ljust(16) + ": "))
            break
        except ValueError:
            print("Input salah! Nilai Assist harus berupa angka.")

    
    while True:
        try:
            data_objective = float(input("Nilai Objective".ljust(16) + ": "))
            break
        except ValueError:
            print("Input salah! Nilai Objective harus berupa angka.")

    isi_data_pemain = Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective)
    data_pemain.append(isi_data_pemain)
    pemain += 1


print("\n--- REKAPITULASI PERFORMA PEMAIN---")
print("=" * 92)
print("| " + "No".ljust(3) + "| " + "Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " | " + "Level".ljust(10) + " |")
print("=" * 92)
for i, isi in enumerate(data_pemain, start=1):
    print(f"| {str(i).ljust(3)}| " + isi.tampilkan_data())
print("=" * 92)
