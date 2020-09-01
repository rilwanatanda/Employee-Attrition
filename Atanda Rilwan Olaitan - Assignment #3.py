#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# import dataset
data = pd.read_csv('Assignment3_Dataset_Heatmap.csv')

# Create pivot using Pandas
pv_data = data.pivot_table(index='continent', columns='year', values='lifeExp')

# Create heatmap using Seaborn
plt.figure(figsize=(12,6))
plt.xlabel('', size=12)
plt.ylabel('', size=12)
plt.title('Gapminder-Five Year Data HeatMap')

sns.heatmap(pv_data, annot=True, linewidths=0.3)

