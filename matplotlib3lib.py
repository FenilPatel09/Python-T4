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

# Plot 3: Pie chart
plt.subplot(3,2,3)
car = ['Maruti', 'Hyundai', 'Kia', 'Toyota', 'Honda']
popularity = [25, 50, 30, 20, 35]
plt.pie(popularity, labels=car, autopct="%1.1f%%", startangle=90)
plt.title("Car Company Popularity")

# Plot 4: Scatter plot
plt.subplot(3,2,4)
math = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
plt.scatter(range(1, 11), math, marker='o', color='y', label='Math')
plt.scatter(range(1, 11), science, marker='*', color='b', label='Science')
plt.legend()

# Plot 5: Horizontal bar chart
plt.subplot(3,2,5)
lan = ['Java', 'Python', 'PHP', 'JavaScript', 'C', 'C++']
pop = [20, 100, 25, 30, 45, 50]
plt.barh(lan, pop, color=['r', 'g', 'b', 'k', 'c', 'm'])

# Plot 6: Histogram
plt.subplot(3,2,6)
data = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 60, 60, 70]
plt.hist(data, color='red')

plt.show()
