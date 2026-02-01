# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]  # Linear search
x = 36
idx = 0
for value in list:
    if(value==x):
        print("found at idx", idx)
    idx+=1
    # else:
    #     print("Not found")    
