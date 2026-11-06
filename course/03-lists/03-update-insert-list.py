items = [1,2,3,4,5]
print(items)

items[0] = 10
print(items)

items.insert(1,20)
print("Insertion: ",items)

items.append(100)
print("Append: ",items)

new_list = [11,12,13,14,15]
items.extend(new_list)
print("Extended list: ",items)