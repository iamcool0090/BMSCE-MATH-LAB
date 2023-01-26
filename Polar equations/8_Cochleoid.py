from pylab import *

theta = linspace(0,2*pi,100)

a = 4
r = (a*sin(theta))/theta

polar(theta,r,"r")


title("Cochleoid : $r = asin(θ)/θ$\n")
show()
