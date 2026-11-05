#MAAF KAK ND TAU
class Pemain:
    def __init__(self, nama, role, skor_kill, skor_objective, skor_teamwork):
        self.nama = nama
        self.role = role
        self.skor_kill = skor_kill
        self.skor_objective = skor_objective
        self.skor_teamwork = skor_teamwork
        self.skor_akhir = self.hitung_skor_akhir()
        self.status = self.tentukan_status()
        self.level = self.tentukan_level()

    def hitung_skor_akhir(self):
        return (self.skor_kill + self.skor_objective + self.skor_teamwork) / 3

    def tentukan_status(self):
        if self.skor_akhir >= 75:
            return "Unggul"
        elif self.skor_akhir >= 60:
            return "Baik"
        else:
            return "Perlu Evaluasi"

    def tentukan_level(self):
        if self.skor_akhir >= 85:
            return "Diamond"
        elif self.skor_akhir >= 70:
            return "Platinum"
        elif self.skor_akhir >= 60:
            return "Gold"
        else:
            return "Bronze"

    def tampilkan_data(self, nomor):
        print(f"{nomor} | {self.nama} | {self.role} | {self.skor_akhir:.2f} | {self.status} | {self.level}")

    def tampilkan_detail(self):
        print(f"Nama: {self.nama}")
        print(f"ID: {self.id_pemain}")
        print(f"Role: {self.role}")
        print(f"skor_akhir: {self.skor_akhir}")


def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 hingga 100")
        except ValueError:
            print("Input tidak valid, harus berupa angka")

def input_id_pemain(pesan):
    while True:
        try:
            id_pemain = input("ID_pemain:")
            if id_pemain == "":
                print("ID pemain tidak boleh kosong.")
                continue
            sudah_ada = False
            for p in daftar_pemain:
                if p.id_pemain == id_pemain:
                    sudah_ada = True
                    break
            if sudah_ada:
                print("ID pemain sudah digunakan, silakan masukkan ID lain.")
                continue
            else:
                return id_pemain

def main():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    try:
        jumlah_pemain = int(input("Masukkan jumlah pemain: "))
    except ValueError:
        print("Input jumlah pemain harus berupa angka.")
        return

    daftar_pemain = []

    for i in range(jumlah_pemain):
        print(f"\nData Pemain ke-{i + 1}")
        nama = input("Nama: ")
        role = input("Role: ")
        skor_kill = input_nilai("Nilai Kill (0-100): ")
        skor_objective = input_nilai("Nilai Objective (0-100): ")
        skor_teamwork = input_nilai("Nilai Teamwork (0-100): ")

        daftar_pemain.append(Pemain(nama, role, skor_kill, skor_objective, skor_teamwork))

    print("\n" + "=" * 75)
    print("REKAPITULASI PERFORMA PEMAIN")
    print("=" * 75)
    print("No | Nama | Role | Skor Akhir | Status | Level")
    print("-" * 75)

    for idx, p in enumerate(daftar_pemain, start=1):
        p.tampilkan_data(idx)

main()   
#MAAF KAK ND TAU