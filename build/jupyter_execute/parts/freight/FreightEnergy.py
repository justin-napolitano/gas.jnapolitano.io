#!/usr/bin/env python
# coding: utf-8

# # United States Rail Freight Energy Usage

# ## Code Section
# 
# In order to create rigorous tools that will influence business decisions it is important to me to remain completely transparent.  Every graph, table, and test will be easy to replicate by running the code included with this document.  

# ### Import Statements
# 
# First import the libraries that will be used in this project.  
# 

# In[1]:


import nasdaqdatalink as link
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ### ReturnData Class
# 
# The ReturnData Class initializes an object that contains all of the information necesary to produce graphs and analyze data 

# In[2]:


class ReturnData():
    def __init__(self,dataframe,unit,ticker,title,xlabel):
        self.dataframe = dataframe
        self.unit = unit
        self.ticker = ticker
        self.title = title
        self.xlabel = xlabel


# ### read_key Function
# 
# The read_key function imports an api key from file to enable this project to interact with the Nasdaq Data Link.
# 

# In[3]:


def read_key():
    try:
        link.read_key(".key")
        return True
    except:
        return False


# ### get_data Function
# 
# The get_data function calls the Nasdaq Data Link to request a data set dictionary according to a specified ticker(ie a data set title).
# 

# In[4]:


def get_data(ticker):
    data = link.get(ticker)
    return data


# ### Test Function
# 
# The test function simply tests whether the api is functioning.  It returns a sample set of data for confirmation.
# 

# In[5]:


def test():
    api_link = read_key()
    if api_link:
        datalink = "EIA/AEO_2016_REF2016_EFI_NA_TRN_RAIL_NA_NA_NA_TONMLPTHBTU_A"
        data = get_data(datalink)
        print(data)


# In[6]:


test()


# ### plot_df Function
# 
# plot_df will plot a datframe object.  A ReturnObject as defined by the ReturnData class contains all necessary information to plot a graph.
# 

# In[7]:


def plot_df(ReturnObject):

    plt.style.use('ggplot')
    index = ReturnObject.dataframe.index
    qx = ReturnObject.dataframe.plot(use_index=True, y = 'Value',kind='line', title =ReturnObject.title,figsize=(15,10),legend=True, fontsize=12)
    qx.set_xlabel(ReturnObject.xlabel,fontsize=12)
    qx.set_ylabel(ReturnObject.unit,fontsize=12)
    plt.show()
    return True


# ### GetData Function
# 
# The GetData function is an improved version of the previous get_data function.  It will request information by ticker.  Then, create a pandas dataframe to facillitate data manipulation and analysis. Finally it creates a ReturnObject by calling the ReturndData class.  ReturnObject is returned to the calling pipeline function to be manipulated and plotted.
# 

# In[8]:


def GetData(ticker,unit,title,xlabel):
    data = get_data(ticker)
    data = pd.DataFrame(data)
    ReturnObject = ReturnData(data,unit,ticker,title,xlabel)
    #data.rename({'Value': unit}, axis=1, inplace=True)
    #print('******Fuel Efficiency********')
    #print(FuelEfficiencyObject.dataframe)
    #print(FuelEfficiencyObject.unit)
    #print(FuelEfficiencyObject.ticker)
    #print(data)
    #print(data.columns)
    return ReturnObject


# ### GetCarbonDioxideData Function
# 
# GetCarbonDioxide data is an obsolete function that needs to be uodated to the new logic presented below.  In its current state it requires ticker, unit, title, ..etc to be defined within this function.  A better implementation is to do this step within the pipeline function.
# 

# In[9]:


def GetCarbonDioxideData():
        ticker = "EIA/AEO_2016_REF2016_EMI_CO2_TRN_RLF_NA_NA_NA_MILLMETNCO2_A"
        unit = "MMmt CO2"
        title = "Department of Energy Freight Rail Carbon Production Projections" 
        xlabel = "Date"
        data = get_data(ticker)
        data = pd.DataFrame(data)
        ReturnObject = ReturnData(data,unit,ticker,title,xlabel)
        
        #data.rename({'Value': unit}, axis=1, inplace=True)
        #print('******Fuel Carbon Dioxide Production********')
        #print(ReturnObject.dataframe)
        #print(ReturnObject.unit)
        #print(ReturnObject.ticker)
        #print(data)
        #print(data.columns)
        return ReturnObject


# ### CarbonPipeline Function
# 
# the CarbonPipeline Function creates the Carbon Dioxide usage reports by calling the GetCarbonDioxideData function and the plot_df utility function. 

# In[10]:


def CarbonPipeline():
    CarbonObject = GetCarbonDioxideData()
    plotted = plot_df(CarbonObject)
    
#CarbonPipeline()


# ### CPPCarbonPipeline Function
# 
# CPPCarbonPipeline is written with an improved logic to the CarbonPipeline function.  Attributes are set at the highest level instead of nesting the initialization within a secondary function.

# In[11]:


def CPPCarbonPipeline():
    ticker = "EIA/AEO_2016_CPPREPBASIC_EMI_CO2_TRN_RLF_NA_NA_NA_MILLMETNCO2_A"
    unit = "MMmt CO2"
    title = "CPP Carbon Dioxide Projections" 
    xlabel = "Year"
    CPPCarbonObject = GetData(ticker,unit,title,xlabel)
    plotted = plot_df(CPPCarbonObject)


# ### GetFuelEfficiency Function
# GetFuelEfficiencyData is an obsolete function that needs to be uodated to the new logic presented below. In its current state it requires ticker, unit, title, ..etc to be defined within this function. A better implementation is to do this step within the pipeline function.

# In[12]:


def GetFuelEfficiencyData():
    ticker = "EIA/AEO_2016_REF2016_EFI_NA_TRN_RAIL_NA_NA_NA_TONMLPTHBTU_A"
    unit = "ton miles/thousand"
    title = "Freight Fuel Efficiency" 
    xlabel = "Date"
    data = get_data(ticker)
    data = pd.DataFrame(data)
    ReturnObject = ReturnData(data,unit,ticker,title,xlabel)

    #data.rename({'Value': unit}, axis=1, inplace=True)
    #print('******Fuel Efficiency********')
    #print(FuelEfficiencyObject.dataframe)
    #print(FuelEfficiencyObject.unit)
    #print(FuelEfficiencyObject.ticker)
    #print(data)
    #print(data.columns)
    return ReturnObject


# ### EfficiencyPipeline Function
# 
# the Efficiency Function creates the Carbon Dioxide usage reports by calling the GetCarbonDioxideData function and the plot_df utility function. 

# In[13]:


def EfficiencyPipeline():
    EfficiencyObject = GetFuelEfficiencyData()
    plotted = plot_df(EfficiencyObject)
    
#EfficiencyPipeline()


# ### LNGUsagePipeline Function
# 
# the LNGUsagePipeline  Function creates the LNG usage reports by calling the Get data function and the plot_df utility function. 

# In[14]:


def LngUsagePipeline():
    ticker = "EIA/AEO_2016_REF2016_CNSM_NA_TRN_FRAIL_LNG_NA_NA_TRLBTU_A"
    unit = "Trillions BTU"
    title = "LNG Usage and Projections" 
    xlabel = "Year"
    LNGObject = GetData(ticker,unit,title,xlabel)
    plotted = plot_df(LNGObject)
    


# ### FreightRailUsagePipeline Function
# 
# the LNGUsagePipeline  Function creates the LNG usage reports by calling the Get data function and the plot_df utility function. 

# In[15]:


def FreightRailUsagePipeline():
    ticker = "EIA/AEO_2016_REF2016_CNSM_NA_TRN_FRAIL_NA_NA_NA_TRLBTU_A"
    unit = "Trillions BTU"
    title = "Department of Energy Total Freight Energy Usage" 
    xlabel = "Year"
    LNGObject = GetData(ticker,unit,title,xlabel)
    plotted = plot_df(LNGObject)


# ### FreightEnergyNoCPPPipeline Function
# 
# The FreightEnergyNoCPPPipeline Function creates the Freight Energy; No CPP; usage reports by calling the Get data function and the plot_df utility function. 

# In[16]:


def FreightEnergyNoCPPPipeline():
    ticker = "EIA/AEO_2016_REF_NO_CPP_CNSM_NA_TRN_RLF_USE_NA_NA_QBTU_A"
    unit = "Quads"
    title = "Transportation ; Energy Use by Mode ; Rail, Freight, No CPP, AEO2016" 
    xlabel = "Year"
    LNGObject = GetData(ticker,unit,title,xlabel)
    plotted = plot_df(LNGObject)


# ### TonMilesPipeline Function
# 
# The TonMilesPipeline Function creates the Ton Miles usage reports by calling the Get data function and the plot_df utility function. 

# In[17]:


def TonMilesPipeline():
    ticker = "EIA/AEO_2016_REF2016_ECI_FTM_TRN_RAIL_NA_NA_NA_BLN_A"
    unit = "Billions"
    title = "Freight ; Railroads ; Ton Miles by Rail, Reference, AEO2016" 
    xlabel = "Year"
    LNGObject = GetData(ticker,unit,title,xlabel)
    plotted = plot_df(LNGObject)


# ## Data Plots
# 
# The functions below plot data by calling the appropriate pipeline.  
# 
# It easy to add new reports to the project because the programs are written modularly. 

# ```{eval-rst}
# 
# .. index::
#    single: Carbon Production Projections Plot
# 
# ```

# ### Carbon Production Plot

# In[18]:


CarbonPipeline()


# ```{eval-rst}
# 
# .. index::
#    single: Carbon Dioxide Projections Map
# 
# ```

# ### Carbon Dioxide Projections

# In[19]:


CPPCarbonPipeline()


# ```{eval-rst}
# 
# .. index::
#    single: Freight Fuel Efficiency Projections Plot
# 
# ```

# ### Freight Fuel Efficiency Projections

# In[20]:


EfficiencyPipeline()


# ```{eval-rst}
# 
# .. index::
#    single: LNG Usage and Projections Plot
# 
# ```

# ### LNG Usage and Projections

# In[21]:


LngUsagePipeline()


# ```{eval-rst}
# 
# .. index::
#    single: Rail Freight Total Energy Usage Plot
# 
# ```

# ### Rail Freight Total Energy Use

# In[22]:


FreightRailUsagePipeline()


# ```{eval-rst}
# 
# .. index::
#    single: Projected Freight Energy Usage, No CPP, Plot
# 
# ```

# ### Projected Energy Usage without Carbon Protection Policies

# In[23]:


FreightEnergyNoCPPPipeline()


# ```{eval-rst}
# 
# .. index::
#    single: Ton/Miles Projections Plot
# 
# ```

# ### Ton/Miles Projections

# In[24]:


TonMilesPipeline()


# In[ ]:




