# r = open("file.txt","r")

# print(r.read())

# r.close()

# r = open("resource/hello.txt","r")

# print(r.read())

# r.close()

#read per row

r = open("resource/hello.txt","r")

temp2= r.readlines()
# print(temp2)

a = []
for li in temp2:
    a.append(li.strip())

print (a[1])
r.close()