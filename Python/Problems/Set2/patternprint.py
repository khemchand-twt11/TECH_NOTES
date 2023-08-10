# print pattern 

n = 5

for i in range(1, n+1): # 1 7 
   
    string = ""
    for j in range(1, i+1):
        # print(i,j)
        string += str(j) + " "
    print(string)

