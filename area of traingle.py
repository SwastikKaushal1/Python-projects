a=float(input("Enter the first side "))
b=float(input("Enter the second side"))
c=float(input("Enter the third side"))
p=a+b+c
print("The perimeter of the triangle =",p)
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(" Area of the triangle =",area)
