def number():
    qwestion = int(input("please enter a number:  "))
    qwestion_1 = int(input("please enter another number:  "))
    if qwestion < qwestion_1:
        return(qwestion)
    elif qwestion_1 < qwestion:
        return(qwestion_1)
    
print(number())