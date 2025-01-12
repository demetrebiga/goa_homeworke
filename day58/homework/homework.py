#1

#Hanoi record

#def hanoi(disks):
#    return (2 ** disks) - 1


#2

#Small enough? - Beginner

#def small_enough(array, limit):
#    return max(array) <= limit


#3

#Handshake problem

#def get_participants(handshakes):
#    if handshakes == 0:
#        return 0
#    n = 1
#    while (n * (n - 1)) // 2 < handshakes:
#        n += 1
#    return n


#4

#How many double digits?

#def number_of_duplicate_digits(ndigit):
#    if ndigit < 2:
#        return 0
#
#    total_numbers = 10**ndigit - 10**(ndigit - 1)
#    no_double_digits = 9 * (9**(ndigit - 1))
#    with_double_digits = total_numbers - no_double_digits
#
#    return with_double_digits

#5

#Array.diff

#def array_diff(a, b):
#    return [item for item in a if item not in b]