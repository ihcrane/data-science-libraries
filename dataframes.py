#!/usr/bin/env python
# coding: utf-8

# In[23]:


from pydataset import data
import pandas as pd
import numpy as np


# In[24]:


students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# In[5]:


df


# In[6]:


# 1.a Create a column named passing_english that indicates whether each student has a passing grade in english.
df = df.assign(passing_english = df.english >= 70)
df


# In[7]:


# 1.b Sort the english grades by the passing_english column. How are duplicates handled? Ordered by index 
df.sort_values(by='passing_english')


# In[7]:


# 1.c Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(['passing_english', 'name'])


# In[8]:


# 1.d Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(['passing_english', 'english'])


# In[10]:


# 1.e Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df = df.assign(overall_grade=round(((df.math+df.english+df.reading)/3), 2))
df


# In[25]:


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
mpg


# In[26]:


# 2.a How many rows and columns are there?
mpg.shape


# In[27]:


# 2.b What are the data types of each column?
mpg.info()


# In[29]:


# 2.c Summarize the dataframe with .info and .describe
mpg.info(), mpg.describe()


# In[30]:


# 2.d Rename the cty column to city.
mpg.rename(columns={'cty':'city'}, inplace = True)
mpg


# In[31]:


# 2.e Rename the hwy column to highway.
mpg.rename(columns={'hwy':'highway'}, inplace = True)
mpg


# In[32]:


# 2.f Do any cars have better city mileage than highway mileage?
mpg[mpg.city > mpg.highway]
sum(mpg.city > mpg.highway)


# In[33]:


# 2.g Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg = mpg.assign(mileage_difference = mpg.highway-mpg.city)
mpg


# In[34]:


# 2.h Which car (or cars) has the highest mileage difference?
mpg[mpg.mileage_difference == mpg.mileage_difference.max()]


# In[42]:


# 2.i Which compact class car has the lowest highway mileage? The best?
mpg[mpg['class'] == 'compact'].sort_values('highway', ascending=False).head()


# In[43]:


mpg[mpg['class'] == 'compact'].sort_values('highway', ascending=False).tail()


# In[49]:


# 2.j Create a column named average_mileage that is the mean of the city and highway mileage.
mpg = mpg.assign(average_mileage = (mpg['city'] + mpg['highway'])/2)
mpg


# In[58]:


# 2.k Which dodge car has the best average mileage? The worst?
mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage').tail()


# In[57]:


mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage').head()


# In[69]:


# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('Mammals')
mammals
data('Mammals', show_doc=True)


# In[25]:


# 3.a How many rows and columns are there?
mammals.shape


# In[61]:


# 3.b What are the data types?
mammals.info()


# In[27]:


# 3.c Summarize the dataframe with .info and .describe
mammals.describe()


# In[56]:


# 3.d What is the the weight of the fastest animal?
mammals.sort_values('speed', ascending=False).head()


# In[67]:


# 3.e What is the overal percentage of specials?
round(((mammals['specials'].sum()/len(mammals)) * 100), 2)


# In[68]:


# 3.f How many animals are hoppers that are above the median speed? What percentage is this?
fast_hoppers = mammals[mammals['hoppers'] & (mammals['speed'] >= mammals['speed'].median())]
fast_hoppers


# In[33]:


round(((len(fast_hoppers)/len(mammals)) * 100), 2)


# In[ ]:




