import pandas as pd
import os

os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')

employees = pd.read_csv('employees.csv')

employees

employees.set_index('id')
employees = employees.set_index('id')

titles = pd.read_csv('titles.csv', index_col=0)
titles
titles
employees.join(titles, rsuffix='_title')
empl_with_title = employees.join(titles, rsuffix='_title', on=['title_id'])
departments = pd.read_csv('departments.csv')
departments = departments.set_index('id')
departments
departments
empl_with_title.join(departments, on=['department_id'], rsuffix='_dept')
empl_with_title.join(departments, on=['department_id'], rsuffix='_dept', how='inner')
empl_with_title.join(departments, on=['department_id'], rsuffix='_dept', how='right')
