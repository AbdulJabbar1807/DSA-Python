def f(n):
    i = 1
    total = 1
    
    while i<=n:
        total += i
        i += 1
        n -= i
        
    return total

print(f(5))