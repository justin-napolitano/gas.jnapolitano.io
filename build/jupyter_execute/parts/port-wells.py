#!/usr/bin/env python
# coding: utf-8

# # Potential Carbon Storage Facilities Near Import/Export Ports

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


# ## Restrictions
# 
# * Must be near a pipeline terminal
# * Must be Near a petrolium Port 

# ### Query Plan
# 
# Imports
# * Import LNG terminal Dataa
# * Import well data
# 
# Filtering
# * for each well calculate nearest terminal
# * for each well calculate distance from nearest terminal
# * eliminate wells further than 15 miles from a terminal
# 
# 

# ## Data Frame Import

# ### Wells DataFrame

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/non-active-wells.geojson"


wells_df = gpd.read_file(gisfilepath)

wells_df = wells_df.to_crs(epsg=3857)


# ### Terminal DataFrame

# In[3]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/data/energy/Liquified_Natural_Gas_Import_Exports_and_Terminals.geojson"


terminal_df = gpd.read_file(gisfilepath)

terminal_df = terminal_df.to_crs(epsg=3857)


# ### Eliminating SUSPENDED Terminal from the DataFrame

# In[4]:


terminal_df.drop(terminal_df[terminal_df['STATUS'] == 'SUSPENDED'].index, inplace = True)
terminal_df.rename(columns={"NAME": "TERMINAL_NAME"})
terminal_df['TERMINAL_GEO'] = terminal_df['geometry'].copy()
terminal_df.columns


# ### Plotting Terminal by TYPE

# In[5]:


terminal_map =terminal_df.explore(
    column="TYPE", # make choropleth based on "PORT_NAME" column
     popup=True, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Set1', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     #tooltip=['NAICS_DESC','REGION', 'COMMODITY' ],
     legend =True, # use black outline)
     categorical=True,
    )


terminal_map


# ### Terminal Impressions
# 
# According to the data there is not an export nor import location on The Western Side of the United States.
# 
# East Asian import or carbon capture export demands could justfity port development.  Another study must be conducted.

# ## Filtering Wells by Terminal Distance in Scipy
# 
# ### Edit
# 
# This method does not accuraletly calculate distance.  The algorith used below calculates distance on a euclidan plane.  In order to calculate a correct answer we must account for sphericity.
# 
# I include the code below as reference and a learning opportunity

# In[6]:


def ckdnearest(gdA, gdB):

    nA = np.array(list(gdA.geometry.apply(lambda x: (x.x, x.y))))
    nB = np.array(list(gdB.geometry.apply(lambda x: (x.x, x.y))))
    btree = cKDTree(nB)
    dist, idx = btree.query(nA, k=1)
    gdB_nearest = gdB.iloc[idx].drop(columns="geometry").reset_index(drop=True)
    gdf = pd.concat(
        [
            gdA.reset_index(drop=True),
            gdB_nearest,
            pd.Series(dist, name='dist')
        ], 
        axis=1)

    return gdf

c = ckdnearest(wells_df, terminal_df)


# In[7]:


c.describe()


# In[8]:


nearest_wells_df= wells_df.sjoin_nearest(terminal_df, distance_col="distance_euclidian")


# In[9]:


nearest_wells_df.describe()


# ### Calculating Distance in Kilometers from Import/Export Terminal

# In[10]:


#df.geopy.distance.distance(coords_1, coords_2).km
#df.apply(lambda row: distance(row['point'], row['point_next']).km if row['point_next'] is not None else float('nan'), axis=1)
# Thanks to https://stackoverflow.com/questions/55909305/using-geopy-in-a-dataframe-to-get-distances

nearest_wells_df['true_distance_km'] = nearest_wells_df.apply(lambda row: distance((row['LATITUDE_left'], row['LONGITUDE_left']), (row['LATITUDE_right'], row['LONGITUDE_right'])).km if row['geometry'] is not None else float('nan'), axis=1)


# In[11]:


nearest_wells_df.describe()


# ### Filtering Wells within 50 KM of a Terminal

# In[12]:


filtered_wells = nearest_wells_df.loc[nearest_wells_df['true_distance_km'] < 50].copy()


# In[13]:


filtered_wells.describe()


# ### Map of Wells within 50 km of an Import/Export Terminal by Type

# In[14]:


filtered_wells.explore(
    column="STATUS_left", # make choropleth based on "PORT_NAME" column
     popup=True, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap='Set1', # use "Set1" matplotlib colormap
     #style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),
     #tooltip=['NAICS_DESC','REGION', 'COMMODITY' ],
     legend =True, # use black outline)
     categorical=True,)


# In[ ]:




