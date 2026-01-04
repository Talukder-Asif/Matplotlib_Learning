import matplotlib.pyplot as lib
import matplotlib.pyplot as plt
import numpy as np


# PI Chart = Circular chart divided into slice to show percentage of the total
# Good for visualizing distribution among categories

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
colors = ["tomato", "yellow", "blue", "green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors= colors,
                explode=[0, 0, 0, 0.1],
                shadow=True,
                startangle=90)

plt.title("KYAY Pre Cadet")

plt.show()