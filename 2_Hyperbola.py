from sympy import plot_implicit, symbols,Eq
import math
x, y, a, b = symbols('x y a b')
a = 2
b = 4
# Define the equation for the shape
eq = Eq((x**2)/(a**2)-(y**2)/(b**2),1)

# Plot the shape

p = plot_implicit(eq , (x,-20,20), (y,-20,20),title='$x^2/a^2 - y^2/b^2 = 1$',line_color='r')
#p=plot_implicit(Eq(LHS,RHS),(x,leftside,rightside),(y,up,down),title='title',color='color')
