class Pemain:
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    def hitung_skor_akhir(self):
        skor_akhir = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor_akhir

    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        pass


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
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        
        try:
            kill = float(input("Nilai Kill: "))
            assist = float(input("Nilai Assist: "))
            objective = float(input("Nilai Objective: "))
        except ValueError:
            print("Nilai komponen harus berupa angka. Silakan ulangi untuk pemain ini.")
            continue

        pemain = Pemain(nama, id_pemain, role, kill, assist, objective)
        daftar_pemain.append(pemain)

    print("\n" + "=" * 75)
    print("REKAPITULASI PERFORMA PEMAIN")
    print("=" * 75)
    print(f"{'No':<3} | {'Nama':<10} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15}")
    print("-" * 75)

    for idx, p in enumerate(daftar_pemain, start=1):
        skor = p.hitung_skor_akhir()
        status = p.status_performa()
        print(f"{idx:<3} | {p.nama:<10} | {p.id_pemain:<12} | {p.role:<10} | {skor:<10.2f} | {status:<15}")

    print("=" * 75)


main()