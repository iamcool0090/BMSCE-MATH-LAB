from sympy import plot_implicit, symbols,Eq,cosh
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq(y,a*cosh(x/a))

# Plot the shape

p = plot_implicit(eq , (x,-20,20), (y,-20,20))
