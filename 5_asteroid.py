from sympy import plot_implicit, symbols
x, y, a = symbols('x y a')
a = 4
# Define the equation for the shape
eq = Eq(x**(2/3) + y**(2/3), a**(2/3))

# Plot the shape
plot_implicit(eq)
