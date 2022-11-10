#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np

fruit = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", 
          "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
          "gooseberry", "papaya"]
fruits = pd.Series(fruit)


# In[19]:


# 1. Determine the number of elements in fruits.
fruits.size


# In[20]:


# 2. Output only the index from fruits.
fruits.index


# In[4]:


# 3. Output only the values from fruits.
fruits.values


# In[6]:


# 4. Confirm the data type of the values in fruits.
fruits.dtype


# In[27]:


# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head()
fruits.tail(3)
fruits.sample(2)


# In[28]:


# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()


# In[29]:


# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()


# In[37]:


# 8. Determine how many times each unique string value occurs in fruits.
fruits.value_counts()


# In[9]:


# 9. Determine the string value that occurs most frequently in fruits.
fruits.mode()
fruits.value_counts().head(1)


# In[10]:


# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().tail(1)
fruits.value_counts().nsmallest(n=1, keep='all')


# In[37]:


# 1. Capitalize all the string values in fruits.
fruits.str.capitalize()


# In[36]:


# 2. Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a').sort_values()


# In[43]:


# 3. Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]').sort_values()


# In[38]:


# 4. Write the code to get the longest string value from fruits.
fruits_long = fruits.str.len().max()
print(fruits[fruits.str.len() == fruits_long])
print(fruits_long)


# In[40]:


# 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]


# In[85]:


# 6. Find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.str.count('o') >= 2]


# In[86]:


# 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]


# In[87]:


# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]


# In[41]:


# 9. Which string value contains the most vowels.
fruits.loc[fruits.str.count('[aeiou]').max()]


# In[6]:


import matplotlib as plt
letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters)


# In[8]:


# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts().nlargest(n=1, keep='all')


# In[9]:


# 2. Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1, keep='all')


# In[21]:


# 3. How many vowels are in the Series?
vowels_count = letters.str.count('[aeiou]').sum()
vowels_count


# In[22]:


# 4. How many consonants are in the Series?
consonant_count = len(letters) - vowels_count
consonant_count


# In[23]:


# 5. Create a Series that has all of the same letters but uppercased.
letters.str.upper()


# In[31]:


# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
most_common_letters = letters.value_counts().nlargest(n=6, keep='all')
most_common_letters.plot.bar(title='Most Common letters',rot=0)


# In[43]:


numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', 
           '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', 
           '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', 
           '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(numbers)


# In[41]:


# 1. What is the data type of the numbers Series?
numbers.dtype


# In[42]:


# 2. How many elements are in the number Series?
len(numbers)


# In[52]:


# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
numbers = numbers.str.replace('$', '').str.replace(',', '')
numbers = numbers.astype('float')


# In[54]:


# 4. Run the code to discover the maximum value from the Series.
numbers.max()


# In[55]:


# 5. Run the code to discover the minimum value from the Series.
numbers.min()


# In[56]:


# 6. What is the range of the values in the Series?
num_range = numbers.max() - numbers.min()
num_range


# In[70]:


# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
num_bin_series = pd.cut(numbers, [0, 1200000, 2400000, 3600000, 5000000])
num_bin_series.value_counts()


# In[71]:


# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
num_bin_series.value_counts().plot.bar(title='Numbers Bin Graph', rot=45).set(xlabel='Bin Interval', ylabel='Bin Amount')


# In[ ]:




