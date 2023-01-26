import numpy as np
import matplotlib.pyplot as plt

def Circle(a):
  x = []
  y = []


  for t in np.linspace(-6,6,50):
    x.append(5*np.cos(t))
    y.append(5*np.sin(t))




  plt.plot(x,y)
  plt.grid()
  plt.title("Circle : $x = 5cos(θ); y = 5sin(θ)$")
  plt.show()

Circle(10)
