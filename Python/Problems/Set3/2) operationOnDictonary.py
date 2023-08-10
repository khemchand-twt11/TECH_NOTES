#- *Input*: Add "John": 25, Update "John": 26, Delete "John"
#- *Output*: "{}, {'John': 26}, {}"

dict = {}

dict["John"] = 25

print(dict)  # {"John":25}

dict["John"] = 26
print(dict)  # {"John":26}

del dict["John"]
print(dict)  # {}
