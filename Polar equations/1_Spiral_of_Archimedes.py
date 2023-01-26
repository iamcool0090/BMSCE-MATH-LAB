from pylab import *

theta = linspace(0,2*pi,100)

a = 3
b = 4


r = a + b*theta
polar(theta,r,"r")
title("Spiral of Archimedes : $a + bθ$\n")
show()
