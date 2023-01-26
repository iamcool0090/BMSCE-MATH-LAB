import numpy as np
import matplotlib.pyplot as plt




def Tractrix(a):
  x = []
  y = []


  for t in np.linspace(-10,10,50):
    x.append(1/np.cosh(t))
    y.append(t - np.tanh(t))




  plt.plot(x,y)
  plt.grid()
  plt.title("Tractrix : $x = 1/cosh(t); y = t - tanh(t)$")
  plt.show()

Tractrix(20)
