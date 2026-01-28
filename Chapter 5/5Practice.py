num = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 9 
idx = 0 # initialization

while idx < len(num):
    if(num[idx]==x):
        print("Found at idx :" ,idx)
    idx+=1 