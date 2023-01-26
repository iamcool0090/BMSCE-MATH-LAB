import numpy as np
import matplotlib.pyplot as plt

def circle(a):
  x = []
  y = []


  for i in np.linspace(-10,10,1000):
    x.append(a * np.cos(i))
    y.append(a * np.sin(i))




  plt.plot(x,y)
  plt.grid()
  plt.title("Circle : $x = acos(θ); y = asin(θ)$")
  plt.show()

circle(10)
