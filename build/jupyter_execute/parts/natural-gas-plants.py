#!/usr/bin/env python
# coding: utf-8

# # Natural Gas Plants

# ## Data Imports

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from folium import plugins
import folium


pd.set_option('display.float_format', lambda x: '%0.4f' % x)


# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/gas.jnapolitano.io/source/data/Power_Plants.geojson"

powerplants_df = gpd.read_file(gisfilepath)
#Selecting only Operational Plants
powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()
na = powerplants_df.COAL_USED.min()
powerplants_df.replace(na, 0 , inplace=True)

#powerplants_df = powerplants_df.to_crs(epsg=3857)

powerplants_df.describe()


# ## Identifying the Natural Gas Plants in the Data Set

# In[3]:


ng_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'NG'].copy()
ng_plants.describe()


# ## Modifying Unit Scale for Map Legend
# 

# In[4]:


ng_plants['NGAS_USED']=ng_plants['NGAS_USED'].apply(lambda x: x/1)
ng_plants.rename(columns = {'NGAS_USED':'NGAS_BTUs'}, inplace = True)
ng_plants.describe()


# ## Natural Gas Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: US Natural Gas Plants Interactive Map
# 
# ```

# In[5]:


ng_map = ng_plants.explore(column="NGAS_BTUs", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
ng_map


# ## Natural Gas Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: US Natural Gas Plant Density Interactive Map
# 
# ```

# In[6]:


heat_data = [[point.xy[1][0], point.xy[0][0]] for point in ng_plants.geometry ]

mapTest = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

test = plugins.HeatMap(data = heat_data, show=True)
test.add_to(mapTest)

mapTest

