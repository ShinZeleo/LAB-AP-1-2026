matkul = input("masukkan matkul: ")
dosen = input("masukkan dosen: ")

with open("jadwal kak imam.txt", "w") as f:
    f.write(f"mata kuliah: {matkul} \n")
    f.write(f"dosen: {dosen} \n")
print("jadwal berhasil diperbarui!")

with open("jadwal kak imam.txt", "r") as f:
    print(f.read())
