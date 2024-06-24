numbers = [-1, 4, 6, -43, 27, -82, 23]
positivenumbers = []
negativenumbers = []
for i in range(len(numbers)):
    if numbers[i] == 0:
        continue
    elif numbers[i] < 0:
        negativenumbers.append(numbers[i])
    else:
        positivenumbers.append(numbers[i])
print("this in positive number: ", positivenumbers)
print("this in negative number: ", negativenumbers)        
