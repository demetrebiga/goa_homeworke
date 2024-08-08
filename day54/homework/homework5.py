def number():
    qwestion = int(input("please enter a number:  "))
    if qwestion < 0:
        return("negative")
    elif 0 < qwestion:
        return("positive")
    
print(number())