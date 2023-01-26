from sympy import plot_implicit, symbols,Eq
x, y, a = symbols('x y a')
a = 4
# Define the equation for the shape
eq = Eq(a*(y**2),x**3 + (y**2)*x)

# Plot the shape

plot_implicit(eq)
