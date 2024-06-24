sum = 0
numbers = [1,4,6,24,98,3,6,12,45,4,2,87,5,90]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 :
        sum += numbers[i]
print(sum)
