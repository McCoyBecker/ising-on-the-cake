import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import random as random
import matplotlib.pyplot as plt
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass as simulation
import DataAnalyzerClass as data
from statsmodels.nonparametric.smoothers_lowess import lowess

#------------------
# Distance and plot
#------------------

LatticeSize = input("What is lattice size of data?: ")
df = pd.read_csv('/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/Cut_data/5000_' + LatticeSize +'_60_cut.csv')
df = df.sort_values(by=['Temp'])
IndexList = []
TempDensityList= []

for m in range(3):
    for (X,i,j,T) in df.loc[df['Labels'] == m][['X','x','y','Temp']].values:
        list = []
        for (k,l) in df.loc[df['Labels'] != m][['x','y']].values:
            list.append((np.sqrt((i-k)**2+(j-l)**2))/float(2))
        
        IndexList.append((X,min(list)))
        TempDensityList.append((T, min(list)))

IndexList.sort()
df = df.sort_values(by=['X'])
DistanceList = [IndexList[i][1] for i in range(len(IndexList))]
df['Min_distance'] = DistanceList
path = '/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/Cut_updated_data/'
df.to_csv(path + '5000_'+ LatticeSize +'_60_cut_updated.csv')

TempDensityList.sort()

#-----------------------------------------------------------
# LOESS smoothing estimates and mean/STD minimum temperature
#-----------------------------------------------------------

BootstrapParameter = int(input("Bootstrap number: "))
PlotButton = input("Plots on?: ")
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

    T = [SamplefromPoints[j][0] for j in range(len(SamplefromPoints))]
    Points = [SamplefromPoints[j][1] for j in range(len(SamplefromPoints))]

    LOESSestimates = lowess(Points,T,return_sorted=True)

    #Fit degree = 4 spline to LOESS output
    spl = InterpolatedUnivariateSpline(temp, LOESS, k=4)

    temp = [LOESSestimates[j][0] for j in range(len(LOESSestimates))]
    LOESS = [LOESSestimates[j][1] for j in range(len(LOESSestimates))]
    if PlotButton not in ["No", "0"]:
        plt.scatter(temp,LOESS)
        plt.plot(temp, spl(temp), 'g', lw=3, alpha=0.7)
        plt.title('LOESS smoothing with univariate spline fit k=4')
        plt.xlabel('Temperature')
        plt.ylabel('Distance from Voronoi boundary')
        plt.show()

    #Generate list of roots using spline methods
    if spl.derivative().roots() != []:
        rootList.append(spl.derivative().roots()[0])
        print(spl.derivative().roots()[0])

print(str(np.mean(rootList)) + " +/- " + str(np.std(rootList)))






