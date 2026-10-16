#Tugas no 1
level_cabai = int(input("Masukkkan persentase cabai :"))

if level_cabai <0:
    print ("input tidak valid")
elif level_cabai <=10:
    print("level aman")
elif level_cabai <=40:
    print("Levl Sedang")
elif level_cabai <=70:
    print("Level Pedas")
elif level_cabai >70:
    print("Level Ekstrem")
