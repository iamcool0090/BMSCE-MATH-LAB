from pylab import *

theta = linspace(0,2*pi,100)

a = 4
b = 10

x = sqrt(a*sin(theta)**2 + b*cos(theta)**2)
r = a*b/x
polar(theta,r,"r")
title("Ellipse\n")
show()
