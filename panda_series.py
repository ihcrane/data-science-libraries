#!/usr/bin/env python
# coding: utf-8

# In[55]:


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


# In[21]:


# 3. Output only the values from fruits.
fruits.values


# In[24]:


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


# In[46]:


# 9. Determine the string value that occurs most frequently in fruits.
fruits.mode()
fruits.value_counts().head(1)


# In[45]:


# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().tail(1)


# In[56]:


# 1. Capitalize all the string values in fruits.
fruits_cap = fruits.str.capitalize()
fruits_cap


# In[62]:


# 2. Count the letter "a" in all the string values (use string vectorization).
fruits_a = fruits.str.count('a')
fruits_a


# In[96]:


# 3. Output the number of vowels in each and every string value.
def vowel_count(string):
    vowels = 'aeiou'
    count = 0
    for n in string:
        if n in vowels:
            count += 1
    return count
fruits_with_vowels = fruits.apply(vowel_count)
fruits_with_vowels


# In[82]:


# 4. Write the code to get the longest string value from fruits.
fruits_long = fruits.str.len().max()
print(fruits[fruits.str.len() == fruits_long])
print(fruits_long)


# In[75]:


# 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() > 5]


# In[85]:


# 6. Find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.str.count('o') >= 2]


# In[86]:


# 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]


# In[87]:


# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]


# In[113]:


# 9. Which string value contains the most vowels.
most_vowels = fruits_with_vowels.sort_values().tail(1)

print(fruits.loc[most_vowels])
most_vowels


# In[ ]:




