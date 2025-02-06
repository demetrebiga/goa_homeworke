#1

#Nickname Generator

#def nickname_generator(name):
#    if len(name) < 4:
#        return "Error: Name too short"
#    vowels = "aeiou"
#    return name[:4] if name[2] in vowels else name[:3]



#2

#Counting Duplicates

#def duplicate_count(text):
#    text = text.lower()
#    dictionary = {}
#    duplicates = 0
#    for letter in text:
#        dictionary[letter] = dictionary.get(letter,0) + 1
#    for letter, amount in dictionary.items():
#        if amount > 1:
#            duplicates += 1
#    return duplicates



#3

#Sum of two lowest positive integers

#def sum_two_smallest_numbers(numbers):
#    numbers.sort()
#    return numbers[0] + numbers[1]




#4

#Sum of Digits / Digital Root

#def digital_root(n):
#    print(n)
#    return n if n <= 9 else digital_root(sum([int(i) for i in str(n)]))

#5

#Nickname Generator

#def nickname_generator(name):
#    if len(name) < 4:
#        return "Error: Name too short"
#    vowels = "aeiou"
#    return name[:4] if name[2] in vowels else name[:3]



#6

#twice_as_old

#def twice_as_old(dad_years_old, son_years_old):
#    age_at_birth = dad_years_old - son_years_old
#    twice_as_old = age_at_birth * 2
#    return abs(dad_years_old - twice_as_old)




#7

#Sum of Triangular Numbers

#def sum_triangular_numbers(n):
#    sum_ = 0
#    for triangle in range(1,n+1):
#        sum_ += triangle * (triangle + 1) / 2
#    return sum_