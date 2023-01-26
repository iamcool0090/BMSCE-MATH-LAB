from sympy import plot_implicit, symbols,Eq
import math
x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape


eq = Eq(y**2*(a-x),x**2*(a+x))

# Plot the shape

p = plot_implicit(eq , (x,-20,20), (y,-20,20),title='$y^2(a-x) = x^2(a+x)$',line_color='r')
#p=plot_implicit(Eq(LHS,RHS),(x,leftside,rightside),(y,up,down),title='title',color='color')

