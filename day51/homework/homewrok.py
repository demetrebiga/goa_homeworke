d = []

c = (input("please enter any number:   "))
e = (input("what do you whant the number to be - or + ?:  "))


d.append(e)
d.append(c)

d.insert(0,"+")
d.remove(d[1])
print(d)


d.append(e)
d.append(c)

d.insert(0,"-")
d.remove(d[1])
print(d)