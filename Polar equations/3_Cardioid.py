from pylab import *

theta = linspace(0,2*pi,100)

a = 3



r = a + a*cos(theta)
polar(theta,r,"r")
title("Cardioid\n")
show()
