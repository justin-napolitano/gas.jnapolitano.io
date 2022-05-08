#!/usr/bin/env python
# coding: utf-8

# # Natural Gas Market Hubs and Interstate Pipeline Corridors

# ## Data Import

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


# ## Natural Gas Pipeline Data

# In[2]:


## Importing our DataFrames

#gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Pipelines.geojson"
gisfilepath = '/Users/jnapolitano/Projects/data/energy/Natural_Gas_Liquid_Pipelines.zip'

ng_pipeline_df = gpd.read_file(gisfilepath)

ng_pipeline_df = ng_pipeline_df.to_crs(epsg=3857)

#colums = ng_pipeline_df.columns
#uniqe = ng_market_df.TYPE.unique()
ng_pipeline_df = ng_pipeline_df[ng_pipeline_df.TYPEPIPE == 'Interstate']
ng_pipeline_df.dropna(inplace=True)
ng_pipeline_df.head()



# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Terrain Interactive Map
# 
# ```

# ### Natural Gas By Operator Map Data 

# In[3]:


ng_pipeline_map =ng_pipeline_df.explore(
    #column="Operator", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles='Stamen Terrain',
     #tiles="CartoDB positron", # use "CartoDB positron" tiles
     #cmap='Reds', # use "Set1" matplotlib colormap
     #m=ng_pipeline_map,
     #style_kwds=dict(color="black"),
     #marker_kwds= dict(radius=2),
     #tooltip=['','State','Hub_name','Operator','Maxthru','Avgdaily','Numcust','Platform'],
     #legend =False, # use black outline)
     #categorical=True,
     color='grey'
    )
#ng_pipeline_map


# ## Natural Gas Market Hub Data

# In[4]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Market_Hubs.geojson"

ng_market_df = gpd.read_file(gisfilepath)

ng_market_df = ng_market_df.to_crs(epsg=3857)

ng_market_df.describe()


# ## Pipelines and Market Hubs Map

# ```{eval-rst}
# 
# .. index::
#    single: Pipelines by Market Hub Interactive Map
# 
# ```

# In[5]:


ng_market_map =ng_market_df.explore(
    column="Hub_name", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     m=ng_pipeline_map,
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=15),
     tooltip=['Region','State','Hub_name','Operator','Maxthru','Avgdaily','Numcust','Platform'],
     legend =True, # use black outline)
     categorical=True,
    )


ng_market_map

