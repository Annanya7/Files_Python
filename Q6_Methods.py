with open('line.txt','w') as f:
    f.write("Amazing Python")
with open('line.txt','r') as f:
    for line in f:
        print(line)
