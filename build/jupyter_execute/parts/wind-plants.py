#!/usr/bin/env python
# coding: utf-8

# # Wind Plants

# # Data Import

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from folium import plugins
import folium


pd.set_option('display.float_format', lambda x: '%0.4f' % x)


# ## US Power Plants Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/gas.jnapolitano.io/source/data/Power_Plants.geojson"

powerplants_df = gpd.read_file(gisfilepath)
#Selecting only Operational Plants
powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()
na = powerplants_df.COAL_USED.min()
powerplants_df.replace(na, 0 , inplace=True)

#powerplants_df = powerplants_df.to_crs(epsg=3857)

powerplants_df.describe()


# ## Identifying the Wind Plants in the Data Set

# In[3]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
wind_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'WND'].copy()

#concatenating coal type dfs into one
wind_plants.describe()



# ## Wind Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Wind Plants Interactive Map
# 
# ```

# In[4]:


wind_map = wind_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
wind_map


# ## Wind Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Wind Plant Density Interactive Map
# 
# ```

# In[5]:


wind_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in wind_plants.geometry ]
#

wind_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

wind_heat_layer = plugins.HeatMap(data = wind_heat_data)
wind_heat_layer.add_to(wind_density_map)

wind_density_map

