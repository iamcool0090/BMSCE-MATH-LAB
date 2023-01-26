from pylab import *

theta = linspace(0,2*pi,100)

a = 3
b = 4


r = a + b*cos(theta)
polar(theta,r,"r")
title("Limacon : $a + bcos(θ)$\n")
show()
