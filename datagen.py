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

#-------------------------------------
# Setup the simulation and run updates
#-------------------------------------

N = int(input("What is the size of lattice?: "))
TSteps = int(input("How many temperature steps?: "))
SampleSize = int(input("How many samples?: "))
mySimulation = simulation.Simulation(N,1,1.9,2.6,TSteps)

for i in range(SampleSize):
    mySimulation.update()
    mySimulation.sample()
    print("Sample("+str(i)+")")

dataAnalyzer = data.DataAnalyzer(mySimulation.dataMatrix,mySimulation.EnergyList,mySimulation.MagnetizationList,2,2,3)
dataAnalyzer.scalerfit()
X1,X2 = zip(*dataAnalyzer.PCA.fit_transform(dataAnalyzer.scaler.transform(dataAnalyzer.dataMatrix)))
df=pd.DataFrame({'x': X1, 'y': X2})
df=df.assign(Energy = dataAnalyzer.EnergyList)
df=df.assign(Magnetization = dataAnalyzer.MagnetizationList)
df=df.assign(Temp = mySimulation.TemperatureList)
path = '/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/Original_data/'
df.to_csv(path + 'ising ' + str(N) + '_' + str(TSteps) + '_' + str(SampleSize) + '_' + '.csv')