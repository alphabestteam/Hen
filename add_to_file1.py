f = open("hen.txt","w")
f.write("my name is hen")
f.close()

f = open("hen.txt","r")
print(f.read())
f.close()