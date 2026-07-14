import numpy as np
import matplotlib.pyplot as plt

'''
now some other types of plot are to be studied 
-> scatterplot - shows individual points to reveal relationship between two variables/cols/features
-> histogram - groups numbers into "bins" to show the shape/spread of one variable's distribution.
-> Boxplot — summarizes a distribution's median, quartiles, and outliers in one compact shape.
'''

#scatter plot:-
# scatterplot -> plots each (x,y) pair as an individual red dot — no connecting line. 
 
x = [1,2,3,4,5]
y = [5,7,4,6,8]

#scatterplot -> 2 cols/variable/features are required
plt.scatter(x,y)
plt.show()

#histogram:- 

#histogram -> shows spread/shape of only one variable
nums = np.random.randn(100)

#bins help to divide the value eqaully
plt.hist(nums,bins=20)
plt.show()

#boxplot:- 

#boxplot -> used to show outliers of a single column
#any value outside these lines are called outliers

plt.boxplot(nums)
plt.show()
#boxplot shows 5 imp things:-
#1. min - lowest
#2. 25% - lower quatile
#3. 50% - median
#4. 75% - upper quatile
#5. max - highest

#values btw loer and upper quatile are generic or actual values
#values outside of them are considered as outliers