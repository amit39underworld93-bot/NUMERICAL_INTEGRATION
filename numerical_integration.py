import math
import sys

dimension = int(input("Enter the dimension between 1 to 3: "))

if dimension < 1 or dimension > 3:
    print("Please enter a valid dimension between 1 and 3!!! ")
    sys.exit()

print("\n==== CHOOSE APPROXIMATION METHOD ====")
print("1. Midpoint Rule")
print("2. Trapezoidal Rule")
print("3. Simpson's 1/3 Rule")

choice = int(input("Enter your choice between 1 to 3: "))

if choice < 1 or choice > 3:
    print("Please enter a valid choice between 1 and 3!!!")
    sys.exit()

def  NumericalIntegration(f, a, b, c, d, p, q, m, n, o):

    if dimension == 1 and choice == 1:

        h = (b-a)/m

        total = 0

        for i in range(m):
            left = a + i*h
            right = left + h
            midpoint = (left + right)/2

            total += f(midpoint)*h
        return total

    if dimension == 1 and choice == 2:

        h = (b-a)/m

        total = 0

        for i in range(1, m):
            x = a + i*h
            total += f(x)

        total = h*(0.5*(f(a)) + 0.5*(f(b)) + total)
        return total

    if dimension == 1 and choice == 3:

        h = (b-a)/m

        total = 0
        total1 = 0
        total2 = 0

        for i in range(1, m):
            x = a + i*h
            if  i % 2 == 0:
                total1 += 2*(f(x))

            if i % 2 != 0:
                total2 += 4*(f(x))

        total = h*(1/3)*(f(a) + f(b) + total1 + total2)

        return total

    if dimension == 2 and choice == 1:

        g = (b-a)/m
        h = (d-c)/n

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

    if dimension == 2 and choice == 2:

        g = (b-a)/m
        h = (d-c)/n

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

    if dimension == 2 and choice == 3:

        g = (b-a)/m
        h = (d-c)/n

        total = 0

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

    if dimension == 3 and choice == 1:

        g = (b-a)/m
        h = (d-c)/n
        s = (q-p)/o

        total = 0

        for i in range(m):
            left_x = a + i*g
            right_x = left_x + g
            midpoint_x = (left_x + right_x)/2

            for j in range(n):
                left_y = c + j*h
                right_y = left_y + h
                midpoint_y = (left_y + right_y)/2

                for k in range(o):
                    left_z = p + k*s
                    right_z = left_z + s
                    midpoint_z = (left_z + right_z)/2

                    total += f(midpoint_x, midpoint_y, midpoint_z)

        return total*g*h*s

    if dimension == 3 and choice == 2:

        g = (b-a)/m
        h = (d-c)/n
        s = (q-p)/o

        corner = 0
        edge = 0
        face = 0
        interior = 0

        for i in range(m+1):
            x = a + i*g
            for j in range(n+1):
                y = c + j*h
                for k in range(o+1):
                    z = p + k*s

                    boundary_count = (
                        int(i == 0 or i == m) + 
                        int(j == 0 or j == n) + 
                        int(k == 0 or k == o)
                    )

                    if boundary_count == 3:
                        corner += f(x, y, z)*0.125
                    elif boundary_count == 2:
                        edge += f(x, y, z)*0.25
                    elif boundary_count == 1:
                        face += f(x, y, z)*0.5
                    else:
                        interior += f(x, y, z)

        return (corner + edge + face + interior)*g*h*s

    if dimension == 3 and choice == 3:

        g = (b-a)/m
        h = (d-c)/n
        s = (q-p)/o

        total = 0

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

                for k in range(o+1):
                    z = p + k*s 
                    if k == 0 or k == o:
                        wz = 1
                    elif (k % 2 == 1):
                        wz = 4
                    else:
                        wz = 2

                    total += (wx)*(wy)*(wz)*f(x, y, z)

        return (total*g*h*s)/27

if dimension == 1:
    expression = input("Enter the function f(x): ")

elif dimension == 2:
    expression = input("Enter the function f(x, y): ")

else:
    expression = input("Enter the function f(x, y, z): ")

allowed = {
    "x" : None, 
    "y" : None,
    "z" : None,
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
m = int(input("Enter the value of m: "))

c = d = p = q = 0.0
n = o = 1

if m <= 0:
    print("value of m must be greater than zero!!!")
    sys.exit()

if dimension >= 2:

    c = float(input("Enter the value of c: "))
    d = float(input("Enter the value of d: "))
    n = int(input("Enter the value of n: "))

    if m <= 0 or n <= 0 :
        print("values of m and n must be greater than zero!!!")
        sys.exit()

if dimension == 3:

    p = float(input("Enter the value of p: "))
    q = float(input("Enter the value of q: "))

    o = int(input("Enter the value of o: "))

    if m <= 0 or n <= 0 or o<= 0:
        print("values of m, n and o must be greater than zero!!!")
        sys.exit()

if choice == 3:
    if dimension >= 1 and m % 2 != 0:
        print("Error: Value of m must be even for Simpson's Rule!!!")
        sys.exit()
    if dimension >= 2 and n % 2 != 0:
        print("Error: Value of n must be even for Simpson's Rule!!!")
        sys.exit()
    if dimension == 3 and o % 2 != 0:
        print("Error: Value of o must be even for Simpson's Rule!!!")
        sys.exit()

if dimension == 1:

    def f(x):
        values = allowed.copy()
        values["x"] = x
        return eval(expression, {"__builtins__": {}}, values)

elif dimension == 2:

    def f(x, y):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y
        return eval(expression, {"__builtins__": {}}, values)

else:

    def f(x, y, z):
        values = allowed.copy()
        values["x"] = x
        values["y"] = y
        values["z"] = z  
        return eval(expression, {"__builtins__": {}}, values)

result = NumericalIntegration(f, a, b, c, d, p, q, m, n, o)

print(result)