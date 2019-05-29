# product of all elements of a list

def prd(a):
    p=1
    for i in a:
        p=p*i
    print(" the product of elements ",p)
a=[]
n=int(input(" enter the size "))
for i in range(n):
    a.append(int(input(" enter the no.")))
prd(a)
             

