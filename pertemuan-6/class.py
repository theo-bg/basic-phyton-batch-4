class MyClass: #class
    x = 5

obj1 = MyClass() #object
obj2 = MyClass() 

print(obj1) #print tipe objek
print(obj1.x) #print object.variabel dari class
print(obj2.x)

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("Hello my name is " + self.name)

nama = input ("Nama: ")
umur = input ("Umur: ")

p1 = Person(nama, umur)
print(p1)
print(p1.name)
print(p1.age)
p1.greeting()

p1 = Person("Theo", 20)
print(p1)
print(p1.name)
print(p1.age)

p2 = Person("Agatha", 19)
print(p2)
print(p2.name)
print(p2.age)

