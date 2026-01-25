#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

# value = {2,2.0}
# value1 = {2,2.54}
# value2 = {"tree",6}
# value3 = {7.2,"tree"}
 
# print(value) 
# print(value1)
# print(value2)
# print(value3)

value = {
    ("Float",9.0),
    ("int",9)
}
print(value)