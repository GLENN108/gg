a=45674
b=str(a)
x=int(input("enter "))
rh=[]
lh=[]

for i in range(len(b)):
    if i <= len(b)/2:
        rh = b[i]
    else:
        lh = b[i]
print(rh,lh)
    
    