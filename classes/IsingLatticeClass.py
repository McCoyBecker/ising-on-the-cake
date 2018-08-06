import numpy as np
import configClass as cf
import random as random

#The IsingLattice class includes all the observables and functions on the lattice

class IsingLattice:
    
    def __init__(self, whatType, LatticeSize, Coupling, Temperature):
        
        #The Ising accessors
        self.Config = cf.Config(whatType, LatticeSize)
        self.Coupling = Coupling
        self.LatticeSize = LatticeSize
        self.Temperature = Temperature
        self.updateEnergy()
        self.updateMagnetization()
    
    '''Update energy and magnetization'''
    def updateEnergy(self):
        self.Energy = 0
        for i in range(len(self.Config.state)):
            for j in range(len(self.Config.state)):
                SpinIndex=self.Config.state[i][j]
                CouplingTerm=self.Config.state[(i+1)%self.LatticeSize][j]+self.Config.state[i][(j+1)%self.LatticeSize]+self.Config.state[(i-1)%self.LatticeSize][j]+self.Config.state[i][(j-1)%self.LatticeSize]
                self.Energy += self.Coupling*CouplingTerm*SpinIndex
        self.Energy = float(self.Energy) / 4

    def updateMagnetization(self):
        self.Magnetization = abs(float(np.sum(self.Config.state))/self.LatticeSize**2)

    '''This is the normal Metropolis algorithm'''
    def MonteCarloStep(self):
        
        #Here I make my index list, to keep track of what indices I've been to already
        IndexList=[]
        for i in range(self.LatticeSize):
            for j in range(self.LatticeSize):
                IndexList.append((i,j))
        
        for i in range(self.LatticeSize):
            for j in range(self.LatticeSize):
                #Random choice of the remaining indices in IndexList, then I remove my choice
                RandomIndexSpin=random.choice(IndexList)
                IndexList.remove(RandomIndexSpin)
                a=RandomIndexSpin[0]
                b=RandomIndexSpin[1]
                Choice=self.Config.state[a][b]
                
                #Here I calculate the energy cost of flipping the spin
                CouplingTerm=self.Config.state[(a+1)%self.LatticeSize][b] + self.Config.state[a][(b+1)%self.LatticeSize] + self.Config.state[(a-1)%self.LatticeSize][b] + self.Config.state[a][(b-1)%self.LatticeSize]
                EnergyCost=2*self.Coupling*Choice*CouplingTerm
                
                #Here's the condition on the Monte Carlo chain, this ensures that we sample from the Boltzmann distribution
                if EnergyCost<0:
                    Choice*=-1
                elif np.random.rand()<np.exp(-EnergyCost*(1/float(self.Temperature))):
                    Choice*=-1
                
                self.Config.state[a][b]=Choice
                
        self.updateEnergy()
        self.updateMagnetization()
