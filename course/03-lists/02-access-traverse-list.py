items = ['Milk','Bread','Butter',[1,2,3]]

print(items[0])
for i in range(len(items)):
    print(items[i])
    
for item in items:
    print(item)
    
print('Milk' in items)

if 'Milk' in items:
    print("Yes item is included.")
else:
    print("No,the item is not included.")
    
print(items[3][1]) # Accessing a list within a list.