p = 2
input_poly = []
for dfjkgsdlfjkh in range(17):
    input_poly.append(0)
input_poly[1] = 1
input_poly[16] = 1


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
    while i >= 0 and a[i] == 0:
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
    return trim(o)


def modp(a, b):
    r, o = divide_poly(a, b)
    return trim(r)


def recursive_search(recursion_level, result_poly, input_poly):
    print('recursion_level= ', recursion_level)
    for i in range(p):
        result_poly[recursion_level] = i
        if recursion_level == len(result_poly) - 1:
            if len(trim(result_poly)) <= 1:
                continue
            print('dividing ', input_poly, trim(result_poly))
            modpres = modp(input_poly, trim(result_poly))
            print('res ', modpres)
            # if len(modpres) == 1 and modpres[0] == 0:
            if len(modpres) == 0:
                return True
        else:
            res = recursive_search(recursion_level + 1, result_poly, input_poly)
            if res:
                return True
    return False


def print_poly(p):
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


def main():
    dividers = []
    divisible = trim(input_poly)
    i = 2
    while len(divisible) > i:
        poly = []
        for j in range(i):
            poly.append(0)
        res = recursive_search(0, poly, divisible)
        if res:
            dividers.append(trim(poly))
            divisible = divp(divisible, poly)
            print(poly)
            print(divisible)
        else:
            i = i+1
    dividers.append(trim(divisible))
    print(dividers)
    for d in dividers:
        print('(', end='')
        print_poly(d)
        print(')', end='')


if __name__ == '__main__':
    main()
