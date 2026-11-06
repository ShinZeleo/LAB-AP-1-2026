level_pedas = int(input("Masukkan persentase cabe: "))

if level_pedas < 0:
    print("invalid")
elif level_pedas >= 0:
     print("Level Aman")
elif level_pedas <= 10:
    print("Level Sedang")
elif level_pedas >= 40:
    print("Level Pedas")
elif level_pedas >= 70:
    print("Level Ekstrem")
else: 
    print("Invalid")
