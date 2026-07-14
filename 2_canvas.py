import matplotlib.pyplot as plt

#creating a canvas - sets the size in pixels 
plt.figure(figsize=(6,4))

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

#we can have multiple lines in one single plot 

#line 1 plotting and labelling a line 
plt.plot(x, y1, label = "Squares", color="pink")
#line 2 
plt.plot(x, y2, label = "Line", color="red")

plt.legend() #shows the labels in highlighted manner 
plt.grid(True)#shows a grid in plot 

plt.show()