def campur_string(s1, s2):
    s2_terbalik = s2[::-1] #karakter terakhir s2 jadi yang pertama
    terpendek = min(len(s1), len(s2))

    s3 = ""
    for i in range(terpendek):
        s3 += s1[i] + s2_terbalik[i]

    #Ketika salah satu string lebih panjang, tambahkan sisa karakter dari string tersebut
    s3 += s1[terpendek:] + s2_terbalik[terpendek:]
    return s3


def main():
    s1 = input("Masukkan s1: ")
    s2 = input("Masukkan s2: ")
    print('Hasil mixed ="' + campur_string(s1, s2) + '"')

main()