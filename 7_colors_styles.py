import matplotlib.pyplot as plt 

#fig 1
fig = plt.figure(figsize=(6,4))

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [1,3,5,7,9]

#-> plotting using subplot
plt.subplot(2,2,1)
plt.plot(x,y1,label = 'blue' , color = 'blue')
plt.title('Axes1')

plt.subplot(2,2,4)
plt.plot(x,y2,label = 'yellow', color = 'yellow' )
plt.title('Axes2')

plt.show()

#fig 2
fig = plt.figure(figsize=(6,4))

x = [1,2,3,4,5]
y1 = [2,4,6,8,10]
y2 = [1,3,5,7,9]

#-> plotting both lines in single figure

'''
-> lw = line width 
-> ls = line style 
-> marker = choose the type of points to be shown on the graph 
'''
plt.plot(x,y1,label = 'blue' , color = 'blue', lw = '2.5')
plt.plot(x,y2,label = 'green', color = 'green', lw = '1.5', ls='-.' , marker = '*')


plt.title('Graph')
plt.legend()

plt.show()