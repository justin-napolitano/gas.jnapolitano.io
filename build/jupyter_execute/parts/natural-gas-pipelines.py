#!/usr/bin/env python
# coding: utf-8

# # Natural Gas Pipelines

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

#uniqe = ng_market_df.TYPE.unique()
ng_pipeline_df.dropna(inplace=True)
ng_pipeline_df.describe()


# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Pipeline  Map
# 
# ```

# ## Natural Gas Pipeline Map

# In[3]:


ng_pipeline_map =ng_pipeline_df.explore(
    column="TYPEPIPE", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Reds', 
     #m=ng_market_map,# use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     #marker_kwds= dict(radius=6),
     tooltip=['TYPEPIPE','Operator'],
     legend =False, # use black outline)
     categorical=True,)

ng_pipeline_map

