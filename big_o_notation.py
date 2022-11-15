#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import math


# In[ ]:


# Make a new Jupyter notebook named big_o_notation.ipynb

#Title your chart "Big O Notation"
#Label your x axis "Elements"
#Label your y axis "Operations"
#Label your curves or make a legend for the curves
#Use LaTex notation where possible
#Curves to graph

# y = 0 n + 1 and label the curve "O(1)"
# y = log(n) and label the curve "O(log n)"
# y = n and label the curve "O(n)"
# y = n * log(n) and label it "O(n log n)"
# y = n^2 and label it "O(n^2)"
# y = 2^n and label it "O(2^n)"
# y = n! and label it "O(n!)"
# y = n^n and label it "O(n^n)"
# Bonus Write the code necessary to write your name on a chart. Use box letters.

# Bonus: use curves for letters in your name that have curves in them.



# In[24]:


x = range(1,10)
y1 = [0*n+1 for n in x]
y2 = [(math.log(n)) for n in x]
y3 = [n for n in x]
y4 = [n*(math.log(n)) for n in x]
y5 = [n**2 for n in x]
y6 = [2**n for n in x]
y7 = [math.factorial(n) for n in x]
y8 = [n**n for n in x]

plt.scatter(x,y1, label='O(1)')
plt.scatter(x,y2, label='O(log(n))')
plt.scatter(x,y3, label='O(n)')
plt.scatter(x,y4, label='O(n log(n))')
plt.scatter(x,y5, label='$O(n^2)$')
plt.scatter(x,y6, label='$O(2^n)$')
plt.scatter(x,y7, label='O(n!)')
plt.scatter(x,y8, label='$O(n^n)$')

plt.axis([0,10,0,90])
plt.legend(loc='upper left')
plt.title('Big O Notation')
plt.xlabel('Elements')
plt.ylabel('Operations')

plt.show()


# In[71]:


x = range(0, 15)
x1 = range(0,5)
x2 = [n*0+2 for n in range(0,7)]
x3 = range(0,5)
x4 = range(5,8)
x5 = range(7,10)
x6 = range(6,9)
x7 = [n*0+10 for n in range(0,7)]
x8 = range(10,15)
x9 = [n*0+14 for n in range(0,7)]

y1 = [n*0 for n in range(0,5)]
y2 = [n for n in range(0,7)]
y3 = [n*0+6 for n in range(0,5)]
y4 = [n*3 for n in range(0,3)]
y5 = [-3*n+27 for n in range(7,10)]
y6 = [0*n+3 for n in range(6,9)]
y7 = [n for n in range(0,7)]
y8 = [(-3*n/2)+21 for n in range(10,15)]
y9 = [n for n in range(0,7)]

plt.plot(x1,y1, c='blue')
plt.plot(x2,y2, c='blue')
plt.plot(x3,y3, c='blue')
plt.plot(x4,y4, c='blue')
plt.plot(x5,y5, c='blue')
plt.plot(x6,y6, c='blue')
plt.plot(x7,y7, c='blue')
plt.plot(x8,y8, c='blue')
plt.plot(x9,y9, c='blue')

plt.title('My Name')
plt.axis([-1,15,-1,10])


# In[ ]:




