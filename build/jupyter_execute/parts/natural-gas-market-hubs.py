#!/usr/bin/env python
# coding: utf-8

# # Natural Gas Market Hubs

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


# ## Natural Gas Market Hub Data

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Market_Hubs.geojson"

ng_market_df = gpd.read_file(gisfilepath)

ng_market_df = ng_market_df.to_crs(epsg=3857)

ng_market_df.describe()


# ## Natural Gas Market Hubs Map

# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Market Hub Map
# 
# ```

# In[3]:


ng_market_df.explore(column="Avgdaily", # make choropleth based on "PORT_NAME" column
    popup=False, # show all values in popup (on click)
    tiles="Stamen Terrain", # use "CartoDB positron" tiles
    cmap='Greens', # use "Set1" matplotlib colormap
    #style_kwds=dict(color="black"),
    marker_kwds= dict(radius=15),
    tooltip=['Region','State','Hub_name','Operator','Maxthru','Avgdaily','Numcust','Platform'],
    legend =True, # use black outline)
    categorical=False,
)

