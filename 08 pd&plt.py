import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

type_cound = (df["Type1"].value_counts(ascending=True))

plt.barh(type_cound.index, type_cound.values)

plt.show()