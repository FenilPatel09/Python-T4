import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,10))

# Plot 1: Line plot
plt.subplot(2,3,1)
x = np.array([3,8,5,3])
plt.plot(x)

# Plot 2: Bar plot
plt.subplot(2,3,2)
x = np.array(['A','B','C','D'])
y = np.array([10,30,20,25])
plt.bar(x, y)

# Plot 3: Histogram
plt.subplot(2,3,3)
x = np.array([1,2,3,4,1,1,2,3,4,1])
plt.hist(x)

# Plot 4: Scatter plot
plt.subplot(2,3,4)
x = np.array([1,2,3,4,6,5])
y = np.array([10,30,20,24,25,30])  # Adjusted 'y' to match the length of 'x'
plt.scatter(x, y)

# Plot 5: Pie chart
plt.subplot(2,3,5)
x = np.array([36,24,39,40])
labels = ['A', 'B', 'C', 'D']  # Added labels for the pie chart
plt.pie(x, labels=labels)

# Plot 6: Line plot
plt.subplot(2,3,6)
y = np.array([12,34,35,24,31])
plt.plot(y)

plt.show()
