#!/usr/bin/env python
# coding: utf-8

# # Identifying Potential Carbon Storage Facilities

# ## Import and Procedural Functions

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
import rtree
from zlib import crc32
import hashlib
from shapely.geometry import Point, LineString, Polygon


# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Oil_and_Natural_Gas_Wells.geojson"


fields_df = gpd.read_file(gisfilepath)

#fields_df = fields_df.to_crs(epsg=3857)


# ## Plot Status Box Plot

# In[3]:


fields_df.STATUS.value_counts().plot(kind='bar')
#data['title'].value_counts()[:20].plot(kind='barh')


# ### Encode Dataframe to Categorical Variables

# In[4]:


#Casting to Category

fields_df["STATUS"] = fields_df["STATUS"].astype('category')

#Creating Cat Column 
fields_df["STAUTS_CAT"] = fields_df["STATUS"].cat.codes
fields_df.head()


# ### Sorting Data by Category

# In[5]:


fields_df = fields_df.sort_values(['STAUTS_CAT'])


# ### Creating Category Table

# In[6]:


# Creating a Dictionary of Categories
cat_dict =dict(enumerate(fields_df['STATUS'].cat.categories)) 

# Creating a Dataframe for references
df = pd.DataFrame.from_dict(data=cat_dict,columns=['Category'], orient='index')
df.style

# {0: 'bad', 1: 'good', 2: 'great'}
#grp = fields_df.groupby('STAUTS_CAT')['STATUS'].aggregate(lambda x: print(x))


# ### Dropping Categories from the Data Frame

# #### Active Well

# In[7]:


fields_df.drop(fields_df[fields_df['STAUTS_CAT'] == 0].index, inplace = True)


# #### Producing Well

# In[8]:


fields_df.drop(fields_df[fields_df['STAUTS_CAT'] == 2].index, inplace = True)


# #### PRODUCING, NON_ACTIVE WEll

# In[9]:


fields_df.drop(fields_df[fields_df['STAUTS_CAT'] == 3].index, inplace = True)


# #### Unknown Well

# In[10]:


fields_df.drop(fields_df[fields_df['STAUTS_CAT'] == 5].index, inplace = True)


# #### Well Development

# In[11]:


fields_df.drop(fields_df[fields_df['STAUTS_CAT'] == 6].index, inplace = True)


# ### Writing filtered DF to CSV 

# In[12]:


fields_df.reset_index(inplace=True)
fields_df["STATUS"] = fields_df["STATUS"].astype('string')
fields_df.to_csv("/Users/jnapolitano/Projects/data/energy/non-active-wells.csv")
fields_df.to_file('/Users/jnapolitano/Projects/data/energy/non-active-wells.geojson', driver='GeoJSON')  

