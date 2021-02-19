a=float(input("Masukkan nilai ujian teori : "))
b=float(input("Masukkan nilai ujian praktik : "))

if a >= 70 and b >= 70:
    print("Selamat, anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktik.")
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktik")