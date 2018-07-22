library(coda)
data=read.csv("/Users/mccoybecker/Documents/GitHub/ising-on-the-cake/data/Cut_updated_data/5000_40_60_cut_updated.csv")

#Plotting Geweke statistic for one chain in the low temperature regime
lowtemp = data[which(data$Temp<1.91),]
geweke.plot(mcmc(lowtemp[seq(1,20000,4),5]))

#Plotting Geweke statistic for one chain in the high temperature regime
hightemp = data[which(data$Temp>2.58),]
geweke.plot(mcmc(hightemp[seq(1,20000,4),5]))

#Gelman-Rudin for low temp
LowTempChainOne = mcmc(lowtemp[seq(1,20000,4),5])
LowTempChainTwo = mcmc(lowtemp[seq(2,20000,4),5])
LowTempChainThree = mcmc(lowtemp[seq(3,20000,4),5])
LowTempChainFour = mcmc(lowtemp[seq(4,20000,4),5])
LowTempList = mcmc.list(LowTempChainOne,LowTempChainTwo,LowTempChainThree,LowTempChainFour)
gelman.plot(LowTempList,main="Equilibration at low temperature for n = 40")
              
#Gelman-Rudin for high temp
HighTempChainOne = mcmc(hightemp[seq(1,20000,4),5])
HighTempChainTwo = mcmc(hightemp[seq(2,20000,4),5])
HighTempChainThree = mcmc(hightemp[seq(3,20000,4),5])
HighTempChainFour = mcmc(hightemp[seq(4,20000,4),5])
HighTempList=mcmc.list(HighTempChainOne,HighTempChainTwo,HighTempChainThree,HighTempChainFour)
gelman.plot(HighTempList,main="Equilibration at high temperature for n = 40")
