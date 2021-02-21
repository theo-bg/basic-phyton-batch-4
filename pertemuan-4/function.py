#function no parameter
def my_function():
    print("Halo")

my_function()

#function with parameter
def hello(first_name,last_name): #definisi function
    print("Halo " + first_name + " " + last_name) #print jika function dipanggil

hello("Theo","Gultom") #call function
hello("Sylvia","Gultom")
hello("Filumena","Gultom")
hello("Samantha","Gultom")

#function with default parameter
def hello(first_name,last_name="(kosong)"): #definisi function dengan default
    print("Halo " + first_name + " " + last_name) #print jika function dipanggil

hello("Theo") #call function

#function keyword parameter
def my_function2(child4, child3, child2, child1): #definisi function
    print("The youngest child is " + child4) #print jika function dipanggil

my_function2(child1 = "Theo", child2 = "Agatha", child3 = "Tanta", child4 = "Quin") #call function

#function return value
def tambah(x,y):
    tambah =  x + y
    return tambah

jumlah = tambah(2,9)
print(jumlah)

def total():
    return 20

totals = total()
print(totals)