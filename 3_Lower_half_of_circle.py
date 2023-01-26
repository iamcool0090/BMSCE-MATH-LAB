from sympy import plot_implicit, symbols,Eq

x, y, a = symbols('x y a')
a = 2
# Define the equation for the shape
eq = Eq(x**2 + 2*x,4 + 4*y-y**2)

# Plot the shape

p = plot_implicit(eq , (x,-5,3), (y,-2,0),title='$x^2 + 2x = 4 + 4y-y^2$',line_color='r')
#p=plot_implicit(Eq(LHS,RHS),(x,leftside,rightside),(y,up,down),title='title',color='color')
