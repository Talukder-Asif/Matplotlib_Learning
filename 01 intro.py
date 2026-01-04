import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 20, 30])
y2 = np.array([12, 18, 30, 25])
y3 = np.array([13, 20, 22, 30])

#plt.plot(x, y)
#plt.plot(x, y, marker= "o")
#plt.plot(x, y, marker= "o", markersize=10) or
#plt.plot(x, y, marker= "o", ms=10)
#plt.plot(x, y, marker= "o", ms=10, markerfacecolor="#000000", markeredgecolor="red", linestyle="dashed", linewidth=4, color="tomato" )
#plt.plot(x, y2)

# we can use same style for both of the plot by manually copy pest the style or make a dictionary and use it multiple time
line_style = dict(marker= "o", ms=10, markerfacecolor="#000000", markeredgecolor="red", linestyle="solid", linewidth=2)

plt.plot(x,y, color="tomato", **line_style)
plt.plot(x,y2, color="green", **line_style)
plt.plot(x,y3, **line_style)

# We can add title

title_style = dict(fontsize=20,
          family="Arial",
          fontweight="bold",
          color="gray")
plt.title("Class size", **title_style)

plt.xlabel("Year", **title_style)
plt.ylabel("Students", **title_style)

# By default value of x is showing like 2024.00 ......
# to remove this->
plt.xticks(x)

# We can also customized the ticks
plt.tick_params(axis="both", colors="red")

plt.show()