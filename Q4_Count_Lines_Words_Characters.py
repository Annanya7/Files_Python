import os,sys
fname=input("Enter filename")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+"does not exist")
    sys.exit()
cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)
print("lines",cl)
print("words",cw)
print("characters",cc)
