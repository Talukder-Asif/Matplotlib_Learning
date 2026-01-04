import matplotlib.pyplot as lib
import matplotlib.pyplot as plt
import numpy as np


# grid() = Helps make plots easier to read by adding reference lines.

x = np.array([1,2,3,4,5])
y = np.array([5, 10, 15, 20, 25])


#plt.grid() # gridline both in x and y axis
#plt.grid(axis="x") # gridline only in x axis
#plt.grid(axis="y") # gridline only in y axis

#Customization
plt.grid(axis="y",
         linewidth = 2,
         color="gray",
         linestyle="dashdot")

plt.plot(x, y)
plt.show()