from sympy import plot_implicit, symbols,Eq
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq((x**2)/(a**2),1 + (y**2)/(a**2))

# Plot the shape

plot_implicit(eq)
