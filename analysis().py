import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import random as random
import matplotlib.pyplot as plt
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass as simulation
import DataAnalyzerClass as data
from statsmodels.nonparametric.smoothers_lowess import lowess

#-------------------
# Distance and plot
#-------------------

df = pd.read_csv('/Users/mccoybecker/equilibrated30by30.csv')
df = df.sort_values(by=['Temp'])
TempDensityList= []
for m in range(3):
    for (i,j,T) in df.loc[df['Labels'] == m][['x','y','Temp']].values:
        list = []
        for (k,l) in df.loc[df['Labels'] != m][['x','y']].values:
            list.append((np.sqrt((i-k)**2+(j-l)**2))/float(2))
        TempDensityList.append((T, min(list)))
TempDensityList.sort()

plt.scatter(*zip(*TempDensityList))
plt.title('Temperature versus distance from boundary')
plt.xlabel('Temperature')
plt.ylabel('Distance from Voronoi boundary')
plt.show()

#------------------------------------------------------------
# LOESS smoothing estimates and mean/STD minimum temperature
#------------------------------------------------------------

BootstrapParameter = input("Bootstrap number: ")
rootList = []
tempList = []

for i in df['Temp']:
    tempList.append(i)

for n in range(BootstrapParameter):
    SamplefromPoints = []
    
    for T in set(tempList):
        Points = [j[1] for j in TempDensityList if j[0] == T]
        SamplefromPoints.append((T, random.choice(Points)))
    
    SamplefromPoints = sorted(SamplefromPoints, key=lambda x: x[0])
    T,Points = zip(*SamplefromPoints)
    LOESSestimates = lowess(Points,T,return_sorted=True)
    temp,LOESS = zip(*LOESSestimates)
    spl = InterpolatedUnivariateSpline(temp, LOESS, k=4)
    plt.scatter(temp,LOESS)
    plt.plot(temp, spl(temp), 'g', lw=3, alpha=0.7)
    plt.title('LOESS smoothing with univariate spline fit k=4')
    plt.xlabel('Temperature')
    plt.ylabel('Distance from Voronoi boundary')
    plt.show()

print(str(np.mean(rootList)) + " +/- " + str(np.std(rootList)))






