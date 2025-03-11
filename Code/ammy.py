name=input("enter the name : ")

math=float(input("Enter the maths marks : "))
chem=float(input("Enter the chem marks : "))
phy=float(input("Enter the phy marks : "))


if math>=40 and chem>=40 and phy>=40:
    percentage=((math+chem+phy)/300)*100
    print(round(percentage))
    
    if math>=90 and chem>=90 and phy>=90:
        print("A ' Grade ")
    elif math>=79 and chem>=79 and phy>=79:
        print("B ' Grade ")    
    else:
        print("Fail")