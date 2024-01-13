def circleArea(r):
    return 3.1416 * r**2

print(circleArea(5))

def triangleArea(b, h):
    return 0.5 * b * h

print(triangleArea(6, 10))

def higherNumber(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(higherNumber(40, 20, 30))

for i in range(45):
    print("easy code")
