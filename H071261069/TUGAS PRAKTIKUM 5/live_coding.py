'''nomor 1'''
s1 = "Abc"
s2 = "Xyz"
hasil = ""
for i in range(max(len(s1),len(s2))):
    if i < len(s1):
        hasil += s1[i]
    if i < len(s2):
        hasil += s2[-1 - i]
print(hasil)

'''nomor 2'''
kata = input("Masukkan nama: ")
pertama = kata[0]
indeks_tengah= len(kata)//2
tengah =  kata[indeks_tengah]
terakhir = kata[-1]
hasil = pertama + tengah + terakhir
print(hasil)

'''nomor 3'''
pertama = input("Masukkan kata peratama : ")
kedua = input("Masukkan kata kedua : ")

def bersih(s):
    return sorted(s.replace(" ","").lower())

print(bersih(pertama) == bersih(kedua))

