import numpy as np

#Input lattice size and what sort of config

class Config:

    def __init__(self, whatType, N):
        
        #The Config accessors
        self.state = np.ones((N,N))
        
        if whatType == -1:
            for i in range(N):
                for j in range(N):
                    self.state[i][j]*=-1
    
        if whatType == 0:
            self.state = 2*np.random.randint(2, size=(N,N))-1

        if whatType == 0.5:
                for i in range(N):
                    for j in range(N):
                        if j > i:
                            self.state[i][j]*=-1

