#1

#Multiply

#def multiply(a, b):
#    x = a * b
#    return x


#2

#Even or Odd

#def even_or_odd(number):
#    if number % 2 == 0:
#        return "Even"
#    else:
#        return "Odd"


#3

#Convert a Number to a String!

# def number_to_string(num):
#     return str(num)


#4

#Reversed Strings

# def solution(string):
#     return string[::-1]


#5

#Return Negative

# def make_negative( number ):
#     if number < 0:
#         return number
#     return number * -1


#6

#Opposite number


# def opposite(number):
#   return number * -1



#7

#Convert boolean values to strings 'Yes' or 'No'.


# def bool_to_word(boolean):
#     if bool(boolean):
#         return "Yes"
#     else:
#         return "No"


#8

#Sum of positive

#def positive_sum(arr):
#    return sum([item for item in arr if item > 0])



#9

#String repeat


# def repeat_str(repeat, string):
#     return string * repeat



#10

#Remove First and Last Character

# def remove_char(s):
#     return s[1:-1]



#11

#Square(n) Sum


# def square_sum(numbers):
#     return sum([ number ** 2 for number in numbers ])



#12

#Find the smallest integer in the array


#def find_smallest_int(arr):
#    return min(arr)



#13

#Convert a String to a Number!


# def string_to_number(s):
#     return int(s)



#14


#Grasshopper - Summation


# def summation(num):
#     total = sum(list(range(1, num + 1)))
#     return total




#15

#Function 1 - hello world

# def greet():
#     return "hello world!"



#16

#Counting sheep...


# def count_sheeps(sheep):
#   return sum(1 for s in sheep if s == True)


#17

#Remove String Spaces


# def no_space(x):
#     z = x.replace(" ","")
#     return z


#18

#You Can't Code Under Pressure #1

# def double_integer(i):
#     return(i * 2)



#19

#Returning Strings

# def greet(name):
#     return f'Hello, {name} how are you doing today?'


#20

#Convert a Boolean to a String

# def boolean_to_string(b):
#     return str(b)


#21

#Basic Mathematical Operations

# def basic_op(operator, value1, value2):
#     if operator == '+': return value1 + value2
#     if operator == '-': return value1 - value2
#     if operator == '*': return value1 * value2
#     if operator == '/': return value1 / value2



#22

#Keep Hydrated!


# def litres(time):
#     return int(time * 0.5)



#23

#Century From Year


# def century(year):
#     century = year // 100
#     if year % 100 == 0:
#         return century
#     return century + 1



#24

#Beginner - Lost Without a Map

# def maps(a):
#     return [number * 2 for number in a]



#25

#Sum Arrays


#def sum_array(a):
#    return sum(a)


#26

#Beginner Series #1 School Paperwork

# def paperwork(n, m):
#     if n < 0 or m < 0:
#         return 0
#     return n * m



#27


#MakeUpperCase


# def make_upper_case(s):
#     return s.upper()



#28

#Moving Zeros To The End

# def move_zeros(lst):
#     non_zeros = [x for x in lst if x != 0]
#     zeros = [0] * (len(lst) - len(non_zeros))
#     return non_zeros + zeros


#29

#Does my number look big in this?


# def narcissistic( value ):
#     digits = [int(d) for d in str(value)]
#     power = len(digits)
#     return sum(d ** power for d in digits) == value 