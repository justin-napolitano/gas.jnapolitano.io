#!/usr/bin/env python
# coding: utf-8

# # US Logistics Network Analysis

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
import rtree


# ## Rail Facilities by Nearest Ports

# ### Intermodal Rail Data

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_RailTOFCCOFC.geojson"

rail_to_all_df = gpd.read_file(gisfilepath)

rail_to_all_df = rail_to_all_df.to_crs(epsg=3857)

rail_to_all_df


# ### Major Ports Data

# In[3]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Major_Ports.geojson"
major_ports_df = gpd.read_file(gisfilepath)
major_ports_df = major_ports_df.to_crs(epsg=3857)

major_ports_df


# ### Intermodal Rail Stations Joined by Nearest Major Port

# In[4]:


major_transit_nodes = rail_to_all_df.sjoin_nearest(major_ports_df)
major_transit_nodes.drop(columns=['OBJECTID_right', 'index_right','OBJECTID_1','OBJECTID_left','PORT_left'], inplace=True)
print(major_transit_nodes.columns)
major_transit_nodes


# ```{eval-rst}
# 
# .. index::
#    single: Rail Facilities by Port Interactive Map
# 
# ```

# ### Rail Facilities by Port Interactive Map
# 

# In[5]:


major_transit_nodes.explore()


# ## Air Freight to Truck Facilites by Major Port

# In[6]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_Air-to-Truck.geojson"
air_freight_to_truck_df = gpd.read_file(gisfilepath)
air_freight_to_truck_df = air_freight_to_truck_df.to_crs(epsg=3857)

air_freight_to_truck_df


# ### Air Freight Hubs joined by Major Ports

# In[7]:


major_air_freight = air_freight_to_truck_df.sjoin_nearest(major_ports_df)

major_air_freight.drop(columns=['OBJECTID_right', 'index_right','OBJECTID_1','OBJECTID_left'], inplace=True)
print(major_air_freight.columns)

major_air_freight


# ```{eval-rst}
# 
# .. index::
#    single: Air Fright Hubs by Nearest Ports Interactive Map
# 
# ```

# ### Air Freight Hubs by Nearest Major Port Port Map

# In[8]:


major_air_freight.explore()


# ## Shipping Networks

# ### Shipping Data

# In[9]:


gisfilepath = "//Users/jnapolitano/Projects/rail-mapping/shipping/Navigable_Waterway_Lines.geojson"
shipping_network = gpd.read_file(gisfilepath)
shipping_network = shipping_network.to_crs(epsg=3857)

shipping_network


# ### Shipping Networks by Major Ports

# In[10]:


port_shipping = shipping_network.sjoin_nearest(major_ports_df)
port_shipping.drop(columns = ['OBJECTID_left','DIR', 'ANODE', 'BNODE', 'ID_left', 'AMILE', 'BMILE', 'LENGTH1', 'LENGTH_SRC', 'SHAPE_SRC', 'GEO_CLASS', 'FUNC_CLASS','OBJECTID_1','CHART_ID', 'index_right', 'NUM_PAIRS', 'CHART_ID', 'DATE_MOD', 'WHO_MOD', 'OBJECTID_right','ID_right'],inplace=True)
print(port_shipping.columns)
port_shipping


# ```{eval-rst}
# 
# .. index::
#    single: Shipping Routes by Major Port Interactive Map
# 
# ```

# ### Shipping Routes by Major Port Interactive Map

# In[11]:


port_shipping.explore()


# In[ ]:




