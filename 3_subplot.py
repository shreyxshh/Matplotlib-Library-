import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# First plot in position 1 of a 2x2 grid
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'r--')
plt.title("line plot")

# Second plot in position 4 of a 2x2 grid
plt.subplot(2, 2, 4)
plt.plot(x, y2, 'g*')
plt.title("square plot")    

plt.tight_layout() #automatically adds spacing in btw labels so they dont overlap
plt.show()