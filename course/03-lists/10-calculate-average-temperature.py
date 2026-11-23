temp = []
total_days = int(input("Enter total number of temp you wants: "))
total_temp = 0

for i in range(total_days):
    temp.append(int(input(f"Enter temperature of day {i+1}: ")))
    total_temp += temp[i]
    
avg = round(total_temp//total_days,2)
    
aboveavg = 0
for i in temp:
    if i > avg:
        aboveavg += 1
        
print(f"Average temp of day(s): {avg}")
print(f"{aboveavg} day(s) have temp above avg temperature.")