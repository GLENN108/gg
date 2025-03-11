# create user defined function to cal , mean median , standard deviation
import math 
l=[1,2,3,4,5]
print(len(l))

def means(ln):
    sum=0
    for i in ln:
        sum+=i
        g=sum/len(ln)
    return g        
    
def median(ln):
    h=(len(ln)//2)
    return h

def devy(n,l):
    sum=0
    print(n,l)
    for i in l:
        sum+=(i-n)**2
        return sum
                
print("the mean of the list is  :: ",means(l))
print("the median of the list is  :: ",median(l))
print("the standard deviation of the list is  :: ",devy(means(l),l))

sum=0
for i in l:
    sum+=(i-3)**2
    print(sum)
    print((sum/len(l)))
    p=math.sqrt((sum/len(l)))
    print(p)