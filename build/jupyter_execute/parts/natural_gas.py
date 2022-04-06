#!/usr/bin/env python
# coding: utf-8

# # US Natural Gas Network Overview

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


# ## Hashing Functions

# In[2]:


def bytes_to_float(b):
    return float(crc32(b) & 0xffffffff) / 2**32

def str_to_float(s, encoding="utf-8"):
    return bytes_to_float(s.encode(encoding))


# ## Oil and Natural Gas Field Data

# In[3]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Oil_and_Natural_Gas_Fields.geojson"

fields_df = gpd.read_file(gisfilepath)

fields_df = fields_df.to_crs(epsg=3857)

fields_df.columns


# ```{eval-rst}
# 
# .. index::
#    single: Oil/Gas Fields Map by Commodity
# 
# ```

# ### Oil Gas Field Map by Commodity

# In[4]:


fields_map =fields_df.explore(
    column="COMMODITY", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['NAICS_DESC','REGION', 'COMMODITY' ],
     legend =True, # use black outline)
     categorical=True,
    )


fields_map


# ## Natural Gas Storage Facility Data

# In[5]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Storage_Facilities.geojson"

ng_storage_df = gpd.read_file(gisfilepath)

ng_storage_df = ng_storage_df.to_crs(epsg=3857)

colums = ng_storage_df.columns
uniqe = ng_storage_df.TYPE.unique()
print(colums)
print(uniqe)


# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Storage Facility Map
# 
# ```

# ###  Natural Gas Storage Facility Map by Type

# In[6]:


ng_storage_map =ng_storage_df.explore(
    column="TYPE", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     tooltip=['NAICS_DESC','REGION', 'TYPE', 'OWNER', 'BASEGAS', 'TOTALCAP','PROPTOTAL', 'RESERVNAME' ],
     legend =True, # use black outline)
     categorical=True,
    )


ng_storage_map


# ## Natural Gas Pipeline Data

# In[7]:


## Importing our DataFrames

#gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Pipelines.geojson"
gisfilepath = '/Users/jnapolitano/Projects/data/energy/Natural_Gas_Liquid_Pipelines.zip'

ng_pipeline_df = gpd.read_file(gisfilepath)

ng_pipeline_df = ng_pipeline_df.to_crs(epsg=3857)

colums = ng_pipeline_df.columns
#uniqe = ng_market_df.TYPE.unique()
ng_pipeline_df.dropna(inplace=True)
ng_pipeline_df


# ```{eval-rst}
# 
# .. index::
#    single: Natural Gas Pipeline  Map
# 
# ```

# ### Natural Gas Pipeline Map

# In[8]:


ng_pipeline_map =ng_pipeline_df.explore(
    column="TYPEPIPE", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Reds', 
     #m=ng_market_map,# use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     #marker_kwds= dict(radius=6),
     tooltip=['TYPEPIPE','Operator'],
     legend =False, # use black outline)
     categorical=True,)

ng_pipeline_map


# ## Natural Gas Market Hub Data

# In[9]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Natural_Gas_Market_Hubs.geojson"

ng_market_df = gpd.read_file(gisfilepath)

ng_market_df = ng_market_df.to_crs(epsg=3857)

colums = ng_market_df.columns
#uniqe = ng_market_df.TYPE.unique()
print(colums)


# ### Natural Gas Markets by Hub by Gas Corridor

# In[10]:


ng_market_map =ng_market_df.explore(
    column="Hub_name", # make choropleth based on "PORT_NAME" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap='Greens', # use "Set1" matplotlib colormap
     m=ng_pipeline_map,
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=15),
     tooltip=['Region','State','Hub_name','Operator','Maxthru','Avgdaily','Numcust','Platform'],
     legend =True, # use black outline)
     categorical=True,
    )


ng_market_map

