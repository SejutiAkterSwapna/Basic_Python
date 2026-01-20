#write a program to find the greatest of 3 numbers entered by the user.

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if(a>b and a>c):
    print("Greatest number is :", a)
elif(b>a and b>c):
    print("Greatest number is :", b) 
else:
    print("Greatest number is :", c)      