prev_list = [3,6,9,12,15]
new_list = [i/3 for i in prev_list]

print(prev_list)
print(new_list)

language = "python"
letters = [letter for letter in language]
print(letters)

# conditional list comprehension
integers = [1,-2,3,4,-5,-9,-14,23,34,76,90]
pos_num = [num for num in integers if num > 0]
print(pos_num)

squarred_neg_num = [s_num*s_num for s_num in integers if s_num < 0]
print(squarred_neg_num)

# Using function in list comprehension
def is_consonants(word):
    vowels = 'aeiou'
    return word.isalpha() and word.lower() not in vowels 

consonant = [i for i in language if is_consonants(i)]
print(consonant)

# if - else statement in list comprehension
consonant = [i if is_consonants(i) else f'{i} is a vowel' for i in language]
print(consonant)