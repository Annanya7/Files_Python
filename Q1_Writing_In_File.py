# Craeting a file
f=open("MyFile1.txt",'w')
print("Enter text @ in the end")
while str!='@':
    str=input("Enter data")
    if(str!='@'):
        f.write(str+"\n")
f.close()
