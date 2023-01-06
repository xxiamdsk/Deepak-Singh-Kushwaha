s = list("deepak singh")
w = list(" abcdefghijklmnopqrsuvwxyz")
c = ""
for i in s:
    for j in w:
        print(c+j)
        
        if(i==j):
            c=c+j
            break
