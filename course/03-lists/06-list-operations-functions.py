# operator 
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a = a * 3
print(a)

print(len(a))

print(sum(a))

# average of given elements in a list,taking user input-
total = 0
count = 0
nums = []
while (True):
    inp = input("Enter the element: ")
    if inp == "done": break
    nums.append(float(inp))

    
average = sum(nums)/len(nums)

print(f"Average: {average}")