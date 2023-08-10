string = "madpamam"


def isPallindrome(string):
  length = len(string)
  for i in range(length):
    if string[i] != string[length - i - 1]:
      return False
  return True


print(isPallindrome(string))