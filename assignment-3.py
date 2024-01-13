def division(a, b):
    divide = a / b
    print (divide)
division(125, 5)

# Extracting the value of Factorial

def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)
value = factorial(10)
print (value)