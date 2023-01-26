import numpy as np
import matplotlib.pyplot as plt




def Nephroid(a):
  x = []
  y = []


  for t in np.linspace(-6,6,50):
    x.append(a*(3*np.cos(t) - np.cos(3*t)))
    y.append(a*(3*np.sin(t) - np.sin(3*t)))




  plt.plot(x,y)
  plt.grid()
  plt.title("Nephroid : $x = a(3cos(t) - cos(3t)); y = a(3sin(t) - sin(3t))$")
  plt.show()

Nephroid(20)
