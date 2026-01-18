A = int(input("Number : "))
B = input("M/F : ")

if(A == 1 or A == 2 and B == "M"):
    print("Fee is 100")

elif(A == 3 or A == 4 or B == "F"):
    print("Fee is 200")

elif(A == 4 and B == "M"):
    print("Fee is 300")

else:
    print("No fee")            