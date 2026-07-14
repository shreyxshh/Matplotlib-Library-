#improting matplotlib
import matplotlib.pyplot as plt

#line plot 
x = [1,2,3,4,5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.xlabel('This is x Label')
plt.ylabel('This is y Label')
plt.title('This is my first line plot')

plt.show()
