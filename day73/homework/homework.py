#1

#Check the exam

# def check_exam(arr1,arr2):
#     score = 0
#     for correct, student in zip(arr1, arr2):
#         if student == correct:
#             score += 4
#         elif student == "":
#             score += 0
#         else:
#             score -= 1
#     return max(score, 0)


#2

#Sum The Strings

# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))



#3

#Pythagorean Triple

# def pythagorean_triple(integers):
#     integers.sort()
#     a, b, c = integers
#     return a**2 + b**2 == c**2



#4

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



#5

#Remove String Spaces

# def no_space(x):
#     z = x.replace(" ","")
#     return z