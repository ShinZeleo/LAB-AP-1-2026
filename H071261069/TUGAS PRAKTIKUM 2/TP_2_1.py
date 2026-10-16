# TASK I
print("=== Tingkat Kepedasan ===")
print("Level Aman = 0 - 10")
print("Level Sedang = 11 - 40")
print("Level Pedas = 41 - 70")
print("Level Ekstrem = Di atas 70")

input_level = int(input('Masukkan presentase cabai :'))

if input_level <  0:
    print("Invalid input !, Masukkan presentase yang sesuai")
elif input_level <= 10 : 
    print("Level Aman")
elif input_level <= 40 :
    print("Level Sedang")
elif input_level <= 70 :
    print("Level Pedas")
else:
    print("Level Ekstrem")