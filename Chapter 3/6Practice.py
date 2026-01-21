#WAP to check if a list contains a palindrome of elements.(Hind: usr copy()method)
list = [ 1,2,1,1,2,1]
R_list = list.copy()
R_list.reverse()
# print(list)
# print(R_list)
 
if(list == R_list):
    print("Palindrome")
else:
    print("Not Palindrome")    