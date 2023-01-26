from sympy import plot_implicit, symbols,Eq
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq(x**3 + y**3,3*a*x*y)

# Plot the shape

plot_implicit(eq)
