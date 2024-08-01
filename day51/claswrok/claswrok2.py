a = []

for i in range(1,8):
    a.append(i)


second = a[2]
third = a[3]

a[2] = third
a[3] = second

a.insert(4,"deme")

a.remove(a[0])
a.remove(a[-1])

print(a)
