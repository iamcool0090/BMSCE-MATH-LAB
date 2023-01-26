from pylab import *

theta = linspace(0,2*pi,100)

a = 4
r = a - a*sin(theta)

polar(theta,r,"r")


title("Cardioid : $r = a - asin(θ)$\n")
show()
