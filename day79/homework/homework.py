#1

# რა არის ცვლადი დაწერეთ თქვენი სიტყვებით, განმარტეთ დეტალებში და paint-ში დახაზეთ როგორ წარმოგიდგენიათ.

#ცვლადი არის სახელით მონიშნული მეხსიერების უჯრა, რომელიც ინახავს მონაცემებს. 
#ის საშუალებას გვაძლევს, პროგრამაში შევინახოთ და გამოვიყენოთ სხვადასხვა სახის ინფორმაცია, როგორიცაა რიცხვები, ტექსტი ან სხვა მონაცემთა ტიპები.

#2

#შექმენით ცვლადი რომელსაც განაახლებთ 4-ჯერ.

# num = 0

# print("პირველი მნიშვნელობა:", num)

# num = 10
# print("მეორე მნიშვნელობა:", num)

# num = 20
# print("მესამე მნიშვნელობა:", num)

# num = 30
# print("მეოთხე მნიშვნელობა:", num)

# num = 40
# print("მეხუთე მნიშვნელობა:", num)



#3

#ძალით დაუშვით შეცდომა ცვლადის სახელის დაწერის დროს და გვერდზე მიუწერეთ რატო აერორებს ცვლადის სახელს.

# 1count = 0  #  შეცდომა: ცვლადის სახელი არ შეიძლება იწყებოდეს რიცხვით
# print(1count)


#4

#კომენტარის სახით დაწერეთ მონაცემთა ტიპები რომლებიც იცით, მიუწერეთ განმარტებაც და მოიფიქრეთ მაგალითებიც.

# 1. მთელი რიცხვი (int)
#    ეს ტიპი ინახავს მთელ რიცხვებს, როგორიცაა 0, 5, -10 და ა.შ.
# num = 25  # int

# 2. ათწილადი (float)
#    ათწილადი რიცხვები, როგორიცაა 3.14, -0.5, 10.0
# pi = 3.14  # float

# 3. სტრიქონი (str)
#    ტექსტური მონაცემები, რომლებიც ბრჭყალებში იწერება.
# name = "ლუკა"  # str

# 4. ლოგიკური (bool)
#    მხოლოდ ორი შესაძლო მნიშვნელობა აქვს: True ან False.
# is_student = True  # bool

# 5. სია (list)
#    მონაცემთა კოლექცია, რომლის ელემენტებიც ინდექსებითაა დანომრილი და შეუძლია შეიცვალოს.
# fruits = ["ვაშლი", "ბანანი", "ატამი"]  # list



#5

#შექმენით ცვლადები სადაც შეინახავთ თქვენს სახელს, გვარს, ასაკს და ეს ყველაფერი დაპრინტეთ ერთად

# name = "დემეტრე"
# surname = "ბიგანისჰვილი"
# age = 14

# print("სახელი არის", name, "გვარი", surname, "ასაკი", age)


#6

#შექმენით 3 ცვლადები სადაც შეინახავთ სხვადასხვა მოცანემთა ტიპებს და გაიგეთ მატი ტიპი, (type() ფუნქციის გამოყენებით.

# age, name, is_student = 14, "დემეტრე", True

# print(type(age), type(name), type(is_student))



#7

# type() ფუნქცია გამოიყენება იმის გასაგებად, თუ რა ტიპის მონაცემია შენახული ცვლადში.


#8

# user_input = input("გთხოვთ შეიტანოთ სიტყვა: ") 
# print("თქვენი შესატანი სიტყვა:", user_input)


#9

# name = input("შეიტანეთ თქვენი სახელი: ")
# surname = input("შეიტანეთ თქვენი გვარი: ")
# age = input("შეიტანეთ თქვენი ასაკი: ")

# print("თქვენი სახელი არის " + name + ", გვარი არის " + surname + " და თქვენ ხართ " + age + " წლის.")




#10

# str_num = "25"
# int_num = int(str_num)
# print(int_num)



#11


# user_name = input("შეიტანეთ თქვენი სახელი: ")

# my_name = "დემეტრე"

# if user_name == my_name:
#     print("თქვენი სახელი დაემთხვევა ჩემს სახელს!")
# else:
#     print("თქვენი სახელი არ დაემთხვევა ჩემს სახელს.")



#12

# ლოგიკური ოპერატორები გამოიყენება_boolean_ ტიპის მონაცემებთან მუშაობისთვის (True ან False).
# მათ ხშირად ვიყენებთ, რათა შევამოწმოთ სხვადასხვა პირობები და დავაკავშიროთ ისინი.


#13

# user_name = input("შეიტანეთ თქვენი სახელი: ")
# user_surname = input("შეიტანეთ თქვენი გვარი: ")


# my_name = "დემეტრე"
# my_surname = "ბიგანისჰვილი"

# if user_name == my_name or user_surname == my_surname:
#     print("თქვენი სახელი ან გვარი ემთხვევა ჩემს სახელსა ან გვარს.")
# else:
#     print("თქვენი სახელი და გვარი არ ემთხვევა ჩემს სახელსა და გვარს.")




#14

# print(5 + 3)
# print(10 + 20)
# print(-5 + 7)
# print(0 + 0)
# print(100 + 200)


# print(10 - 5)
# print(20 - 10)
# print(-7 - 2)
# print(0 - 10)
# print(50 - 50)


# print(10 / 2)
# print(9 / 3)
# print(5 / 2)
# print(7 / 2)
# print(10 / 4)


# print(4 * 3)
# print(5 * 6)
# print(2 * 0)
# print(7 * 7)
# print(-3 * 3)


# print(10 // 3)
# print(20 // 6)
# print(5 // 2)
# print(7 // 4)
# print(9 // 2)


# print(10 % 3)
# print(20 % 6)
# print(7 % 4)
# print(15 % 5)
# print(9 % 4)



#15

# num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
# num2 = float(input("შეიტანეთ მეორე რიცხვი: "))


# if num1 == num2:
#     print("რიცხვები თანაბარია.")
# elif num1 > num2:
#     print("პირველი რიცხვი დიდი არის.")
# else:
#     print("მეორე რიცხვი დიდი არის.")



#16


# user_name = input("შეიტანეთ თქვენი სახელი: ")


# reversed_name = ""
# for char in user_name:
#     reversed_name = char + reversed_name

# print("თქვენი სახელი პირიქით:", reversed_name)



#17

#    "if" ოპერატორი გამოიყენება იმისთვის, რომ შეამოწმოთ პირობა და თუ ის მართალია, შესრულდეს გარკვეული კოდი.
# x = 5
# if x > 0:  # თუ x მეტია 0-ზე
#     print("x დადებითია.")

#  2. elif (else if)
#     "elif" გამოიყენება, როდესაც "if" პირობა არ აღმოჩნდა მართალი და გსურთ დამატებით სხვა პირობების შემოწმება.
# x = -3
# if x > 0:
#     print("x დადებითია.")
# elif x < 0:  # თუ x ნაკლებია 0-ზე
#     print("x უარყოფითია.")
# else:  # თუ x არაა არც დადებითი და არც უარყოფითი
#     print("x არის 0.")

#  3. else
#     "else" გამოიყენება "if" ან "elif"-ის შემდეგ, როცა სხვა პირობები ვერ შესრულდა და აუცილებლად უნდა შესრულდეს კოდი.
# x = 0
# if x > 0:
#     print("x დადებითია.")
# else:  # თუ x არ არის დადებითი
#     print("x არაა დადებითი.")

#  4. ternary operator (inline if)
#     ერთი ხაზის პირობითი ოპერატორი, როდესაც გსურთ კოდში მოკლედ დაწეროთ "if-else" ამოცანა.
# x = 5
# result = "positive" if x > 0 else "negative"  # ერთი ხაზი პირობითი ოპერატორის გამოყენებით
# print(result)  # "positive"


#18

# age = int(input("შეიტანეთ თქვენი ასაკი: "))


# if age >= 18:
#     print("თქვენი ასაკი საკმარისია, თქვენ ხართ სრულწლოვანი.")
# elif 0 <= age < 18:
#     print("თქვენ ხართ არასრულწლოვანი.")
# else:
#     print("სისტემაში ხარვეზია. გთხოვთ, შეიყვანოთ სწორი ასაკი.")



#19

# user_name = input("შეიტანეთ თქვენი სახელი: ")

# my_name = "დემეტრე"

# user_name_length = len(user_name)
# my_name_length = len(my_name)

# if user_name_length == my_name_length:
#     print("თქვენი სახელის ასოების რაოდენობა და ჩემი სახელის ასოების რაოდენობა ერთნაირია.")
# else:
#     print("თქვენი სახელის ასოების რაოდენობა განსხვავდება ჩემი სახელის ასოების რაოდენობისგან.")



#20

# num = int(input("შეიტანეთ რიცხვი: "))

# if num % 2 == 0:
#     print("რიცხვი ლუწია.")
# else:
#     print("რიცხვი კენტია.")


#21

# print("აირჩიეთ მოქმედება:")
# print("1. დამატება (+)")
# print("2. გამოყოფა (-)")
# print("3. გამრავლება (*)")
# print("4. გახლეჩა (/)")

# operation = input("მომხმარებელო, აირჩიე მოქმედების ნომერი (1/2/3/4): ")

# num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
# num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

# if operation == '1':
#     result = num1 + num2
#     print("შედეგი: " + str(num1) + " + " + str(num2) + " = " + str(result))
# elif operation == '2':
#     result = num1 - num2
#     print("შედეგი: " + str(num1) + " - " + str(num2) + " = " + str(result))
# elif operation == '3':
#     result = num1 * num2
#     print("შედეგი: " + str(num1) + " * " + str(num2) + " = " + str(result))
# elif operation == '4':
#     if num2 != 0:
#         result = num1 / num2
#         print("შედეგი: " + str(num1) + " / " + str(num2) + " = " + str(result))
#     else:
#         print("არ შეიძლება გახლეჩა 0-ით!")
# else:
#     print("არასწორი არჩევანი.")



#22

# academy = input("კითხვა: რომელ აკადემიაში სწავლობ? ")

# if academy.lower() == "goa":
#     print("შენ ნამდვილი ჩადი და პროგრამისტი ხარ!")
# else:
#     print("შეუერთდი goa-ს აკადემია და გახდი ნამდვილი ჩადი და პროგრამისტი!")


#23

#True ეს იმიტომ, რომ ლოგიკური ოპერატორი or დაბრუნებს True


#24


#False ეს იმიტომ, რომ ლოგიკური ოპერატორი and დაბრუნებს False



#25


#გამოიტანს False პირველი, ხორციელდება True or True ოპერაცია,ლოგიკური ოპერატორი or დააბრუნებს True.




#26

#True and False – შედეგი იქნება False, რადგან and მხოლოდ მაშინ დაბრუნებს True, როცა ორივე operand არის True. True and True – შედეგი იქნება True, რადგან ორივე operand არის True.



#27

#True and True – პირველი ოპერაცია. and დააბრუნებს True, რადგან ორივე operand არის True.



#28

# name = input("შეიყვანეთ თქვენი სახელი: ")

# print("გამარჯობა, " + name + "! კეთილი იყოს თქვენი მობრძანება!")


#29

# width = float(input("შეიყვანეთ მართკუთხედის სიგანე: "))

# height = float(input("შეიყვანეთ მართკუთხედის სიმაღლე: "))

# area = width * height

# print("მართკუთხედის ფართობია:", area)

