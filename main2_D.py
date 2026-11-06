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

def NumericalIntegration_In_2D(f, a, b, c, d, m, n):

    g = (b-a)/m
    h = (d-c)/n

    if choice == 1:

        total = 0

        for i in range(m):
            left_x = a + i*g
            right_x = left_x + g
            midpoint_x = (left_x + right_x)/2

            for j in range(n):
                left_y = c + j*h
                right_y = left_y + h
                midpoint_y = (left_y + right_y)/2

                total += f(midpoint_x, midpoint_y)

        return total*g*h

    elif choice == 2:

        corner = 0
        edge = 0
        interior = 0

        for i in range(m+1):
            x = a + i*g
            for j in range(n+1):
                y = c + j*h
                if (i == 0 or i == m) and (j == 0 or j == n):
                    corner += f(x, y)*0.25
                elif i == 0 or i == m or j == 0 or j == n:
                    edge += f(x, y)*0.5
                else:
                    interior += f(x, y)

        return (corner + edge + interior)*g*h

    elif choice == 3:
        total = 0

        if m % 2 != 0 or n % 2 != 0:
            print("Values of m and n must be even!!!")
            sys.exit()

        for i in range(m+1):
            x = a + i*g
            if i == 0 or i == m:
                wx = 1
            elif (i % 2 == 1):
                wx = 4
            else:
                wx = 2

            for j in range(n+1):
                y = c + j*h
                if j == 0 or j == n:
                    wy = 1
                elif (j % 2 == 1):
                    wy = 4
                else:
                    wy = 2

                total += (wx)*(wy)*f(x, y)

        return (total)*(g*h)/9   

expression = input("Enter the function f(x, y): ")

allowed = {
    "x" : None, 
    "y" : None,
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

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
m = int(input("Enter the value of m(number if sub-intervals for x-axis): "))
n = int(input("Enter the value of n(number if sub-intervals for y-axis): "))

if m<= 0 or n <= 0:
    raise ValueError("values of m and n must be greater than zero!!!")

def f(x, y):
    values = allowed.copy()
    values["x"] = x
    values["y"] = y
    return eval(expression, {"__builtins__": {}}, values)

result = NumericalIntegration_In_2D(f, a, b, c, d, m, n)
print(result)


