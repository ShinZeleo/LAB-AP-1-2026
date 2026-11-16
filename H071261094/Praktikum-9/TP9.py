class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
        self.level = self.tentukan_level()  

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return round(skor, 2)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
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

    def tampilkan_data(self, nomor):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        level = self.tentukan_level()
        print(f"| {nomor:<4} | {self.nama:<12} | {self.id_pemain:<12} | {self.role:<12} | {skor:<10.2f} | {status:<14} | {level:<10} |")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong. Silakan coba lagi.")
        else:
            return teks


def input_angka(pesan):
    while True:
        try:
            angka = float(input(pesan))
            if angka < 0 or angka > 100:
                print("Nilai harus antara 0 sampai 100. Silakan coba lagi.")
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah <= 0:
                print("Jumlah pemain harus lebih dari 0. Silakan coba lagi.")
            else:
                return jumlah
        except ValueError:
            print("Input harus berupa bilangan bulat. Silakan coba lagi.")


def id_sudah_ada(daftar_pemain, id_baru):
    for pemain in daftar_pemain:
        if pemain.id_pemain.lower() == id_baru.lower():
            return True
    return False


def input_id(daftar_pemain):
    while True:
        id_pemain = input_teks("ID Pemain: ")
        if id_sudah_ada(daftar_pemain, id_pemain):
            print("ID Pemain sudah digunakan. Silakan masukkan ID lain.")
        else:
            return id_pemain


def cari_pemain(daftar_pemain, id_dicari):
    for pemain in daftar_pemain:
        if pemain.id_pemain.lower() == id_dicari.lower():
            return pemain
    return None


def tampilkan_hasil_pencarian(pemain):
    print("Pemain ditemukan!")
    print(f"Nama           : {pemain.nama}")
    print(f"ID Pemain      : {pemain.id_pemain}")
    print(f"Role           : {pemain.role}")
    print(f"Skor Akhir     : {pemain.hitung_skor_akhir():.2f}")
    print(f"Status Performa: {pemain.status_performa()}")


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

jumlah_pemain = input_jumlah("Masukkan jumlah pemain: ")
daftar_pemain = []

for i in range(jumlah_pemain):
    print()
    print(f"-- Data Pemain ke-{i + 1} --")
    nama = input_teks("Nama: ")
    id_pemain = input_id(daftar_pemain)
    role = input_teks("Role: ")
    nilai_kill = input_angka("Nilai Kill: ")
    nilai_assist = input_angka("Nilai Assist: ")
    nilai_objective = input_angka("Nilai Objective: ")

    pemain_baru = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain_baru)

print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
garis = "=" * 96
print(garis)
print(f"| {'No':<4} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':<10} | {'Status':<14} | {'Level':<10} |")
print(garis)

nomor = 1
for pemain in daftar_pemain:
    pemain.tampilkan_data(nomor)
    nomor += 1

print(garis)


print()
print("=== CARI PEMAIN BERDASARKAN ID ===")
while True:
    id_dicari = input_teks("Masukkan ID pemain yang ingin dicari: ")
    hasil = cari_pemain(daftar_pemain, id_dicari)

    if hasil is not None:
        tampilkan_hasil_pencarian(hasil)
    else:
        print("Pemain tidak ditemukan!")

    jawaban = input("Cari pemain lain? (y/n): ").strip().lower()
    if jawaban != "y":
        break