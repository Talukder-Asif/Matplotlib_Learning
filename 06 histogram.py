import matplotlib.pyplot as plt
import numpy as np

# Histogram = A visual representation of the distribution of quantitative data.
# They group values into bins and count how manu fall in each range

scores = np.random.normal(loc=80, scale=10, size= 100)
print(scores)
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=15,
         edgecolor="white")

plt.show()

