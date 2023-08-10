#implementation of selection sort

# arr = [1,2]
# [arr[0],arr[1]] = [arr[1],arr[0]]

# print(arr)

def selectionSort(arr):
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        
        [arr[i],arr[min_index]] = [arr[min_index],arr[i]]

    return arr

arr=[1,-1,6,5,8,7,10]
print(selectionSort(arr));