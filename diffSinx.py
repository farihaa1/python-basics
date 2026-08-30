import sympy as sp

x = sp.symbols('x')

f = sp.sin(x)
first = sp.diff(f,x)
second = sp.diff(f, x, 2)

print("First derivative:", first)
print("Second derivative:", second)
