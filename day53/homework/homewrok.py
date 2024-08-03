
num = int(input("enter a number:  "))

def number(num):

    if num == 0 :
        print(num, " is nether odd nether even")

    elif num % 2 == 0 :
        print(num, " is an odd number")

    else:
        print(num," is an even number")



number(num)
