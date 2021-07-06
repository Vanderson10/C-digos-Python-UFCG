l = [10, 20, 30, 40]
e = 5

l.append(e)

j = len(l) - 1
print(l)

while j>0 and l[j] < l[j - 1]:
    l[j], l[j-1] = l[j - 1], l[j]
    j -= 1
    print(l)
