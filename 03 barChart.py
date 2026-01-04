import matplotlib.pyplot as lib
import matplotlib.pyplot as plt
import numpy as np


# Bar Chart = Compare categories of data by representing each category with a bar

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 5, 2, 6, 3, 1])

# for bar chart, we use plt.bar() function
plt.bar(categories, values)
# for horizontal bar chart, we use plt.barh() function
#plt.barh(categories, values)

plt.show()