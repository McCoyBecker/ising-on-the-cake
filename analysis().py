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

#-----------------
# Distance and plot
#-----------------

df = pd.read_csv('/Users/mccoybecker/equilibrated40by40.csv')
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

#-------------------------
# LOESS smoothing estimates
#-------------------------

BootstrapParameter = 1000
rootList = []
for n in range(100):
    SamplefromPoints = []
    for T in set(mySimulation.TemperatureList):
        Points = [j[1] for j in TempDensityList if j[0] == T]
        Points = [random.choice(Points) for j in range(BootstrapParameter)]
        SamplefromPoints.append((T, np.mean(Points)))

    SamplefromPoints = sorted(SamplefromPoints, key=lambda x: x[0])
    T,Points = zip(*SamplefromPoints)
    LOESSestimates = lowess(Points,T,return_sorted=True)
    #rootList.append(sorted(LOESSestimates,key=lambda x: x[1])[0][1])

plt.scatter(*zip(*LOESSestimates))
plt.title('LOESS smoothing')
plt.xlabel('Temperature')
plt.ylabel('Distance from Voronoi boundary')
plt.show()

temp,LOESS = zip(*LOESSestimates)
spl = InterpolatedUnivariateSpline(temp, LOESS,k=4)
print(spl.derivative().roots())

#print(str(np.mean(rootList)) + " +/- " + str(np.std(rootList)))






