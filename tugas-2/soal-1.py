def welcome():
    print("\nSelamat Datang!\n")

def show_menu():
    print("---MENU---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def show_contact_list():
    print("\nDaftar Kontak:")
    for i in range(len(contact_list)):
        show = contact_list[i]
        print("Nama: {}".format(show["Nama"]))
        print("Nomor Telepon: {}".format(show["Nomor Telepon"]))
        print() 

def add_contact():
    print()
    insert = {"Nama":"","Nomor_Telepon":""}
    insert["Nama"] = input("Masukkan Nama: ")
    insert["Nomor Telepon"] = input("Masukkan Nomor Telepon: ")
    contact_list.append(insert)
    print("\nKontak Berhasil Ditambahkan\n")

def close():
    print("\nProgram Selesai, Sampai Jumpa\n")

def not_menu():
    print("\nMenu Tidak Tersedia\n")

contact_list = []
welcome()
while True:
    show_menu()
    option = int(input("\nPilih Menu: "))  
    if option == 1:
        if contact_list == []:
            print("\nAnda Belum Menambahkan Kontak\n")
        else:
            show_contact_list()
    elif option == 2: 
        add_contact()
    elif option == 3:
        close()
        exit()
    else:
        not_menu()