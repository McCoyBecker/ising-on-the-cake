import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import configClass as cf
import IsingLatticeClass as Ising
import SimulationClass as simulation

#The DataAnalyzer class supports principle component analysis, k-means clustering, Voronoi plots, and more!

class DataAnalyzer:

    def __init__(self, dataMatrix, Energy, Magnetization, HowManyPCA, HowManyTSNE, HowManyClusters):
        self.dataMatrix = dataMatrix
        self.EnergyList = Energy
        self.MagnetizationList = Magnetization
        self.PCA = PCA(n_components = HowManyPCA)
        self.TSNE = TSNE(n_components=HowManyTSNE)
        self.K = HowManyClusters
        self.scaler = StandardScaler()
        self.PComponents = [[0] for j in range(HowManyPCA)]


    def scalerfit(self):
        self.scaler.fit(self.dataMatrix)

