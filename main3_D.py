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

def NumericalIntegration_In_3D(f, a, b, c, d, p, q, m, n, o):

    g = (b-a)/m
    h = (d-c)/n
    s = (q-p)/o

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

                for k in range(o):
                    left_z = p + k*s
                    right_z = left_z + s
                    midpoint_z = (left_z + right_z)/2

                    total += f(midpoint_x, midpoint_y, midpoint_z)

        return total*g*h*s

    elif choice == 2:

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

    elif choice == 3:
        total = 0

        if m % 2 != 0 or n % 2 != 0 or o % 2 != 0:
            print("Values of m, n and o must be even!!!")
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

                for k in range(o+1):
                    z = p + k*s
                    if k == 0 or k == o:
                        wz = 1
                    elif (k % 2 == 1):
                        wz = 4
                    else:
                        wz = 2

                    total += (wx)*(wy)*(wz)*f(x, y, z)

        return (total)*(g*h*s)/27

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
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))
p = float(input("Enter the value of p: "))
q = float(input("Enter the value of q: "))
m = int(input("Enter the value of m(number of sub-intervals for x-axis): "))
n = int(input("Enter the value of n(number of sub-intervals for y-axis): "))
o = int(input("Enter the value of o(number of sub-intervals for z-axis): "))

if m<= 0 or n <= 0 or o <= 0:
    print("values of m, n and o must be greater than zero!!!")
    sys.exit()

def f(x, y, z):
    values = allowed.copy()
    values["x"] = x
    values["y"] = y
    values["z"] = z
    return eval(expression, {"__builtins__": {}}, values)

result = NumericalIntegration_In_3D(f, a, b, c, d, p, q, m, n, o)
print(result)


