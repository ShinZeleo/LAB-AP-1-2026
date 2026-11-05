import re

class Pemain:
    def __init__(self, nama_pemain, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama_pemain = nama_pemain
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor_akhir = (0.3*self.nilai_kill) + (0.3*self.nilai_assist) + (0.4*self.nilai_objective)
        return round(skor_akhir, 2)
    
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tentukan_level(self):
        if self.hitung_skor_akhir() >= 85:
            return "Diamond"
        elif self.hitung_skor_akhir() >= 70:
            return "Platinum"
        elif self.hitung_skor_akhir() >= 60:
            return "Gold"
        else:
            return "Bronze"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        level = self.tentukan_level()
        print (f"| {no:<3} | {self.nama_pemain:<12} | {self.id_pemain:<12} | {self.role:<12} | {skor:<12} | {status:<16} | {level:<16} |")

    def tampilkan_statistik(self):
        skor = self.hitung_skor_akhir()
        pemain_unggul = 0
        pemain_perlu_evaluasi = 0
        if skor >= 60:
            pemain_unggul += 1
        else:
            pemain_perlu_evaluasi += 1

        print(f"Total Pemain    : {len(daftar_pemain)}")
        print(f"Pemain Unggul   : {pemain_unggul}")
        print(f"Perlu Evaluasi  : {pemain_perlu_evaluasi}")
        print(f"Rata-rata Skor  : {skor}")
                    

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
jumlah_pemain = int(input("Masukkan Jumlah Pemain: "))
print()

daftar_pemain = []

for i in range (jumlah_pemain):
    print(f"-- Data Pemain ke-{i+1} --")
    nama_pemain = input("Nama             : ").capitalize()
    id_pemain = input("ID Pemain        : ")
    role = input("Role             : ").capitalize()
    nilai_kill = float(     input("Nilai Kill       : "))
    nilai_assist = float(   input("Nilai Assist     : "))
    nilai_objective = float(input("Nilai Objective  : "))
    print()

    pemain = Pemain(nama_pemain, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

garis = "="*105

print("=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<3} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':<12} | {'Status':<16} | {'Level':<16} |")
print(garis)

for i in range(len(daftar_pemain)):
    daftar_pemain[i].tampilkan_data(i+1)
print(garis)

cari_pemain = input("Apakah anda ingin mencari pemain? (Y/N)\n").capitalize()
if cari_pemain == "Y":
    print("=== PENCARIAN PEMAIN ===")
    id_dicari = input("Masukkan ID Pemain: ")
    print()
    for Pemain in daftar_pemain:
            if Pemain.id_pemain == id_dicari:
                print("Data Pemain Ditemukan!")
                print()
                print(f"Nama        : {Pemain.nama_pemain}")
                print(f"ID          : {Pemain.id_pemain}")
                print(f"Role        : {Pemain.role}")
                print(f"Skor Akhir  : {Pemain.hitung_skor_akhir()}")
                print(f"Status      : {Pemain.status_performa()}")
                print(f"Level       : {Pemain.tentukan_level()}")
                print()


print("=== STATISTIK PERTANDINGAN ===")
Pemain.tampilkan_statistik()