# take a list of numbers from 1 to 10 and peform add and remove operation also sort the array

list_python = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]
# print(type(list_python))

list_python.append(11)
print(list_python)
list_python.pop()
print(list_python)

list_python.sort(reverse=True)  # decreasing order
print(list_python)

list_python.sort(reverse=False)  # increasing order
print(list_python)
