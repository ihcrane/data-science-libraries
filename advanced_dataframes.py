#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from pydataset import data
from env import username, hostname, password

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url


# In[8]:


url = get_db_url(username, hostname, password, 'employees')


# In[11]:


employees = pd.read_sql('SELECT * FROM employees', url)
employees


# In[12]:


titles = pd.read_sql('SELECT * FROM titles', url)
titles


# In[35]:


employees.info(), employees.describe()


# In[36]:


titles.info(), titles.describe()


# In[25]:


titles.title.nunique()


# In[39]:


titles.to_date.max()


# In[26]:


titles.to_date.min()


# In[29]:


from datetime import date
titles[titles.to_date < date.today()].sort_values(by='to_date', ascending=False).head(1)


# In[54]:


# Exercises II


# In[31]:


# 1. Copy the users and roles DataFrames from the examples above.
# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[32]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[33]:


# 2. What is the result of using a right join on the DataFrames?
users.merge(roles, how='right', left_on='role_id', right_on='id')


# In[35]:


# 3. What is the result of using an outer join on the DataFrames?
users.merge(roles, how='outer', left_on='role_id', right_on='id')


# In[37]:


# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
users_dropped = users.drop(columns='role_id')
roles_dropped = roles.drop(columns='id')
users_dropped.merge(roles_dropped, how='outer')


# In[40]:


# 5. Load the mpg dataset from PyDataset.
mpg = data('mpg')
mpg


# In[36]:


# 6. Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True)


# In[41]:


# 7. How many rows and columns are in the dataset?
mpg.shape


# In[47]:


# 8. Check out your column names and perform any cleanup you may want on them.
mpg = mpg.rename(columns={'cty':'city', 'hwy':'highway'})
mpg


# In[99]:


# 9. Display the summary statistics for the dataset.
mpg.info(), mpg.describe()


# In[43]:


# 10. How many different manufacturers are there?
mpg['manufacturer'].nunique()


# In[45]:


# 11. How many different models are there?
mpg['model'].nunique()


# In[60]:


# 12. Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
mpg['mileage_diff'] = mpg['highway'] - mpg['city']
mpg


# In[49]:


# 13. Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
mpg = mpg.assign(avg_mileage = round(((mpg['highway']+mpg['city'])/2), 2))
mpg


# In[50]:


# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
mpg = mpg.assign(is_auto = mpg['trans'].str.contains('auto'))
mpg


# In[73]:


# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.groupby('manufacturer')['avg_mileage'].mean().sort_values(ascending=False)


# In[72]:


# 16. Do automatic or manual cars have better miles per gallon?
mpg.groupby('is_auto')['avg_mileage'].mean().rename(index={0:'Manual', 1:'Automatic'})


# In[81]:


# 1. Use your get_db_url function to help you explore the data from the chipotle database.
chipotle_url = get_db_url(username, hostname, password, 'chipotle')
chipotle = pd.read_sql('SELECT * FROM orders', chipotle_url)
chipotle


# In[82]:


# 2. What is the total price for each order?
chipotle['item_price'] = chipotle['item_price'].str.replace('$','').astype('float')
chipotle


# In[84]:


chipotle.groupby('order_id')['item_price'].sum()


# In[85]:


# 3. What are the most popular 3 items?
chipotle.groupby('item_name')['quantity'].sum().nlargest(3)


# In[86]:


# 4. Which item has produced the most revenue?
chipotle.groupby('item_name')['item_price'].sum().nlargest(1)


# In[90]:


# 5. Join the employees and titles DataFrames together.
emp_title = employees.merge(titles, on='emp_no')
emp_title


# In[91]:


# 6. For each title, find the hire date of the employee that was hired most recently with that title.
emp_title.groupby('title')['hire_date'].max()


# In[93]:


# 7. Write the code necessary to create a cross tabulation of the number of titles by department. 
## (Hint: this will involve a combination of SQL code to pull the necessary 
### data and python/pandas code to perform the manipulations.)
emp_titles = pd.read_sql('SELECT * FROM employees JOIN titles USING(emp_no) WHERE to_date > CURDATE()', url)
dept_emp = pd.read_sql('SELECT * FROM dept_emp', url)
departments = pd.read_sql('SELECT * FROM departments', url)


# In[95]:


emp_title_dept = emp_titles.merge(dept_emp, how='inner', on='emp_no')
full_db = emp_title_dept.merge(departments, how='inner', on='dept_no')

pd.crosstab(full_db.title, full_db.dept_name).T


# In[ ]:




