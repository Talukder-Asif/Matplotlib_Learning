import matplotlib.pyplot as plt
import numpy as np

#Scatter Graph = show the relationship between two variables
#               helps to identify a correlations

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 82, 85, 87, 90]) #Grades
x2 = np.array([0, 2, 0, 4, 7, 4, 2, 4, 5, 6, 6]) # Hours studied
y2 = np.array([60, 40, 50, 80, 50, 33, 55, 70, 92, 78, 91]) #Grades

plt.scatter(x1, y1, color="skyblue",
            alpha=0.5, # Transparency
            s = 100, #size
            label= "Class A")

plt.scatter(x2, y2, label= "Class A")
plt.title("Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.legend()
plt.show()