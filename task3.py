# list of words finding the largest
b=[]
def lword(a):
    k=" "
    for i in a:
        if len(i) > len(k) :
           k=i
    return k
n=int(input(" enter the no. of words "))
for i in range(n):

    b.append(str(input(" enter the words ")))
print(" the largest word is ", end="") 
print(lword(b)) 
      


