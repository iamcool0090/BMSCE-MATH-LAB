from sympy import plot_implicit, symbols,Eq
x, y, a = symbols('x y a')
a = 4
# Define the equation for the shape
eq = Eq(x**2 + y**2, a)

# Plot the shape
plot_implicit(eq)
