user_name = input("please enter your name:  ")
user_surname = input("plesae enter your surname:  ")
user_age = input("please enter your age:  ")
user_location = input("please enter your location: ")

def user_info(name,surname,age,location):
    return "helo " + name + " " + surname + " you are " + age + " and you live in " + location
print(user_info(user_name,user_surname,user_age,user_location))