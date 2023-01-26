import numpy as np
import matplotlib.pyplot as plt

def Folium_descartes(a):
  x = []
  y = []


  for t in np.linspace(-6,6,50):
    x.append((3*a*t)/(1+t**3))
    y.append((3*a*(t**2)/(1+t**3)))




  plt.plot(x,y)
  plt.grid()
  plt.title("Folium of Descartes : $x(t) = (3at)/(1+t^3); y = 3at^2/(1+t^3)$")
  plt.show()

Folium_descartes(10)
