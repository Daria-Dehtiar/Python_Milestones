equation = "4x^2 +4x +    (-8) =  0"

equation_without_spaces = equation.replace(" ", "")
equation_without_parentheses = equation_without_spaces.replace("(", "").replace(")", "")
equation_without_x = equation_without_parentheses.replace("x^2", "x").replace("x", "")
equation_without_equal_sign = equation_without_x.replace("=0", "")

coefficients = equation_without_equal_sign.split("+")

a = int(coefficients[0])
b = int(coefficients[1])
c = int(coefficients[2])
print(a, b, c)

d = b**2-(4*a*c)

x1 = ((-b+(d**0.5))/(2*a))
x2 = ((-b-(d**0.5))/(2*a))

print(int(x1), int(x2))