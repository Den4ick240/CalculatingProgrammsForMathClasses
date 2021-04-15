p = 3
m = 2
divider = [2, 1, 1]


def mul(a, b):
    return (a * b) % p


def sum(a, b):
    return (a + b) % p


def sub(a, b):
    return (a - b) % p


def div(a, b):
    i = 0
    while mul(i, b) != a:
        i += 1
    return i


def trim(a):
    i = len(a) - 1
    while a[i] == 0 and i >= 0:
        i -= 1
    o = []
    for j in range(i + 1):
        o.append(a[j])
    return o


def mulp(a, b):
    o = []
    for i in range(len(a) * len(b)):
        o.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            o[i + j] += (a[i] * b[j])
            o[i + j] %= p;
    return trim(o)


def sump(a, b):
    o = []
    olen = max(len(a), len(b))
    for i in range(olen):
        o.append(0)
    for i in range(len(a)):
        o[i] = a[i]
    for i in range(olen):
        if i < len(b):
            o[i] = sum(o[i], b[i])
    return trim(o)


def subp(a, b):
    negative_b = []
    for i in range(len(b)):
        negative_b.append(sub(0, b[i]))
    return sump(a, negative_b)


def divide_poly(a, b):
    o = []
    for i in range(max(len(a), len(b))):
        o.append(0)
    r = trim(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        e = len(r) - len(b)
        o[e] = div(r[len(r) - 1], b[len(b) - 1])
        r = subp(a, mulp(o, b))
    o = trim(o)
    return r, o


def divp(a, b):
    r, o = divide_poly(a, b)
    return o


def modp(a, b):
    r, o = divide_poly(a, b)
    return r


def is_primitive(a):
    if len(trim(a)) == 0:
        return False
    s = a
    for i in range(pow(p, m) - 2):
        print(s)
        if len(s) == 1 and s[0] == 1:
            return False
        s = modp(mulp(a, s), divider)
    return True


def recursive_search(recursion_level, poly, primitives):
    for i in range(p):
        poly[recursion_level] = i
        if recursion_level == (m - 1):
            if is_primitive(poly):
                print('primitive: ', poly)
                primitives.append(poly.copy())
            else:
                print('not primitive: ', poly)
        else:
            recursive_search(recursion_level + 1, poly, primitives)


def print_primitive():
    primitives = []
    poly = []
    for i in range(m):
        poly.append(0)
    recursive_search(0, poly, primitives)
    # print(primitives)
    for p in primitives:
        i = len(p) - 1
        while i >= 0:
            if p[i] == 0:
                i += -1
                continue
            if i < len(p) - 1:
                print(' + ', end='')
            if p[i] != 1 or i == 0:
                print(p[i], end='')
            if i == 1:
                print('x', end='')
            elif i > 1:
                print('x^' + str(i), end='')
            i -= 1
        print()

print_primitive()
