for i in range(2):
    print("i : {}".format(i)) #eksekusi data i pertama
    for j in range(4):
        print("j : {}".format(j)) #eksekusi semua data j, lalu akan kembali ke eksekusi i data selanjutnya sampai data i habis
    print("-----")

for baris in range(2): #eksekusi data baris yg pertama
    for kolom in range (3): #eksekusi smeua data kolom lalu lanjut eksekusi data baris yg selanjutnya
        print("{}.{}".format(baris+1,kolom+1), end = " ")
    print()