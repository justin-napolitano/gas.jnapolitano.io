#!/usr/bin/env python
# coding: utf-8

# # Natural Gas Storage Facilities

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


# ## Natural Gas Storage Facility Data

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Storage_Facilities.geojson"

ng_storage_df = gpd.read_file(gisfilepath)

na = ng_storage_df.PROPMAX.min()
ng_storage_df.replace(na, 0 , inplace=True)

ng_storage_df = ng_storage_df.to_crs(epsg=3857)


ng_storage_df.describe()


# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Storage Facility Map
# 
# ```

# ##  Natural Gas Storage Facility Map by Type

# In[3]:


ng_storage_map =ng_storage_df.explore(
    column="TYPE", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['NAICS_DESC','REGION', 'TYPE', 'OWNER', 'BASEGAS', 'TOTALCAP','PROPTOTAL', 'RESERVNAME' ],
     legend =True, # use black outline)
     categorical=True,
    )


ng_storage_map

