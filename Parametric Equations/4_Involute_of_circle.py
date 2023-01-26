import numpy as np
import matplotlib.pyplot as plt


#not quite sure about this one check it before

def Involute_Circle(a):
  x = []
  y = []


  for t in np.linspace(-100,100,40):
    x.append(a*(np.cos(t) + t*np.sin(t)))
    y.append(a*(np.sin(t)-t*np.cos(t)))




  plt.plot(x,y)
  plt.grid()
  plt.title("Involute of Circle : $x = a(cos(t) + tsin(t)); y = a(sin(t) - tcos(t))$")
  plt.show()

Involute_Circle(10)
