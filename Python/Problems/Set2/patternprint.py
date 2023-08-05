# print pattern 

n = 5

for i in range(1, n+2):
    string = ""
    for j in range(1, i):
        string += str(j) + " "
    print(string)

