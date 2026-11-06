input_level = int(input("Masukkan persentase: "))

if input_level < 0:
    print("Invalid")
elif input_level <= 10:
    print ("Level Aman")
elif input_level <= 40:
    print ("Level Sedang")
elif input_level <= 70:
    print ("Level Pedas")
else:
    print ("Level Ekstrem")

  