#1

#Jaden Casing Strings

#def to_jaden_case(string):
#    list = string.split()
#    new_list = [i.capitalize() for i in list]
#    print(new_list)
#    return " ".join(new_list)

#2

#Find The Parity Outlier

#def find_outlier(integers):
#    odds = [x for x in integers if x %2 != 0]
#    evens = [x for x in integers if x %2 == 0]
#    return odds[0] if len(odds) < len(evens) else evens[0]

#3

#Take a Ten Minutes Walk

#def is_valid_walk(walk):
#    if len(walk) != 10:
#        return False
#    if walk.count('n') != walk.count('s'):
#        return False
#    if walk.count('w') != walk.count('e'):
#        return False
#    return True