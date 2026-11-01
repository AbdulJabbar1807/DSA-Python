def plusone(digits):
    for i in range(1,len(digits)+1):
        if digits[-i] < 9:
            digits[-i] += 1
            return digits
        elif digits[-i] == 9:
            digits[-i] = 0
    return [1] + digits
    

def main():
    digits = [9,9,9]
    new_arr = plusone(digits)
    print(new_arr)
    
if __name__ == "__main__":
    main()
    
    