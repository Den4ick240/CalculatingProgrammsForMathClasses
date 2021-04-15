p = int(input())
m = int(input())

print(p, m)

classes = []

l = list(i for i in range(m))

while len(l) > 0:
    cclass = []
    c = l.pop(0)
    cclass.append(c)
    n = (c * p) % m
    while n != c:
        cclass.append(n)
        l.remove(n)
        n = (n * p) % m
    classes.append(cclass)
    print(classes)
