import matplotlib.pyplot as plt
import numpy as np

# Figure = The entier Canvas
#Ax = Single plot (subplot)

x= np.array([1,2,3,4,5])

figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x*x, color="red")
axes[0,1].bar(x, x*x)

axes[1,0].plot(x, x**3, color="green")
axes[1,1].bar(x, x**3)

plt.tight_layout()
plt.show()