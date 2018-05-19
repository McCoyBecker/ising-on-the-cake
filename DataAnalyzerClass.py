import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass as simulation

#The DataAnalyzer class supports principle component analysis, k-means clustering, Voronoi plots, and more!

class DataAnalyzer:

    def __init__(self, dataMatrix, HowManyPCA, HowManyClusters):
        self.dataMatrix = dataMatrix
        self.PCA = PCA(n_components = HowManyPCA)
        self.K = HowManyClusters
        self.scaler = StandardScaler()
        self.PComponents = [[0] for j in range(HowManyPCA)]


    def scalerfit(self):
        self.scaler.fit(self.dataMatrix)

