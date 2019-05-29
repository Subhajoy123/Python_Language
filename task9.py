# displaying the no. of odd and even no.s
a=[]
c=0
d=0
n=int(input("enter the no. of no.s "))
for i in range(n):
    a.append(int(input("enter ")))
for i in range(n):
    if a[i]%2==0:
        c=c+1
    else:
        d=d+1
print("even numbers", c)
print("odd numbers", d)
