def sum():
    sum = 0
    different_number = [1,7,24,86,36,90,46,35,89,10]
    for i in range (len(different_number)):
        sum = sum + different_number[i]
    print("sum of numbers:" + str(sum))

sum()