#!/usr/bin/env python
# coding: utf-8

# In[112]:


from pydataset import data
import pandas as pd
import numpy as np


# In[6]:


students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# In[7]:


df


# In[36]:


# 1.a Create a column named passing_english that indicates whether each student has a passing grade in english.
df = df.assign(passing_english=df.english >= 70)
df


# In[38]:


# 1.b Sort the english grades by the passing_english column. How are duplicates handled? Ordered by index 
df.sort_values(by='passing_english')


# In[45]:


# 1.c Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english', 'name'])


# In[46]:


# 1.d Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by=['passing_english', 'english'])


# In[53]:


# 1.e Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df = df.assign(overall_grade=round(((df.math+df.english+df.reading)/3), 2))
df


# In[113]:


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
mpg


# In[59]:


# 2.a How many rows and columns are there?
mpg.shape


# In[60]:


# 2.b What are the data types of each column?
mpg.info()


# In[61]:


# 2.c Summarize the dataframe with .info and .describe
mpg.info(), mpg.describe()


# In[65]:


# 2.d Rename the cty column to city.
mpg = mpg.rename(columns={'cty':'city'})
mpg


# In[66]:


# 2.e Rename the hwy column to highway.
mpg = mpg.rename(columns={'hwy':'highway'})
mpg


# In[67]:


# 2.f Do any cars have better city mileage than highway mileage?
mpg[mpg.city > mpg.highway]


# In[69]:


# 2.g Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg = mpg.assign(mileage_difference = mpg.highway-mpg.city)
mpg


# In[74]:


# 2.h Which car (or cars) has the highest mileage difference?
mileage_max = mpg[mpg.mileage_difference == mpg.mileage_difference.max()]
mileage_max


# In[83]:


# 2.i Which compact class car has the lowest highway mileage? The best?
mpg_compact = mpg[mpg['class'] == 'compact']
mpg_compact[mpg_compact.highway == mpg_compact.highway.min()]


# In[85]:


# 2.j Create a column named average_mileage that is the mean of the city and highway mileage.
mpg = mpg.assign(average_mileage = (mpg.city + mpg.highway)/2)
mpg


# In[106]:


# 2.k Which dodge car has the best average mileage? The worst?
dodge = mpg[mpg.manufacturer == 'dodge']

dodge[dodge.average_mileage == dodge.average_mileage.max()]


# In[107]:


dodge[dodge.average_mileage == dodge.average_mileage.min()]


# In[114]:


# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('Mammals')
mammals


# In[115]:


# 3.a How many rows and columns are there?
mammals.shape


# In[116]:


# 3.b What are the data types?
mammals.info()


# In[139]:


# 3.c Summarize the dataframe with .info and .describe
mammals.describe()


# In[118]:


# 3.d What is the the weight of the fastest animal?
mammals[mammals.speed == mammals.speed.max()]


# In[129]:


# 3.e What is the overal percentage of specials?
num_spec = len(mammals[mammals.specials == True])
round(((num_spec/len(mammals)) * 100), 2)


# In[147]:


# 3.f How many animals are hoppers that are above the median speed? What percentage is this?
med = mammals.speed.median()
hop = mammals[(mammals.hoppers == True) & (mammals.speed >= med)]
hop


# In[148]:


round(((len(hop)/len(mammals)) * 100), 2)


# In[ ]:




