import math
def quadratic_solver(a, b, c):
    delta= b**2 -4*a*c
    if delta< 0 :
        return" no real roots"
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1,x2
a = 1
b= -4
c= 3
roots = quadratic_solver(a, b, c)
print(roots)