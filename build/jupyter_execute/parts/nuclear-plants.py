#!/usr/bin/env python
# coding: utf-8

# # Nuclear Plants

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


# ## Identifying the Nuclear Plants in the Data Set

# In[3]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
nuclear_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'NUC'].copy()

#concatenating coal type dfs into one
nuclear_plants.describe()



# ## Nuclear Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Nuclear Plants Interactive Map
# 
# ```

# In[4]:


nuclear_map = nuclear_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="Stamen Terrain", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
nuclear_map


# ## Nuclear Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Nuclear Plant Density Interactive Map
# 
# ```

# In[5]:


nuclear_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in nuclear_plants.geometry ]
#

nuclear_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

nuclear_heat_layer = plugins.HeatMap(data = nuclear_heat_data, show=True)
nuclear_heat_layer.add_to(nuclear_density_map)

nuclear_density_map

