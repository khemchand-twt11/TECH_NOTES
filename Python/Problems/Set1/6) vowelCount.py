vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}

str = "hello"
count = 0
for item in str:
    if item in vowels:
        count += 1

print(count)
