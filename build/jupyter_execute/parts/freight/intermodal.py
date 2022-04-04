#!/usr/bin/env python
# coding: utf-8

# # Intermodal Freight Analysis

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx


# ## Air to Truck Facilities Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_Air-to-Truck.geojson"

air_to_truck_df = gpd.read_file(gisfilepath)

air_to_truck_df


# ```{eval-rst}
# 
# .. index::
#    single: Air to Truck Facility Map
# 
# ```
# 
# ### Air to Truck Facility Map

# In[3]:


air_to_truck_df.explore()


# ## Intermodal Freight Marine Role On/Role Off Data

# In[4]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_Marine_Roll-on_Roll-off.geojson"

roll_on_off_df = gpd.read_file(gisfilepath)

roll_on_off_df


# ```{eval-rst}
# 
# .. index::
#    single: Marine Roll On/ Roll Off Map
# 
# ```
# 
# ### Marine Roll on/Role Off Map

# In[5]:


roll_on_off_df.explore()


# ## Intermodal Rail Freight Stations Data
# 
# ### Data Source 
# 
# https://geo.dot.gov/server/rest/services/NTAD/Intermodal_Freight_Facilities_RailTOFCCOFC/MapServer/0
# 
# 
# ### Data Values
# 
# Every facility is assumed to be served by both rail and truck, and those facilities which support port operations, the name of the port is also identified

# In[6]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_RailTOFCCOFC.geojson"

rail_to_all_df = gpd.read_file(gisfilepath)

rail_to_all_df


# ```{eval-rst}
# 
# .. index::
#    single: Rail Freight Stations Map
# 
# ```
# 
# ### Rail Freight Stations Map

# In[7]:


rail_to_all_df.explore()


# ## Conclusions 
# 
# Concentrate industrial activity in Texas because if its massive rail and shipping infrastructure or along a major water way. 
# 
# ### Regulatory Considerations
# 
# Rust Belt States and Northern states along the Mississippi with access to rail and internal shipping routes may face greater regulatory pressures than states such as Texas or Tennessee.  An investigation into this must be completed.
