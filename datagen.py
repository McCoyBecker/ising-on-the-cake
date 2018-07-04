import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import random as random
import matplotlib.pyplot as plt
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass

#-------------------------------------
# Setup the simulation and run updates
#-------------------------------------

N = int(input("What is the size of lattice?: "))
TSteps = int(input("How many temperature steps?: "))
SampleSize = int(input("How many samples?: "))
UpdateSteps = int(input("How many update non-sample steps?: "))

#-------------------------------------
# Update and sample steps
#-------------------------------------

mySimulation = Simulation(N,1,1.9,2.6,TSteps)

for j in range(UpdateSteps):
    mySimulation.update()
    print("Update("+str(j)+")")

for i in range(SampleSize):
    mySimulation.update()
    mySimulation.sample()
    print("Sample("+str(i)+")")

#-------------------------------------
# Preprocessing and PCA
#-------------------------------------

scaled_data = scaler.fit(mySimulation.dataMatrix)
X1,X2 = zip(*PCA.fit_transform(scaler.transform(scaled_data)))

df=pd.DataFrame({'x': X1, 'y': X2})
df=df.assign(Energy = mySimulation.Energylist)
df=df.assign(Magnetization = mySimulation.MagnetizationList)
df=df.assign(Temp = mySimulation.TemperatureList)

#-------------------------------------
# Write to .csv file
#-------------------------------------

path = '/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/Original_data/'
df.to_csv(path + 'ising ' + str(N) + '_' + str(TSteps) + '_' + str(SampleSize) + '_' + '.csv')