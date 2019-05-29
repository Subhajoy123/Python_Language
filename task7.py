# finding median of three values
print(" enter three no.s")
a=[]
for i in range(3):
    a.append(int(input("enter ")))
a.sort()
print("the median is ", a[1])
