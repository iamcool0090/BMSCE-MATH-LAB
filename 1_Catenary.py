from sympy import plot_implicit, symbols,Eq,cosh

x, y, a = symbols('x y a')
a = 4
# Define the equation for the shape
eq = Eq(y,a*cosh(x/a))

# Plot the shape

p = plot_implicit(eq , (x,-20,20), (y,-20,20),title='$y=acosh(x/a)$',line_color='r')
#p=plot_implicit(Eq(LHS,RHS),(x,leftside,rightside),(y,up,down),title='title',color='color')
