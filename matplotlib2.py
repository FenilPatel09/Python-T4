import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,10))

# Plot 1: Line plot
plt.subplot(3,2,1)
x = [5, 10, 25, 60, 80]
y = [5, 17, 25, 40, 30]
plt.plot(x, y, 'D:g')

# Plot 2: Bar plot
plt.subplot(3,2,2)
m = [22, 30, 35, 35, 26]
w = [25, 32, 30, 35, 29]
menx = np.arange(len(m))  # Create an array of positions for men bars
barwidth = 0.3
womenx = menx + barwidth  # Shift positions for women bars

plt.bar(menx, m, width=0.3, color='g', label='Men')  # Men bars
plt.bar(womenx, w, width=0.3, color='r', label='Women')  # Women bars

plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Bar plot", fontdict={"fontweight": "bold"})
plt.legend()

plt.show()
