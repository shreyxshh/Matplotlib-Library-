import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.figure(figsize=(7,4))

# Plot first line
plt.plot(x, y1, color="blue", marker="o", label="Squares")

# Plot second line
plt.plot(x, y2, color="red", marker="s", label="Line")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Example: Legends, Labels & Title")

# Show legend
plt.legend(loc="upper left")

plt.grid(True)
plt.show()