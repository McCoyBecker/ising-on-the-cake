libary(ggplot2)
libary(deldir)

ggplot(equilibratedData, aes(x=x, y=y)) + geom_point(aes(col=((equilibratedData$Temp-1.9)/0.7)*200), size=0.1) + labs(titles = "K-means clustering on Ising lattice samples at n = 40", x = "First principle component", y = "Second principle component") + scale_color_gradient(name="Temp",breaks=c(0,100,200),labels=c("Low",2.3,"High"))
