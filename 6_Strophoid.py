from sympy import plot_implicit, symbols,Eq
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq(a*(y**2),(y**2)*x + a * (x**2) + x**3)

# Plot the shape

plot_implicit(eq)
