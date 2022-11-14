#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import numpy as np
from pydataset import data
from env import username, hostname, password

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url


# In[29]:


url = get_db_url(username, hostname, password, 'employees')


# In[30]:


employees = pd.read_sql('SELECT * FROM employees', url)
employees


# In[33]:


titles = pd.read_sql('SELECT * FROM titles', url)
titles


# In[35]:


employees.info(), employees.describe()


# In[36]:


titles.info(), titles.describe()


# In[38]:


titles.title.unique()


# In[39]:


titles.to_date.max()


# In[52]:


from datetime import date
titles[titles.to_date < date.today()].sort_values(by='to_date').head(1)


# In[53]:


titles[titles.to_date < date.today()].sort_values(by='to_date', ascending=False).head(1)


# In[54]:


# Exercises II


# In[71]:


# 1. Copy the users and roles DataFrames from the examples above.
# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[72]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[74]:


# 2. What is the result of using a right join on the DataFrames?
users.merge(roles, how='right')


# In[76]:


# 3. What is the result of using an outer join on the DataFrames?
users.merge(roles, how='outer')


# In[86]:


# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
users_dropped = users.drop(columns='id')
roles_dropped = roles.drop(columns='id')
users_dropped.merge(roles_dropped, how='inner')


# In[93]:


# 5. Load the mpg dataset from PyDataset.
mpg = data('mpg')
mpg


# In[94]:


# 6. Output and read the documentation for the mpg dataset.
mpg


# In[61]:


# 7. How many rows and columns are in the dataset?
#234 rows, 11 columns


# In[97]:


# 8. Check out your column names and perform any cleanup you may want on them.
mpg = mpg.rename(columns={'cty':'city', 'hwy':'highway'})
mpg


# In[99]:


# 9. Display the summary statistics for the dataset.
mpg.info(), mpg.describe()


# In[103]:


# 10. How many different manufacturers are there?
mpg.manufacturer.unique(), len(mpg.manufacturer.unique())


# In[106]:


# 11. How many different models are there?
mpg.model.unique(), len(mpg.model.unique())


# In[109]:


# 12. Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
mpg = mpg.assign(mileage_dif = (mpg.highway-mpg.city))
mpg


# In[110]:


# 13. Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
mpg = mpg.assign(avg_mileage = round(((mpg.highway+mpg.city)/2), 2))
mpg


# In[111]:


# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
mpg = mpg.assign(is_auto = mpg.trans.str.contains('auto'))
mpg


# In[117]:


# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.groupby('manufacturer').avg_mileage.agg(['mean'])


# In[125]:


# 16. Do automatic or manual cars have better miles per gallon?
mpg.groupby('is_auto').avg_mileage.agg(['mean']).rename(index={0:'Manual', 1:'Automatic'})


# In[ ]:





# In[ ]:




