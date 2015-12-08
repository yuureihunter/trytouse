import random
import numpy
import matplotlib.pyplot as plt
import plotly.plotly as py  # tools to communicate with Plotly's server

histogram=plt.figure()

x = [random.gauss(3,1) for _ in range(400)]
y = [random.gauss(4,2) for _ in range(400)]

bins = numpy.linspace(-10, 10, 100)

plt.hist(x, bins, alpha=0.5)
plt.hist(y, bins, alpha=0.5)
plt.show()
