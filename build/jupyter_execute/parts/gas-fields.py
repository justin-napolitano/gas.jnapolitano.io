#!/usr/bin/env python
# coding: utf-8

# # US Gas and Oil Fields

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


# ## Oil and Natural Gas Field Data

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Oil_and_Natural_Gas_Fields.geojson"

fields_df = gpd.read_file(gisfilepath)
na = fields_df.PR_OIL.min()
fields_df.replace(na, 0 , inplace=True)


fields_df = fields_df.to_crs(epsg=3857)

fields_df.describe()


# ```{eval-rst}
# 
# .. index::
#    single: Oil/Gas Fields Map by Commodity
# 
# ```

# ## Oil Gas Field Map by Commodity

# In[3]:


fields_map =fields_df.explore(
    column="COMMODITY", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['NAICS_DESC','REGION', 'COMMODITY' ],
     legend =True, # use black outline)
     categorical=True,
    )


fields_map

