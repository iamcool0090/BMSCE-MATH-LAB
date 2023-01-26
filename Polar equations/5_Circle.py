from pylab import *

theta = linspace(0,2*pi,100)

a = 1
r = linspace(a,a,100)
polar(theta,r,"r")

a = 2
r = linspace(a,a,100)
polar(theta,r,"g")

a = 3
r = linspace(a,a,100)
polar(theta,r,"b")

title("Circles of a=1,2,3\n")
show()
