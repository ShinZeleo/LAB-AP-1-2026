catatan = input("masukkan catatan kegiatan kuliah: ")

with open("catatan.txt", "a") as f:
    f.write("\n")
    f.write(catatan)
print ("Catatan berhasil")
