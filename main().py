import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import random as random
import matplotlib.pyplot as plt
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass as simulation
import DataAnalyzerClass as data


mySimulation = simulation.Simulation(20,1,1.6,2.9,20)

for i in range(50):
    mySimulation.update()
    print("Update("+str(i)+")")

for i in range(100):
    for j in range(1):
        mySimulation.update()
    mySimulation.sample()
    print("Sample("+str(i)+")")

print(len(mySimulation.dataMatrix))
dataAnalyzer = data.DataAnalyzer(mySimulation.dataMatrix,2,3)
dataAnalyzer.scalerfit()
X1,X2 = zip(*dataAnalyzer.PCA.fit_transform(dataAnalyzer.scaler.transform(dataAnalyzer.dataMatrix)))


colmap={1:'r', 2:'g', 3:'b'}
df=pd.DataFrame({'x': X1, 'y': X2})
kmeans=KMeans(n_clusters=3)
kmeans.fit(df)
labels=kmeans.predict(df)
transformed=kmeans.transform(df)
df=df.assign(Labels=labels)
df=df.assign(Temp = mySimulation.TemperatureList)
centroids=kmeans.cluster_centers_

KMeans_Fig=plt.figure(4)
KMeans_Ax = KMeans_Fig.add_subplot(1,1,1)
colors=map(lambda x: colmap[x+1], labels)
KMeans_Ax.scatter(df['x'],df['y'],color=colors,alpha=0.5,edgecolor='k')
CentroidX,CentroidY=zip(*centroids)
KMeans_Ax.scatter(CentroidX,CentroidY,color='blue',marker="x")
KMeans_Ax.set_xlim(min(df['x'])-1,max(df['x'])+1)
KMeans_Ax.set_ylim(min(df['y'])-1,max(df['y'])+1)
KMeans_Ax.grid(linestyle='-',linewidth=0.5)
plt.title('K-means on projection to first and second principle component')
KMeans_Ax.grid(linestyle='-',linewidth=0.5)
KMeans_Ax.set_xlabel('First principle component')
KMeans_Ax.set_ylabel('Second principle component')
plt.show()

df = df.sort_values(by=['Temp'])
print(df)

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
    z = np.polyfit(T,Points,3)
    p = np.poly1d(z)
    rootList.append(np.polyder(p).roots[0])


xs = np.arange(1.5,3,0.001)
plt.figure(figsize=(6.5, 4))
plt.plot(T, Points, 'o', label="data")
plt.plot(xs, p(xs), label="Poly(deg = 3) regression")
plt.title('Sample temperature versus distance from boundary')
plt.xlabel('Temperature')
plt.ylabel('Distance from Voronoi boundary')
plt.show()

print(str(np.mean(rootList)) + " +/- " + str(np.std(rootList)))






