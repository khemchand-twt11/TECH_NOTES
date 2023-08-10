#- *Input*: [2, 7, 11, 15], target = 9
#- *Output*: "[0, 1]"
arr = [2, 7, 11, 12]
target = 19


def twoSum(arr, target):
  dict = {}
  for index, item in enumerate(arr):
    required = target - item
    if required in dict:
      
      return [dict[required], index]
    dict[item] = index

  return []


print(twoSum(arr, target))
