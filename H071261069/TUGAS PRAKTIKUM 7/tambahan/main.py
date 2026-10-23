import os

old_file = "tugas_lama.txt"
new_file = "tugas_baru.txt"

with open(old_file, "w") as f:
    f.write('Hello World!')

try:
    os.rename(old_file, new_file)
    print("File berhasil diubah menjadi tugas_baru.txt")
except IOError:
    print(f"Error: file {old_file} tidak bisa di rename")