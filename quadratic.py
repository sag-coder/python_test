import cmath

print("ax**2+bx+c=0")
a = int(input("enter the value a: "))
b = int(input("enter the value b: "))
c = int(input("enter the value c: "))

#discriminant D= b**2 - 4ac
d = (b**2)-(4*a*c)    #b**2 is denote by squar

sol1 = (-b + cmath.sqrt(d))/2*a  # cmath.sqrt is squar root
sol2 = (-b - cmath.sqrt(d))/2*a

if d > 0:
    print(" two distinct real root ")
elif d == 0:
    print("the two real equal root")
elif d < 0:
    print(" then two complex root ")
print("solution_1 : %s , solution_2 : %s " % (sol1, sol2))
