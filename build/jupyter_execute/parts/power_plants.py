#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from folium import plugins
import folium


pd.set_option('display.float_format', lambda x: '%0.4f' % x)


# # US Power Plants Meta Analysis

# ## US Power Plants Data

# In[2]:


gisfilepath = "/Users/jnapolitano/Projects/gas.jnapolitano.io/source/data/Power_Plants.geojson"

powerplants_df = gpd.read_file(gisfilepath)
#Selecting only Operational Plants
powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#powerplants_df = powerplants_df.to_crs(epsg=3857)

powerplants_df


# ```{eval-rst}
# 
# .. index::
#    single: US Power Plants Interactive Map
# 
# ```

# ### US Power Plants Interactive Map

# In[3]:


operational_powerplants_map = powerplants_df.explore(column="PRIM_FUEL", # make choropleth based on "BoroName" column
     popup=False, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5
)
#ng_map
operational_powerplants_map


# ## Natural Gas Plants

# ### Identifying the Natural Gas Plants in the Dataset

# In[4]:


ng_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'NG'].copy()
ng_plants


# ### Modifying Unit Scale for Map Legend
# 

# In[5]:


ng_plants['NGAS_USED']=ng_plants['NGAS_USED'].apply(lambda x: x/1)
ng_plants.rename(columns = {'NGAS_USED':'NGAS_BTUs'}, inplace = True)
ng_plants


# ### Natural Gas Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: US Natural Gas Plants Interactive Map
# 
# ```

# In[6]:


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


# ### Natural Gas Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: US Natural Gas Plant Density Interactive Map
# 
# ```

# In[7]:


heat_data = [[point.xy[1][0], point.xy[0][0]] for point in ng_plants.geometry ]

mapTest = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

test = plugins.HeatMap(data = heat_data, show=True)
test.add_to(mapTest)

mapTest


# ## Coal Plants

# ### Identifying the Coal Plants in the Dataset

# In[8]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
wc_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'WC'].copy()
rc_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'RC'].copy()

#concatenating coal type dfs into one
coal_df = pd.concat([wc_plants,rc_plants])
coal_df.columns



# ### Coal Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Coal Plants Interactive Map
# 
# ```

# In[9]:


coal_map = coal_df.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
coal_map


# ### Coal Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Coal Plant Density Interactive Map
# 
# ```

# In[10]:


coal_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in coal_df.geometry ]
#

coal_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

coal_heat_layer = plugins.HeatMap(data = coal_heat_data, show=True)
coal_heat_layer.add_to(coal_density_map)

coal_density_map


# ## Solar Plants

# ### Identifying the Solar Plants in the Dataset

# In[11]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
solar_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'SUN'].copy()

#concatenating coal type dfs into one
solar_plants.columns



# ### Solar Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Solar Plants Interactive Map
# 
# ```

# In[12]:


solar_map = solar_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
solar_map


# ### Solar Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Solar Plant Density Interactive Map
# 
# ```

# In[13]:


solar_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in solar_plants.geometry ]
#

solar_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

solar_heat_layer = plugins.HeatMap(data = solar_heat_data, show=True)
solar_heat_layer.add_to(solar_density_map)

solar_density_map


# ## Wind Plants

# ### Identifying the Wind Plants in the Dataset

# In[14]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
wind_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'WND'].copy()

#concatenating coal type dfs into one
wind_plants.columns



# ### Wind Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Wind Plants Interactive Map
# 
# ```

# In[15]:


wind_map = wind_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
wind_map


# ### Wind Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Wind Plant Density Interactive Map
# 
# ```

# In[16]:


wind_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in wind_plants.geometry ]
#

wind_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

wind_heat_layer = plugins.HeatMap(data = wind_heat_data)
wind_heat_layer.add_to(wind_density_map)

wind_density_map


# In[ ]:





# In[ ]:





# ## Hydro Plants

# ### Identifying the Hydro Plants in the Dataset

# In[17]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
hydro_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'WAT'].copy()

#concatenating coal type dfs into one
hydro_plants.columns



# ### Hydro Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Hydro Plants Interactive Map
# 
# ```

# In[18]:


hydro_map = hydro_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'Percentiles',
     k = 5

)
hydro_map


# ### Hydro Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Solar Plant Density Interactive Map
# 
# ```

# In[19]:


hydro_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in hydro_plants.geometry ]
#

hydro_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

hydro_heat_layer = plugins.HeatMap(data = hydro_heat_data, show=True)
hydro_heat_layer.add_to(hydro_density_map)

hydro_density_map


# ## Nuclear Plants

# ### Identifying the Nuclear Plants in the Dataset

# In[20]:


#powerplants_df.PRIM_FUEL.unique()
#RC,WC,NUC
#Selecting only Operational Plants
#powerplants_df=powerplants_df.loc[powerplants_df['STATUS'] == 'OP'].copy()

#selecting coal plants
nuclear_plants = powerplants_df.loc[powerplants_df['PRIM_FUEL'] == 'NUC'].copy()

#concatenating coal type dfs into one
nuclear_plants.columns



# ### Nuclear Plants Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Nuclear Plants Interactive Map
# 
# ```

# In[21]:


nuclear_map = nuclear_plants.explore(column="NET_GEN", # make choropleth based on "BoroName" column
     popup=True, # show all values in popup (on click)
     tiles="CartoDB positron", # use "CartoDB positron" tiles
     cmap="Set1", # use "Set1" matplotlib colormap
     style_kwds=dict(color="black"),
     marker_kwds= dict(radius=6),# use black outline)
     scheme = 'EqualInterval',
     k = 5

)
nuclear_map


# ### Nuclear Plant Density Interactive Map

# ```{eval-rst}
# 
# .. index::
#    single: Nuclear Plant Density Interactive Map
# 
# ```

# In[22]:


nuclear_heat_data = [[point.xy[1][0], point.xy[0][0]] for point in solar_plants.geometry ]
#

nuclear_density_map = folium.Map(location = [30, -90], tiles='Cartodb dark_matter', zoom_start = 4)

nuclear_heat_layer = plugins.HeatMap(data = nuclear_heat_data, show=True)
nuclear_heat_layer.add_to(nuclear_density_map)

nuclear_density_map

