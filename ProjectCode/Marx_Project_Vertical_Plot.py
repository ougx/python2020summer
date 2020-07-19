# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:32:35 2020

@author: smarx2
"""
##Veritcal Plot


import geopandas
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import numpy as np
from matplotlib.font_manager import FontProperties
ShapeData=geopandas.read_file("19_Roberts_AA_Planting.shp")
#ShapeData=geopandas.read_file("19_Saathoff_AA_Planting.shp")
Q1=ShapeData.Rt_Apd_Ct_.quantile(0.05)
Q3=ShapeData.Rt_Apd_Ct_.quantile(0.95)
IQR=Q3-Q1
ShapeData=ShapeData[~(ShapeData.Rt_Apd_Ct_>(Q3+1.5*IQR))]#Removes only upper outliers
#ShapeData=ShapeData[~((ShapeData.Rt_Apd_Ct_<(Q1-1.5*IQR))|(ShapeData.Rt_Apd_Ct_>(Q3+1.5*IQR)))]##Removes lower and upper outliers

######## Below lines didn't work
#ShapeData[np.abs(ShapeData.Rt_Apd_Ct_-ShapeData.Rt_Apd_Ct_.mean())<=(3*ShapeData.Rt_Apd_Ct_.std())]
#ShapeData[(np.abs(stats.zscore(ShapeData))<3).all(axis=1)]
#ShapeData[~((ShapeData-ShapeData.mean()).abs()>3*ShapeData.std())]
########

#print(ShapeData)
print(max(ShapeData['Rt_Apd_Ct_']))
ShapeData['RateError']=((ShapeData.Rt_Apd_Ct_ - ShapeData.Tgt_Rate_k)/ShapeData.Tgt_Rate_k)*100
avg_RateError=(ShapeData['RateError']).mean()
print("The avergae rate error is", avg_RateError,'%')
Max_Applied=max(ShapeData['Rt_Apd_Ct_'])
####Figure Plots
fig, ax= plt.subplots(1,4, figsize=(30,10))

cmap_1=plt.get_cmap('jet',10)

ShapeData.plot(ax=ax[0],column='Tgt_Rate_k', cmap=cmap_1, vmin=0, vmax=Max_Applied, markersize=2, legend=True, legend_kwds={'label':"Target Rate", 'orientation':"horizontal"});
ax[0].set_title('Target Rate', fontsize=30)
ax[0].set_xlabel('Longitude', fontsize=20)
ax[0].set_ylabel('Latitude', fontsize=20)
ax[0].tick_params(labelsize=10)
#ax[0,0].set_xticklabels(ShapeData['geometry'], rotation=45, fontsize=25)


cmap_2=plt.get_cmap('jet',10)
ShapeData.plot(column='Rt_Apd_Ct_', ax=ax[1],cmap=cmap_2, vmin=0, vmax=Max_Applied, markersize=2, legend=True, legend_kwds={'label':"Applied Rate", 'orientation':"horizontal"});#for some reason fontsize won't work as in this example: https://dmnfarrell.github.io/plotting/categorical-geopandas-maps
ax[1].set_title('Applied Rate', fontsize=30)
ax[1].set_xlabel('Longitude', fontsize=20)
ax[1].set_ylabel('Latitude', fontsize=20)
cmap3=mpl.colors.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple'])
ShapeData.plot(column='Speed_mph_', ax=ax[2], cmap=cmap3, markersize=2, legend=True, legend_kwds={'label':"Speed (mph)", 'orientation':"horizontal"});
ax[2].set_title('Application Speed', fontsize=30)
ax[2].set_xlabel('Longitude', fontsize=20)
ax[2].set_ylabel('Latitude', fontsize=20)
cmap_4=plt.get_cmap('jet',10)#where number after 'jet' is the number of values to be in the legend
ShapeData.plot(ax=ax[3], column='RateError', cmap=cmap_4, vmin=-10, vmax=10, markersize=2, legend=True, legend_kwds={'label':"Rate Percent Error", 'orientation':"horizontal"});#Vmin and Vmax set bounds for legend values.  
ax[3].set_title('Rate Percent Error', fontsize=30)
ax[3].set_xlabel('Longitude', fontsize=20)
ax[3].set_ylabel('Latitude', fontsize=20)