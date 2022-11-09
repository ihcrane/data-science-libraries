#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[5]:


a[a < 0]


# In[6]:


a[a > 0]


# In[4]:


new_a = a[a > 0]
new_a[new_a % 2 == 0]


# In[6]:


a + 3
a[a > 0]


# In[12]:


new_a = a ** 2

new_a.mean()
new_a.std()


# In[16]:


a - a.mean()


# In[17]:


(a - a.mean())/a.std()


# In[29]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
print(sum_of_a)


# In[22]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min_of_a)


# In[23]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
print(max_of_a)


# In[30]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = a.mean()
print(mean_of_a)


# In[33]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = np.prod(a)
print(product_of_a)


# In[37]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = a ** 2
print(squares_of_a)


# In[39]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = a[a % 2 == 1]
print(odds_in_a)


# In[40]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a % 2 == 0]
print(evens_in_a)


# In[46]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = np.sum(b)
print(sum_of_b)


# In[48]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = np.amin(b)
print(min_of_b)


# In[49]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = np.amax(b)
print(max_of_b)


# In[51]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = np.mean(b)
print(mean_of_b)


# In[52]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.prod(b)
print(product_of_b)


# In[54]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b ** 2
print(squares_of_b)


# In[56]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 == 1]
print(odds_in_b)


# In[57]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# In[60]:


# Exercise 9 - print out the shape of the array b.
print(b.shape)


# In[63]:


# Exercise 10 - transpose the array b.
print(np.transpose(b))


# In[70]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(np.reshape(b, 6))


# In[73]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(b.reshape(6, 1))


# In[75]:


## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
print(c.min())
print(c.max())
print(c.sum())
print(c.prod())


# In[87]:


# Exercise 2 - Determine the standard deviation of c.
print(c.std())


# In[83]:


# Exercise 3 - Determine the variance of c.
print(np.var(c))


# In[89]:


# Exercise 4 - Print out the shape of the array c
print(c.shape)


# In[90]:


# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))


# In[91]:


# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c, c))


# In[95]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print((np.transpose(c) * c).sum())


# In[97]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print((np.transpose(c) * c).prod())


# In[99]:


## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))


# In[101]:


# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))


# In[102]:


# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))


# In[103]:


# Exercise 4 - Find all the negative numbers in d
d[d < 0]


# In[104]:


# Exercise 5 - Find all the positive numbers in d
d[d > 0]


# In[106]:


# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))


# In[111]:


# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))


# In[113]:


# Exercise 8 - Print out the shape of d.
print(d.shape)


# In[117]:


# Exercise 9 - Transpose and then print out the shape of d.
print(d.transpose())


# In[118]:


# Exercise 10 - Reshape d into an array of 9 x 2
print(d.reshape(9, 2))


# In[ ]:




