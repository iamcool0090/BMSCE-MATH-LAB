from sympy import plot_implicit, symbols,Eq
x, y, a = symbols('x y a')
a = 4
# Define the equation for the shape
eq = Eq(x**2 + y**2, a**2)

# Plot the shape
p = plot_implicit(eq , (x,-4,4), (y,-4,4),title='$x^2 + y^2 = a^2$',line_color='r')
#p=plot_implicit(Eq(LHS,RHS),(x,leftside,rightside),(y,up,down),title='title',color='color')

