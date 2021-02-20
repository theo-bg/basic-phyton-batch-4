count = int(input('Berapa data: '))

nama_pelanggan = [] #list
umur_pelanggan = [] #list

for i in range (count):
    print("Data ke {}".format(i+1)) #print Data ke: inputan range count
    nama = input("Nama: ") #input nama
    umur = int(input("Umur: ")) #input umur
    #program akan eksekusi sebanyak inputan banyakanya data di count
    
    nama_pelanggan.append(nama) #memasukkan inputan nama ke list nama_pelanggan
    umur_pelanggan.append(umur) #memasukkan inputan umur ke list umur_pelanggan
    
print(nama_pelanggan) #menampilakn list
print(umur_pelanggan) #menampilkan list

for i in range(len(nama_pelanggan)): #i berisi sebanyak n data di nama_pelanggan
    print("Pelanggan {} berumur {}".format(nama_pelanggan[i],umur_pelanggan[i])) #menampilkan sebanyak data yang ada di list nama_pelanggan