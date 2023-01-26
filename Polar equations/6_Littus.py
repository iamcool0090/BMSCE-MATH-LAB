from pylab import *

theta = linspace(0,2*pi,100)

a = 4
r = sqrt(a**2/theta)

polar(theta,r,"r")


title("Lituus : $r^2 = a^2/θ$\n")
show()
