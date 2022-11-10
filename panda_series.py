#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:




