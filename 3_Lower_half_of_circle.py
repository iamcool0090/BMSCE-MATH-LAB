from sympy import plot_implicit, symbols,Eq
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq(x**2 + 2*x,4 + 4*y-y**2)

# Plot the shape

plot_implicit(eq)
