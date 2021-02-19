a=int(input('angka pertama : '))
b=int(input('angka kedua :'))

if a>b:
    print("{} lebih besar dari {}".format(a,b))
elif a==b:
    print("{} sama dengan dari {}".format(a,b))
else:
    print("{} lebih kecil dari {}".format(a,b))

num=int(input('Angka: ')) 

if num % 2 ==0:
    print("Angka {} adalah bilangan genap".format(num))
else:
    print("Angka {} adalah bilangan ganjil".format(num))