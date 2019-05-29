# diplaying the type of triangle
a=float(input(" enter the first side "))
b=float(input(" enter the second side "))
c=float(input(" enter the third side "))
if a+b<= c or b+c<=a or c+a<=b :
    print(" not a triangle ")
elif a==b and b== c and c==a:
    print(" the triangle is equilateral ")
elif a==b or b==c or a==c :
    print(" the triangle is isosceles ")
else:
    print(" the triangle is scelene ")

    
