#1

#simple calculator

# def calculator(x, y, op):
#     if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
#         return "unknown value"
    
#     if op == "+":
#         return x + y
#     elif op == "-":
#         return x - y
#     elif op == "*":
#         return x * y
#     elif op == "/":
#         if y == 0:
#             return "Cannot divide by zero"
#         return x / y
#     else:
#         return "unknown value"



#2

#Drink about

# def people_with_age_drink(age):
#     if age < 14:
#         return 'drink toddy'
#     elif age < 18:
#         return 'drink coke'
#     elif age < 21:
#         return 'drink beer'
#     else:
#         return 'drink whisky'


#2

#Century From Year

# def century(year):
#     century = year // 100
#     if year % 100 == 0:
#         return century
#     return century + 1


#3

#Remove String Spaces

# def no_space(x):
#     z = x.replace(" ","")
#     return z