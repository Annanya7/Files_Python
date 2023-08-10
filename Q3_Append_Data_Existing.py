f=open("MyFile.txt",'a+')
print("Enter data")
while str!='@':
    str=input("Enter ur data")
    if str!='@':
        f.write(str+"\n")
f.seek(5,1)
print("Contents of file are")
str=f.read()
print(str)
f.close()
