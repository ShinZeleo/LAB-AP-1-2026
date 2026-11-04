class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        return f" {self.nama}".ljust(12) + " | " + self.id_pemain.ljust(10) + " | " + self.role.ljust(10) + " | " + f"{skor}".ljust(10) + " | " + status.ljust(16) + " |"

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")
# input
jumlah_pemain = int(input("Masukkan jumlah pemain: "))

daftar_pemain = []
for i in range(1, jumlah_pemain+1):
    print(f"\n--- Data Pemain ke-{i} ---")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = int(input("Nilai Kill: "))
    nilai_assist = int(input("Nilai Assist: "))
    nilai_objective = int(input("Nilai Objective: "))

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

# output
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("="*78)
print("| " + "No".ljust(3) + "|" + " Nama".ljust(12) + " | " + "ID Pemain".ljust(10) + " | " + "Role".ljust(10) + " | " + "Skor Akhir".ljust(10) + " | " + "Status".ljust(16) + " |")
print("="*78)
for i, pemain in enumerate(daftar_pemain, start=1):
    print(f"| {i}  |" + pemain.tampilkan_data())
print("="*78)