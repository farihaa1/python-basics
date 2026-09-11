import sympy as sp

x = sp.symbols('x')

f = x**3 + 2*x**2 - 5*x + 7
derivative = sp.diff(f, x)
value = derivative.subs(x, 2)
#
print("f(2) = ", derivative)
print("f(2) =", value)
