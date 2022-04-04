#!/usr/bin/env python
# coding: utf-8

# # US Shipping Routes and Ports Analysis
# 
# 
# This is a precursor project to one that will create a graph of rail, shipping, trucking, and air freight transport networks for analysis.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx


# ## Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Navigable_Waterway_Lines.geojson"

waterway_df = gpd.read_file(gisfilepath)



waterway_df.head()


# ### Checking Cooridindate System.  
# 
# The coordinate system must be in the epsg 3857 format to overlay.

# In[3]:


waterway_df.crs


# #### Converting to EPSG 3857 System

# In[4]:


df_wm = waterway_df.to_crs(epsg=3857)


# In[5]:


ax = df_wm.plot(figsize=(20, 20), alpha=0.5, edgecolor='k')
cx.add_basemap(ax, zoom=4)


# ### Impressions
# 
# The Gulf Waters are interestengly concentrated and dependent on non US Ports.  For instance the Gulf-Carribean Access Point concentrates near the Yucatan penninsula.  There is also a major concentration near the islands of cuba and hispanola. This surpise me I would have considered Puerto Rico to be a more important shipping route.

# ## US Ports Data Set

# In[6]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Ports.geojson"

ports_df = gpd.read_file(gisfilepath)

ports_df


# In[7]:


ports_df.columns


# ### Impressions
# There are 24,1117 ports recorded in this dataset.  There are also 43 fields of data.  Columns of interests are Highway_No and Railway_No.  I would like to investigate this further.

# #### Converting to EPSG 3857 System

# In[8]:


ports_df_wm = ports_df.to_crs(epsg=3857)


# In[9]:


ax = ports_df_wm.plot(figsize=(20, 20), alpha=0.5, edgecolor='k')
cx.add_basemap(ax, zoom=4)


# ```{eval-rst}
# 
# .. index::
#    single: US Ports Map Interactive
# 
# ```
# ### US Ports Map

# In[10]:


ports_df_wm.explore()


# ### Results
# 
# It is interesting to see all of the ports in the UNited States, but I notice that the majority are small ports registered by organizations to move goods to market.  For the purpose of this analysis there is too much noise to yield information.

# ## Major US Ports Data Set

# In[11]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Major_Ports.geojson"

major_ports_df = gpd.read_file(gisfilepath)

major_ports_df


# In[12]:


major_ports_df.columns


# ### Impressions
# 
# This data is far more managable.  It also contains data relating to freight volumes.

# In[13]:


major_ports_df_wm = major_ports_df.to_crs(epsg=3857)


# ```{eval-rst}
# 
# .. index::
#    single: Major US Ports Map Interactive
# ```
# 
# ### Major Us Ports Map

# In[14]:


major_ports_df.explore()

