#dic 1
pelanggan = {
    "Nama" : "Astuti",  #key : value
    "Umur" : 20
}

print(pelanggan)
 #dic 2
pelanggan_2 = {
    "Nama" : "Joko",  #key : value
    "Umur" : 23
}

print("Nama : {}".format(pelanggan["Nama"]))
print("Umur : {}".format(pelanggan["Umur"]))


#ganti nilai dictionary
pelanggan["Umur"]=21
print(pelanggan)

#loop throught dict
for x in pelanggan:
    print(x) #eks key dic 1
    print(pelanggan[x]) #eks value dic 1
    print(pelanggan_2[x]) #eks value dic 2

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

print(daftar_pelanggan) #print list

for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan["Nama"]))
    print("Umur: {}".format(pelanggan["Umur"]))