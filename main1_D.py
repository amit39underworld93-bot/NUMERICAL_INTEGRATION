import math
import sys

print("\n==== CHOOSE METHOD OF INTEGRATION ====")
print("1. Midpoint Rule")
print("2. Trapezoidal Rule")
print("3. Simpson's 1/3 Rule")

choice = int(input("Enter your choice between 1 to 3: "))
if choice < 1 or choice > 3:
    print("Please enter a valid choice between 1 to 3: ")
    sys.exit()

def NumericalIntegration_In_1D(f, a, b, n):

    h = (b-a)/n

    total = 0

    if choice == 1:
        for i in range(n):
            left = a + i*h
            right = left + h
            midpoint = (left + right)/2

            total += f(midpoint)*h
        return total

    if choice == 2:
        for i in range(1, n):
            x = a + i*h
            total += f(x)

        total = h*(0.5*(f(a)) + 0.5*(f(b)) + total)
        return total

    if choice == 3:
        total1 = 0
        total2 = 0

        for i in range(1, n):
            x = a + i*h
            if  i % 2 == 0:
                total1 += 2*(f(x))

            if i % 2 != 0:
                total2 += 4*(f(x))

        total = h*(1/3)*(f(a) + f(b) + total1 + total2)

        return total

expression = input("Enter the function f(x): ")

allowed = {
    "x" : None, 
    "sin" : math.sin,
    "cos" : math.cos,
    "tan" : math.tan,
    "sqrt" : math.sqrt,
    "asin" : math.asin,
    "acos" : math.acos,
    "atan" : math.atan,
    "log" : math.log,
    "exp" : math.exp,
    "pi" : math.pi,
    "e" : math.e
}

n = int(input("Enter the value of n(number of sub-intervals): "))
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

def f(x):
    values = allowed.copy()
    values["x"] = x
    return eval(expression, {"__builtins__": {}}, values)

result = NumericalIntegration_In_1D(f, a, b, n)
print(result)


