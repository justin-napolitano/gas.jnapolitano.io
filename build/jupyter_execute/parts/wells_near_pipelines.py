#!/usr/bin/env python
# coding: utf-8

# # Potential Carbon Storage Wells Near Pipelines

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
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point
from haversine import Unit
from geopy.distance import distance


# ## Query Plan
# 
# ### Restrictions
# * Must be near a pipeline terminal
# 
# ### Imports 
# 
# * Pipeline Data
# * Well Data
# 
# ### Filtering
# 
# * For each well calculate nearest pipeline
# 
# * For each well calculate geographic distance from pipeline
# 
# * eliminate wells further than 2 km from a pipeline
# 

# ## Data Frame Import

# ### Wells Dataframe

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/non-active-wells.geojson"


wells_df = gpd.read_file(gisfilepath)

wells_df = wells_df.to_crs(epsg=3857)


# In[3]:


wells_df.columns


# ### Pipeline DataFrame

# In[4]:


## Importing Pipeline Dataframe

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Pipelines.geojson"


pipeline_df = gpd.read_file(gisfilepath)

pipeline_df = pipeline_df.to_crs(epsg=3857)


# #### Removing Gathering Pipes from the Data

# In[5]:


pipeline_df.drop(pipeline_df[pipeline_df['TYPEPIPE'] == 'Gathering'].index, inplace = True)


# #### Adding PipeGeometry Column

# In[6]:


pipeline_df['PipeGeometry'] = pipeline_df['geometry'].copy()


# In[7]:


pipeline_df.columns


# ## Joining Well and Pipeline Data

# In[8]:


nearest_wells_df= wells_df.sjoin_nearest(pipeline_df, how = 'left', distance_col="distance_euclidian")
nearest_wells_df.columns


# In[9]:


nearest_wells_df


# ###  Adding a Distance Km Column

# In[10]:


nearest_wells_df['distance_km'] = nearest_wells_df.distance_euclidian.apply(lambda x: x / 1000)


# In[11]:


filtered_wells = nearest_wells_df.loc[nearest_wells_df['distance_km'] < 2].copy()


# In[12]:


filtered_wells.describe()


# ## Wells Base Map

# In[13]:


well_map_ax = filtered_wells.plot(figsize=(15, 15), alpha=0.5, edgecolor='k', markersize = .5)
cx.add_basemap(well_map_ax, zoom=6)
#filtered_wells.plot()


# ## Pipelines Base Map

# In[14]:


pipeline_map = pipeline_df.plot(figsize = (15,15), alpha=0.5,)
cx.add_basemap(pipeline_map, zoom=6)


# ## Pipeline and Potential Carbon Storage Well Map

# In[15]:


combined_map = wells_df.plot(ax = pipeline_map, alpha=0.5, figsize = (20,20), edgecolor='k', markersize = .5)

#cx.add_basemap(well_map, zoom=6)
#plt.show()


# In[16]:


combined_map.figure

