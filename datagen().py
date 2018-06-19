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

#-------------------------------------
# Setup the simulation and run updates
#-------------------------------------

N = input("What is the size of lattice?: ")
TSteps = input("How many temperature steps?: ")
SampleSize = input("How many samples?: ")
mySimulation = simulation.Simulation(N,1,1.9,2.6,TSteps)

for i in range(0):
    mySimulation.update()
    print("Update("+str(i)+")")

for i in range(SampleSize):
    for j in range(1):
        mySimulation.update()
    mySimulation.sample()
    print("Sample("+str(i)+")")

dataAnalyzer = data.DataAnalyzer(mySimulation.dataMatrix,mySimulation.EnergyList,mySimulation.MagnetizationList,2,2,3)
dataAnalyzer.scalerfit()
X1,X2 = zip(*dataAnalyzer.PCA.fit_transform(dataAnalyzer.scaler.transform(dataAnalyzer.dataMatrix)))

#X1TSNE,X2TSNE = zip(*dataAnalyzer.TSNE.fit_transform(dataAnalyzer.scaler.transform(dataAnalyzer.dataMatrix)))

#---------------
#KMeans and plot
#---------------

colmap={1:'r', 2:'g', 3:'b'}
df=pd.DataFrame({'x': X1, 'y': X2})
kmeans=KMeans(n_clusters=3)
kmeans.fit(df)
labels=kmeans.predict(df)
transformed=kmeans.transform(df)
df=df.assign(Labels=labels)
df=df.assign(Energy =dataAnalyzer.EnergyList)
df=df.assign(Magnetization=dataAnalyzer.MagnetizationList)
df=df.assign(Temp = mySimulation.TemperatureList)
path = '/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/'
df.to_csv(path + 'ising ' + str(N) + '_' + str(TSteps) + '_' + str(SampleSize) + '_' + '.csv')






