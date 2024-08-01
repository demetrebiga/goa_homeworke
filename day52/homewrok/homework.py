import random

print("welcome lets plat  rock paper sicors")

choices = ['rock','paper', 'sicors']

computer_choice = random.choice(choices)

user_choice = input("enter in you choice (rock paper sicors):  ")

while user_choice not in choices:
    print("not right choice")
    user_choice = input("enter in you choice (rock paper sicors):  ")



print("you chouse: ", user_choice)
print("compiuter chose:  ",computer_choice)

if user_choice == computer_choice:
    print("it's draw")

elif (user_choice == 'rock' and computer_choice == 'sicors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'sicors' and computer_choice == 'paper'):
    print("you won!:")

else:
    print("you lost:(")