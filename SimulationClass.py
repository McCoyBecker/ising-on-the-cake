import numpy as np
import configClass as cf
import IsingLatticeClass as Ising
import matplotlib.pyplot as plt

#The Simulation class includes plotting functionality and sampling over a range of temperatures and also handles equilibration

class Simulation:

    def __init__(self, LatticeSize, Coupling, TemperatureLowerBound, TemperatureUpperBound, TemperatureRange):
        
        #The Simulation accessors
        self.LatticeSize = LatticeSize
        self.SimulationList = []
        self.dataMatrix = []
        self.EnergyList = []
        self.MagnetizationList = []
        self.LowerTemp = TemperatureLowerBound
        self.UpperTemp = TemperatureUpperBound
        self.TempRange = TemperatureRange
        self.TemperatureList = []
        self.SimulationList = [[Ising.IsingLattice(k, LatticeSize, Coupling, TemperatureLowerBound + j*((TemperatureUpperBound-TemperatureLowerBound))/float(TemperatureRange)) for k in [1,-1,0,0.5]] for j in range(TemperatureRange)]

    def update(self):
        for i in range(len(self.SimulationList)):
            for j in range(4):
                self.SimulationList[i][j].MonteCarloStep()
    
    def sample(self):
            for i in range(len(self.SimulationList)):
                f = f = open('80by80.csv','w')
                for j in range(4):
                    f.write(str(self.SimulationList[i][j].Config.state.flatten())+'\n')
                    #self.dataMatrix.append(self.SimulationList[i][j].Config.state.flatten())
                    self.EnergyList.append(self.SimulationList[i][j].Energy)
                    self.MagnetizationList.append(self.SimulationList[i][j].Magnetization)
                    self.TemperatureList.append(self.LowerTemp + i*((self.UpperTemp-self.LowerTemp)/float(self.TempRange)))
                f.close()



