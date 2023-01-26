import numpy as np
import matplotlib.pyplot as plt


#not quite sure about this one check it before

def Cardioid(a):
  x = []
  y = []


  for t in np.linspace(-6,6,50):
    x.append(a*(2*np.cos(t) - np.cos(2*t)))
    y.append(a*(3*np.sin(t) - np.sin(3*t)))




  plt.plot(x,y)
  plt.grid()
  plt.title("Cardioid : $x = a(2cos(t) - cos(2t)); y = a(3sin(t) - sin(3t))$")
  plt.show()

Cardioid(20)
