items = [1,2,3,4,5,6,7,8,9]
print(items[:])
print(items[:3])

items[:1] = [10,20]
print(items)

# pop method
print(items.pop())
print(items.pop(0))

# del method
del items[:2]
print(items)

# remove method
items.remove(8)
print(items)